# CoPa Café pitch: guards + asserts + send + read-back + registry append + lane.db event (abort-on-any-gate)
# Adapted from the proven threemonkeys send_pitch.py (2026-11-22 08:58 run). Resume-safe: existing registry pitch row = skip.
import json, re, subprocess, sys, os, time, datetime, imaplib

DRAFT = '/Users/rleon/sites/copa-cafe/PITCH-DRAFT.md'
REG = '/Users/rleon/.hermes/projects/websites/pitch_registry.jsonl'
LANEDB = '/Users/rleon/.hermes/projects/websites/lane.db'
ENVOUT = '/Users/rleon/sites/copa-cafe/send-envelope.json'
TO = 'copacafecc@gmail.com'
SUBJ = 'Website demo for CoPa Café'
TOKEN = 'copa-cafe-t1'
SLUG = 'copa-cafe'
CARD = 't_9cf90b6f'
body = open(DRAFT, encoding='utf-8').read()
assert '\u2026' not in body, 'U+2026 mangled token in draft'

def norm(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())
rows = [json.loads(l) for l in open(REG) if l.strip()]
nto = norm(TO)

# 0) resume predicate
if any(r.get('type') == 'pitch' and r.get('slug') == SLUG for r in rows):
    sys.exit('SKIP: registry already has a pitch row for this slug — never re-send')

# 1) never-pitch-twice guards
email_hits = [r for r in rows if norm(r.get('email', '')) == nto]
nameq = norm('copa cafe')
name_hits = [r for r in rows if any(nameq == norm(a) or nameq in norm(a) or norm(a) in nameq
              for a in ([r.get('business', '')] + list(r.get('name_aliases', []) or [])) if norm(a))]
print('GUARD email rows:', [(r.get('type'), r.get('slug'), r.get('email')) for r in email_hits])
print('GUARD name rows:', [(r.get('type'), r.get('slug'), r.get('business')) for r in name_hits])
pitched_emails = {norm(r['email']) for r in rows if r.get('type') == 'pitch' and r.get('email')}
blocking_names = [r for r in name_hits if r.get('type') in ('pitch', 'no', 'optout', 'has_site', 'sent')]
if any(norm(r.get('email', '')) in pitched_emails for r in email_hits) or blocking_names:
    sys.exit('ABORT: already pitched/known on this email-or-name key')

# 2) inbox cap (2 businesses max per inbox; gmail local-part is the alias)
inbox_alias = 'copacafecc'
n_same_inbox = sum(1 for r in rows if r.get('type') == 'pitch' and (r.get('alias') == inbox_alias or norm(r.get('email', '')) == nto))
print(f'inbox cap check ({inbox_alias}):', n_same_inbox, '(cap 2)')
assert n_same_inbox < 2, 'ABORT: inbox cap'

# 3) optout suppression (email is globally suppressed)
opt_emails = {norm(r.get('email', '')) for r in rows if r.get('type') == 'optout'}
assert nto not in opt_emails, 'ABORT: opted-out address'
try:
    sup = open('/Users/rleon/.hermes/projects/websites/optout_list.txt').read()
    assert nto not in norm(sup), 'ABORT: optout_list.txt'
except FileNotFoundError:
    pass

# 4) copy form asserts (proven formula; ABORT before send) — URLs derived from the draft itself
assert body.count('](http') == 2, f'links {body.count("](http")}'
assert body.count('<img') == 1, 'img count'
demo = re.search(r'\]\((https://copa-cafe-demo[^)]+)\)', body).group(1)
pay = re.search(r'\]\((https://buy\.stripe[^)]+)\)', body).group(1)
pixel = re.search(r'<img src="([^"]+)"', body)
for need in ('utm_medium=email', 'utm_campaign=websites', f'utm_content={TOKEN}'):
    assert need in demo, 'demo missing ' + need
    assert need in pay, 'pay missing ' + need
assert f'client_reference_id={TOKEN}' in pay, 'pay missing client_reference_id'
assert pixel and pixel.group(1) == f'https://copa-cafe-demo.up.railway.app/open?t={TOKEN}', 'pixel token'
t = re.sub(r'\*\*', '', body)
t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
t = re.sub(r'<img[^>]*>', '', t)
lines = [l for l in t.splitlines() if l.strip()]
lines = [l for l in lines if not l.startswith('Hi ') and not l.startswith('— Jarvis')
         and not l.startswith('OnSmalltalk Media ·') and not l.startswith('<img')]
n = len(re.findall(r'\S+', ' '.join(lines)))
print(f'ASSERT core words: {n} (limit 110); links 2; utm+pixel token {TOKEN} OK')
assert n <= 110, f'ABORT words {n}'

if os.environ.get('DRY'):
    sys.exit(f'GUARDS+ASSERTS PASS (dry, not sent); words={n}')

# 5) send (body on stdin, --json envelope; message_id from the envelope JSON)
res = subprocess.run(['email', 'send', '--account', 'jarvis', '--as', 'websites',
                      '--to', TO, '--subject', SUBJ, '--json'],
                     input=body.encode(), capture_output=True, timeout=120)
try:
    env = json.loads(res.stdout.decode())
except Exception:
    open(ENVOUT, 'w').write(res.stdout.decode() + '\n---STDERR---\n' + res.stderr.decode())
    sys.exit('ABORT: unparseable send envelope — do NOT resend, read back Sent Mail first')
json.dump({'ok': env.get('ok'), 'env': env}, open(ENVOUT, 'w'))
ok = env.get('ok')
mid = (env.get('data') or {}).get('message_id') or (env.get('data') or {}).get('msg_id')
print('SEND ok=', ok, 'msg:', mid if ok else env)
if not ok or not mid:
    sys.exit('ABORT send — read back [Gmail]/Sent Mail before any retry')

# 6) sent read-back (raw imaplib): Message-ID equality + identity header pair
conf = {}
for l in open(os.path.expanduser('~/.hermes/config/jarvis-email.conf')):
    if '=' in l: k, v = l.split('=', 1); conf[k.strip()] = v.strip()
    elif ':' in l: k, v = l.split(':', 1); conf[k.strip()] = v.strip()
M = imaplib.IMAP4_SSL(conf.get('IMAP_SERVER', 'imap.gmail.com'))
M.login(conf['EMAIL'], conf['APP_PASSWORD'])
M.select('"[Gmail]/Sent Mail"')
typ, m = M.uid('search', None, 'SUBJECT', '"Website demo for CoPa Café"')
ids = [i.decode() for i in m[0].split()]
hit = None
for uid in ids[-3:]:
    typ, d = M.uid('fetch', uid, '(BODY.PEEK[HEADER])')
    hdr = d[0][1].decode(errors='replace')
    if mid in hdr:
        orp = bool(re.search(r'X-Google-Original-From:[^>]*jarvis\+websites', hdr, re.I))
        rto = bool(re.search(r'Reply-To:\s*\S*jarvis\+websites', hdr, re.I))
        hit = {'uid': uid, 'ogf': orp, 'reply_to': rto}
        break
M.logout()
print('READBACK:', hit)
assert hit and hit['ogf'] and hit['reply_to'], 'ABORT READBACK — mail out but unproven; append registry only after proof, never re-send'

# 7) registry append AT SEND (type IN the dict), then recount-verify
row = {
    'type': 'pitch', 'date': '2026-11-22',
    'ts': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
    'slug': SLUG, 'business': 'CoPa Café (Corpus Christi TX)',
    'name_aliases': ['CoPa Café', 'CoPa Cafe', 'copa-cafe', 'CoPa Café Corpus Christi', 'copacafe'],
    'email': TO, 'alias': inbox_alias, 'card': CARD,
    'msg_id': mid, 'preview': 'https://copa-cafe-demo.up.railway.app',
    'subject': SUBJ, 'subject_arm': 'v7', 'cohort': 'A',
    'shot': False, 'pixel': True, 'utm_content': TOKEN,
    'followup_due': '2026-12-01',
    'ladder': 't2 2026-12-01 / t3 2026-12-08 / t4 2026-12-15 (weekday ladder, US-holiday shift); teardown recheck >= 2026-12-21',
    'feed_id': 'press-corpuschristi', 'shop_id': 'copa-cafe-corpus-christi',
    'note': ('owner email self-published on the shop\'s own FB Page intro (verified logged-out 2026-11-22 at card creation); '
             'press: The Bend Magazine Table Talk Nov 2026 + comingsoonproject.com timeline (sales-tax reg 2026-08-01, "recently opened"); '
             'no-site evidence: GBP place embeds empty (no listing), copa.cafe = 3rd-party domainer for-sale lander (RDAP 2025-10-30), '
             'copacafe.com = 2000-vintage empty body, brand-SERP top hits are IG/FB/directories only; '
             'founder bundle T1 $249+$39/mo 31d trial; v7 subject arm; 10-page site'),
}
with open(REG, 'a') as f:
    f.write(json.dumps(row, ensure_ascii=False) + '\n')
pitches = 0; mine = 0; line_no = 0
for i, l in enumerate(open(REG), 1):
    try: d = json.loads(l)
    except Exception: continue
    if d.get('type') == 'pitch':
        pitches += 1
        if d.get('slug') == SLUG: mine += 1; line_no = pitches
assert mine == 1, f'copa-cafe pitch rows={mine}'
print(f'REGISTRY_OK total_pitch_rows={pitches} mine=1 line={line_no}')

# 8) lane.db events mirror row
import sqlite3
db = sqlite3.connect(LANEDB)
db.execute("""INSERT INTO events (line,type,slug,business,email,msg_id,followup_due,date_txt,ts,note)
VALUES (?,?,?,?,?,?,?,?,?,?)""",
 (line_no, 'pitch', SLUG, 'CoPa Café (Corpus Christi TX)', TO, mid,
  '2026-12-01', '2026-11-22', int(time.time()),
  'pitched via websites desk; demo copa-cafe-demo.up.railway.app; founder bundle T1 $249+$39/mo 31d trial; v7 subject arm; read-back proof uid=' + hit['uid']))
db.commit()
print('EVENT_ROW_OK', db.execute("SELECT line,type,slug,msg_id FROM events WHERE slug=?", (SLUG,)).fetchall())
print('ALL_DONE', mid)

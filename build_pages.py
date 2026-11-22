#!/usr/bin/env python3
"""CoPa Café — template v2 generator (websites lane, t_9cf90b6f, 2026-11-22).
Copy discipline: only facts verified on the card — The Bend Magazine Table Talk
(Nov 2026), comingsoonproject.com registry timeline, and the shop's own FB/IG
bio fields. No phone, no prices — neither published; unknown = omitted.
Output: public/*.html + sitemap.xml + robots.txt. Run before `railway up`."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
ORIGIN = "https://copa-cafe-demo.up.railway.app"
BUILT = "2026-11-22"

NAP_LINE = "1133 County Rd 22, Corpus Christi, TX 78415"
ADDRESS_HTML = "1133 County Rd 22<br>Corpus Christi, TX 78415"
MAP_Q = "1133+Co+Rd+22,+Corpus+Christi,+TX+78415"
EMAIL = "copacafecc@gmail.com"
FB = "https://www.facebook.com/p/CoPa-Caf%C3%A9-61593492866132/"
IG = "https://www.instagram.com/copa.cafe.llc/"
BEND = "https://www.thebendmag.com/table-talk-corpus-christi-food-drink-news/"

HOURS_SHORT = "Mon&ndash;Fri 8&ndash;4 &middot; Sat 9&ndash;5 &middot; Sun closed"

# Hand-drawn cup-and-steam stamp mark (ticket/stamp identity; stroke inherits color)
STAMP = ('<svg class="stamp" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
         '<circle cx="12" cy="12" r="10.8" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="2.4 2.1"/>'
         '<path d="M8 10.5h6.4v3.2a3.2 3.2 0 0 1-3.2 3.2h0a3.2 3.2 0 0 1-3.2-3.2z" fill="none" stroke="currentColor" stroke-width="1.3"/>'
         '<path d="M14.4 11.2h1.3a1.3 1.3 0 0 1 0 2.6h-1.3" fill="none" stroke="currentColor" stroke-width="1.3"/>'
         '<path d="M9.6 6.2c.7.8.7 1.6 0 2.4M12 5.6c.7.8.7 1.6 0 2.4" fill="none" stroke="currentColor" stroke-width="1.1"/></svg>')

STEAM = ('<svg class="steam" viewBox="0 0 120 40" aria-hidden="true" focusable="false">'
         '<path d="M20 36c4-6 4-10 0-16s-4-10 0-16M60 36c4-6 4-10 0-16s-4-10 0-16M100 36c4-6 4-10 0-16s-4-10 0-16" '
         'fill="none" stroke="currentColor" stroke-width="1.1" stroke-linecap="round" opacity=".45"/></svg>')

HEADER = (f'<a class="skip" href="#main">Skip to content</a>\n'
          '<header class="site"><div class="wrap hdr">'
          f'<a class="wm" href="/">{STAMP}<span>CoPa <em>Caf&eacute;</em></span></a>'
          '<nav aria-label="Site"><ul>'
          '<li><a href="/menu">Menu</a></li>'
          '<li><a href="/espresso-bar-corpus-christi">Espresso</a></li>'
          '<li><a href="/matcha-chai-corpus-christi">Matcha &amp; Chai</a></li>'
          '<li><a href="/visit">Visit</a></li>'
          '</ul></nav>'
          '<a class="btn sm" href="/contact">Send a note</a>'
          '</div></header>')

FOOTER = ('<footer class="site"><div class="wrap foottop">'
          f'<div><p class="fbrand">{STAMP}<span>CoPa <em>Caf&eacute;</em></span></p>'
          '<p class="ftag">Espresso &middot; Matcha &middot; Chai &middot; inside Echelon Performance Gym</p>'
          '<div class="fnaps"><p class="ftown">Find us</p>'
          f'<address class="addr">{ADDRESS_HTML}</address>'
          f'<p class="fhrs">{HOURS_SHORT}</p>'
          f'<p>Questions: <a href="mailto:{EMAIL}">{EMAIL}</a> &middot; <a href="/contact">contact form</a></p></div></div>'
          '<nav aria-label="Footer"><ul>'
          '<li><a href="/menu">Fall menu</a></li>'
          '<li><a href="/espresso-bar-corpus-christi">Espresso &amp; flavor combos</a></li>'
          '<li><a href="/matcha-chai-corpus-christi">Matcha, chai &amp; cold brew</a></li>'
          '<li><a href="/visit">Visit</a></li>'
          '<li><a href="/contact">Contact</a></li>'
          '<li><a href="/privacy">Privacy</a></li>'
          '</ul></nav>'
          '<p class="fpress">In the news:<br>'
          f'<a href="{BEND}" rel="noopener">The Bend Magazine: Table Talk &mdash; new micro cafe</a></p>'
          '</div><div class="wrap"><p class="footline">'
          f'&copy; 2026 CoPa Caf&eacute; &middot; Specialty micro cafe &middot; {NAP_LINE}'
          '</p></div></footer>')

def head(title, desc, path, og=True):
    canonical = ORIGIN + ("" if path == "/" else path)
    ogblock = ""
    if og:
        ogblock = (f'<meta property="og:type" content="website">\n'
                   '<meta property="og:site_name" content="CoPa Café">\n' +
                   f'<meta property="og:title" content="{title}">\n'
                   f'<meta property="og:description" content="{desc}">\n'
                   f'<meta property="og:url" content="{canonical}">\n'
                   f'<meta property="og:image" content="{ORIGIN}/og.png">\n'
                   '<meta name="twitter:card" content="summary_large_image">\n'
                   f'<meta name="twitter:title" content="{title}">\n'
                   f'<meta name="twitter:description" content="{desc}">\n'
                   f'<meta name="twitter:image" content="{ORIGIN}/og.png">\n')
    return (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<!-- BUILT-{BUILT} -->\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{title}</title>\n'
            f'<meta name="description" content="{desc}">\n'
            '<meta name="robots" content="noindex, nofollow">\n'
            f'<link rel="canonical" href="{canonical}">\n'
            + ogblock +
            '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
            '<link rel="stylesheet" href="/style.css">\n</head>')

def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=1) + '\n</script>\n'

def page(title, desc, path, body, ldobj=None, og=True):
    return (head(title, desc, path, og) + (ldobj or "") + '<body>\n' + HEADER +
            '\n<main id="main">\n' + body + '\n</main>\n' + FOOTER + '\n</body>\n</html>\n')

def faq(items):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in items]}

def crumb(steps):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + p}
        for i, (n, p) in enumerate(steps)]}

# ---------------------------------------------------------------- HOME
CAFE_ND = {
    "@type": "CafeOrCoffeeShop", "@id": ORIGIN + "/#cafe", "name": "CoPa Café",
    "description": ("Specialty micro cafe inside Echelon Performance Gym in Corpus Christi, Texas. "
                    "Espresso, matcha and chai built around gourmet flavor combinations — blueberry-cardamom, "
                    "fig-brown sugar, pumpkin-cookie butter — plus cold brew. Opened 2026; fall menu out now."),
    "url": ORIGIN + "/", "image": ORIGIN + "/og.png",
    "telephone": "+1-361-NOT-PUBLISHED",  # placeholder stripped below — no phone published
    "email": "copacafecc@gmail.com",
    "address": {"@type": "PostalAddress", "streetAddress": "1133 County Rd 22",
                "addressLocality": "Corpus Christi", "addressRegion": "TX",
                "postalCode": "78415", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": 27.6735979, "longitude": -97.472375},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
         "opens": "08:00", "closes": "16:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday",
         "opens": "09:00", "closes": "17:00"}],
    "menu": ORIGIN + "/menu",
    "sameAs": [FB, IG]}
CAFE_ND.pop("telephone")  # no published phone — omit, never fake

HOME_LDS = {"@graph": [
    {"@type": "WebSite", "@id": ORIGIN + "/#website", "name": "CoPa Café", "url": ORIGIN + "/"},
    {"@type": "WebPage", "@id": ORIGIN + "/#webpage",
     "name": "CoPa Café — Espresso, Matcha & Chai Micro Cafe, Corpus Christi TX",
     "url": ORIGIN + "/", "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@id": ORIGIN + "/#cafe"}},
    CAFE_ND,
    faq([
        ("Where is CoPa Café?",
         "Inside Echelon Performance Gym at 1133 County Road 22 in Corpus Christi, Texas — in the London District area. The cafe is small, so look past the gym's signage."),
        ("When did CoPa Café open?",
         "Recently — its fall menu is out now. The cafe's sales-tax registration as a coffee, snack and dessert shop lists sales beginning August 1, 2026."),
        ("What do you serve?",
         "Drinks first: espresso, matcha and chai as your base, then a gourmet flavor combination on top — blueberry and cardamom, fig and brown sugar, pumpkin and cookie butter, and more."),
        ("Do you have plain cold brew?",
         "Yes. Cold-brew purists who want no extras are covered, too."),
        ("What are your hours?",
         "Monday through Friday 8 a.m. to 4 p.m., Saturday 9 a.m. to 5 p.m., closed Sunday.")])] }

HOME = page(
    "CoPa Caf&eacute; — Espresso, Matcha &amp; Chai Micro Cafe, Corpus Christi TX",
    "CoPa Café is a specialty micro cafe inside Echelon Performance Gym in Corpus Christi, TX: espresso, matcha and chai with gourmet flavor combos — plus cold brew. Mon–Fri 8–4, Sat 9–5.",
    "/",
    f'''
<section class="band ink hero"><div class="wrap center">
  {STEAM}
  <p class="eyebrow">New in Corpus Christi &middot; inside Echelon Performance Gym</p>
  <h1 class="big">CoPa <em>Caf&eacute;</em></h1>
  <p class="lede">A specialty micro cafe hiding where the gym is &mdash; in the London District
  area of Corpus Christi. Espresso, matcha and chai, each built around a gourmet flavor
  combination &mdash; with plain cold brew for the purists. The fall menu is out now.</p>
  <div class="ctarow"><a class="btn gold" href="/menu">See the fall menu</a>
  <a class="btn ghost" href="/contact">Send us a note</a></div>
</div></section>

<section class="band paper"><div class="wrap narrow center">
  <p class="eyebrow">How the counter works</p>
  <h2 class="sec">Two choices. That&rsquo;s the whole order.</h2>
  <div class="steps">
    <div class="step"><p class="num">1</p><h3 class="stept">Pick a base</h3>
      <p class="stepd">Espresso, matcha or chai. Cold brew stands on its own, no ceremony
      required.</p></div>
    <div class="step"><p class="num">2</p><h3 class="stept">Pick a pairing</h3>
      <p class="stepd">Blueberry &amp; cardamom. Fig &amp; brown sugar. Pumpkin &amp; cookie
      butter &mdash; and more pairings on the board.</p></div>
    <div class="step"><p class="num">3</p><h3 class="stept">Drink it at the gym</h3>
      <p class="stepd">You&rsquo;re already at the entrance. The counter is steps from the
      gym floor.</p></div>
  </div>
</div></section>

<section class="band cream"><div class="wrap">
  <p class="eyebrow">The fall board &middot; flavor combinations</p>
  <h2 class="sec">Gourmet pairings, on purpose</h2>
  <p class="secsub">The cafe&rsquo;s drinks are built as pairings, not add-ons. These are the
  combinations The Bend Magazine called out on the fall menu.</p>
  <div class="tickets">
    <a class="ticket t-blue" href="/espresso-bar-corpus-christi"><p class="tkick">Pairing no. 1</p>
      <h3 class="tname">Blueberry &amp;<br>cardamom</h3>
      <p class="tper">Bright, deep fruit against a cool, resinous spice &mdash; the dessert-plate
      pairing, in a cup.</p><p class="tmore">On the espresso bar &rarr;</p></a>
    <a class="ticket t-fig" href="/espresso-bar-corpus-christi"><p class="tkick">Pairing no. 2</p>
      <h3 class="tname">Fig &amp;<br>brown sugar</h3>
      <p class="tper">Jammy fig and molasses-deep sugar &mdash; the quiet one of the three,
      and the one regulars keep to themselves.</p><p class="tmore">On the espresso bar &rarr;</p></a>
    <a class="ticket t-cookie" href="/espresso-bar-corpus-christi"><p class="tkick">Pairing no. 3</p>
      <h3 class="tname">Pumpkin &amp;<br>cookie butter</h3>
      <p class="tper">Pumpkin with spiced-cookie richness instead of the usual
      pumpkin-spice routine &mdash; fall, ordered differently.</p><p class="tmore">On the espresso bar &rarr;</p></a>
  </div>
</div></section>

<section class="band ink"><div class="wrap split">
  <div>
    <p class="eyebrow">Matcha &middot; chai &middot; cold brew</p>
    <h2 class="sec light">Not an espresso shop that happens to have tea</h2>
    <p class="bodycopy">Matcha and chai are full bases here &mdash; built into the same
    pairing program as the espresso drinks. And if you want cold brew with nothing extra,
    they&rsquo;ve got that too, no fluff.</p>
    <div class="ctarow"><a class="btn gold" href="/matcha-chai-corpus-christi">Matcha, chai &amp; cold brew</a></div>
  </div>
  <aside class="infocard">
    <h3 class="infh">Counter card</h3>
    <dl class="factlist">
      <div><dt>Where</dt><dd>Inside Echelon Performance Gym<br>1133 County Rd 22<br>Corpus Christi, TX 78415</dd></div>
      <div><dt>Hours</dt><dd>Mon&ndash;Fri 8&ndash;4<br>Sat 9&ndash;5<br>Sun closed</dd></div>
      <div><dt>On the bar</dt><dd>Espresso &middot; matcha &middot; chai<br>gourmet pairings &middot; cold brew</dd></div>
    </dl>
    <p class="bigm"><a href="/visit">Directions &amp; hours</a></p>
  </aside>
</div></section>

<section class="band cream"><div class="wrap narrow">
  <p class="eyebrow">New here?</p>
  <h2 class="sec">The Bend found it first</h2>
  <p class="bodycopy">&ldquo;While driving along 1133 County Road in the London District area,
  you might see the Echelon Performance Gym signage, but look a bit harder, and you&rsquo;ll find
  a new, small but mighty coffee shop.&rdquo; &mdash; The Bend Magazine, Table Talk</p>
  <p class="note">Full write-up: <a href="{BEND}" rel="noopener">Table Talk: what&rsquo;s new in
  Corpus Christi food &amp; drink</a>. Follow the counter: <a href="{IG}" rel="noopener">Instagram</a>
  &middot; <a href="{FB}" rel="noopener">Facebook</a>.</p>
  <div class="ctarow"><a class="btn" href="/contact">Ask us something</a>
  <a class="btn ghost" href="/menu">The fall menu</a></div>
</div></section>
''',
    ld(HOME_LDS))

# ---------------------------------------------------------------- MENU HUB
MENU_LDS = {"@graph": [
    {"@type": "WebPage", "name": "The fall menu — CoPa Café, Corpus Christi TX", "url": ORIGIN + "/menu",
     "isPartOf": {"@id": ORIGIN + "/#website"}},
    crumb([("Home", "/"), ("Menu", "/menu")]),
    {"@type": "Menu", "name": "CoPa Café — fall menu",
     "description": ("Bases: espresso, matcha, chai, cold brew. Gourmet flavor pairings: blueberry-cardamom, "
                     "fig-brown sugar, pumpkin-cookie butter, and more. Prices at the counter. Reported by The Bend Magazine."),
     "hasMenuSection": [
        {"@type": "MenuSection", "name": "Bases", "description": "Choose your caffeine base.",
         "hasMenuItem": [
            {"@type": "MenuItem", "name": "Espresso", "description": "The bar's espresso base for the pairing program."},
            {"@type": "MenuItem", "name": "Matcha", "description": "Ground green tea as a drink base."},
            {"@type": "MenuItem", "name": "Chai", "description": "Spiced tea as a drink base."},
            {"@type": "MenuItem", "name": "Cold brew", "description": "Slow-steeped coffee, straight — no fluff."}]},
        {"@type": "MenuSection", "name": "Flavor pairings", "description": "Pick a pairing for your base, per The Bend Magazine's fall-menu report.",
         "hasMenuItem": [
            {"@type": "MenuItem", "name": "Blueberry & cardamom", "description": "Deep fruit against cool spice."},
            {"@type": "MenuItem", "name": "Fig & brown sugar", "description": "Jammy fig with molasses-deep sugar."},
            {"@type": "MenuItem", "name": "Pumpkin & cookie butter", "description": "Pumpkin with spiced-cookie richness."}]}]},
    faq([
        ("How do I order?",
         "Pick a base — espresso, matcha or chai — then pick a flavor pairing. That's the fall menu's ordering experience, as The Bend Magazine described it."),
        ("How much is a drink?",
         "Prices live at the counter, not on this page — so the board can change with the season without a web edit."),
        ("Is there food?",
         "The cafe's registration covers coffee, snack and dessert service. Ask at the counter what's coming out that day."),
        ("I just want cold brew. Is that weird here?",
         "Not at all — plain cold brew is on the menu, for people who want their coffee without the flourishes.")])] }

MENU = page(
    "The Fall Menu: Bases &amp; Flavor Pairings — CoPa Caf&eacute;, Corpus Christi TX",
    "CoPa Café's fall menu: pick a base — espresso, matcha or chai — then a gourmet pairing: blueberry-cardamom, fig-brown sugar, pumpkin-cookie butter. Cold brew, too. Corpus Christi, TX.",
    "/menu",
    '''
<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">The fall board</p>
  <h1>The fall menu</h1>
  <p class="lede">The counter works in two moves: choose your caffeine base, then pick a
  gourmet flavor combination. Bases first, then the pairings &mdash; and plain cold brew for
  everyone who wants none of the rest.</p>
</div></section>

<section class="band paper"><div class="wrap boardgrid">
  <div class="group">
    <p class="eyebrow">Step one &middot; the bases</p>
    <h2 class="sec">Choose your base</h2>
    <ul class="plist">
      <li><span class="pname">Espresso</span> <span class="pdash">&mdash;</span> the bar&rsquo;s
      anchor; the pairing program is built around it.</li>
      <li><span class="pname">Matcha</span> <span class="pdash">&mdash;</span> ground green tea,
      a full base, not an afterthought.</li>
      <li><span class="pname">Chai</span> <span class="pdash">&mdash;</span> spiced tea, ready
      for a pairing of its own.</li>
      <li><span class="pname">Cold brew</span> <span class="pdash">&mdash;</span> slow-steeped
      coffee, straight up, no fluff.</li>
    </ul>
    <p class="bigm"><a href="/matcha-chai-corpus-christi">Matcha, chai &amp; cold brew page</a></p>
  </div>
  <div class="group">
    <p class="eyebrow">Step two &middot; the pairings</p>
    <h2 class="sec">Pick your flavor combination</h2>
    <ul class="plist">
      <li><span class="pname">Blueberry &amp; cardamom</span> <span class="pdash">&mdash;</span>
      deep fruit against cool, resinous spice.</li>
      <li><span class="pname">Fig &amp; brown sugar</span> <span class="pdash">&mdash;</span>
      jammy fig, molasses-deep sugar.</li>
      <li><span class="pname">Pumpkin &amp; cookie butter</span> <span class="pdash">&mdash;</span>
      fall done as spiced-cookie richness, not pumpkin-spice rerun.</li>
      <li><span class="pname">And more</span> <span class="pdash">&mdash;</span> the board
      carries combinations beyond the ones printed here.</li>
    </ul>
    <p class="bigm"><a href="/espresso-bar-corpus-christi">Espresso bar &amp; pairings page</a></p>
  </div>
</div></section>

<section class="band cream"><div class="wrap narrow center">
  <p class="eyebrow">The honest note</p>
  <h2 class="sec">Prices live at the counter</h2>
  <p class="bodycopy">This page lists what the fall menu is &mdash; bases and pairings, as
  reported by The Bend Magazine. Numbers and any of-the-day items live on the board at the
  cafe, so the menu can move with the season.</p>
  <div class="ctarow center"><a class="btn" href="/visit">Hours &amp; directions</a>
  <a class="btn ghost" href="/contact">Ask the counter a question</a></div>
</div></section>
''',
    ld(MENU_LDS))

# ---------------------------------------------------------------- ESPRESSO DETAIL
ESP_LDS = {"@graph": [
    {"@type": "WebPage", "name": "Signature espresso drinks and flavor combos — CoPa Café, Corpus Christi TX",
     "url": ORIGIN + "/espresso-bar-corpus-christi", "isPartOf": {"@id": ORIGIN + "/#website"}},
    crumb([("Home", "/"), ("Menu", "/menu"), ("Espresso bar", "/espresso-bar-corpus-christi")]),
    {"@type": "Service", "name": "Signature espresso drinks with gourmet flavor combinations",
     "serviceType": "Coffee", "areaServed": {"@type": "City", "name": "Corpus Christi"},
     "provider": {"@id": ORIGIN + "/#cafe"}},
    faq([
        ("What exactly is a flavor combination?",
         "The fall menu is built as pairings: you choose your caffeine base, then a combination such as blueberry and cardamom, fig and brown sugar, or pumpkin and cookie butter — the way The Bend Magazine described the ordering experience."),
        ("Can I get my pairing on espresso, matcha or chai?",
         "The pairing program runs across the cafe's bases — espresso, matcha and chai. Ask the counter which pairings are on for your base that day."),
        ("What is cookie butter?",
         "A spread made from spiced cookies — speculoos-style — blended into a smooth, caramelized butter. Paired with pumpkin here instead of the usual pumpkin-spice formula."),
        ("Do you have straight espresso or a plain Americano?",
         "Espresso is the bar's base drink. Whatever you want it to become, the counter will make it that."),
        ("Where is the espresso bar?",
         "Inside Echelon Performance Gym at 1133 County Road 22, Corpus Christi, Texas 78415 — open Monday–Friday 8 a.m.–4 p.m., Saturday 9 a.m.–5 p.m.")])] }

ESP = page(
    "Signature Espresso Drinks &amp; Flavor Combos — CoPa Caf&eacute;, Corpus Christi TX",
    "CoPa Café's espresso bar in Corpus Christi: pick espresso, matcha or chai as a base, then a gourmet pairing — blueberry-cardamom, fig-brown sugar, pumpkin-cookie butter.",
    "/espresso-bar-corpus-christi",
    '''
<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Espresso &middot; Corpus Christi</p>
  <h1>The espresso bar &amp; its pairings</h1>
  <p class="lede">Most cafes ask what size you want. CoPa&rsquo;s counter asks two real
  questions: what base, and what pairing. Espresso is where the pairing program starts.</p>
</div></section>

<section class="band paper"><div class="wrap plate">
  <h2 class="pname bigname">Blueberry &amp; cardamom</h2>
  <p class="tagline">Deep fruit &middot; cool spice</p>
  <p class="bodycopy">Blueberry is fruit with weight and a bass note &mdash; nothing like the
  syrups on the flavored-coffee rack. Cardamom is cool, faintly eucalyptus, a spice that cuts
  rather than coats. Together they read like the dessert-plate pairing they are: the bright
  and the resinous, in the same cup.</p>
</div></section>

<section class="band cream"><div class="wrap plate">
  <h2 class="pname bigname">Fig &amp; brown sugar</h2>
  <p class="tagline">Jammy fruit &middot; molasses depth</p>
  <p class="bodycopy">Fig brings jam and a hint of seedy texture; brown sugar brings the
  molasses roundness that dark-roast espresso is already reaching for. This is the subtle one
  of the fall board &mdash; it tastes like it belongs to whoever ordered it.</p>
</div></section>

<section class="band t-cookie-bg"><div class="wrap plate">
  <h2 class="pname bigname">Pumpkin &amp; cookie butter</h2>
  <p class="tagline">Squash sweetness &middot; spiced-cookie richness</p>
  <p class="bodycopy">Every cafe does pumpkin this time of year. CoPa does pumpkin paired with
  cookie butter &mdash; the caramelized, spiced-cookie spread &mdash; so the fall drink lands
  closer to a cookie at the bottom of the cup than to a spice jar.</p>
</div></section>

<section class="band paper"><div class="wrap narrow">
  <p class="eyebrow">More than the three</p>
  <h2 class="sec">&ldquo;And more&rdquo; is part of the menu</h2>
  <p class="bodycopy">The Bend Magazine&rsquo;s fall-menu report lists these three pairings and
  then &mdash; correctly &mdash; &ldquo;and more.&rdquo; The board at the counter is the live
  list; this page keeps the named ones. The pairings work on the cafe&rsquo;s bases: espresso,
  matcha or chai. Cold brew stays unbothered.</p>
  <div class="ctarow"><a class="btn" href="/matcha-chai-corpus-christi">Matcha, chai &amp; cold brew</a>
  <a class="btn ghost" href="/menu">Back to the fall menu</a></div>
</div></section>
''',
    ld(ESP_LDS))

# ---------------------------------------------------------------- MATCHA/CHAI/COLD BREW
MCC_LDS = {"@graph": [
    {"@type": "WebPage", "name": "Matcha, chai and cold brew — CoPa Café, Corpus Christi TX",
     "url": ORIGIN + "/matcha-chai-corpus-christi", "isPartOf": {"@id": ORIGIN + "/#website"}},
    crumb([("Home", "/"), ("Menu", "/menu"), ("Matcha, chai & cold brew", "/matcha-chai-corpus-christi")]),
    {"@type": "Service", "name": "Matcha, chai and cold brew",
     "serviceType": "Tea and coffee beverages", "areaServed": {"@type": "City", "name": "Corpus Christi"},
     "provider": {"@id": ORIGIN + "/#cafe"}},
    faq([
        ("Do you take matcha seriously here?",
         "Yes — matcha is one of the cafe's three named bases, per The Bend Magazine's fall-menu report, and it feeds into the same pairing program as espresso."),
        ("What kind of chai?",
         "Chai is one of the cafe's bases — spiced tea, with the pairing program available on top of it."),
        ("Is the cold brew any good?",
         "The fall menu report points it out for exactly that: cold-brew lovers 'without the fluff' are covered — slow-steeped coffee, straight."),
        ("Can kids get something here?",
         "Matcha and chai bases are tea-forward; the plainest cold brew is an option too. Ask the counter."),
        ("Where is it?",
         "Inside Echelon Performance Gym, 1133 County Road 22, Corpus Christi, TX 78415. Mon–Fri 8 a.m.–4 p.m., Sat 9 a.m.–5 p.m., closed Sunday.")])] }

MCC = page(
    "Matcha, Chai &amp; Cold Brew — CoPa Caf&eacute;, Corpus Christi TX",
    "CoPa Café serves matcha and chai as full bases with gourmet pairings, plus plain cold brew for purists — a specialty micro cafe inside Echelon Performance Gym, Corpus Christi, TX.",
    "/matcha-chai-corpus-christi",
    '''
<section class="band t-matcha-bg herol"><div class="wrap">
  <p class="eyebrow">Tea &amp; cold brew &middot; Corpus Christi</p>
  <h1>Matcha, chai &amp; cold brew</h1>
  <p class="lede">&ldquo;The drinks focus on espresso, matcha and chai&rdquo; &mdash; what The
  Bend Magazine saw on the fall menu. Tea here is a base, not a consolation prize. And cold
  brew stays exactly itself.</p>
</div></section>

<section class="band paper"><div class="wrap plates2">
  <div class="platecard">
    <h2 class="pname">Matcha</h2>
    <p class="tagline">Ground green tea, whisked into the menu&rsquo;s center</p>
    <p class="bodycopy">Matcha is the whole leaf, stone-ground and whisked, so it carries the
    green-tea bitterness with it rather than drowning it in milk. On this board it can also
    wear a pairing &mdash; blueberry-cardamom reads differently, and better, on a grassy base.</p>
  </div>
  <div class="platecard">
    <h2 class="pname">Chai</h2>
    <p class="tagline">Spiced tea, built for a pairing too</p>
    <p class="bodycopy">Chai&rsquo;s own spice work &mdash; cardamom up front, warm layers
    behind &mdash; makes it the base that argues least with the flavor combinations. Fig and
    brown sugar on chai is a quiet winter-drink move.</p>
  </div>
</div></section>

<section class="band ink"><div class="wrap plate">
  <h2 class="pname bigname light">Cold brew</h2>
  <p class="tagline">Slow-steeped coffee &middot; no fluff</p>
  <p class="bodycopy">&ldquo;Fear not, cold brew lovers without the fluff; they&rsquo;ve got
  that, too&rdquo; &mdash; the magazine&rsquo;s line says it plainly. Slow-steeped, served as
  coffee: no pairing required, no syrup pilgrimage, in and out before leg day.</p>
  <div class="ctarow"><a class="btn gold" href="/espresso-bar-corpus-christi">The espresso bar &amp; pairings</a>
  <a class="btn ghost" href="/menu">Back to the fall menu</a></div>
</div></section>

<section class="band cream"><div class="wrap narrow">
  <p class="eyebrow">At the counter</p>
  <h2 class="sec">Hours &amp; where to find the cup</h2>
  <p class="bodycopy">Inside Echelon Performance Gym at 1133 County Rd 22, Corpus Christi.
  Monday&ndash;Friday 8 a.m. to 4 p.m., Saturday 9 a.m. to 5 p.m., Sunday closed. Follow
  <a href="{IG}" rel="noopener">the cafe&rsquo;s Instagram</a> for board changes.</p>
  <div class="ctarow"><a class="btn" href="/visit">Directions</a>
  <a class="btn ghost" href="/contact">Send a note</a></div>
</div></section>
'''.replace("{IG}", IG),
    ld(MCC_LDS))

# ---------------------------------------------------------------- VISIT
VISIT_LDS = {"@graph": [
    {"@type": "WebPage", "name": "Visit CoPa Café — inside Echelon Performance Gym, Corpus Christi TX",
     "url": ORIGIN + "/visit", "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@id": ORIGIN + "/#cafe"}},
    crumb([("Home", "/"), ("Visit", "/visit")]),
    faq([
        ("Where exactly is CoPa Café?",
         "Inside Echelon Performance Gym, 1133 County Road 22, Corpus Christi, TX 78415 — in the London District area. It's a micro cafe, so the sign to look for is the gym's."),
        ("What are the hours?",
         "Monday through Friday 8 a.m. to 4 p.m.; Saturday 9 a.m. to 5 p.m.; closed Sunday."),
        ("Is there parking?",
         "It's a gym — park where gym members do, at Echelon Performance Gym's lot at 1133 County Road 22."),
        ("How do we reach the cafe before a visit?",
         "Email copacafecc@gmail.com or use the contact form; the team answers there.")])] }

VISIT = page(
    "Visit: Inside Echelon Performance Gym — CoPa Caf&eacute;, Corpus Christi TX",
    "CoPa Café is inside Echelon Performance Gym at 1133 County Rd 22, Corpus Christi, TX 78415. Hours: Mon–Fri 8–4, Sat 9–5, Sun closed. Directions, hours and contacts.",
    "/visit",
    f'''
<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Visit</p>
  <h1>Look past the gym&rsquo;s sign</h1>
  <p class="lede">Echelon Performance Gym gets the signage on County Road 22 &mdash; the cafe
  is inside it, in the London District area of Corpus Christi. Small counter, big pairing
  program.</p>
</div></section>

<section class="band cream"><div class="wrap cardgrid">
  <div class="infocard"><h3 class="infh">Address</h3>
    <address class="addr">{ADDRESS_HTML}</address>
    <p class="note">Inside Echelon Performance Gym. Park with the gym.</p>
    <p class="bigm"><a href="https://www.google.com/maps/dir/?api=1&amp;destination={MAP_Q}" rel="noopener">Get directions</a></p></div>
  <div class="infocard"><h3 class="infh">Hours</h3>
    <dl class="factlist">
      <div><dt>Mon&ndash;Fri</dt><dd>8 a.m. &ndash; 4 p.m.</dd></div>
      <div><dt>Saturday</dt><dd>9 a.m. &ndash; 5 p.m.</dd></div>
      <div><dt>Sunday</dt><dd>Closed</dd></div>
    </dl></div>
  <div class="infocard"><h3 class="infh">Reach the counter</h3>
    <p class="note">Email <a href="mailto:{EMAIL}">{EMAIL}</a> or use the
    <a href="/contact">contact form</a>.</p>
    <p class="note">Board changes land on <a href="{IG}" rel="noopener">Instagram</a>
    &middot; <a href="{FB}" rel="noopener">Facebook</a>.</p></div>
</div></section>

<section class="band paper"><div class="wrap">
  <div class="mapcell"><iframe src="https://www.google.com/maps?q={MAP_Q}&amp;output=embed"
    title="Map: CoPa Café, 1133 County Rd 22, Corpus Christi, TX 78415" loading="lazy"></iframe></div>
  <p class="fineprint">Map: 1133 County Rd 22, Corpus Christi, TX 78415 &mdash; Echelon Performance Gym.</p>
</div></section>

<section class="band ink"><div class="wrap narrow center">
  <h2 class="sec light">Before you come</h2>
  <p class="secsub">Read the fall menu &mdash; the bases, the three named pairings, and where
  cold brew fits.</p>
  <div class="ctarow"><a class="btn gold" href="/menu">See the fall menu</a>
  <a class="btn ghost" href="/contact">Send a note</a></div>
</div></section>
''',
    ld(VISIT_LDS))

# ---------------------------------------------------------------- CONTACT
CONTACT_LDS = {"@graph": [
    {"@type": "WebPage", "name": "Contact CoPa Café — Corpus Christi TX", "url": ORIGIN + "/contact",
     "isPartOf": {"@id": ORIGIN + "/#website"}, "about": {"@id": ORIGIN + "/#cafe"}},
    crumb([("Home", "/"), ("Contact", "/contact")])]}

CONTACT = page(
    "Contact CoPa Caf&eacute; — Corpus Christi TX",
    "Questions for CoPa Café in Corpus Christi: menu, pairings, hours or catering at the gym. The form and copacafecc@gmail.com both reach the counter.",
    "/contact",
    f'''
<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1>Send the counter a note</h1>
  <p class="lede">Menu questions, pairing requests, hours, catering for the gym floor
  &mdash; this form lands with the cafe, same as email to {EMAIL}.</p>
</div></section>

<section class="band paper"><div class="wrap contactgrid">
  <div class="formside"><form class="cform" method="post" action="/contact" accept-charset="utf-8">
    <h2 class="infh">Leave a note</h2>
    <div class="fields">
      <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field full"><label for="f-email">Email <span class="opt">(optional &mdash; so we can answer)</span></label><input id="f-email" name="email" type="email" autocomplete="email"></div>
      <div class="field full"><label for="f-msg">Your message</label><textarea id="f-msg" name="message" required></textarea></div>
    </div>
    <p class="formnote">Notes are read in the order they arrive.</p>
    <button class="btn full" type="submit">Send it</button>
  </form></div>
  <aside class="infocard"><h3 class="infh">Other ways</h3>
    <p class="note">Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <address class="addr">{ADDRESS_HTML}</address>
    <p class="note">Hours: Mon&ndash;Fri 8&ndash;4 &middot; Sat 9&ndash;5 &middot; Sun closed.</p>
    <p class="note">Instagram: <a href="{IG}" rel="noopener">copa.cafe.llc</a> &middot;
    <a href="{FB}" rel="noopener">the Facebook page</a></p>
    <p class="note">Seen in: <a href="{BEND}" rel="noopener">The Bend Magazine &mdash; Table Talk</a></p>
  </aside>
</div></section>
''',
    ld(CONTACT_LDS))

# ---------------------------------------------------------------- PRIVACY
PRIVACY_LDS = {"@graph": [
    {"@type": "WebPage", "name": "Privacy — CoPa Café, Corpus Christi TX", "url": ORIGIN + "/privacy",
     "isPartOf": {"@id": ORIGIN + "/#website"}},
    crumb([("Home", "/"), ("Privacy", "/privacy")])]}

PRIVACY = page(
    "Privacy — CoPa Caf&eacute;, Corpus Christi TX",
    "How CoPa Café's website handles the contact form: what it collects, what it doesn't, and who reads it.",
    "/privacy",
    f'''
<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Privacy</p>
  <h1>What this site does with your information</h1>
</div></section>

<section class="band paper"><div class="wrap narrow">
  <h2 class="sec">The contact form</h2>
  <p class="bodycopy">The form asks for a name and a message, and optionally a phone number and
  an email address. Those details go to CoPa Caf&eacute; so the counter can answer you
  &mdash; nothing else. Notes are kept only as long as it takes to reply and settle whatever
  you asked about.</p>
  <h2 class="sec">No cookies, no trackers</h2>
  <p class="bodycopy">This site sets no cookies, runs no advertising pixels and loads no
  third-party scripts. There is no analytics software watching your visit and nothing to opt
  out of.</p>
  <h2 class="sec">The map</h2>
  <p class="bodycopy">The Visit page embeds a Google Maps view. When that map loads, Google
  receives the standard request data of your browser (including its IP address), under
  Google&rsquo;s own privacy terms. Every other page loads without contacting Google.</p>
  <h2 class="sec">Questions about your note</h2>
  <p class="bodycopy">Ask the cafe through the <a href="/contact">contact form</a> to see,
  correct or delete what a note contains. We will honor it.</p>
  <p class="note">Postal address: {NAP_LINE}.</p>
</div></section>
''',
    ld(PRIVACY_LDS))

# ---------------------------------------------------------------- 404 / THANKS
THANKS = page(
    "Thank You — CoPa Caf&eacute;",
    "Your note has reached CoPa Café. The counter answers messages in the order they arrive.",
    "/thanks",
    '''
<section class="band t-matcha-bg herol"><div class="wrap narrow center">
  <p class="eyebrow">Note received</p>
  <h1>Your message is in.</h1>
  <p class="lede">The counter reads every note and answers in the order they arrive. Board
  changes land on Instagram first.</p>
  <div class="ctarow center"><a class="btn" href="/">Back to the front page</a>
  <a class="btn ghost" href="/menu">See the fall menu</a></div>
</div></section>
''', None, og=False)

E404 = page(
    "Page Not Found — CoPa Caf&eacute;",
    "That page isn't here. The fall menu, the pairing pages and the visit page are one click away.",
    "/404",
    '''
<section class="band cream herol"><div class="wrap narrow center">
  <p class="eyebrow">404</p>
  <h1>That page went cold.</h1>
  <p class="lede">No cup at this address. Try one of these:</p>
  <div class="ctarow center"><a class="btn" href="/">Front page</a>
  <a class="btn ghost" href="/menu">Fall menu</a>
  <a class="btn ghost" href="/contact">Contact</a></div>
</div></section>
''', None, og=False)

# ---------------------------------------------------------------- sitemap / robots
PAGES_SITEMAP = ["/", "/menu", "/espresso-bar-corpus-christi", "/matcha-chai-corpus-christi",
                 "/visit", "/contact", "/privacy"]
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
for pp in PAGES_SITEMAP:
    sitemap += f'<url><loc>{ORIGIN}/</loc><lastmod>{BUILT}</lastmod></url>\n' if pp == "/" else f'<url><loc>{ORIGIN}{pp}</loc><lastmod>{BUILT}</lastmod></url>\n'
sitemap += "</urlset>\n"

robots = f"""User-agent: *
Disallow: /thanks
Disallow: /404

Sitemap: {ORIGIN}/sitemap.xml
"""

FILES = {"index.html": HOME, "menu.html": MENU, "espresso-bar-corpus-christi.html": ESP,
         "matcha-chai-corpus-christi.html": MCC, "visit.html": VISIT,
         "contact.html": CONTACT, "privacy.html": PRIVACY, "thanks.html": THANKS, "404.html": E404,
         "sitemap.xml": sitemap, "robots.txt": robots}

os.makedirs(PUBLIC, exist_ok=True)
for name, content in FILES.items():
    with open(os.path.join(PUBLIC, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name, len(content.encode("utf-8")), "bytes")

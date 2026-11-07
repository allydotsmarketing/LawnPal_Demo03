#!/usr/bin/env python3
"""Builds the LawnPal demo as plain static HTML.

Edit tools/site.json (name, phone, cities…) and the content below,
then run:  python3 tools/build.py
Output goes to the repo root, ready for GitHub Pages.
"""
import html
import json
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
S = json.loads((ROOT / "tools" / "site.json").read_text())
E = html.escape

# ---------------------------------------------------------------- icons
ICON = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/><path d="M8.5 10.5c.5 2 2.5 4 4.5 4.5l1.3-1.3 2.2 1-.4 1.8c-3.6.3-8.2-4.3-7.9-7.9l1.8-.4 1 2.2Z"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/>',
    "quote": '<path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2Z"/><path d="M9 13h6M9 17h4"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "instagram": '<rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><path d="M17.5 6.5h.01"/>',
    "pinterest": '<circle cx="12" cy="12" r="10"/><path d="m9.5 21 2.2-9.3"/><path d="M10.6 15.3c.5.6 1.3 1 2.2 1 2.4 0 4-2.1 4-4.7 0-2.8-2.2-4.6-4.9-4.6-3 0-5 2.1-5 4.6 0 1 .4 2 1.1 2.5"/>',
}


def icon(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>')


def wa(text):
    return f"https://wa.me/{S['whatsapp']}?text=" + urllib.parse.quote(text)


WA_GENERAL = wa(f"Hi {S['name']}! I'd like a free quote. My address or ZIP code is: ")


def wa_for(service):
    return wa(f"Hi {S['name']}! I'd like a free quote for {service}. My address or ZIP code is: ")


# ---------------------------------------------------------------- content
SERVICES = [
    {
        "slug": "lawn-mowing-edging",
        "name": "Lawn Mowing & Edging",
        "lower": "lawn mowing & edging",
        "img": "mowing-push-mower.jpg",
        "alt": "Lawn care worker mowing a residential lawn beside a house",
        "img2": "curb-edging.jpg",
        "alt2": "Freshly edged lawn along a curb and sidewalk",
        "short": "Even cuts, sharp edges along every sidewalk and bed, and clippings cleared before we leave.",
        "bullets": ["Weekly or every-other-week visits", "Edging on every hard surface", "Clippings blown off before we go"],
        "meta": "Lawn mowing and edging in Fort Lauderdale & Tamarac, FL. Even cuts, crisp edges and clean walkways for homes and small businesses. Free quotes.",
        "intro": "A clean cut and a crisp edge make the whole property look cared for. We mow at the right height for your grass, edge every hard surface, trim where the mower can't reach, and blow off the clippings before we go.",
        "includes": [
            "Mowing at the right height for your grass",
            "Edging along sidewalks, driveways and curbs",
            "String trimming around trees, fences and beds",
            "Clipping cleanup on walkways and patios",
            "Weekly or every-other-week visits",
            "Homes and small commercial properties",
        ],
        "local_h": "Cut for South Florida grass",
        "local": "Most lawns here are St. Augustine grass, which stays healthiest when it's kept on the taller side. In the rainy season, from late spring through fall, grass grows fast, and that's when regular visits matter most.",
        "faqs": [
            ("How often should my lawn be mowed?", "In the rainy season most South Florida lawns need a cut every week or every two weeks. In the drier months, every two weeks is usually enough."),
            ("Do you clean up after mowing?", "Yes. Every visit ends with clippings blown off sidewalks, driveways and patios."),
            ("Do you mow commercial properties?", "Yes. We take care of homes and small commercial properties."),
        ],
    },
    {
        "slug": "hedge-shrub-trimming",
        "name": "Hedge & Shrub Trimming",
        "lower": "hedge & shrub trimming",
        "img": "hedge-trimming.jpg",
        "alt": "Hedge trimmer shaping a round evergreen shrub",
        "img2": "hedge-trimmer-closeup.jpg",
        "alt2": "Close-up of a hedge trimmer cutting along a tall hedge",
        "short": "Hedges, shrubs and garden plants shaped neatly and kept clear of walls, windows and walkways.",
        "bullets": ["Hedge shaping and leveling", "Shrubs kept off walls and paths", "All cuttings hauled away"],
        "meta": "Hedge and shrub trimming in Fort Lauderdale & Tamarac, FL. Neat, even hedges and tidy garden beds, with all cuttings removed. Free quotes.",
        "intro": "Overgrown hedges make a yard look neglected fast. We shape hedges and shrubs, keep plants off walls, windows and walkways, and haul away the cuttings.",
        "includes": [
            "Hedge shaping and leveling",
            "Shrub and bush trimming",
            "Plants cut back from walls, windows and paths",
            "Garden bed tidy-up",
            "All cuttings removed",
            "One-time or recurring service",
        ],
        "local_h": "Kept in shape all year",
        "local": "South Florida's heat and rain keep hedges growing almost year-round. Regular trimming keeps them dense and even instead of thin and overgrown.",
        "faqs": [
            ("How often should hedges be trimmed?", "Most hedges here look their best trimmed every one to two months during the growing season."),
            ("Do you take the cuttings away?", "Yes. We clean up and remove all cuttings when we're done."),
            ("Can trimming be part of a maintenance plan?", "Yes. Hedge and shrub trimming can be added to the biweekly maintenance plan."),
        ],
    },
    {
        "slug": "yard-leaf-cleanup",
        "name": "Yard & Leaf Cleanup",
        "lower": "yard & leaf cleanup",
        "img": "leaf-cleanup-blower.webp",
        "alt": "Worker with a backpack blower clearing dry leaves from a backyard lawn",
        "img2": "edging-string-trimmer.jpg",
        "alt2": "Worker trimming grass and leaves around a large tree",
        "short": "Dry leaves, fallen branches and overgrowth cleared from the front yard, backyard and beds.",
        "bullets": ["Dry leaves and debris removed", "Backyards and side yards", "One-time or seasonal"],
        "meta": "Yard and leaf cleanup in Fort Lauderdale & Tamarac, FL. Dry leaves, branches and overgrowth cleared from front yards and backyards. Free quotes.",
        "intro": "Whether it's a backyard that got away from you or weeks of fallen leaves, we clear it out and leave the property clean and ready for regular care.",
        "includes": [
            "Dry leaf removal",
            "Backyard and side-yard cleanup",
            "Overgrown areas cleared",
            "Small branches and debris removed",
            "Beds and walkways cleaned up",
            "One-time or seasonal cleanups",
        ],
        "local_h": "A fresh start for the yard",
        "local": "A cleanup is often the first visit before regular maintenance begins. Once the yard is clear, the biweekly plan keeps it that way.",
        "faqs": [
            ("Is a cleanup a one-time service?", "It can be. Many customers book a one-time cleanup, and some follow it with the biweekly plan."),
            ("Do you haul away the debris?", "Yes. Leaves, branches and yard debris are removed as part of the cleanup."),
            ("Can you clean up a very overgrown yard?", "Yes. Send us a photo on WhatsApp and we'll quote it."),
        ],
    },
    {
        "slug": "weed-control-fertilization",
        "name": "Weed Control & Fertilization",
        "lower": "weed control & fertilization",
        "img": "fertilization-before-after.webp",
        "card": "florida-lawn-palms.jpg",
        "alt": "Before and after: a dry, patchy lawn next to the same lawn green and full",
        "img2": "florida-lawn-palms.jpg",
        "alt2": "Wide green lawn with palm trees and trimmed hedges",
        "short": "Treatments that keep weeds down and help your grass stay thick, green and healthy.",
        "bullets": ["Weed treatment for lawns and beds", "Fertilization on a schedule", "Thin, patchy areas fill back in"],
        "meta": "Weed control and lawn fertilization in Fort Lauderdale & Tamarac, FL. Fewer weeds and greener, thicker grass all year. Free quotes.",
        "intro": "A thick, healthy lawn is the best defense against weeds. We treat weeds and feed your grass on a schedule so the lawn stays green and even through the year.",
        "includes": [
            "Weed treatment for lawn areas",
            "Lawn fertilization",
            "Weeds in beds and walkway cracks",
            "Scheduled follow-up visits",
            "Advice on watering and mowing height",
            "Homes and small commercial lawns",
        ],
        "local_h": "Greener grass, fewer weeds",
        "local": "Florida's warm weather helps weeds as much as it helps grass. Treatments on a regular schedule keep weeds from taking over and help thin, patchy areas fill back in.",
        "faqs": [
            ("How long until I see results?", "Most lawns start looking greener within a few weeks. Weeds and thin areas take a few treatments to fully improve."),
            ("Can weed control be part of my maintenance plan?", "Yes. It can be added to the biweekly maintenance plan."),
            ("Do you treat weeds in flower beds?", "Yes, along with weeds in walkway and driveway cracks."),
        ],
    },
]

HOME_FAQS = [
    ("What areas do you serve?", f"We work in {', '.join(S['areas'][:-1])} and {S['areas'][-1]}. Not sure about your street? Call or text us your ZIP code."),
    ("Is the quote free?", "Yes. Quotes are free and there's no obligation. Call, send a WhatsApp message or fill out the quote form."),
    ("What's included in the biweekly plan?", "Two visits a month: mowing, edging, string trimming and clipping cleanup every time. Hedge trimming, weed control and cleanups can be added."),
    ("Are you licensed and insured?", f"Yes. {S['name']} is licensed and insured, with {S['years']} years of experience in lawn care."),
    ("Do you work with homes and businesses?", "Yes. We take care of residential properties and small commercial properties."),
]

PLAN = {
    "slug": "biweekly-lawn-maintenance",
    "name": "Biweekly Maintenance Plan",
    "img": "maintenance-striped-lawn.webp",
    "alt": "Freshly mowed striped lawn in front of a Florida home with palm trees",
}


# ---------------------------------------------------------------- shared parts
def head(root, title, desc, path, extra_ld=None):
    robots = '<meta name="robots" content="noindex, nofollow">' if S["noindex"] else ""
    ld = [business_ld()] + (extra_ld or [])
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x)}</script>' for x in ld)
    url = S["base_url"] + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{robots}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{S['base_url']}assets/img/hero-crew-mowing.webp">
<meta name="theme-color" content="#386641">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Figtree:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/styles.css">
{ld_html}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def business_ld():
    return {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": S["name"],
        "url": S["base_url"],
        "telephone": S["phone_tel"],
        "image": S["base_url"] + "assets/img/hero-crew-mowing.webp",
        "address": {"@type": "PostalAddress", "addressRegion": "FL", "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": f"{c}, FL"} for c in S["areas"]],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "08:00", "closes": "17:00",
        }],
    }


def header(root, current):
    def cur(key):
        return ' aria-current="page"' if key == current else ""
    sub = "".join(
        f'<li><a href="{root}services/{s["slug"]}/"{cur(s["slug"])}>{E(s["name"])}</a></li>' for s in SERVICES)
    home = root or "./"
    return f"""<header class="site-header">
  <div class="container header-inner">
    <a class="logo" href="{home}" aria-label="{S['name']} home"><span class="logo-mark" aria-hidden="true"></span>{S['name']}</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">{icon('menu')}</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav-list">
        <li>
          <button class="nav-link" data-submenu aria-expanded="false" aria-controls="services-menu">Services {icon('chevron')}</button>
          <ul class="submenu" id="services-menu">{sub}</ul>
        </li>
        <li><a class="nav-link" href="{root}{PLAN['slug']}/"{cur('plan')}>Maintenance plan</a></li>
        <li><a class="nav-link" href="{root}gallery/"{cur('gallery')}>Gallery</a></li>
        <li><a class="nav-link" href="{root}about/"{cur('about')}>About</a></li>
        <li><a class="nav-link" href="{home}#areas">Service areas</a></li>
        <li><a class="nav-link" href="{root}contact/"{cur('contact')}>Contact</a></li>
      </ul>
      <div class="nav-mobile-cta">
        <a class="btn btn--primary" href="tel:{S['phone_tel']}">{icon('phone')} Call {S['phone_display']}</a>
        <a class="btn btn--outline" href="{root}contact/">Get a free quote</a>
      </div>
    </nav>
    <div class="header-cta">
      <a class="header-phone" href="tel:{S['phone_tel']}">{S['phone_display']}</a>
      <a class="btn btn--primary" href="{root}contact/">Free quote</a>
    </div>
  </div>
</header>
"""


def footer(root):
    home = root or "./"
    svc = "".join(f'<li><a href="{root}services/{s["slug"]}/">{E(s["name"])}</a></li>' for s in SERVICES)
    areas = ", ".join(S["areas"])
    ig = S["instagram"] or "#"
    pin = S["pinterest"] or "#"
    return f"""<div class="mow mow--thin" aria-hidden="true"></div>
<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-about">
      <a class="logo" href="{home}"><span class="logo-mark" aria-hidden="true"></span>{S['name']}</a>
      <p>Lawn care and landscaping for homes and small businesses in Broward County. Licensed and insured, {S['years']} years of experience.</p>
      <div class="socials">
        <a href="{ig}" aria-label="{S['name']} on Instagram">{icon('instagram')}</a>
        <a href="{pin}" aria-label="{S['name']} on Pinterest">{icon('pinterest')}</a>
      </div>
    </div>
    <div>
      <h2>Services</h2>
      <ul>{svc}<li><a href="{root}{PLAN['slug']}/">Biweekly maintenance plan</a></li></ul>
    </div>
    <div>
      <h2>Company</h2>
      <ul>
        <li><a href="{root}about/">About us</a></li>
        <li><a href="{root}gallery/">Gallery</a></li>
        <li><a href="{home}#areas">Service areas</a></li>
        <li><a href="{home}#faq">FAQ</a></li>
        <li><a href="{root}contact/">Free quote</a></li>
      </ul>
    </div>
    <div>
      <h2>Contact</h2>
      <ul>
        <li><a href="tel:{S['phone_tel']}">{S['phone_display']}</a></li>
        <li><a href="{WA_GENERAL}">Message on WhatsApp</a></li>
        <li>{S['hours']}</li>
        <li>{areas}</li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© {S['year']} {S['name']}. All rights reserved.</span>
    <span>Website by <a href="{S['credit_url']}" target="_blank" rel="noopener">{S['credit_name']}<span class="visually-hidden"> (opens in a new tab)</span></a></span>
  </div>
</footer>
<nav class="mobile-bar" aria-label="Quick contact">
  <a href="tel:{S['phone_tel']}">{icon('phone')} Call</a>
  <a href="{WA_GENERAL}">{icon('chat')} WhatsApp</a>
</nav>
<script src="{root}assets/js/main.js" defer></script>
</body>
</html>
"""


def contact_buttons(wa_link, light=False):
    if light:
        return f"""<div class="btn-row">
  <a class="btn btn--light" href="tel:{S['phone_tel']}">{icon('phone')} Call {S['phone_display']}</a>
  <a class="btn btn--ghost-light" href="{wa_link}">{icon('chat')} Message on WhatsApp</a>
</div>"""
    return f"""<div class="btn-row">
  <a class="btn btn--primary" href="tel:{S['phone_tel']}">{icon('phone')} Call {S['phone_display']}</a>
  <a class="btn btn--outline" href="{wa_link}">{icon('chat')} Message on WhatsApp</a>
</div>"""


def checks(items, two=False):
    cls = "checks checks--two" if two else "checks"
    lis = "".join(f"<li>{icon('check')}<span>{E(i)}</span></li>" for i in items)
    return f'<ul class="{cls}">{lis}</ul>'


def faq_block(faqs):
    items = "".join(
        f'<details><summary>{E(q)}{icon("plus")}</summary><div class="answer"><p>{E(a)}</p></div></details>'
        for q, a in faqs)
    return f'<div class="faq">{items}</div>'


def faq_ld(faqs):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }


def crumbs_ld(items):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": S["base_url"] + p}
                            for i, (n, p) in enumerate(items)],
    }


def crumbs(root, items):
    lis = []
    for i, (name, path) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{E(name)}</li>')
        else:
            lis.append(f'<li><a href="{root}{path}">{E(name)}</a></li>' if path else
                       f'<li><a href="{root or "./"}">{E(name)}</a></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'


def cta_band(wa_link, title="Ready for a cleaner yard?"):
    return f"""<section class="cta-band" aria-labelledby="cta-title">
  <div class="mow" aria-hidden="true"></div>
  <div class="container">
    <h2 id="cta-title">{E(title)}</h2>
    <p class="lede">Call for a free quote, or send us a message on WhatsApp with your address and a photo of the yard.</p>
    <a class="phone-big" href="tel:{S['phone_tel']}" aria-label="Call {S['phone_display']}">{S['phone_display']}</a>
    <a class="btn btn--light" href="{wa_link}">{icon('chat')} Message on WhatsApp</a>
  </div>
</section>
"""


def calendar():
    dows = "".join(f'<span class="dow">{d}</span>' for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
    days = []
    visits = {2, 14}  # Tuesday of week 1 and week 3
    for n in range(1, 25):
        if n in visits:
            days.append(f'<span class="day visit">Visit</span>')
        else:
            days.append('<span class="day" aria-hidden="true"></span>')
    return f"""<figure class="calendar" aria-label="Example month with two visits, every other Tuesday">
  <div class="calendar-head">
    <span class="calendar-title">One month, two visits</span>
    <span class="calendar-legend">Visit day</span>
  </div>
  <div class="calendar-grid">{dows}{''.join(days)}</div>
  <p class="calendar-foot">Same day of the week, every other week. Example shown: every other Tuesday.</p>
</figure>"""


def map_src(query, zoom):
    return ("https://maps.google.com/maps?q=" + urllib.parse.quote(query) +
            f"&t=m&z={zoom}&ie=UTF8&iwloc=&output=embed")


def areas_section(cream=False):
    county = "Broward County, FL"
    items = "".join(
        f'<li><button class="area" type="button" data-map="{E(map_src(c + ", FL", 13))}" aria-pressed="false">'
        f'{icon("pin")}<span>{E(c)}</span></button></li>'
        for c in S["areas"])
    cls = "section section--cream" if cream else "section"
    return f"""  <section class="{cls}" id="areas" aria-labelledby="areas-title">
    <div class="container">
      <div class="section-head">
        <h2 id="areas-title">Where we work</h2>
        <p class="lede">We cover these cities across Broward County. Choose a city to see it on the map. Don't see your area? Call or text us your ZIP code.</p>
      </div>
      <div class="areas-map">
        <div class="map-frame">
          <iframe id="area-map" title="Map of the {S['name']} service area in Broward County, Florida" src="{E(S.get('map_embed') or map_src(county, 10))}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>
        <div class="areas-side">
          <ul class="areas">{items}</ul>
          <button class="text-link map-reset" type="button" data-map="{E(S.get('map_embed') or map_src(county, 10))}">Show all of Broward County</button>
        </div>
      </div>
    </div>
  </section>"""


def write(path, content):
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content)
    print("wrote", path)


# ---------------------------------------------------------------- pages
def home():
    root = ""
    title = f"Lawn Care & Landscaping in {S['primary_cities']}, FL | {S['name']}"
    desc = (f"Lawn mowing, edging, hedge trimming, yard cleanup and weed control in {S['primary_cities']}, FL. "
            f"Licensed & insured, {S['years']} years of experience. Free quotes.")
    service_items = "".join(f"""
      <article class="service">
        <a class="service-img" href="services/{s['slug']}/" tabindex="-1" aria-hidden="true"><img src="assets/img/{s.get('card', s['img'])}" alt="" loading="lazy" width="1200" height="800"></a>
        <h3><a href="services/{s['slug']}/">{E(s['name'])}</a></h3>
        <p>{E(s['short'])}</p>
        {checks(s['bullets'])}
        <p><a class="text-link" href="services/{s['slug']}/">More about {E(s['lower'])}</a></p>
      </article>""" for s in SERVICES)
    body =f"""{head(root, title, desc, "", [faq_ld(HOME_FAQS)])}{header(root, 'home')}
<main id="main">
  <section class="hero">
    <div class="hero-copy">
      <h1>Lawn care and landscaping in {S['primary_cities']}</h1>
      <p class="lede">Mowing, edging, hedge trimming, yard cleanup and weed control for homes and small businesses. Licensed, insured and {S['years']} years in South Florida lawns.</p>
      {contact_buttons(WA_GENERAL)}
      <p class="hero-note">Prefer to write it down? <a class="text-link" href="contact/">Request a quote online</a></p>
    </div>
    <div class="hero-media">
      <img src="assets/img/hero-crew-mowing.webp" alt="Lawn crew mowing, fertilizing and trimming a striped lawn on a Florida street" width="1376" height="768" fetchpriority="high">
    </div>
  </section>
  <div class="mow mow--reveal" aria-hidden="true"></div>
  <div class="facts">
    <ul class="container">
      <li>{icon('leaf')}{S['years']} years of experience</li>
      <li>{icon('shield')}Licensed &amp; insured</li>
      <li>{icon('quote')}Free, no-obligation quotes</li>
      <li>{icon('clock')}{S['hours']}</li>
    </ul>
  </div>

  <section class="section" id="services" aria-labelledby="services-title">
    <div class="container">
      <div class="section-head">
        <h2 id="services-title">Services</h2>
        <p class="lede">Everything the yard needs, from the regular cut to the big cleanup.</p>
      </div>
      <div class="services">{service_items}
      </div>
    </div>
  </section>

  <section class="section section--cream" aria-labelledby="plan-title">
    <div class="container split">
      <div class="stack">
        <h2 id="plan-title">Twice a month, every month</h2>
        <p class="lede">With the biweekly maintenance plan, your lawn is mowed, edged and cleaned up every other week on a set schedule. The yard always looks finished, and you never have to call to ask.</p>
        {checks(["Mowing, edging and trimming every visit", "Clippings and debris blown off", "Hedges, weeds and cleanups can be added"])}
        <p><a class="btn btn--primary" href="{PLAN['slug']}/">See the maintenance plan</a></p>
      </div>
      {calendar()}
    </div>
  </section>

  <section class="section" aria-labelledby="how-title">
    <div class="container">
      <div class="section-head"><h2 id="how-title">Getting started is simple</h2></div>
      <ol class="steps">
        <li class="step"><span class="step-num">1</span><h3>Call or message us</h3><p>Tell us your address and what you need. A photo of the yard helps.</p></li>
        <li class="step"><span class="step-num">2</span><h3>Get your free quote</h3><p>We'll give you a clear price with no obligation.</p></li>
        <li class="step"><span class="step-num">3</span><h3>We take care of the yard</h3><p>Pick a day that works and we'll handle the rest.</p></li>
      </ol>
    </div>
  </section>

  <section class="section section--cream" aria-labelledby="diff-title">
    <div class="container split">
      <div class="stack">
        <h2 id="diff-title">The difference regular care makes</h2>
        <p class="lede">Dry, patchy grass can come back green and full with steady mowing, feeding and weed control.</p>
        <h3>Why homeowners choose {S['name']}</h3>
        {checks(["Shows up on the scheduled day", "Clear communication by phone or WhatsApp", "Sharp edges and attention to detail", "Property left clean after every visit", "Homes and small businesses", "Free, no-obligation quotes"])}
      </div>
      <figure class="figure">
        <img src="assets/img/fertilization-before-after.webp" alt="Before and after: a dry, patchy lawn next to the same lawn green and full" width="1000" height="480" loading="lazy">
        <figcaption>Before and after: what fertilization and weed control can do for a tired lawn. <a class="text-link" href="gallery/">See more in the gallery</a></figcaption>
      </figure>
    </div>
  </section>

{areas_section()}

  <section class="section section--cream" id="reviews" aria-labelledby="reviews-title">
    <div class="container split">
      <div class="stack">
        <h2 id="reviews-title">Customer reviews</h2>
        <p class="lede">We only publish real reviews from real customers.</p>
      </div>
      <div class="reviews-empty">
        <h3>Reviews are on the way</h3>
        <p>Reviews from {S['name']} customers will appear here. Had a great visit? Tell us on WhatsApp and we'll share your words with your permission.</p>
      </div>
    </div>
  </section>

  <section class="section" id="faq" aria-labelledby="faq-title">
    <div class="container split" style="align-items:start">
      <div class="stack"><h2 id="faq-title">Questions</h2><p class="lede">Still wondering about something? Call {S['phone_display']}.</p></div>
      {faq_block(HOME_FAQS)}
    </div>
  </section>
</main>
{cta_band(WA_GENERAL)}{footer(root)}"""
    write("index.html", body)


def service_page(s):
    root = "../../"
    path = f"services/{s['slug']}/"
    title = f"{s['name']} in {S['primary_cities']}, FL | {S['name']}"
    service_ld = {
        "@context": "https://schema.org", "@type": "Service",
        "name": s["name"], "serviceType": s["name"],
        "description": s["meta"],
        "provider": {"@type": "HomeAndConstructionBusiness", "name": S["name"], "telephone": S["phone_tel"]},
        "areaServed": [{"@type": "City", "name": f"{c}, FL"} for c in S["areas"]],
        "url": S["base_url"] + path,
    }
    others = [o for o in SERVICES if o["slug"] != s["slug"]]
    related = "".join(
        f'<a href="{root}services/{o["slug"]}/"><img src="{root}assets/img/{o.get("card", o["img"])}" alt="" loading="lazy"><span>{E(o["name"])}</span></a>'
        for o in others)
    wl = wa_for(s["lower"])
    body = f"""{head(root, title, s['meta'], path, [service_ld, faq_ld(s['faqs']), crumbs_ld([("Home", ""), (s['name'], path)])])}{header(root, s['slug'])}
<main id="main">
  <section class="hero page-hero">
    <div class="hero-copy">
      {crumbs(root, [("Home", None), ("Services", "#services"), (s['name'], path)])}
      <h1>{E(s['name'])} in {S['primary_cities']}</h1>
      <p class="lede">{E(s['intro'])}</p>
      {contact_buttons(wl)}
    </div>
    <div class="hero-media">
      <img src="{root}assets/img/{s['img']}" alt="{E(s['alt'])}" fetchpriority="high">
    </div>
  </section>
  <div class="mow mow--reveal" aria-hidden="true"></div>

  <section class="section">
    <div class="container with-aside">
      <div class="main">
        <div>
          <h2>What's included</h2>
          {checks(s['includes'], two=True)}
        </div>
        <div>
          <h2>{E(s['local_h'])}</h2>
          <p class="lede">{E(s['local'])}</p>
          <img class="photo-wide" src="{root}assets/img/{s['img2']}" alt="{E(s['alt2'])}" loading="lazy">
        </div>
        <div>
          <h2>Add it to the biweekly plan</h2>
          <p>Want the yard handled without booking every visit? The <a class="text-link" href="{root}{PLAN['slug']}/">biweekly maintenance plan</a> covers mowing and edging twice a month, and {E(s['lower'])} can be part of it.</p>
        </div>
        <div>
          <h2>Questions about {E(s['lower'])}</h2>
          {faq_block(s['faqs'])}
        </div>
      </div>
      <aside class="aside-card" aria-label="Get a quote">
        <h3>Free quote for {E(s['lower'])}</h3>
        <p>Call or send your address on WhatsApp. Photos of the yard help us quote faster.</p>
        <a class="btn btn--primary" href="tel:{S['phone_tel']}">{icon('phone')} Call {S['phone_display']}</a>
        <a class="btn btn--outline" href="{wl}">{icon('chat')} WhatsApp</a>
        <p><a class="text-link" href="{root}contact/">Or fill out the quote form</a></p>
        <p class="hours">{icon('clock')} {S['hours']}</p>
      </aside>
    </div>
  </section>

  <section class="section section--cream" aria-labelledby="more-title">
    <div class="container">
      <div class="section-head"><h2 id="more-title">More services</h2></div>
      <div class="related">{related}</div>
    </div>
  </section>
</main>
{cta_band(wl)}{footer(root)}"""
    write(path + "index.html", body)


def plan_page():
    root = "../"
    path = f"{PLAN['slug']}/"
    title = f"Biweekly Lawn Maintenance in {S['primary_cities']}, FL | {S['name']}"
    desc = (f"Biweekly lawn maintenance in {S['primary_cities']}, FL: mowing, edging, trimming and cleanup "
            f"twice a month on a set schedule. Free quotes.")
    faqs = [
        ("How does the biweekly schedule work?", "We visit every other week on the same day of the week, so you get two visits a month."),
        ("Can I add other services?", "Yes. Hedge and shrub trimming, weed control and fertilization, and yard cleanups can be added to the plan."),
        ("Can I change my visit day?", "Call or message us and we'll find a day that works."),
        ("What if it rains on my visit day?", "If weather stops a visit, we'll let you know and move it to the next available day."),
    ]
    service_ld = {
        "@context": "https://schema.org", "@type": "Service",
        "name": "Biweekly lawn maintenance", "serviceType": "Lawn maintenance",
        "description": desc,
        "provider": {"@type": "HomeAndConstructionBusiness", "name": S["name"], "telephone": S["phone_tel"]},
        "areaServed": [{"@type": "City", "name": f"{c}, FL"} for c in S["areas"]],
        "url": S["base_url"] + path,
    }
    addons = "".join(
        f'<li>{icon("check")}<span><a class="text-link" href="{root}services/{s["slug"]}/">{E(s["name"])}</a></span></li>'
        for s in SERVICES[1:])
    wl = wa_for("the biweekly maintenance plan")
    body = f"""{head(root, title, desc, path, [service_ld, faq_ld(faqs), crumbs_ld([("Home", ""), ("Biweekly maintenance plan", path)])])}{header(root, 'plan')}
<main id="main">
  <section class="hero page-hero">
    <div class="hero-copy">
      {crumbs(root, [("Home", None), ("Biweekly maintenance plan", path)])}
      <h1>Biweekly lawn maintenance in {S['primary_cities']}</h1>
      <p class="lede">Two visits a month, on a set schedule. Your lawn is mowed, edged and cleaned up every other week, so it always looks finished and you never have to think about it.</p>
      {contact_buttons(wl)}
    </div>
    <div class="hero-media">
      <img src="{root}assets/img/{PLAN['img']}" alt="{E(PLAN['alt'])}" fetchpriority="high">
    </div>
  </section>
  <div class="mow mow--reveal" aria-hidden="true"></div>

  <section class="section">
    <div class="container split">
      <div class="stack">
        <h2>Every visit includes</h2>
        {checks(["Mowing at the right height for your grass", "Edging along sidewalks, driveways and curbs", "String trimming around trees, fences and beds", "Clippings and debris blown off hard surfaces", "A quick look at the lawn's health"])}
      </div>
      {calendar()}
    </div>
  </section>

  <section class="section section--cream">
    <div class="container split">
      <div class="stack">
        <h2>Add what your yard needs</h2>
        <p class="lede">Build the plan around your property. These services can be added to your regular visits.</p>
        <ul class="checks">{addons}</ul>
      </div>
      <div class="stack">
        <h2>Who it's for</h2>
        <p class="lede">Homeowners who want the yard ready for guests any day of the month, and small businesses that need a clean, professional front lawn.</p>
        <p>Starting with an overgrown yard? We'll begin with a <a class="text-link" href="{root}services/yard-leaf-cleanup/">yard cleanup</a>, then keep it in shape with the plan.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container split" style="align-items:start">
      <div class="stack"><h2>Plan questions</h2></div>
      {faq_block(faqs)}
    </div>
  </section>
</main>
{cta_band(wl, "Put your lawn on a schedule")}{footer(root)}"""
    write(path + "index.html", body)


def contact_page():
    root = "../"
    path = "contact/"
    title = f"Free Lawn Care Quote in {S['primary_cities']}, FL | {S['name']}"
    desc = f"Get a free lawn care quote from {S['name']}. Call {S['phone_display']}, message us on WhatsApp or fill out the quote form."
    options = "".join(f'<option value="{E(s["name"])}">{E(s["name"])}</option>' for s in SERVICES)
    body = f"""{head(root, title, desc, path, [crumbs_ld([("Home", ""), ("Free quote", path)])])}{header(root, 'contact')}
<main id="main">
  <section class="hero page-hero">
    <div class="hero-copy">
      {crumbs(root, [("Home", None), ("Free quote", path)])}
      <h1>Get a free quote</h1>
      <p class="lede">Tell us about your property and the service you need. The fastest way is a phone call.</p>
    </div>
    <div class="hero-media">
      <img src="{root}assets/img/striped-lawn-flowers.jpg" alt="Striped green lawn with flowering plants and palm trees" fetchpriority="high">
    </div>
  </section>
  <div class="mow mow--reveal" aria-hidden="true"></div>

  <section class="section">
    <div class="container contact-grid">
      <div class="ways">
        <div class="way">
          <span class="way-label">Call us</span>
          <a class="way-main" href="tel:{S['phone_tel']}">{S['phone_display']}</a>
          <span>{S['hours']}</span>
        </div>
        <div class="way">
          <span class="way-label">Message us</span>
          <a class="way-alt" href="{WA_GENERAL}">WhatsApp</a>
          <span>Send your address and a photo of the yard.</span>
        </div>
        <div class="way">
          <span class="way-label">Service areas</span>
          <span>{', '.join(S['areas'])}</span>
        </div>
      </div>

      <div>
        <form class="form" id="quote-form" novalidate>
          <h2>Request a quote online</h2>
          <div class="form-row">
            <div class="field">
              <label for="name">Name</label>
              <input id="name" name="name" autocomplete="name" aria-describedby="name-error" required>
              <span class="error" id="name-error" aria-live="polite"></span>
            </div>
            <div class="field">
              <label for="phone">Phone</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" aria-describedby="phone-error" required>
              <span class="error" id="phone-error" aria-live="polite"></span>
            </div>
          </div>
          <div class="field">
            <label for="email">Email <span class="opt">(optional)</span></label>
            <input id="email" name="email" type="email" autocomplete="email" aria-describedby="email-error">
            <span class="error" id="email-error" aria-live="polite"></span>
          </div>
          <div class="field">
            <label for="address">Address or ZIP code</label>
            <input id="address" name="address" autocomplete="street-address" aria-describedby="address-error" required>
            <span class="error" id="address-error" aria-live="polite"></span>
          </div>
          <div class="form-row">
            <div class="field">
              <label for="service">Service</label>
              <select id="service" name="service" aria-describedby="service-error" required>
                <option value="">Choose a service</option>
                {options}
                <option value="Biweekly Maintenance Plan">Biweekly Maintenance Plan</option>
                <option value="Not sure yet">Not sure yet</option>
              </select>
              <span class="error" id="service-error" aria-live="polite"></span>
            </div>
            <div class="field">
              <label for="date">Preferred date <span class="opt">(optional)</span></label>
              <input id="date" name="date" type="date">
            </div>
          </div>
          <fieldset class="field">
            <legend>How often?</legend>
            <div class="choices">
              <label class="choice"><input type="radio" name="frequency" value="once" checked><span>One time</span></label>
              <label class="choice"><input type="radio" name="frequency" value="biweekly"><span>Every two weeks</span></label>
              <label class="choice"><input type="radio" name="frequency" value="unsure"><span>Not sure</span></label>
            </div>
          </fieldset>
          <div class="field">
            <label for="message">Anything we should know? <span class="opt">(optional)</span></label>
            <textarea id="message" name="message" placeholder="Yard size, gate code, problem areas…"></textarea>
          </div>
          <div><button class="btn btn--primary" type="submit">Request my free quote</button></div>
          <p class="form-note">We'll only use your details to reply to your request.</p>
        </form>
        <div class="form-success" id="form-success" tabindex="-1" hidden>
          <h2>Thanks, <span id="success-name"></span>. Your request is ready.</h2>
          <p>This is a demo form, so requests aren't sent yet. To get your quote today, call <a class="text-link" href="tel:{S['phone_tel']}">{S['phone_display']}</a> or <a class="text-link" href="{WA_GENERAL}">message us on WhatsApp</a>.</p>
        </div>
      </div>
    </div>
  </section>
</main>
{footer(root)}"""
    write(path + "index.html", body)


def demo_note(text):
    return f'<p class="demo-note"><strong>Provisional:</strong> {text}</p>'


def about_page():
    root = "../"
    path = "about/"
    title = f"About {S['name']} | Lawn Care in {S['primary_cities']}, FL"
    desc = (f"Meet {S['name']}, a local lawn care and landscaping company in Broward County. "
            f"Licensed and insured, {S['years']} years of experience.")
    owner = E(S["owner_name"])
    body = f"""{head(root, title, desc, path, [crumbs_ld([("Home", ""), ("About us", path)])])}{header(root, 'about')}
<main id="main">
  <section class="hero page-hero">
    <div class="hero-copy">
      {crumbs(root, [("Home", None), ("About us", path)])}
      <h1>About {S['name']}</h1>
      <p class="lede">{S['name']} is a local lawn care and landscaping company serving homes and small businesses across Broward County. Led by {owner}, with {S['years']} years of experience keeping South Florida lawns cut, trimmed and clean.</p>
      {contact_buttons(WA_GENERAL)}
    </div>
    <div class="hero-media">
      <img src="{root}assets/img/edging-string-trimmer.jpg" alt="Lawn care worker trimming grass around a large tree" fetchpriority="high">
    </div>
  </section>
  <div class="mow mow--reveal" aria-hidden="true"></div>

  <section class="section">
    <div class="container split" style="align-items:start">
      <div class="stack">
        <h2>Our story</h2>
        {demo_note(f"replace this story with {owner}'s own words: how the business started, why lawn care, and what makes the crew different.")}
      </div>
      <div class="stack">
        <p class="lede">{owner} has spent more than eight years working on lawns and landscapes across Broward County. {S['name']} started with a simple idea: show up on the day you promised, do the job right, and leave the property cleaner than you found it.</p>
        <p>Today the crew takes care of front yards, backyards and small commercial properties from Fort Lauderdale to Coral Springs. Most customers start with a single visit and stay on the biweekly plan because they never have to think about the yard again.</p>
      </div>
    </div>
  </section>

  <section class="section section--cream">
    <div class="container">
      <div class="section-head"><h2>How we work</h2></div>
      <div class="values">
        <div><h3>On time</h3><p>We show up on the scheduled day. If weather changes the plan, we let you know.</p></div>
        <div><h3>Clean</h3><p>Every visit ends with clippings and debris blown off walkways, driveways and patios.</p></div>
        <div><h3>Clear</h3><p>Quotes are simple and free. Questions get answered by phone or WhatsApp.</p></div>
        <div><h3>Local</h3><p>We live and work in Broward County, and we know how South Florida grass grows.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container split">
      <figure class="figure">
        <img src="{root}assets/img/hero-crew-mowing.webp" alt="Lawn crew mowing, fertilizing and trimming a lawn on a Florida street" loading="lazy">
        <figcaption>A photo of {owner} and the crew goes here.</figcaption>
      </figure>
      <div class="stack">
        <h2>Licensed, insured and local</h2>
        {checks([f"{S['years']} years of experience", "Licensed and insured", "Homes and small commercial properties", "Serving " + ", ".join(S['areas'])])}
        <p><a class="text-link" href="{root}gallery/">See our work in the gallery</a></p>
      </div>
    </div>
  </section>
</main>
{cta_band(WA_GENERAL, "Let's take care of your yard")}{footer(root)}"""
    write(path + "index.html", body)


GALLERY = [
    ("hero-crew-mowing.webp", "mowing", "Lawn crew mowing, fertilizing and trimming a residential lawn", 1376, 768),
    ("hedge-trimming.jpg", "hedges", "Round shrub being shaped with a hedge trimmer", 1600, 1067),
    ("leaf-cleanup-blower.webp", "cleanup", "Dry leaves being blown off a backyard lawn", 1000, 750),
    ("fertilization-before-after.webp", "weeds", "Before and after fertilization and weed control", 1000, 480),
    ("maintenance-striped-lawn.webp", "mowing", "Striped lawn in front of a Florida home", 800, 800),
    ("mowing-push-mower.jpg", "mowing", "Mowing the side yard of a home", 867, 1300),
    ("hedge-trimmer-closeup.jpg", "hedges", "Trimming along a tall hedge", 1600, 1066),
    ("edging-string-trimmer.jpg", "cleanup", "Trimming grass and leaves around a tree", 867, 1300),
    ("florida-lawn-palms.jpg", "weeds", "Thick green lawn with palm trees and hedges", 896, 512),
    ("curb-edging.jpg", "mowing", "Freshly edged lawn along a curb", 800, 485),
    ("striped-lawn-flowers.jpg", "hedges", "Striped lawn beside trimmed shrubs and flowers", 678, 452),
]
GALLERY_FILTERS = [("all", "All work"), ("mowing", "Mowing & edging"), ("hedges", "Hedges & shrubs"),
                   ("cleanup", "Yard cleanup"), ("weeds", "Weed control")]


def gallery_page():
    root = "../"
    path = "gallery/"
    title = f"Lawn Care Gallery in {S['primary_cities']}, FL | {S['name']}"
    desc = f"Photos of lawn mowing, hedge trimming, yard cleanup and weed control work by {S['name']} in Broward County, FL."
    filters = "".join(
        f'<button type="button" class="filter" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{E(v)}</button>'
        for k, v in GALLERY_FILTERS)
    items = "".join(
        f'<li class="g-item" data-cat="{c}"><button type="button" class="g-open" data-full="{root}assets/img/{f}" data-caption="{E(a)}">'
        f'<img src="{root}assets/img/{f}" alt="{E(a)}" width="{w}" height="{h}" loading="lazy"></button></li>'
        for f, c, a, w, h in GALLERY)
    body = f"""{head(root, title, desc, path, [crumbs_ld([("Home", ""), ("Gallery", path)])])}{header(root, 'gallery')}
<main id="main">
  <section class="section gallery-top">
    <div class="container">
      {crumbs(root, [("Home", None), ("Gallery", path)])}
      <div class="section-head" style="margin-top:24px">
        <h1>Our work</h1>
        <p class="lede">Lawns, hedges and yards we take care of across Broward County. Choose a service to filter the photos, or open any photo to see it larger.</p>
        {demo_note("these are sample photos. They will be replaced with photos from real " + E(S['name']) + " jobs.")}
      </div>
      <div class="filters" role="group" aria-label="Filter photos by service">{filters}</div>
    </div>
  </section>
  <div class="mow mow--thin" aria-hidden="true"></div>
  <section class="section" style="padding-top:48px">
    <div class="container">
      <ul class="gallery" id="gallery">{items}</ul>
      <p class="gallery-empty" hidden>No photos for this service yet.</p>
    </div>
  </section>
  <dialog class="lightbox" id="lightbox" aria-label="Photo viewer">
    <form method="dialog"><button class="lightbox-close" aria-label="Close photo">{icon('plus')}</button></form>
    <img alt="">
    <p class="lightbox-caption"></p>
  </dialog>
</main>
{cta_band(WA_GENERAL, "Want your yard to look like this?")}{footer(root)}"""
    write(path + "index.html", body)


def extras():
    urls = ([""] + [f"services/{s['slug']}/" for s in SERVICES] +
            [f"{PLAN['slug']}/", "gallery/", "about/", "contact/"])
    sm = "".join(f"<url><loc>{S['base_url']}{u}</loc></url>" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {S['base_url']}sitemap.xml\n")
    write(".nojekyll", "")
    write("assets/favicon.svg",
          '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#386641"/>'
          '<rect x="8" width="8" height="32" fill="#a7c957"/><rect x="24" width="8" height="32" fill="#a7c957"/></svg>')


if __name__ == "__main__":
    home()
    for s in SERVICES:
        service_page(s)
    plan_page()
    about_page()
    gallery_page()
    contact_page()
    extras()

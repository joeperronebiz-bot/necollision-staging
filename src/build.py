#!/usr/bin/env python3
"""Builds the NEC staging site into ../site. STAGING=True adds noindex everywhere (see LAUNCH.md)."""
import json, html, os, re, shutil, hashlib
STAGING = True
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, '..', 'site')
CANON = 'https://necollision.com'
TEL = 'tel:+12033896400'; TELTXT = '(203) 389-6400'
CARWISE = 'https://www.carwise.com/online-photo-estimate/new-england-collision-west-haven-ct-06516/462487'
MAPS = 'https://www.google.com/maps/search/?api=1&query=New+England+Collision+465+Derby+Ave+West+Haven+CT+06516'
REVIEW = 'https://g.page/r/CdqqLEWWuIMlEAE/review'
GREVIEWS = 'https://www.google.com/maps/search/New+England+Collision+465+Derby+Ave+West+Haven+CT?hl=en'
FB = 'https://www.facebook.com/newenglandcollision'
LAW1 = 'You have the right to choose the licensed repair shop where the damage to your vehicle will be repaired.'
LAW2 = 'Your insurance company cannot require you to use a specific repair shop.'
CSS = open(os.path.join(ROOT, 'site.css')).read()
E = html.escape
def C(s): return f'<span class="conf">[{s}]</span>'

ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
ICON_CAM = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M9 3 7.2 5H4a2 2 0 0 0-2 2v11a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-3.2L15 3zm3 14a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"/></svg>'
ICON_MSG = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M4 3h16a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 1-2z"/></svg>'

def schema_shop():
    return {
      "@context": "https://schema.org", "@type": "AutoBodyShop", "@id": CANON + "/#shop",
      "name": "New England Collision", "url": CANON + "/", "telephone": "+1-203-389-6400",
      "image": CANON + "/og-image-1200x630.png", "logo": CANON + "/assets/img/nec-logo-320.webp",
      "address": {"@type": "PostalAddress", "streetAddress": "465 Derby Ave", "addressLocality": "West Haven", "addressRegion": "CT", "postalCode": "06516", "addressCountry": "US"},
      "geo": {"@type": "GeoCoordinates", "latitude": 41.30659, "longitude": -72.97122},
      "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "16:30"}],
      "foundingDate": "1996", "knowsLanguage": ["en", "es"],
      "areaServed": ["West Haven","New Haven","Orange","Milford","Hamden","East Haven","Branford","Guilford","Madison","Seymour","Shelton"],
      "sameAs": [FB],
      "hasMap": MAPS
    }

def page(path, title, desc, body, base, ld=None, crumbs=None, og_type='website'):
    url = CANON + '/' + path
    lds = [schema_shop()] + (ld or [])
    if crumbs:
        lds.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":CANON+'/'+p} for i,(n,p) in enumerate(crumbs)]})
    ldtxt = '\n'.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    css = CSS.replace('url(assets/', f'url({base}assets/')
    robots = '<meta name="robots" content="noindex, nofollow">\n' if STAGING else ''
    staging = '<div class="staging">STAGING PREVIEW. Not the live site. Items marked [CONFIRM] need a yes before launch.</div>' if STAGING else ''
    return f'''<!doctype html>
<html lang="en" data-base="{base}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{robots}<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="New England Collision">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{CANON}/og-image-1200x630.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F3EFE7">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="{base}assets/img/favicon-64.png" sizes="64x64">
<link rel="apple-touch-icon" href="{base}assets/img/apple-touch-icon.png">
<link rel="preload" href="{base}assets/fonts/inter-tight-var.woff2" as="font" type="font/woff2" crossorigin>
<style>{css}</style>
{ldtxt}
<script src="{base}assets/js/tracker.js" defer></script>
<script src="{base}assets/js/chat.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{staging}
<header class="top"><div class="wrap">
<a class="brand" href="{base or './'}"><img src="{base}assets/img/nec-logo-160.webp" width="52" height="52" alt="New England Collision logo"><span><b>New England Collision</b><small>West Haven, CT</small></span></a>
<nav class="nav" aria-label="Main">{NAV(base)}</nav>
<div class="actions"><details class="menu"><summary>Menu</summary><nav class="menu-list" aria-label="Menu">{NAV(base, True)}</nav></details>
<a class="btn btn-call" href="{TEL}" data-where="header" aria-label="Call {TELTXT}">{ICON_PHONE}<span class="short">Call</span><span class="full">Call {TELTXT}</span></a></div>
</div></header>
<main id="main">
{body}
</main>
{FOOTER(base)}
<div class="bar" role="region" aria-label="Quick contact">
<a class="btn btn-call" href="{TEL}" data-where="sticky">{ICON_PHONE}Call</a>
<a class="btn btn-soft" href="{MAPS}" data-where="sticky" target="_blank" rel="noopener">Directions</a>
<a class="btn btn-soft" href="#chat" data-chat data-where="sticky">{ICON_MSG}Message Us</a>
</div>
<a class="btn btn-call launch" href="#chat" data-chat data-where="launcher">{ICON_MSG}Message Us</a>
<script>
(function(){{var v=document.querySelector('.rv-view'),b=document.querySelector('.rv-pause');if(!v||!b)return;
function set(p){{v.classList.toggle('paused',p);b.setAttribute('aria-pressed',p?'true':'false');b.textContent=p?'Play reviews':'Pause reviews';}}
b.addEventListener('click',function(){{set(!v.classList.contains('paused'));}});
v.addEventListener('click',function(e){{if(!e.target.closest('a'))set(!v.classList.contains('paused'));}});}})();
</script>
</body>
</html>
'''

PAGES_NAV = [('Services','services/'),('Insurance help','services/insurance-claim-help/'),('Your right to choose','your-right-to-choose/'),('FAQ','faq/'),('About','about/'),('Contact','contact/')]
def NAV(base, full=False):
    items = ([('Home','')] if full else []) + PAGES_NAV
    return ''.join(f'<a href="{base}{p}">{n}</a>' if p else f'<a href="{base or './'}">{n}</a>' for n,p in items)

def FOOTER(base):
    return f'''<footer><div class="wrap fgrid">
<div><p class="label">New England Collision</p>
<p>465 Derby Ave<br>West Haven, CT 06516<br><a href="{TEL}" data-where="footer">{TELTXT}</a></p>
<p>Family owned. 30 years, same location.<br>Se habla español.</p></div>
<div><p class="label">Hours</p><p>Mon to Fri<br>8:00 AM to 4:30 PM</p>
<p class="label">Pages</p><ul class="flinks">{''.join(f'<li><a href="{base}{p}">{n}</a></li>' for n,p in PAGES_NAV + SERVICE_LINKS)}</ul></div>
<div><p class="label">Find us</p><p><a href="{MAPS}" target="_blank" rel="noopener" data-where="footer">Directions</a><br>
<a href="{FB}" target="_blank" rel="noopener" data-where="footer">Facebook</a> {C('CONFIRM page URL')}<br>
<a href="{GREVIEWS}" target="_blank" rel="noopener" data-where="reviews">Google reviews</a><br>
<a href="{REVIEW}" target="_blank" rel="noopener" data-where="footer">Leave us a review</a></p></div>
</div></footer>'''

def reviews_strip():
    revs = json.load(open(os.path.join(ROOT, '..', 'data', 'reviews-used.json')))
    def card(r):
        return f'''<article class="rv"><div class="meta"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span> 5.0 · GOOGLE</div>
<blockquote>{E(r["text"])}</blockquote>
<div><div class="who">{E(r["name"])}</div><div class="meta">{E(r["when"])}</div></div>
<a href="{GREVIEWS}" target="_blank" rel="noopener" data-where="reviews">See it on Google</a></article>'''
    ph = f'''<article class="rv ph"><div class="meta">FACEBOOK</div>
<p>Facebook recommendations go here. {C('CONFIRM: add real Facebook recommendations, copied word for word. They need a login to read, so none are shown yet.')}</p>
<a href="{FB}" target="_blank" rel="noopener" data-where="reviews">Visit us on Facebook</a></article>'''
    cards = ''.join(card(r) for r in revs) + ph
    return f'''<div class="rv-view" tabindex="0" aria-label="Customer reviews, scrolling. Hover, tap or focus to pause.">
<div class="rv-track"><div style="display:flex;gap:16px">{cards}</div><div style="display:flex;gap:16px" aria-hidden="true">{cards.replace('<a ', '<a tabindex="-1" ')}</div></div></div>'''

def home():
    body = f'''
<section class="hero"><div class="wrap">
<p class="label">465 Derby Ave · West Haven, CT · Since 1996</p>
<p class="motto">Relax, it was an accident.</p>
<h1>Had an accident? Take a breath. We'll help from here.</h1>
<p class="lead">We're a family-owned body shop, 30 years at the same location. Call us or send a few photos, and we'll walk you through what comes next.</p>
<div class="ctas">
<a class="btn btn-call" href="{TEL}" data-where="hero">{ICON_PHONE}Call {TELTXT}</a>
<a class="btn btn-soft" href="{CARWISE}" target="_blank" rel="noopener" data-where="hero">{ICON_CAM}Send photos for an estimate</a>
<a class="btn btn-soft" href="#chat" data-chat data-where="hero">{ICON_MSG}Message Us</a>
</div>
<ul class="trust">
<li><span class="stars" aria-hidden="true">★</span> 4.7 on Google</li>
<li>Family owned</li>
<li>30 years, same location</li>
<li>Se habla español</li>
<li>All insurance companies welcome</li>
</ul>
</div></section>

<section class="alt" id="reviews" aria-labelledby="rv-h"><div class="wrap">
<div class="rv-head"><div><p class="label">What neighbors say</p><h2 id="rv-h">4.7 stars on Google</h2></div>
<button type="button" class="rv-pause" aria-pressed="false">Pause reviews</button></div>
{reviews_strip()}
<p class="src">Reviews are copied word for word from our public Google listing, with the name as it appears there. <a href="{GREVIEWS}" target="_blank" rel="noopener" data-where="reviews">Read all our Google reviews</a>. {C('CONFIRM: re-check each review on Google the day we launch')}</p>
</div></section>

<section id="how" aria-labelledby="how-h"><div class="wrap">
<p class="label">How it works</p>
<h2 id="how-h">Three simple steps</h2>
<ol class="steps">
<li><h3>Call or send photos</h3><p>Call {TELTXT}, or send photos of the damage from your phone. You can also stop by 465 Derby Ave.</p></li>
<li><h3>We help with insurance and a rental</h3><p>Insurance claim assistance, and rental car delivery and pickup (some exceptions apply). {C('from old site, CONFIRM still offered')}</p></li>
<li><h3>Drive home fixed</h3><p>We repair your car here in our West Haven shop, and you pick it up when it's ready.</p></li>
</ol>
<div class="ctas"><a class="btn btn-call" href="{TEL}" data-where="steps">{ICON_PHONE}Call {TELTXT}</a></div>
</div></section>

<section class="alt"><div class="wrap grid2">
<div class="photo"><img src="assets/img/front-office-720.webp" srcset="assets/img/front-office-400.webp 400w, assets/img/front-office-720.webp 720w" sizes="(min-width:820px) 520px, 100vw" width="720" height="720" loading="lazy" decoding="async" alt="Two members of the New England Collision office team on the phones at their desks"></div>
<div><p class="label">Real people, real shop</p>
<h2>When you call, you talk to our front office.</h2>
<p>Our office is right inside the shop at 465 Derby Ave. Family owned. 30 years, same location.</p>
<p class="cap">Photo: our front office, from our own website. {C('CONFIRM: staff okay to show this photo')}</p>
<a class="btn btn-call" href="{TEL}" data-where="office">{ICON_PHONE}Call {TELTXT}</a></div>
</div></section>

<section class="bone" id="insurance" aria-labelledby="ins-h"><div class="wrap">
<p class="label">Your insurance, your choice</p>
<h2 id="ins-h">In Connecticut, you choose the shop.</h2>
<p class="quote-law">{LAW1}</p>
<p class="quote-law">{LAW2}</p>
<p class="src">Source: Connecticut General Statutes, Sec. 38a-354. <a href="https://www.cga.ct.gov/current/pub/chap_700.htm#sec_38a-354" target="_blank" rel="noopener">Read the law</a>. More on <a href="your-right-to-choose/">your right to choose</a>.</p>
<div class="cards">
<div class="card"><h3>All insurance companies welcome</h3><p>We're an independent shop. Whoever your insurer is, you can bring your car to us.</p></div>
<div class="card"><h3>Inspections inside the shop</h3><p>Insurance inspections happen inside our shop, so you and the adjuster stay out of the snow.</p></div>
</div>
<div class="ctas"><a class="btn btn-call" href="{TEL}" data-where="insurance">{ICON_PHONE}Call {TELTXT}</a><a class="btn btn-soft" href="#chat" data-chat data-where="insurance">{ICON_MSG}Message Us</a></div>
</div></section>

<section id="fix" aria-labelledby="fix-h"><div class="wrap">
<p class="label">What we fix</p>
<h2 id="fix-h">Collision repair, start to finish</h2>
<p>These are the services listed on our old website. {C('from old site, CONFIRM still offered')}</p>
<div class="cards">
<div class="card"><h3>Collision and auto body repair</h3><p>Dents, crushed panels and bumpers after a crash, big or small.</p><a class="more" href="services/collision-repair/">Collision repair</a></div>
<div class="card"><h3>Paint and computerized color matching</h3><p>Paint work that matches the rest of your car.</p><a class="more" href="services/paint-color-matching/">Paint and color matching</a></div>
<div class="card"><h3>Frame straightening</h3><p>Getting the structure of the car back where it belongs.</p><a class="more" href="services/frame-straightening/">Frame straightening</a></div>
<div class="card"><h3>Insurance claim assistance</h3><p>Help with your insurance claim.</p><a class="more" href="services/insurance-claim-help/">Insurance claim help</a></div>
<div class="card"><h3>Rental car delivery and pickup</h3><p>Some exceptions apply.</p><a class="more" href="services/towing-rental-help/">Towing and rental help</a></div>
<div class="card"><h3>Need a tow?</h3><p>We don't tow, but we know trusted local tow companies and can call them for you.</p><a class="more" href="services/towing-rental-help/">Towing and rental help</a></div>
</div>
<div class="thumbs">
<img src="assets/img/paint-booth-400.webp" width="400" height="400" loading="lazy" decoding="async" alt="A painter spraying a car part in the paint booth at New England Collision">
<img src="assets/img/structure-repair-400.webp" width="400" height="400" loading="lazy" decoding="async" alt="A technician working under a car in the New England Collision shop">
<img src="assets/img/panel-prep-400.webp" width="400" height="400" loading="lazy" decoding="async" alt="A technician preparing a van door for paint in the shop">
</div>
<p class="cap">Photos: inside our West Haven shop, from our own website. {C('CONFIRM: staff okay to show these photos')}</p>
<div class="card" style="margin-top:18px"><h3>Veterans and active military</h3><p>10% off labor. Please bring your military ID. Labor only.</p></div>
</div></section>

<section class="alt visit" id="visit" aria-labelledby="visit-h"><div class="wrap grid2">
<div><p class="label">Visit us</p>
<h2 id="visit-h">465 Derby Ave, West Haven</h2>
<dl><dt>Address</dt><dd>465 Derby Ave, West Haven, CT 06516</dd>
<dt>Phone</dt><dd><a href="{TEL}" data-where="visit">{TELTXT}</a></dd>
<dt>Hours</dt><dd>Mon to Fri, 8:00 AM to 4:30 PM</dd>
<dt>Language</dt><dd>Se habla español</dd></dl>
<div class="ctas"><a class="btn btn-call" href="{TEL}" data-where="visit">{ICON_PHONE}Call {TELTXT}</a><a class="btn btn-soft" href="{MAPS}" target="_blank" rel="noopener" data-where="visit">Get directions</a></div>
<p>Say hello on <a href="{FB}" target="_blank" rel="noopener" data-where="visit">Facebook</a> {C('CONFIRM page URL')}, or <a href="{REVIEW}" target="_blank" rel="noopener" data-where="visit">leave us a Google review</a>.</p>
</div>
<div><p class="motto serif" style="font-size:30px;line-height:1.3;color:var(--ink)"><i>Nobody plans an accident. We'll take it from here.</i></p>
<p>Family owned on Derby Ave since 1996. Call, send photos, or tap Message Us, and a real person from our shop gets back to you.</p></div>
</div></section>
'''
    return page('', 'New England Collision | Auto Body and Collision Repair, West Haven CT',
                'Family-owned collision repair at 465 Derby Ave, West Haven, CT. 30 years, same location. Call (203) 389-6400 or send photos for an estimate.',
                body, '')

def main_old():
    os.makedirs(os.path.join(OUT, 'assets', 'js'), exist_ok=True)
    for f in ('tracker.js', 'chat.js'):
        shutil.copy(os.path.join(ROOT, f), os.path.join(OUT, 'assets', 'js', f))
    open(os.path.join(OUT, 'index.html'), 'w').write(home())
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    open(os.path.join(OUT, 'robots.txt'), 'w').write('# STAGING: block all crawlers. At launch replace with the version in LAUNCH.md\nUser-agent: *\nDisallow: /\n' if STAGING else f'User-agent: *\nAllow: /\nSitemap: {CANON}/sitemap.xml\n')
    urls = ['']
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{CANON}/{u}</loc><lastmod>2026-11-24</lastmod></url>\n' for u in urls) + '</urlset>\n')

exec(open(os.path.join(ROOT,'pages.py')).read())
main()

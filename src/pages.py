# Phase 2 pages. Executed by build.py (shares its globals).
SERVICE_LINKS = [('Collision repair','services/collision-repair/'),('Dent repair','services/dent-repair/'),('Paint and color matching','services/paint-color-matching/'),('Frame straightening','services/frame-straightening/'),('Insurance claim help','services/insurance-claim-help/'),('Towing and rental help','services/towing-rental-help/')]
REVS = {r['name']: r for r in json.load(open(os.path.join(ROOT, '..', 'data', 'reviews-used.json')))}
OLD = 'from old site, CONFIRM still offered'

def pending(txt):
    """Staging-only note. Not rendered when STAGING is False."""
    return f'<div class="pending"><span class="conf">[CONFIRM]</span> {txt}</div>' if STAGING else ''

def crumbs_html(base, crumbs):
    li = []
    for i,(n,p) in enumerate(crumbs):
        if i == len(crumbs)-1: li.append(f'<li aria-current="page">{E(n)}</li>')
        else: li.append(f'<li><a href="{base}{p}">{E(n)}</a></li>' if p else f'<li><a href="{base or "./"}">{E(n)}</a></li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(li)}</ol></nav>'

def ctas(base, where, photos=True):
    out = f'<div class="ctas"><a class="btn btn-call" href="{TEL}" data-where="{where}">{ICON_PHONE}Call {TELTXT}</a>'
    if photos: out += f'<a class="btn btn-soft" href="{CARWISE}" target="_blank" rel="noopener" data-where="{where}">{ICON_CAM}Send photos for an estimate</a>'
    out += f'<a class="btn btn-soft" href="#chat" data-chat data-where="{where}">{ICON_MSG}Message Us</a></div>'
    return out

def review_block(name):
    r = REVS[name]
    return f'''<figure class="one-review"><p class="stars" aria-label="5 out of 5 stars" style="margin:0 0 6px">★★★★★</p><blockquote>{E(r["text"])}</blockquote>
<figcaption><span class="who">{E(r["name"])}</span> <span class="meta">· Google · {E(r["when"])}</span><br><a href="{GREVIEWS}" target="_blank" rel="noopener" data-where="reviews">Read our Google reviews</a></figcaption></figure>'''

def hero(base, crumbs, label, h1, lead, where):
    return f'''<section class="hero"><div class="wrap">{crumbs_html(base, crumbs)}
<p class="label">{label}</p><h1>{h1}</h1><p class="lead">{lead}</p>{ctas(base, where)}</div></section>'''

def law_block(base):
    return f'''<p class="quote-law">{LAW1}</p><p class="quote-law">{LAW2}</p>
<p class="src">Source: Connecticut General Statutes, Sec. 38a-354. <a href="https://www.cga.ct.gov/current/pub/chap_700.htm#sec_38a-354" target="_blank" rel="noopener">Read the law</a>.</p>'''

def related(base, skip):
    return '<div class="links">' + ''.join(f'<a href="{base}{p}">{n}</a>' for n,p in SERVICE_LINKS if p != skip) + '</div>'

def photo(base, name, alt, cap):
    return f'''<div class="photo"><img src="{base}assets/img/{name}-720.webp" srcset="{base}assets/img/{name}-400.webp 400w, {base}assets/img/{name}-720.webp 720w" sizes="(min-width:820px) 520px, 100vw" width="720" height="720" loading="lazy" decoding="async" alt="{E(alt)}"></div><p class="cap">{cap} {C('CONFIRM: staff okay to show this photo')}</p>'''

def service_ld(name, desc, path):
    return {"@context":"https://schema.org","@type":"Service","name":name,"serviceType":name,"description":desc,"url":CANON+'/'+path,
            "provider":{"@id":CANON+"/#shop"},"areaServed":{"@type":"City","name":"West Haven, CT"}}

def service_page(path, name, title, desc, label, h1, lead, body_html, review, ld_name=None):
    base = '../../'
    crumbs = [('Home',''),('Services','services/'),(name,path)]
    body = hero(base, crumbs, label, h1, lead, 'service-hero') + body_html + f'''
<section class="alt"><div class="wrap"><p class="label">What a neighbor said</p>{review_block(review)}</div></section>
<section><div class="wrap"><p class="label">Other ways we help</p><h2>More from our shop</h2>{related(base, path)}
<div class="ctas"><a class="btn btn-call" href="{TEL}" data-where="service-bottom">{ICON_PHONE}Call {TELTXT}</a></div></div></section>'''
    ld = [service_ld(ld_name, desc, path)] if ld_name else []
    return path, page(path, title, desc, body, base, ld=ld, crumbs=crumbs)

def services_pages():
    base = '../../'
    out = []
    # 1 Collision repair
    out.append(service_page('services/collision-repair/', 'Collision repair',
      'Collision Repair in West Haven, CT | New England Collision',
      'Collision repair at 465 Derby Ave, West Haven. Family owned, 30 years, same location. Call (203) 389-6400 or send photos for an estimate.',
      'Services · Collision repair', 'Collision repair, one calm step at a time.',
      "Nobody plans an accident. Call us or send photos, and we'll walk you through what happens next. Family owned, 30 years at the same location on Derby Ave.",
      f'''<section><div class="wrap grid2"><div class="prose">
<h2>What happens when you call</h2>
<ul>
<li>You talk to our front office. Tell us what happened and where the car is.</li>
<li>If the car can't be driven, we don't tow, but we can call a trusted local tow company for you.</li>
<li>If there's an insurance claim, we help you with it. {C(OLD)}</li>
<li>Insurance inspections happen inside our shop, so you and the adjuster stay out of the snow.</li>
<li>We repair the car here at 465 Derby Ave and call you when it's ready.</li>
</ul>
<h2>What we fix</h2>
<p>Bumpers, doors, fenders, hoods, trunks and quarter panels. Big crashes and small ones. Collision repair and auto body repair were the first services on our old website. {C(OLD)}</p>
{pending('Not on the page until confirmed: factory or I-CAR certifications, ADAS sensor calibration, aluminum repair, warranty terms.')}
</div>{photo(base,'structure-repair','A technician working under a car in the New England Collision shop','Inside our West Haven shop, from our own website.')}</div></section>''',
      'Erin Eberhardt', 'Collision repair'))
    # 2 Dent repair
    out.append(service_page('services/dent-repair/', 'Dent repair',
      'Dent Repair in West Haven, CT | New England Collision',
      'Dents from a parking lot, a pole or a fender bender. Family-owned body shop at 465 Derby Ave, West Haven. Call (203) 389-6400.',
      'Services · Dent repair', 'Dents, big or small.',
      "Most dents come with a story: a parking lot, a pole, a car that backed into you. Send photos or stop by, and we'll look at it with you.",
      f'''<section><div class="wrap grid2"><div class="prose">
<h2>How it works</h2>
<ul>
<li>Send photos from your phone, or stop by 465 Derby Ave, Mon to Fri, 8:00 AM to 4:30 PM.</li>
<li>We look at the dent and talk through the repair with you.</li>
<li>If it's part of an insurance claim, we help with that too. {C(OLD)}</li>
</ul>
<p>Dent repair is part of our auto body work. {C('CONFIRM: dent repair named as its own service')}</p>
{pending('Hail damage repair and paintless dent repair (PDR) are NOT verified. They stay off the page until Joe confirms NEC offers them.')}
</div>{photo(base,'panel-prep','A technician preparing a van door for paint in the shop','Panel work in our West Haven shop, from our own website.')}</div></section>''',
      'Ryan D.', None))
    # 3 Paint
    out.append(service_page('services/paint-color-matching/', 'Paint and color matching',
      'Auto Paint and Color Matching in West Haven, CT | New England Collision',
      'Auto body paint and color matching at our West Haven shop. Family owned, 30 years, same location. Call (203) 389-6400.',
      'Services · Paint and color matching', 'Paint that fits the rest of your car.',
      "After a repair, the new paint should blend in with the old. We paint in our own shop at 465 Derby Ave.",
      f'''<section><div class="wrap grid2"><div class="prose">
<h2>Paint, done in our shop</h2>
<p>Paint and computerized color matching were listed on our old website. {C(OLD)}</p>
<ul>
<li>We paint the repaired parts in our own paint booth.</li>
<li>We match the new paint to the color already on your car.</li>
<li>Have a question about a scratch or a faded spot? Send photos and ask.</li>
</ul>
</div>{photo(base,'paint-booth','A painter spraying a car part in the paint booth at New England Collision','Painting in our shop, from our own website.')}</div></section>''',
      'Yajayra Torres', 'Auto body paint and color matching'))
    # 4 Frame
    out.append(service_page('services/frame-straightening/', 'Frame straightening',
      'Frame Straightening in West Haven, CT | New England Collision',
      'Frame straightening after a hard hit, at our family-owned shop on Derby Ave, West Haven. Call (203) 389-6400.',
      'Services · Frame straightening', 'Frame straightening after a hard hit.',
      "A hard hit can move the structure of a car, not just the panels you can see. We check it and straighten it before the car goes home.",
      f'''<section><div class="wrap grid2"><div class="prose">
<h2>What frame work means</h2>
<p>The frame, or unibody, is the skeleton of the car. If it's out of place, doors may not close right and the car may not drive straight. Frame straightening was listed on our old website. {C(OLD)}</p>
<ul>
<li>We measure the structure and compare it to where it should be.</li>
<li>We straighten what moved, then finish the body and paint.</li>
<li>Questions about a car that pulls or doors that won't shut right? Call and ask.</li>
</ul>
<p>Frame and measuring equipment: Car-O-Liner. {C('CONFIRM: name the Car-O-Liner system on the site?')}</p>
</div>{photo(base,'structure-repair','A technician working under a car in the New England Collision shop','Structural work in our shop, from our own website.')}</div></section>''',
      'Lucas Cecchetto', 'Frame straightening'))
    # 5 Insurance
    out.append(service_page('services/insurance-claim-help/', 'Insurance claim help',
      'Insurance Claim Help After a Crash | New England Collision, West Haven CT',
      'In Connecticut you choose the repair shop. All insurance companies welcome at New England Collision, 465 Derby Ave, West Haven. Call (203) 389-6400.',
      'Services · Insurance claim help', "Insurance claim help, so you're not doing it alone.",
      "Insurance can feel like the hardest part. Bring your questions to us. All insurance companies welcome.",
      f'''<section class="bone"><div class="wrap"><p class="label">Your right to choose</p><h2>In Connecticut, the shop is your choice.</h2>{law_block(base)}</div></section>
<section><div class="wrap"><div class="cards">
<div class="card"><h3>All insurance companies welcome</h3><p>We're an independent shop. Whoever insures you, or the other driver, you can bring your car to us.</p></div>
<div class="card"><h3>Inspections inside our shop</h3><p>Insurance inspections happen inside our shop, so you and the adjuster stay out of the snow.</p></div>
<div class="card"><h3>Help with the claim</h3><p>Insurance claim assistance, from your first call. {C(OLD)}</p></div>
<div class="card"><h3>What to have ready</h3><p>Your claim number if you have one, the other driver's insurance details if you have them, and a few photos of the damage.</p></div>
</div></div></section>''',
      'Emily Loquine', 'Insurance claim assistance'))
    # 6 Towing and rental
    out.append(service_page('services/towing-rental-help/', 'Towing and rental help',
      'Towing and Rental Car Help After a Crash | New England Collision, West Haven CT',
      "We don't tow, but we can call trusted local tow companies for you. Rental car help too. New England Collision, West Haven. Call (203) 389-6400.",
      'Services · Towing and rental help', 'Need a tow or a rental? Start with one call.',
      "Take a breath. One call to us, and we'll help you sort out the car and how you'll get around.",
      f'''<section><div class="wrap"><div class="cards">
<div class="card"><h3>Towing</h3><p>We don't tow. We've worked with trusted local tow companies for years, and we can call them directly for you.</p></div>
<div class="card"><h3>Already at a tow yard?</h3><p>Every situation is different. Call us and we'll help you sort it out.</p></div>
<div class="card"><h3>Rental car</h3><p>Rental car delivery and pickup (some exceptions apply). {C(OLD)}</p></div>
<div class="card"><h3>The choice is yours</h3><p>{LAW1}</p></div>
</div>
{pending('Not on the page: names of tow companies, tow response times, rental partners. The CEO profile mentions "Hertz Rentals On Site" and "Enterprise Concierge Available"; both are unverified and left out.')}
</div></section>''',
      'Erin Eberhardt', None))
    return out

def services_hub():
    base = '../'
    crumbs = [('Home',''),('Services','services/')]
    cards = {
      'services/collision-repair/': 'Crash damage, big or small, repaired in our West Haven shop.',
      'services/dent-repair/': 'Dents from a parking lot, a pole or a fender bender.',
      'services/paint-color-matching/': 'Paint that blends with the rest of your car.',
      'services/frame-straightening/': 'Getting the structure back where it belongs after a hard hit.',
      'services/insurance-claim-help/': 'Your right to choose, and help with the claim.',
      'services/towing-rental-help/': "We don't tow, but we can call trusted tow companies. Rental help too.",
    }
    cs = ''.join(f'<div class="card"><h3>{n}</h3><p>{cards[p]}</p><a class="more" href="{base}{p}">{n}</a></div>' for n,p in SERVICE_LINKS)
    body = hero(base, crumbs, 'Services', 'How we can help', "Family owned. 30 years, same location. Here's what our shop does after an accident.", 'services-hero') + f'''
<section><div class="wrap"><p>{C('Services from our old website. CONFIRM each is still offered.')}</p><div class="cards">{cs}</div></div></section>'''
    return 'services/', page('services/', 'Auto Body and Collision Services | New England Collision, West Haven CT',
      'Collision repair, dent repair, paint, frame straightening, insurance claim help, towing and rental help. 465 Derby Ave, West Haven. (203) 389-6400.', body, base, crumbs=crumbs)

FAQS = [
 ("What should I do right after an accident?", "First, make sure everyone is okay. If anyone is hurt, call 911. When you're safe, call us at (203) 389-6400 and we'll help you with the next steps.", True),
 ("Do I have to use the shop my insurance company picks?", "No. Connecticut law says: \u201cYou have the right to choose the licensed repair shop where the damage to your vehicle will be repaired.\u201d And: \u201cYour insurance company cannot require you to use a specific repair shop.\u201d (Conn. Gen. Stat. Sec. 38a-354)", True),
 ("Do you work with my insurance company?", "All insurance companies are welcome. We're an independent shop, so you can bring your car to us whoever your insurer is.", True),
 ("Where does the insurance inspection happen?", "Inside our shop, so you and the adjuster stay out of the snow.", True),
 ("Do you tow?", "We don't tow. We've worked with trusted local tow companies for years, and we can call them directly for you.", True),
 ("My car is at a tow yard. What do I do?", "Call us at (203) 389-6400 and we'll help you sort it out. You have the right to choose the licensed repair shop where the damage to your vehicle will be repaired.", True),
 ("Can I get an estimate without coming in?", "Yes. You can send photos of the damage from your phone through CarWise, or call us and we'll talk it through.", True),
 ("Can you help me with a rental car?", "Rental car delivery and pickup (some exceptions apply) was listed on our old website. Call us and ask.", False),
 ("What are your hours?", "Monday to Friday, 8:00 AM to 4:30 PM.", True),
 ("Where are you?", "465 Derby Ave, West Haven, CT 06516. Derby Ave is Route 34, in the Allingtown part of West Haven.", True),
 ("Do you speak Spanish?", "S\u00ed. Se habla espa\u00f1ol.", True),
 ("Do you have a military discount?", "Yes. Veterans and active military get 10% off labor. Please bring your military ID. The discount is on labor only.", True),
 ("How long have you been in business?", "Since 1996. We're family owned, 30 years at the same location on Derby Ave.", True),
 ("How long will my repair take?", "It depends on the damage and the parts. We'll talk it through with you once we've seen the car, and you can call us any time we're open to ask how it's going.", True),
]
def faq_page():
    base = '../'
    crumbs = [('Home',''),('FAQ','faq/')]
    items = ''
    for q,a,ok in FAQS:
        extra = '' if ok else ' ' + C(OLD)
        items += f'<details><summary>{E(q)}</summary><div class="a"><p>{E(a)}{extra}</p></div></details>'
    ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a,ok in FAQS if ok]}
    body = hero(base, crumbs, 'Questions', 'Questions people ask us', "Short answers to the questions we hear most after an accident. Still not sure? Call us. We're happy to help.", 'faq-hero') + f'''
<section><div class="wrap faq prose">{items}
<p class="src">Questions marked {C(OLD)} are left out of the FAQ schema until confirmed.</p></div></section>'''
    return 'faq/', page('faq/', 'FAQ: Collision Repair, Insurance and Towing | New England Collision',
      'Answers about insurance, your right to choose a shop in CT, towing, rentals, hours and estimates. New England Collision, West Haven. (203) 389-6400.', body, base, ld=[ld], crumbs=crumbs)

def about_page():
    base = '../'
    crumbs = [('Home',''),('About','about/')]
    body = hero(base, crumbs, 'About us', 'Family owned. 30 years, same location.', "New England Collision has been on Derby Ave in West Haven since 1996. Same family, same location, still answering the phone.", 'about-hero') + f'''
<section><div class="wrap grid2"><div class="prose">
<h2>Our story</h2>
<p>We opened at 465 Derby Ave in 1996, and we're still there. Our owner has been at the shop for 28 years, running it for 20 and owning it for 15.</p>
<p>Our motto is on our logo: <i class="serif" style="font-size:22px">Relax, it was an accident.</i> Nobody plans a crash. Our job is to make the rest of it easier.</p>
<p>We're an independent, family-owned shop. All insurance companies are welcome, and se habla español.</p>
<p>Veterans and active military get 10% off labor. Please bring your military ID. Labor only.</p>
{pending('Staff names and roles are not on the page. Add only with Joe\u2019s okay (copy rule: staff by role).')}
</div>{photo(base,'front-office','Two members of the New England Collision office team on the phones at their desks','Our front office at 465 Derby Ave, from our own website.')}</div></section>
<section class="alt"><div class="wrap"><p class="label">What a neighbor said</p>{review_block('Lucas Cecchetto')}{ctas(base,'about-bottom',False)}</div></section>'''
    return 'about/', page('about/', 'About New England Collision | Family Owned in West Haven Since 1996',
      'Family-owned collision repair at 465 Derby Ave, West Haven, CT since 1996. 30 years, same location. Call (203) 389-6400.', body, base, crumbs=crumbs)

def rights_page():
    base = '../'
    crumbs = [('Home',''),('Your right to choose','your-right-to-choose/')]
    body = hero(base, crumbs, 'Connecticut law', 'In Connecticut, you choose the repair shop.', "After a crash, your insurance company may give you a list of shops. You can still pick the shop you trust.", 'rights-hero') + f'''
<section class="bone"><div class="wrap prose"><h2>What the law says</h2>{law_block(base)}</div></section>
<section><div class="wrap prose"><h2>What that means for you</h2>
<ul>
<li>You can tell your insurance company you'd like your car repaired at New England Collision.</li>
<li>All insurance companies are welcome here.</li>
<li>Insurance inspections happen inside our shop, so you and the adjuster stay out of the snow.</li>
<li>Have a question about your claim? Call us and we'll help you sort it out.</li>
</ul>
<p class="src">This page shares the wording of the law. It isn't legal advice. For legal questions, please ask an attorney.</p>
{ctas(base,'rights-bottom')}</div></section>'''
    return 'your-right-to-choose/', page('your-right-to-choose/', 'Your Right to Choose a Repair Shop in CT | New England Collision',
      'Connecticut law (Sec. 38a-354): you have the right to choose the licensed repair shop for your car. New England Collision, West Haven. (203) 389-6400.', body, base, crumbs=crumbs)

def contact_page():
    base = '../'
    crumbs = [('Home',''),('Contact and directions','contact/')]
    body = hero(base, crumbs, 'Contact and directions', 'Come see us on Derby Ave.', "Call, send photos, message us, or stop by. We're at 465 Derby Ave in West Haven.", 'contact-hero') + f'''
<section class="visit"><div class="wrap grid2"><div>
<dl><dt>Address</dt><dd>465 Derby Ave, West Haven, CT 06516</dd>
<dt>Phone</dt><dd><a href="{TEL}" data-where="contact">{TELTXT}</a></dd>
<dt>Hours</dt><dd>Mon to Fri, 8:00 AM to 4:30 PM</dd>
<dt>Language</dt><dd>Se habla español</dd>
<dt>Facebook</dt><dd><a href="{FB}" target="_blank" rel="noopener" data-where="contact">New England Collision on Facebook</a> {C('CONFIRM page URL')}</dd></dl>
<div class="ctas"><a class="btn btn-call" href="{TEL}" data-where="contact">{ICON_PHONE}Call {TELTXT}</a><a class="btn btn-soft" href="{MAPS}" target="_blank" rel="noopener" data-where="contact">Get directions</a></div>
</div><div class="prose"><h2>Finding us</h2>
<p>Derby Ave is Route 34. We're in the Allingtown part of West Haven, at 465 Derby Ave.</p>
<p>Driving directions from nearby towns are coming to this site soon. For now, tap Get directions and your map app will take you right to our door.</p>
{pending('Town-by-town directions arrive in Phase 3 (Wednesday). Holiday hours are not on staging.')}
</div></div></section>'''
    return 'contact/', page('contact/', 'Contact and Directions | New England Collision, 465 Derby Ave, West Haven CT',
      'New England Collision, 465 Derby Ave (Route 34), West Haven, CT 06516. Mon to Fri 8:00 AM to 4:30 PM. Call (203) 389-6400.', body, base, crumbs=crumbs)

def main():
    os.makedirs(os.path.join(OUT, 'assets', 'js'), exist_ok=True)
    for f in ('tracker.js', 'chat.js'):
        shutil.copy(os.path.join(ROOT, f), os.path.join(OUT, 'assets', 'js', f))
    pages = [('', home())] + services_pages() + [services_hub(), faq_page(), about_page(), rights_page(), contact_page()]
    for path, htmltxt in pages:
        d = os.path.join(OUT, path); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w').write(htmltxt)
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    open(os.path.join(OUT, 'robots.txt'), 'w').write('# STAGING: block all crawlers. At launch the build writes the open version (see LAUNCH.md)\nUser-agent: *\nDisallow: /\n' if STAGING else f'User-agent: *\nAllow: /\nSitemap: {CANON}/sitemap.xml\n')
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{CANON}/{p}</loc><lastmod>2026-11-24</lastmod></url>\n' for p,_ in pages) + '</urlset>\n')
    print(len(pages), 'pages')

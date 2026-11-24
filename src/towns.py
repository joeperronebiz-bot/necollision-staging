# Phase 3: town pages. Executed by pages.py main() (shares build.py globals).
# Drive data: data/routes/townhall-routes-2026-11-24.json (Valhalla + OSRM, OpenStreetMap data, fetched Nov 24, 2026).
# Town facts: Wikipedia infoboxes (2020 U.S. Census population), data/routes/wikipedia-infobox-2026-11-24.json.
ROUTES = json.load(open(os.path.join(ROOT, '..', 'data', 'routes', 'townhall-routes-2026-11-24.json')))
DEST_Q = 'New+England+Collision,+465+Derby+Ave,+West+Haven,+CT+06516'
TOWNS = [
 # slug, name, origin label, steps, county, region, pop, est label, est year, official site, wiki, review
 ('west-haven','West Haven','West Haven City Hall',
  ['From City Hall on Main Street, head to Campbell Avenue and take it north for about 2.7 miles.',
   'Turn left onto Derby Avenue (Route 34). We\u2019re at 465.'],
  'New Haven','South Central Connecticut','55,584','was incorporated as a town','1921','https://www.cityofwesthaven.com/','West_Haven,_Connecticut','John Poulsen'),
 ('new-haven','New Haven','New Haven City Hall',
  ['From City Hall on Church Street, follow Orange Street to Martin Luther King Jr. Boulevard and take it west for about 1.5 miles.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10).',
   'Turn left onto Derby Avenue (Route 34) and drive about a mile to 465.'],
  'New Haven','South Central Connecticut','134,023','was settled','1638','https://www.newhavenct.gov/','New_Haven,_Connecticut','Yajayra Torres'),
 ('orange','Orange','Orange Town Hall',
  ['From Town Hall, take Orange Center Road (Route 152) northwest for about 1.7 miles.',
   'Turn right onto the Derby Turnpike (Route 34) and stay on Route 34 east for about 3 miles into West Haven.',
   'We\u2019re at 465 Derby Avenue, near Forest Road (Route 122).'],
  'New Haven','South Central Connecticut','14,280','was incorporated','1822','https://www.orange-ct.gov/','Orange,_Connecticut','Frank Miele'),
 ('milford','Milford','Milford City Hall',
  ['From City Hall, head to the Boston Post Road (US 1) and follow the ramp toward Route 15.',
   'Take the Wilbur Cross Parkway (Route 15) north toward Hartford for about 5 miles.',
   'Take the Route 34 East exit toward New Haven and stay on Route 34 for about 3.7 miles to 465 Derby Avenue.'],
  'New Haven','South Central Connecticut','50,558','was settled','1639','https://www.milfordct.us/','Milford,_Connecticut','Ryan D.'),
 ('hamden','Hamden','the Hamden Government Center',
  ['From the Government Center on Dixwell Avenue, take Whitney Avenue to the Wilbur Cross Parkway (Route 15) and follow it about 5 miles.',
   'Take the exit for Route 69 toward New Haven and Woodbridge, then follow Whalley Avenue.',
   'Turn right onto Forest Road (Route 122) and follow it about 1.4 miles.',
   'Turn right onto Derby Avenue (Route 34). We\u2019re at 465.'],
  'New Haven','South Central Connecticut','61,169','was incorporated','1786','https://www.hamden.com/','Hamden,_Connecticut','Alissa Stover'),
 ('east-haven','East Haven','East Haven Town Hall',
  ['From Town Hall on Main Street, head to US 1 and take I-95 South.',
   'Keep left for exit 47 toward Downtown New Haven, onto the connector to Martin Luther King Jr. Boulevard.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10), then left onto Derby Avenue (Route 34) for about a mile to 465.'],
  'New Haven','South Central Connecticut','27,923','was incorporated','1785','https://www.easthaven-ct.gov/','East_Haven,_Connecticut','Erin Eberhardt'),
 ('branford','Branford','Branford Town Hall',
  ['From Town Hall on Main Street, take South Main Street (Route 146) and Cedar Street to I-95 South, about 5 miles on the highway.',
   'Keep left for exit 47 toward Downtown New Haven, onto the connector to Martin Luther King Jr. Boulevard.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10), then left onto Derby Avenue (Route 34) for about a mile to 465.'],
  'New Haven','South Central Connecticut','28,273','was settled','1644','https://www.branford-ct.gov/','Branford,_Connecticut','Lucas Cecchetto'),
 ('guilford','Guilford','Guilford Town Hall',
  ['From Town Hall on Park Street, take Church Street (Route 77) to I-95 South, about 12 miles on the highway.',
   'Keep left for exit 47 toward Downtown New Haven, onto the connector to Martin Luther King Jr. Boulevard.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10), then left onto Derby Avenue (Route 34) for about a mile to 465.'],
  'New Haven','South Central Connecticut','22,073','was settled','1639','https://www.guilfordct.gov/','Guilford,_Connecticut','Emily Loquine'),
 ('madison','Madison','the Madison Town Offices on Campus Drive',
  ['From the Town Offices, take Campus Drive and Duck Hole Road to I-95 South, about 18.5 miles on the highway.',
   'Take exit 47 toward Downtown New Haven, onto the connector to Martin Luther King Jr. Boulevard.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10), then left onto Derby Avenue (Route 34) for about a mile to 465.'],
  'New Haven','South Central Connecticut','17,691','was incorporated','1826','https://www.madisonct.org/','Madison,_Connecticut','Laura'),
 ('seymour','Seymour','Seymour Town Hall',
  ['From Town Hall on First Street, take Main Street (Route 115), then bear left onto Maple Street (Route 313) and stay on Route 313 for about 4 miles.',
   'Turn right onto Racebrook Road (Route 114) for about 3.5 miles.',
   'Turn left onto the Derby Turnpike (Route 34) and stay on Route 34 east for about 2.6 miles to 465 Derby Avenue.'],
  'New Haven','Naugatuck Valley','16,748','was incorporated','1850','https://www.seymourct.org/','Seymour,_Connecticut','loyd inabinet'),
 ('shelton','Shelton','Shelton City Hall',
  ['From City Hall on Hill Street, take Route 8 North for a short stretch to exit 12B, Route 34 toward Derby and New Haven.',
   'Follow Route 34 east through Derby, about 7 miles on Derby Avenue and the Derby Turnpike.',
   'We\u2019re at 465 Derby Avenue in West Haven, near Forest Road (Route 122).'],
  'Fairfield','Naugatuck Valley','40,869','was incorporated as a town','1789','https://www.cityofshelton.org/','Shelton,_Connecticut','John Poulsen'),
]

def drive(name):
    r = ROUTES[name]; a, b = sorted((r['v_mi'], r['o_mi']))
    miles = f"about {r['v_mi']:g} miles" if b - a <= 0.5 else f"about {round(a)} to {round(b)} miles"
    lo, hi = sorted((r['v_min'], r['o_min']))
    mins = f"about {lo} minutes" if lo == hi else f"about {lo} to {hi} minutes"
    return miles, mins

def route_src(name):
    r = ROUTES[name]
    return (f'Source: drive routes from {E(r["origin"])} to 465 Derby Ave on OpenStreetMap data, worked out with two free routers, '
            f'<a href="https://valhalla1.openstreetmap.de/" target="_blank" rel="noopener">Valhalla</a> ({r["v_mi"]:g} mi, {r["v_min"]} min) and '
            f'<a href="https://project-osrm.org/" target="_blank" rel="noopener">OSRM</a> ({r["o_mi"]:g} mi, {r["o_min"]} min), checked Nov 24, 2026. '
            f'Times are without traffic. Map data \u00a9 <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a>.')

def town_page(t, idx):
    slug, name, origin, steps, county, region, pop, estl, esty, site, wiki, rev = t
    path = f'towns/{slug}/'; base = '../../'
    crumbs = [('Home',''),('Towns we serve','towns/'),(name, path)]
    miles, mins = drive(name)
    oq = ROUTES[name]['origin'] + ', ' + name + ', CT'
    dirs = f'https://www.google.com/maps/dir/?api=1&origin={oq.replace(" ","+")}&destination={DEST_Q}'
    here = name == 'West Haven'
    h1 = 'Collision repair in West Haven' if here else f'Collision repair for {name} drivers'
    lead = (f"We\u2019re right here in West Haven. From City Hall, our shop at 465 Derby Ave is {miles}, {mins} without traffic." if here else
            f"From {origin} to our shop at 465 Derby Ave in West Haven is {miles}, {mins} without traffic.")
    far = ROUTES[name]['v_mi'] > 12
    start = (f'<p>Long drive after a rough day? You can start from home. Send photos of the damage from your phone, and our shop looks them over.</p>' if far else
             f'<p>Not sure if the car should be driven? Call us first, and we\u2019ll talk it through with you. We don\u2019t tow, but we know trusted local tow companies and can call them for you.</p>')
    others = ''.join(f'<a href="{base}towns/{s}/">{n}</a>' for s,n,*_ in TOWNS if s != slug)
    body = hero(base, crumbs, f'Serving {name}', h1, lead, 'town-hero') + f'''
<section><div class="wrap grid2"><div class="prose">
<h2>Getting here from {name}</h2>
<ol class="steps-list">{''.join(f'<li>{E(s)}</li>' for s in steps)}</ol>
<p class="src">{route_src(name)}</p>
<div class="ctas"><a class="btn btn-soft" href="{dirs}" target="_blank" rel="noopener" data-where="town-directions">Directions from {E(name)}</a></div>
</div><div class="prose">
<h2>Before you head over</h2>
{start}
<p>Mon to Fri, 8:00 AM to 4:30 PM. All insurance companies are welcome, and se habla espa\u00f1ol.</p>
<p>In Connecticut, the choice of repair shop is yours. <a href="{base}your-right-to-choose/">Read what the law says</a>.</p>
</div></div></section>
<section class="bone"><div class="wrap prose"><p class="label">About {name}</p>
<p>{name} is in {county} County, in the {region} planning region. Its population was {pop} in the 2020 U.S. Census. {name} {estl} in {esty}.</p>
<p class="src">Source: <a href="https://en.wikipedia.org/wiki/{wiki}" target="_blank" rel="noopener">Wikipedia, {E(wiki.replace("_"," "))}</a>, citing the 2020 U.S. Census. Town website: <a href="{site}" target="_blank" rel="noopener">{site.split("//")[1].rstrip("/")}</a>.</p>
</div></section>
<section class="alt"><div class="wrap"><p class="label">What a customer said</p>{review_block(rev)}</div></section>
<section><div class="wrap"><p class="label">Nearby towns</p><div class="links">{others}</div>
<div class="ctas"><a class="btn btn-call" href="{TEL}" data-where="town-bottom">{ICON_PHONE}Call {TELTXT}</a></div></div></section>'''
    title = ('Collision Repair in West Haven, CT | New England Collision' if here else f'Collision Repair Near {name}, CT | New England Collision, West Haven')
    desc = (f'From {name} to 465 Derby Ave, West Haven: {miles}, {mins}. Family owned, 30 years, same location. Call (203) 389-6400.')
    return path, page(path, title, desc, body, base, crumbs=crumbs)

def towns_hub():
    base = '../'; crumbs = [('Home',''),('Towns we serve','towns/')]
    rows = ''
    for s,n,*_ in TOWNS:
        miles, mins = drive(n)
        rows += f'<tr><th scope="row"><a href="{base}towns/{s}/">{n}</a></th><td>{miles.replace("about ","")}</td><td>{mins.replace("about ","")}</td></tr>'
    body = hero(base, crumbs, 'Towns we serve', 'Towns we serve', "Our shop is at 465 Derby Ave in West Haven. Here\u2019s how far it is from towns nearby, with directions for each.", 'towns-hero') + f'''
<section><div class="wrap prose"><table class="towns"><thead><tr><th scope="col">From</th><th scope="col">Distance</th><th scope="col">Drive time</th></tr></thead><tbody>{rows}</tbody></table>
<p class="src">Distances and times are from each town or city hall to our shop, worked out with two free routers on OpenStreetMap data (Valhalla and OSRM), checked Nov 24, 2026. Times are without traffic. Map data \u00a9 <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a>.</p>
{ctas(base,'towns-bottom')}</div></section>'''
    return 'towns/', page('towns/', 'Towns We Serve | New England Collision, West Haven CT',
      'Drive distance and time to 465 Derby Ave, West Haven from New Haven, Orange, Milford, Hamden, East Haven, Branford, Guilford, Madison, Seymour and Shelton.', body, base, crumbs=crumbs)

def towns_pages():
    return [towns_hub()] + [town_page(t,i) for i,t in enumerate(TOWNS)]

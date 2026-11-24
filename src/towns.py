# Phase 3: town pages. Executed by pages.py main() (shares build.py globals).
# Drive data: data/routes/townhall-routes-2026-11-24.json (Valhalla + OSRM, OpenStreetMap data, fetched Nov 24, 2026).
ROUTES = json.load(open(os.path.join(ROOT, '..', 'data', 'routes', 'townhall-routes-2026-11-24.json')))
DEST_Q = 'New+England+Collision,+465+Derby+Ave,+West+Haven,+CT+06516'
TOWNS = [
 # slug, name, origin label, steps
 ('west-haven','West Haven','West Haven City Hall',
  ['From City Hall on Main Street, head to Campbell Avenue and take it north for about 2.7 miles.',
   'Turn left onto Derby Avenue (Route 34). We\u2019re at 465.']),
 ('new-haven','New Haven','New Haven City Hall',
  ['From City Hall on Church Street, follow Orange Street to Martin Luther King Jr. Boulevard and take it west for about 1.5 miles.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10).',
   'Turn left onto Derby Avenue (Route 34) and drive about a mile to 465.']),
 ('orange','Orange','Orange Town Hall',
  ['From Town Hall, take Orange Center Road (Route 152) for about 1.7 miles.',
   'Turn right onto the Derby Turnpike (Route 34) and stay on Route 34 east for about 3 miles into West Haven.',
   'We\u2019re at 465 Derby Avenue, near Forest Road (Route 122).']),
 ('milford','Milford','Milford City Hall',
  ['From City Hall, head to the Boston Post Road (US 1) and follow the ramp toward Route 15.',
   'Take the Wilbur Cross Parkway (Route 15) north toward Hartford for about 5 miles.',
   'Take the Route 34 East exit toward New Haven and stay on Route 34 for about 3.7 miles to 465 Derby Avenue.']),
 ('hamden','Hamden','the Hamden Government Center',
  ['From the Government Center on Dixwell Avenue, take Whitney Avenue to the Wilbur Cross Parkway (Route 15) and follow it about 5 miles.',
   'Take the exit for Route 69 toward New Haven and Woodbridge onto Whalley Avenue.',
   'Turn left to stay on Whalley Avenue (Route 63), then turn right onto Dayton Street and left onto Fountain Street.',
   'Turn right onto Forest Road (Route 122) and follow it about 1.4 miles.',
   'Turn right onto Derby Avenue (Route 34). We\u2019re at 465.']),
 ('east-haven','East Haven','East Haven Town Hall',
  ['From Town Hall on Main Street, head to US 1 and take I-95 South.',
   'Keep left for exit 47 toward Downtown New Haven, onto the connector to Martin Luther King Jr. Boulevard.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10), then left onto Derby Avenue (Route 34) for about a mile to 465.']),
 ('branford','Branford','Branford Town Hall',
  ['From Town Hall on Main Street, take South Main Street (Route 146) and Cedar Street to I-95 South, about 5 miles on the highway.',
   'Keep left for exit 47 toward Downtown New Haven, onto the connector to Martin Luther King Jr. Boulevard.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10), then left onto Derby Avenue (Route 34) for about a mile to 465.']),
 ('guilford','Guilford','Guilford Town Hall',
  ['From Town Hall on Park Street, take Church Street (Route 77) to I-95 South, about 12 miles on the highway.',
   'Keep left for exit 47 toward Downtown New Haven, onto the connector to Martin Luther King Jr. Boulevard.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10), then left onto Derby Avenue (Route 34) for about a mile to 465.']),
 ('madison','Madison','the Madison Town Offices on Campus Drive',
  ['From the Town Offices, take Campus Drive and Duck Hole Road to I-95 South, about 18.5 miles on the highway.',
   'Take exit 47 toward Downtown New Haven, onto the connector to Martin Luther King Jr. Boulevard.',
   'Turn right onto Ella T. Grasso Boulevard (Route 10), then left onto Derby Avenue (Route 34) for about a mile to 465.']),
 ('seymour','Seymour','Seymour Town Hall',
  ['From Town Hall on First Street, take Main Street (Route 115), then bear left onto Maple Street (Route 313) and stay on Route 313 for about 4 miles.',
   'Turn right onto Racebrook Road (Route 114) for about 3.5 miles.',
   'Turn left onto the Derby Turnpike (Route 34) and stay on Route 34 east for about 2.6 miles to 465 Derby Avenue.']),
 ('shelton','Shelton','Shelton City Hall',
  ['From City Hall on Hill Street, take Route 8 North for a short stretch to exit 12B, Route 34 toward Derby and New Haven.',
   'Follow Route 34 east through Derby, about 7 miles on Derby Avenue and the Derby Turnpike.',
   'We\u2019re at 465 Derby Avenue in West Haven, near Forest Road (Route 122).']),
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
            f'<a href="https://github.com/valhalla/valhalla" target="_blank" rel="noopener">Valhalla</a> ({r["v_mi"]:g} mi, {r["v_min"]} min) and '
            f'<a href="https://project-osrm.org/" target="_blank" rel="noopener">OSRM</a> ({r["o_mi"]:g} mi, {r["o_min"]} min), checked Nov 24, 2026. '
            f'Times are without traffic. Map data \u00a9 <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a>.')

def dirs_link(name):
    oq = ROUTES[name]['origin'] + ', ' + name + ', CT'
    return f'https://www.google.com/maps/dir/?api=1&origin={oq.replace(" ","+")}&destination={DEST_Q}'

def towns_hub():
    # Mirror P3 FIX 1: one hub, town sections with in-page anchors, no separate town pages.
    base = '../'; crumbs = [('Home',''),('Towns we serve','towns/')]
    rows = ''; secs = ''
    for s,n,origin,steps in TOWNS:
        miles, mins = drive(n)
        rows += f'<tr><th scope="row"><a href="#{s}">{n}</a></th><td>{miles.replace("about ","")}</td><td>{mins.replace("about ","")}</td></tr>'
        li = ''.join(f'<li>{E(x)}</li>' for x in steps)
        secs += (f'<section class="town" id="{s}"><div class="wrap prose"><h2>From {n}</h2>\n'
                 f'<p>From {origin} to our shop at 465 Derby Ave is {miles}, {mins} without traffic.</p>\n'
                 f'<ol class="steps-list">{li}</ol>\n'
                 f'<div class="ctas"><a class="btn btn-soft" href="{dirs_link(n)}" target="_blank" rel="noopener" data-where="town-directions">Directions from {E(n)}</a></div></div></section>\n')
    shared = ("Not sure if the car should be driven? Call us first, and we\u2019ll talk it through with you. We don\u2019t tow, but we know trusted local tow companies "
              "and can call them for you. Coming from farther out? You can start from home. Send photos of the damage from your phone, and our shop looks them over.")
    src = ('Distances and times are from each town or city hall to our shop, worked out with two free routers on OpenStreetMap data '
           '(<a href="https://github.com/valhalla/valhalla" target="_blank" rel="noopener">Valhalla</a> and <a href="https://project-osrm.org/" target="_blank" rel="noopener">OSRM</a>), '
           'checked Nov 24, 2026. Times are without traffic. Exit numbers are current as of Nov 24, 2026. '
           'Map data \u00a9 <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap contributors</a>.')
    body = (hero(base, crumbs, 'Towns we serve', 'Towns we serve', "Our shop is at 465 Derby Ave in West Haven. Here\u2019s how far it is from towns nearby, with directions for each.", 'towns-hero')
            + f'\n<section><div class="wrap prose"><table class="towns"><thead><tr><th scope="col">From</th><th scope="col">Distance</th><th scope="col">Drive time</th></tr></thead><tbody>{rows}</tbody></table>\n'
            + f'<p>{shared}</p>\n</div></section>\n' + secs
            + f'<section><div class="wrap prose"><p class="src">{src}</p>\n{ctas(base,"towns-bottom")}</div></section>')
    return 'towns/', page('towns/', 'Towns We Serve | New England Collision, West Haven CT',
      'Drive distance, time and directions to 465 Derby Ave, West Haven from New Haven, Orange, Milford, Hamden, East Haven, Branford, Guilford, Madison, Seymour and Shelton.', body, base, crumbs=crumbs)

def towns_pages():
    return [towns_hub()]

# NEC website research

Tue Nov 24, 2026. Phase 1 (about 7:55 AM ET) and Phase 2 (about 8:15 AM ET onward).
Every site below was fetched on Nov 24, 2026 with a phone browser user agent (curl), except where it says the facts came from a search-result snapshot. We modeled STRUCTURE and SEO only. No text, images, or design files from any site were copied into NEC's site.

## A. The 5 collision sites we modeled

| # | Site | Type | What the fetch showed | What NEC borrowed (structure only) |
|---|---|---|---|---|
| 1 | Caliber Collision, https://www.caliber.com/ | National MSO | H1 "Get back on track with Caliber." Top paths: /online-estimate, /request-an-appointment, /find-a-location, /services/collision, /faq, /why-caliber. JSON-LD: Organization, WebSite with SearchAction, WebPage. | One short, reassuring H1. Estimate path as the second action. FAQ as its own page. |
| 2 | Gerber Collision & Glass, https://www.gerbercollision.com/ | National MSO | The phone number sits inside the H1. Paths: /online-repair-estimate, /schedule-appointment, /collision-repair hub with child pages (/collision-repair/auto-body-repair), /locations/<state>. JSON-LD: Organization, PostalAddress. | Phone in the first screen. A /services/ hub with one child page per service. Location pages under one folder (our town pages, Phase 3). |
| 3 | Crash Champions, https://www.crashchampions.com/ | National MSO | 4 tel: links on the homepage. JSON-LD: AutomotiveBusiness with OpeningHoursSpecification. A process folder: /our-process/getting-repair-estimate, /working-your-insurance-company, /rental-onsite, /towing-services, /repair-process. Service folder /repair-services/... | Tap-to-call repeated down every page. Hours in schema. Insurance help and towing/rental help as their own pages. |
| 4 | DG Collision Center, https://dgcollision.com/ | Independent, family owned since 1978, Lewisville TX | Title carries rating, review count and founding year. 12 tel: links and 9 sms: links on the homepage. JSON-LD: AutoBodyShop, AggregateRating, FAQPage, HowTo, BreadcrumbList, GeoCoordinates, City and AdministrativeArea. 121 internal paths, including about 35 town pages (/collision-repair-<town>/) and one page per car make and per insurer. Owner bio page (/about/shah-jiwani/). Spanish section (/es/). | Founding year and family in the title and first screen. FAQPage schema. One page per town (Phase 3). Text/message as a lead path next to Call. Spanish noted on every page. We did NOT copy its unverified-style claims (#1 rated, lifetime warranty, 24/7 towing) because NEC has not confirmed any of them. |
| 5 | Dewire Brothers Auto Body, https://dewirebrosautobody.com/ | Independent, family owned since 1947, Newton MA | Homepage HTML is 4.0 MB and renders in JavaScript (the server HTML has no tel: links or internal links). From a search snapshot of the page: family story told plainly ("still on the same corner"), hours and phone in the top bar, a photo-upload estimate form by damage zone. | The family story and "same corner" angle for our About page (NEC's own facts: 30 years, same location). Photo estimate as a calm second path. Also a warning: a heavy JavaScript page hides links from crawlers, so NEC stays static HTML. |

Also seen in the search snapshot (not modeled): Invisible Touch (Bedford MA) opens with a 3-step "before you call the insurer" plan and a right-to-choose line. Certified Collision Craft (Sherman Oaks CA) shows named, dated Yelp excerpts with links back to Yelp.

## B. High-converting local service sites outside collision

| Site | Trade | What the fetch showed | Pattern NEC used |
|---|---|---|---|
| Parker & Sons, https://www.parkerandsons.com/ | HVAC, plumbing, electrical (Phoenix) | Service hubs with children: /cooling/ac-repair, /heating/heating-repair, /plumbing/water-heaters. /service-area, /about-us/reviews, /offers, /warranties, /financing-options. Online scheduler (ServiceTitan). JSON-LD: GeoCircle service area, GeoCoordinates. | Hub and child service URLs (/services/<service>/). Service area pages (Phase 3). |
| Roto-Rooter, https://www.rotorooter.com/ | Plumbing (national) | H1 "The Plumbing Experts You've Trusted for Over 90 Years." Years in business in the H1. /schedule-service, /frequently-asked-questions/, /locations/, deep service tree (/plumbing/drain-cleaning ...). Chat vendor script (Ngage) on the page. | Years in business as trust right under the H1. Dedicated FAQ page. |
| Morgan & Morgan, https://www.forthepeople.com/ | Personal injury law | H1 "Personal Injury Lawyers Fighting For You." /free-case-evaluation as the single main action, /practice-areas/ with one page per case type (for example /practice-areas/auto-accident-attorneys/), /faq/, /office-locations/. JSON-LD: Service, OfferCatalog, ContactPoint. A chatbot on the page. | One main action per page. One page per problem the visitor has. A guided chat path. NEC's chat is scripted buttons only, no AI, per Joe's rule. |
| Baker Roofing, https://www.bakerroofing.com/ | Roofing (mostly commercial) | /schedule-an-estimate as the action, /our-locations/, /projects/ with case pages, /our-story-always-good-work/. BreadcrumbList schema. | Breadcrumbs on every inner page. A plain "our story" page. (Baker is mostly commercial, so it says less about drivers after a crash.) |

## C. Sourced statistics (only numbers read from the source on Nov 24, 2026)

From BrightLocal, Local Consumer Review Survey 2026 (published Feb 11, 2026; 1,002 US adults), https://www.brightlocal.com/research/local-consumer-review-survey/ :
- 97% of consumers read reviews for local businesses.
- 74% only care about reviews written in the last three months.
- 31% will only use a business with 4.5 stars or more (17% in 2025); 68% will only use one with 4 or more stars.
- After reading positive reviews, 54% then check the business's website (32% when last asked in 2019).
- 80% say they're likely to use a business that responds to all of its reviews; 89% expect owners to respond.
What NEC does with it: real, named, dated Google reviews near every Call button; link to the live Google listing; keep reviews fresh (re-check on launch day); the website has to answer the questions people bring from reviews.

From web.dev, "Milliseconds Make Millions" (study commissioned by Google, run by 55 and Deloitte; 37 brand sites, over 30 million sessions, late 2019), https://web.dev/case-studies/milliseconds-make-millions :
- A 0.1 second improvement in four speed metrics raised lead-generation sites' progression to the form submission page by 21.6%, and page views by 7%.
What NEC does with it: static HTML, inline CSS, no third-party scripts, small images with set sizes, lazy-load below the fold. Phase 1 homepage measured 1.2 s largest paint on Lighthouse mobile.

Not cited: the often-quoted "53% of mobile visits leave after 3 seconds." The Think with Google page we tried now shows a sign-in wall, so we could not read the source today.

## D. Patterns applied
1. One calm promise above the fold, one main action (Call), two quiet ones (photos, Message Us).
2. Sticky Call / Directions / Message Us on phones. Tap-to-call in the header, the first screen, mid-page and the footer of every page.
3. Real reviews, word for word with names and dates, right after the first screen and on service pages.
4. A 3-step plan (Call or send photos; help with insurance and a rental [CONFIRM]; drive home fixed).
5. Insurance fear reversal using the CT statute wording (38a-354) and "All insurance companies welcome" (verified).
6. Hub and child URLs: /services/<service>/, /faq/, /about/, /your-right-to-choose/, /contact/ (and /towns/<town>/ in Phase 3).
7. Schema: AutoBodyShop on every page, Service on service pages, FAQPage on /faq/, BreadcrumbList on every inner page.
8. Speed: static HTML, self-hosted subset fonts, WebP images with width and height, no tracker on by default.

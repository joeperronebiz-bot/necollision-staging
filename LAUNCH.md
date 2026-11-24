# NEC staging site: launch notes (Phase 1, Nov 24, 2026)

This repo is a STAGING copy. It must not be indexed and is not the live site.

## What to flip at launch (only after: CEO check, Mirror PASS, logged-out real-phone test with the tester named, and Joe's own yes)
1. In `src/build.py` set `STAGING = False` and rebuild. That removes `<meta name="robots" content="noindex, nofollow">` from every page and the black "STAGING PREVIEW" bar.
2. `robots.txt` becomes: `User-agent: *` / `Allow: /` / `Sitemap: https://necollision.com/sitemap.xml` (the build writes this when STAGING is False).
3. Copy the built files into the live repo joeperronebiz-bot/necollision-site. Keep that repo's `CNAME` file (necollision.com) and `.nojekyll`. Never add a CNAME here.
4. Canonicals and og:url already point at https://necollision.com/... No change needed.
5. og:image points at https://necollision.com/og-image-1200x630.png, which exists in the live repo. Keep it there (or replace it with a new image of the same name).
6. Tracking: in `assets/js/tracker.js` set `ENABLED = true` and fill in `send()` for the ONE provider Joe picks. Add that provider's script tag. Until then it is off.
7. Clear every [CONFIRM] marker (search the built HTML and JS for "[CONFIRM").
8. Re-check the Google rating and each quoted review on Google the day of launch.

# NEC staging site: launch notes (updated Phase 2, Nov 24, 2026)

This repo is a STAGING copy. It must not be indexed and is not the live site.

## What to flip at launch (only after: CEO check, Mirror PASS, logged-out real-phone test with the tester named, and Joe's own yes)
1. In `src/build.py` set `STAGING = False` and rebuild. That removes `<meta name="robots" content="noindex, nofollow">` from every page, the black "STAGING PREVIEW" bar, and the dashed staging-only [CONFIRM] note boxes.
2. sitemap.xml is NOT on staging (Mirror fix 13). The build writes it to the site only when STAGING is False; a copy is kept in `src/launch-kit/sitemap.xml`.
3. `robots.txt` becomes: `User-agent: *` / `Allow: /` / `Sitemap: https://necollision.com/sitemap.xml` (the build writes this when STAGING is False).
4. Copy the built files into the live repo joeperronebiz-bot/necollision-site. Keep that repo's `CNAME` file (necollision.com) and `.nojekyll`. Never add a CNAME here.
5. Canonicals and og:url already point at https://necollision.com/... No change needed.
6. og:image points at https://necollision.com/og-image-1200x630.png, which exists in the live repo. Keep it there (or replace it with a new image of the same name).
7. Tracking: in `assets/js/tracker.js` set `ENABLED = true` and fill in `send()` for the ONE provider Joe picks. Add that provider's script tag. Until then it is off.
8. Clear every [CONFIRM] marker (search the built HTML and JS for "[CONFIRM").
9. Re-check the Google rating and each quoted review on Google the day of launch.

10. Shop photos: the 4 photos with identifiable staff are off the site (Mirror fix 12). Kept on the box only in /workspace/nec/website/seo-site-2026-11-24/held-photos/. Add back only after consent, or use a no-people shop photo.
11. Chat: `SMS_ON` in chat.js stays false until Phones & Admin confirms (203) 389-6400 takes texts.
12. Thanksgiving week lines come off on Mon Nov 30.

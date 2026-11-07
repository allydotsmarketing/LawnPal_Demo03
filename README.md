# LawnPal Demo 03

Demo website for a South Florida lawn care & landscaping company, by [AllyDots Marketing](https://allydotsmarketing.com).
9 static pages, no build tools needed to host (GitHub Pages ready). The site is marked `noindex` while it is a demo.

## Pages
- `/` Home
- `/services/lawn-mowing-edging/`
- `/services/hedge-shrub-trimming/`
- `/services/yard-leaf-cleanup/`
- `/services/weed-control-fertilization/`
- `/biweekly-lawn-maintenance/`
- `/about/` (provisional copy, owner name in `tools/site.json`)
- `/gallery/` (sample photos, filters + photo viewer)
- `/contact/` (demo quote form, sends nothing)

## Rebrand for a new client
1. Edit `tools/site.json` (name, phone, WhatsApp, hours, cities, social links, base URL). Set `"noindex": false` when it goes live. `map_embed` can hold a custom Google My Maps embed URL; empty shows Broward County.
2. Edit service copy in `tools/build.py` (`SERVICES`, `HOME_FAQS`).
3. Colors live at the top of `assets/css/styles.css` (`:root`).
4. Run `python3 tools/build.py` to regenerate every page.

Photos: Unsplash images are free for commercial use. Other photos in `assets/img` should be replaced with the client's own before the site goes live.

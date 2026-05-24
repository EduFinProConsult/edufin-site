# EDU-FIN PROCONSULT SERVICES — Marketing Site

A complete, production-ready, responsive one-page website for **EDU-FIN PROCONSULT SERVICES**, delivering educational, financial, and business consulting to students, entrepreneurs, and organizations across Nigeria and the wider African continent.

## Deliverable

- **Single self-contained file:** `index.html` (~140 KB, no external assets required beyond Google Fonts + Font Awesome CDN)
- Logo embedded as base64 inside the HTML — no separate image file is required to render the site.

## Files

| File | Purpose |
|---|---|
| `index.html` | The production site. Open directly in a browser or deploy as a static asset. |
| `build.py` | Build script that injects the base64 logo into the HTML template. Re-run if the source logo changes. |
| `logo.jpg` | Optimised JPEG of the source logo (400×266, ~12 KB). |
| `logo.b64` | Base64 payload of `logo.jpg` consumed by `build.py`. |
| `_qa/` | Screenshots captured during QA at 1440 / 1024 / 768 / 375 viewports. |

## Tech stack

- Semantic HTML5
- CSS custom properties (design tokens) — no framework
- Vanilla JS (IIFE) — no React/Vue/Angular, no build step
- Google Fonts: **Poppins** (display) + **Inter** (body)
- Font Awesome 6 (icons, CDN)
- Inline SVG icons for service tiles and post placeholders

## Design system

| Token | Value |
|---|---|
| Navy | `#1A3C6E` |
| Green | `#0E7C4A` |
| Gold | `#F0A500` |
| Background | `#F5F7FA` |
| Ink | `#2D2D2D` |
| Brand gradient | `linear-gradient(135deg, #1A3C6E → #0E7C4A)` |

## Features implemented

- Sticky transparent-to-solid navbar with mobile hamburger
- Hero with gradient background, animated blob shapes, dual CTAs, trust indicators, and brand card
- Animated counters (Intersection Observer triggered)
- About section with pills, mission/vision/values
- Six-card services grid with hover lift and inline SVG icons
- Why-Choose-Us section on navy with six benefit cards
- Testimonial carousel: 5 quotes, prev/next, dots, auto-rotate (6 s), touch swipe, pause-on-hover/focus
- Blog preview: 3 posts with gradient art placeholders and tags
- Contact: gradient info card + map placeholder + validated form (first/last/email/phone/service/message)
- Newsletter form in the mega footer
- Mega footer (brand, company, services, newsletter, socials)
- Skip link, focus-visible outlines, ARIA labels, prefers-reduced-motion handling
- Responsive breakpoints at 375 / 768 / 1024 / 1440 (hamburger activates ≤900 px so the desktop nav stays uncluttered)

## QA performed

- Cross-viewport visual review at 1440, 1024, 768, 375 (screenshots in `_qa/`)
- No JS console errors at any viewport
- Hamburger toggles correctly; menu closes on link click or `Escape`
- Counter animation triggers on scroll and ends with correct values (500+, 12+, 95%, 15)
- Testimonial carousel paginates and renders 5 dots
- Contact form: empty submit shows 5 inline errors; valid submit shows success notice
- Tag balance verified (all `section`, `article`, and `div` open/close counts match)

## Re-building

```bash
python3 build.py
```

This regenerates `index.html` with the latest CSS, copy, and embedded base64 logo.

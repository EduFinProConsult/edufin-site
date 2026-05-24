#!/usr/bin/env python3
"""Build self-contained index.html for EDU-FIN PROCONSULT SERVICES."""
from pathlib import Path

ROOT = Path(__file__).parent
LOGO_B64 = (ROOT / "logo.b64").read_text().strip()
LOGO_DATA_URI = f"data:image/jpeg;base64,{LOGO_B64}"

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="EDU-FIN PROCONSULT SERVICES — trusted educational, financial, and business advisory partner for students, entrepreneurs, and organizations across Nigeria and Africa." />
  <meta name="theme-color" content="#1A3C6E" />
  <meta property="og:title" content="EDU-FIN PROCONSULT SERVICES" />
  <meta property="og:description" content="Educational, financial, and business consulting that helps you make confident decisions and grow with purpose." />
  <meta property="og:type" content="website" />
  <title>EDU-FIN PROCONSULT SERVICES — Educational & Financial Consulting in Nigeria & Africa</title>

  <!-- Preconnect & Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet" />
  <!-- Font Awesome (allowed by brief) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" referrerpolicy="no-referrer" />

  <!-- Favicon (inline SVG) -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%231A3C6E'/><path d='M6 22 L12 16 L18 19 L26 9' stroke='%230E7C4A' stroke-width='3' fill='none' stroke-linecap='round' stroke-linejoin='round'/><circle cx='26' cy='9' r='2.5' fill='%23F0A500'/></svg>" />

  <style>
    /* ---------- Design tokens ---------- */
    :root {
      --c-navy: #1A3C6E;
      --c-green: #0E7C4A;
      --c-gold: #F0A500;
      --c-bg: #F5F7FA;
      --c-ink: #2D2D2D;
      --c-white: #ffffff;
      --c-muted: #5A6477;
      --c-border: #E2E8F0;
      --grad: linear-gradient(135deg, #1A3C6E 0%, #0E7C4A 100%);
      --grad-soft: linear-gradient(135deg, rgba(26,60,110,0.06) 0%, rgba(14,124,74,0.06) 100%);
      --shadow-sm: 0 2px 8px rgba(26,60,110,0.06);
      --shadow-md: 0 8px 24px rgba(26,60,110,0.10);
      --shadow-lg: 0 18px 40px rgba(26,60,110,0.16);
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 22px;
      --radius-pill: 999px;
      --font-display: 'Poppins', 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      --font-body: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
      --container: 1200px;
      --nav-h: 76px;
      --ease: cubic-bezier(0.4, 0, 0.2, 1);
    }

    *, *::before, *::after { box-sizing: border-box; }
    html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
    body {
      margin: 0;
      font-family: var(--font-body);
      color: var(--c-ink);
      background: var(--c-white);
      line-height: 1.65;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    img { max-width: 100%; display: block; }
    a { color: var(--c-navy); text-decoration: none; transition: color .2s var(--ease); }
    a:hover { color: var(--c-green); }
    h1, h2, h3, h4 { font-family: var(--font-display); color: var(--c-navy); line-height: 1.2; margin: 0 0 .5em; font-weight: 700; }
    h1 { font-size: clamp(2rem, 4.5vw + 1rem, 3.6rem); font-weight: 800; }
    h2 { font-size: clamp(1.6rem, 2.2vw + 1rem, 2.4rem); }
    h3 { font-size: 1.25rem; }
    p { margin: 0 0 1rem; }
    button, input, textarea, select { font: inherit; }
    .container { width: min(100% - 2rem, var(--container)); margin-inline: auto; }
    .section { padding: clamp(4rem, 8vw, 7rem) 0; }
    .section--alt { background: var(--c-bg); }
    .eyebrow {
      display: inline-block;
      font-family: var(--font-display);
      font-size: .8rem;
      font-weight: 600;
      letter-spacing: .14em;
      text-transform: uppercase;
      color: var(--c-green);
      margin-bottom: .9rem;
    }
    .section-title { text-align: center; max-width: 760px; margin-inline: auto; margin-bottom: clamp(2rem, 4vw, 3.2rem); }
    .section-title p { color: var(--c-muted); font-size: 1.05rem; }
    .gradient-text {
      background: var(--grad);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
    }

    /* ---------- Buttons ---------- */
    .btn {
      display: inline-flex;
      align-items: center;
      gap: .6rem;
      padding: .85rem 1.6rem;
      border-radius: var(--radius-pill);
      font-family: var(--font-display);
      font-weight: 600;
      font-size: .98rem;
      cursor: pointer;
      border: 2px solid transparent;
      transition: transform .2s var(--ease), box-shadow .2s var(--ease), background .2s var(--ease), color .2s var(--ease), border-color .2s var(--ease);
      text-decoration: none;
      white-space: nowrap;
    }
    .btn--primary { background: var(--c-gold); color: var(--c-navy); box-shadow: 0 8px 20px rgba(240,165,0,0.35); }
    .btn--primary:hover { transform: translateY(-2px); box-shadow: 0 12px 26px rgba(240,165,0,0.45); color: var(--c-navy); }
    .btn--ghost { background: transparent; color: var(--c-white); border-color: rgba(255,255,255,0.6); }
    .btn--ghost:hover { background: var(--c-white); color: var(--c-navy); border-color: var(--c-white); }
    .btn--solid { background: var(--c-navy); color: #fff; }
    .btn--solid:hover { background: var(--c-green); color: #fff; transform: translateY(-2px); }

    /* ---------- Navbar ---------- */
    .nav {
      position: fixed;
      inset: 0 0 auto 0;
      z-index: 100;
      background: transparent;
      transition: background .3s var(--ease), box-shadow .3s var(--ease), backdrop-filter .3s var(--ease);
    }
    .nav.is-scrolled {
      background: rgba(255,255,255,0.96);
      backdrop-filter: saturate(150%) blur(8px);
      -webkit-backdrop-filter: saturate(150%) blur(8px);
      box-shadow: var(--shadow-sm);
    }
    .nav__inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: var(--nav-h);
      gap: 1.5rem;
    }
    .nav__brand { display: flex; align-items: center; gap: .7rem; }
    .nav__logo { height: 44px; width: auto; border-radius: 6px; }
    .nav__brand-text {
      font-family: var(--font-display);
      font-weight: 700;
      color: var(--c-white);
      font-size: 1.05rem;
      letter-spacing: .01em;
      transition: color .3s var(--ease);
      line-height: 1.1;
    }
    .nav__brand-text small {
      display: block;
      font-weight: 500;
      font-size: .7rem;
      letter-spacing: .14em;
      text-transform: uppercase;
      opacity: .8;
    }
    .nav.is-scrolled .nav__brand-text { color: var(--c-navy); }
    .nav__menu {
      display: flex;
      align-items: center;
      gap: .25rem;
      list-style: none;
      margin: 0;
      padding: 0;
    }
    .nav__menu a {
      display: inline-block;
      padding: .55rem .95rem;
      color: var(--c-white);
      font-weight: 500;
      font-size: .95rem;
      border-radius: var(--radius-pill);
      transition: background .2s var(--ease), color .2s var(--ease);
      white-space: nowrap;
    }
    .nav__menu a:hover { background: rgba(255,255,255,0.15); }
    .nav.is-scrolled .nav__menu a { color: var(--c-navy); }
    .nav.is-scrolled .nav__menu a:hover { background: var(--c-bg); color: var(--c-green); }
    .nav__cta { margin-left: .5rem; }
    .nav__toggle {
      display: none;
      background: transparent;
      border: 0;
      width: 44px;
      height: 44px;
      cursor: pointer;
      color: var(--c-white);
      align-items: center;
      justify-content: center;
      border-radius: 8px;
    }
    .nav.is-scrolled .nav__toggle { color: var(--c-navy); }
    .nav__toggle:focus-visible { outline: 2px solid var(--c-gold); outline-offset: 2px; }
    .nav__toggle .bar {
      display: block;
      width: 24px;
      height: 2px;
      background: currentColor;
      position: relative;
      transition: transform .25s var(--ease), opacity .25s var(--ease);
    }
    .nav__toggle .bar::before,
    .nav__toggle .bar::after {
      content: '';
      position: absolute;
      left: 0;
      width: 24px;
      height: 2px;
      background: currentColor;
      transition: transform .25s var(--ease), top .25s var(--ease);
    }
    .nav__toggle .bar::before { top: -8px; }
    .nav__toggle .bar::after  { top: 8px; }
    .nav__toggle.is-active .bar { background: transparent; }
    .nav__toggle.is-active .bar::before { top: 0; transform: rotate(45deg); }
    .nav__toggle.is-active .bar::after  { top: 0; transform: rotate(-45deg); }

    /* ---------- Hero ---------- */
    .hero {
      position: relative;
      min-height: 100vh;
      padding: calc(var(--nav-h) + 3rem) 0 5rem;
      background: var(--grad);
      color: #fff;
      overflow: hidden;
      display: flex;
      align-items: center;
    }
    .hero::after {
      content: '';
      position: absolute;
      inset: auto 0 0 0;
      height: 80px;
      background: linear-gradient(to bottom, transparent, rgba(245,247,250,0.4), var(--c-bg));
      pointer-events: none;
    }
    .hero__grid {
      position: relative;
      z-index: 2;
      display: grid;
      grid-template-columns: 1.1fr .9fr;
      gap: 3rem;
      align-items: center;
    }
    .hero__copy h1 { color: #fff; }
    .hero__copy h1 .accent { color: var(--c-gold); }
    .hero__copy p.lead {
      font-size: clamp(1.05rem, 1.1vw + .8rem, 1.2rem);
      color: rgba(255,255,255,0.92);
      max-width: 560px;
      margin-bottom: 2rem;
    }
    .hero__actions { display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 2.5rem; }
    .hero__trust {
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem 2rem;
      color: rgba(255,255,255,0.9);
      font-size: .92rem;
    }
    .hero__trust span { display: inline-flex; align-items: center; gap: .5rem; }
    .hero__trust i { color: var(--c-gold); }

    /* Hero visual card */
    .hero__visual {
      position: relative;
      display: grid;
      place-items: center;
    }
    .hero__card {
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.18);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-radius: var(--radius-lg);
      padding: 2rem;
      max-width: 420px;
      width: 100%;
      box-shadow: var(--shadow-lg);
      position: relative;
      z-index: 2;
    }
    .hero__card-logo {
      background: #fff;
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-md);
    }
    .hero__card-logo img { width: 100%; height: auto; }
    .hero__card h3 { color: #fff; margin-bottom: .35rem; }
    .hero__card p { color: rgba(255,255,255,0.88); margin: 0; font-size: .95rem; }
    .hero__card-meta {
      display: flex;
      gap: 1rem;
      margin-top: 1.25rem;
      padding-top: 1.25rem;
      border-top: 1px solid rgba(255,255,255,0.15);
    }
    .hero__card-meta div { flex: 1; }
    .hero__card-meta strong {
      display: block;
      font-family: var(--font-display);
      font-size: 1.4rem;
      color: var(--c-gold);
      line-height: 1;
    }
    .hero__card-meta span { font-size: .8rem; color: rgba(255,255,255,0.75); }

    /* Animated shapes */
    .shape {
      position: absolute;
      border-radius: 50%;
      filter: blur(2px);
      opacity: .35;
      pointer-events: none;
      z-index: 1;
    }
    .shape--1 { width: 380px; height: 380px; background: radial-gradient(circle, rgba(240,165,0,0.6), transparent 70%); top: -120px; left: -120px; animation: floatA 14s ease-in-out infinite; }
    .shape--2 { width: 320px; height: 320px; background: radial-gradient(circle, rgba(14,124,74,0.7), transparent 70%); bottom: -100px; right: -80px; animation: floatB 16s ease-in-out infinite; }
    .shape--3 { width: 220px; height: 220px; background: radial-gradient(circle, rgba(255,255,255,0.5), transparent 70%); top: 40%; right: 35%; animation: floatC 12s ease-in-out infinite; opacity: .2; }
    .shape--4 { width: 160px; height: 160px; background: radial-gradient(circle, rgba(240,165,0,0.5), transparent 70%); bottom: 18%; left: 8%; animation: floatA 18s ease-in-out infinite reverse; }
    @keyframes floatA { 0%,100% { transform: translate(0,0) scale(1); } 50% { transform: translate(40px, 30px) scale(1.08); } }
    @keyframes floatB { 0%,100% { transform: translate(0,0) scale(1); } 50% { transform: translate(-30px, -40px) scale(1.05); } }
    @keyframes floatC { 0%,100% { transform: translate(0,0); } 50% { transform: translate(20px, -25px); } }

    /* ---------- Stats / Counters ---------- */
    .stats {
      position: relative;
      z-index: 3;
      margin-top: -3rem;
      margin-bottom: -3rem;
    }
    .stats__grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1rem;
      background: #fff;
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--c-border);
    }
    .stat { text-align: center; padding: .5rem 1rem; }
    .stat__num {
      font-family: var(--font-display);
      font-weight: 800;
      font-size: clamp(1.8rem, 2.6vw + .5rem, 2.6rem);
      line-height: 1;
      background: var(--grad);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      display: inline-block;
    }
    .stat__label {
      display: block;
      margin-top: .5rem;
      color: var(--c-muted);
      font-size: .92rem;
      font-weight: 500;
    }

    /* ---------- About ---------- */
    .about__grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3rem;
      align-items: center;
    }
    .about__media {
      position: relative;
      border-radius: var(--radius-lg);
      background: var(--grad-soft);
      padding: 2rem;
      aspect-ratio: 4/3;
      display: grid;
      place-items: center;
      overflow: hidden;
    }
    .about__media::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 20% 30%, rgba(240,165,0,0.18), transparent 50%),
                  radial-gradient(circle at 80% 75%, rgba(14,124,74,0.18), transparent 50%);
      pointer-events: none;
    }
    .about__media-card {
      position: relative;
      background: #fff;
      border-radius: var(--radius-md);
      padding: 1.75rem;
      box-shadow: var(--shadow-lg);
      max-width: 320px;
      text-align: center;
    }
    .about__media-card img { width: 100%; }
    .about__media-card h4 {
      margin-top: 1rem;
      margin-bottom: .25rem;
      font-family: var(--font-display);
      color: var(--c-navy);
    }
    .about__media-card p { color: var(--c-muted); font-size: .9rem; margin: 0; }
    .about__pills {
      display: flex;
      gap: .6rem;
      flex-wrap: wrap;
      margin: 1.25rem 0 1.75rem;
    }
    .pill {
      display: inline-flex;
      align-items: center;
      gap: .4rem;
      padding: .45rem .9rem;
      border-radius: var(--radius-pill);
      background: var(--grad-soft);
      color: var(--c-navy);
      font-size: .85rem;
      font-weight: 600;
      border: 1px solid rgba(26,60,110,0.1);
    }
    .pill i { color: var(--c-green); }
    .about__points { list-style: none; padding: 0; margin: 0 0 2rem; display: grid; gap: .9rem; }
    .about__points li { display: flex; gap: .8rem; align-items: flex-start; }
    .about__points i {
      flex: none;
      width: 28px; height: 28px;
      border-radius: 50%;
      background: var(--grad);
      color: #fff;
      display: grid;
      place-items: center;
      font-size: .75rem;
    }
    .about__points strong { color: var(--c-navy); font-family: var(--font-display); }

    /* ---------- Services ---------- */
    .services__grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }
    .service {
      position: relative;
      background: #fff;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-lg);
      padding: 2rem;
      transition: transform .3s var(--ease), box-shadow .3s var(--ease), border-color .3s var(--ease);
      overflow: hidden;
    }
    .service::before {
      content: '';
      position: absolute;
      inset: auto 0 0 0;
      height: 4px;
      background: var(--grad);
      transform: scaleX(0);
      transform-origin: left;
      transition: transform .35s var(--ease);
    }
    .service:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); border-color: transparent; }
    .service:hover::before { transform: scaleX(1); }
    .service__icon {
      width: 56px;
      height: 56px;
      border-radius: var(--radius-md);
      background: var(--grad);
      display: grid;
      place-items: center;
      color: #fff;
      margin-bottom: 1.25rem;
      box-shadow: 0 10px 20px rgba(26,60,110,0.18);
    }
    .service__icon svg { width: 28px; height: 28px; }
    .service h3 { color: var(--c-navy); }
    .service p { color: var(--c-muted); font-size: .96rem; }
    .service ul {
      list-style: none;
      padding: 0;
      margin: 1rem 0 0;
      display: grid;
      gap: .4rem;
    }
    .service ul li {
      position: relative;
      padding-left: 1.25rem;
      font-size: .9rem;
      color: var(--c-ink);
    }
    .service ul li::before {
      content: '';
      position: absolute;
      left: 0; top: .6em;
      width: 6px; height: 6px;
      background: var(--c-green);
      border-radius: 50%;
    }

    /* ---------- Why Choose Us ---------- */
    .why { background: var(--c-navy); color: #fff; position: relative; overflow: hidden; }
    .why::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 10% 0%, rgba(14,124,74,0.4), transparent 45%),
                  radial-gradient(circle at 90% 100%, rgba(240,165,0,0.18), transparent 50%);
    }
    .why .container { position: relative; z-index: 1; }
    .why h2 { color: #fff; }
    .why .section-title p { color: rgba(255,255,255,0.85); }
    .why .eyebrow { color: var(--c-gold); }
    .why__grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.25rem;
    }
    .why__card {
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      transition: transform .3s var(--ease), background .3s var(--ease);
    }
    .why__card:hover { transform: translateY(-4px); background: rgba(255,255,255,0.1); }
    .why__card-icon {
      width: 48px; height: 48px;
      border-radius: var(--radius-sm);
      background: var(--c-gold);
      color: var(--c-navy);
      display: grid;
      place-items: center;
      margin-bottom: 1rem;
      font-size: 1.1rem;
    }
    .why__card h3 { color: #fff; font-size: 1.1rem; }
    .why__card p { color: rgba(255,255,255,0.82); font-size: .92rem; margin: 0; }

    /* ---------- Testimonials ---------- */
    .testimonials__viewport {
      position: relative;
      overflow: hidden;
      border-radius: var(--radius-lg);
    }
    .testimonials__track {
      display: flex;
      transition: transform .55s var(--ease);
      will-change: transform;
    }
    .testimonial {
      flex: 0 0 100%;
      padding: 1rem;
    }
    .testimonial__card {
      background: #fff;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      box-shadow: var(--shadow-md);
      max-width: 820px;
      margin: 0 auto;
      text-align: center;
      position: relative;
    }
    .testimonial__quote-icon {
      width: 48px; height: 48px;
      margin: 0 auto 1rem;
      border-radius: 50%;
      background: var(--grad);
      color: #fff;
      display: grid;
      place-items: center;
      font-size: 1.1rem;
      box-shadow: var(--shadow-md);
    }
    .testimonial__text {
      font-size: 1.1rem;
      color: var(--c-ink);
      font-style: italic;
      margin-bottom: 1.5rem;
      line-height: 1.7;
    }
    .testimonial__author {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
    }
    .testimonial__avatar {
      width: 56px; height: 56px;
      border-radius: 50%;
      background: var(--grad);
      color: #fff;
      display: grid;
      place-items: center;
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.1rem;
    }
    .testimonial__meta { text-align: left; }
    .testimonial__name {
      font-family: var(--font-display);
      font-weight: 700;
      color: var(--c-navy);
      display: block;
    }
    .testimonial__role { color: var(--c-muted); font-size: .9rem; }
    .testimonials__nav {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      margin-top: 1.5rem;
    }
    .testimonials__arrow {
      width: 44px; height: 44px;
      border-radius: 50%;
      border: 1px solid var(--c-border);
      background: #fff;
      cursor: pointer;
      color: var(--c-navy);
      display: grid;
      place-items: center;
      transition: background .2s var(--ease), color .2s var(--ease), transform .2s var(--ease);
    }
    .testimonials__arrow:hover { background: var(--c-navy); color: #fff; transform: translateY(-2px); }
    .testimonials__dots { display: flex; gap: .5rem; }
    .testimonials__dot {
      width: 10px; height: 10px;
      border-radius: 50%;
      background: var(--c-border);
      border: 0;
      cursor: pointer;
      transition: background .2s var(--ease), transform .2s var(--ease);
    }
    .testimonials__dot.is-active { background: var(--c-green); transform: scale(1.3); }

    /* ---------- Blog ---------- */
    .blog__grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.75rem;
    }
    .post {
      background: #fff;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform .3s var(--ease), box-shadow .3s var(--ease);
    }
    .post:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); }
    .post__media {
      aspect-ratio: 16/10;
      background: var(--grad);
      position: relative;
      display: grid;
      place-items: center;
      color: rgba(255,255,255,0.92);
      overflow: hidden;
    }
    .post__media svg { width: 60%; height: 60%; opacity: .9; }
    .post__media::after {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 70% 20%, rgba(240,165,0,0.35), transparent 50%);
    }
    .post--b .post__media { background: linear-gradient(135deg, #0E7C4A 0%, #1A3C6E 100%); }
    .post--c .post__media { background: linear-gradient(135deg, #1A3C6E 0%, #F0A500 130%); }
    .post__body { padding: 1.5rem; display: flex; flex-direction: column; flex: 1; gap: .5rem; }
    .post__tag {
      display: inline-block;
      align-self: flex-start;
      background: var(--grad-soft);
      color: var(--c-green);
      font-size: .72rem;
      font-weight: 700;
      letter-spacing: .1em;
      text-transform: uppercase;
      padding: .35rem .7rem;
      border-radius: var(--radius-pill);
      margin-bottom: .3rem;
    }
    .post h3 { font-size: 1.15rem; margin-bottom: .35rem; }
    .post p { color: var(--c-muted); font-size: .92rem; margin: 0; }
    .post__meta {
      margin-top: auto;
      padding-top: 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: var(--c-muted);
      font-size: .85rem;
    }
    .post__link {
      color: var(--c-green);
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: .3rem;
    }
    .post__link:hover i { transform: translateX(3px); }
    .post__link i { transition: transform .2s var(--ease); }

    /* ---------- Contact ---------- */
    .contact__grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5rem;
    }
    .contact__info {
      background: var(--c-navy);
      background-image: var(--grad);
      color: #fff;
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      position: relative;
      overflow: hidden;
    }
    .contact__info::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at 90% 10%, rgba(240,165,0,0.22), transparent 50%);
    }
    .contact__info > * { position: relative; z-index: 1; }
    .contact__info h3 { color: #fff; font-size: 1.5rem; }
    .contact__info p { color: rgba(255,255,255,0.88); margin-bottom: 1.5rem; }
    .contact__list { list-style: none; padding: 0; margin: 0 0 2rem; display: grid; gap: 1.1rem; }
    .contact__list li { display: flex; gap: 1rem; align-items: flex-start; }
    .contact__list i {
      flex: none;
      width: 40px; height: 40px;
      border-radius: 10px;
      background: rgba(255,255,255,0.12);
      color: var(--c-gold);
      display: grid;
      place-items: center;
    }
    .contact__list strong { display: block; font-family: var(--font-display); color: #fff; margin-bottom: .15rem; }
    .contact__list span { color: rgba(255,255,255,0.85); font-size: .95rem; }
    .contact__list a { color: rgba(255,255,255,0.85); }
    .contact__list a:hover { color: var(--c-gold); }
    .contact__socials { display: flex; gap: .6rem; margin-top: 1rem; }
    .contact__socials a {
      width: 40px; height: 40px;
      border-radius: 50%;
      background: rgba(255,255,255,0.12);
      display: grid;
      place-items: center;
      color: #fff;
      transition: background .2s var(--ease), transform .2s var(--ease), color .2s var(--ease);
    }
    .contact__socials a:hover { background: var(--c-gold); color: var(--c-navy); transform: translateY(-3px); }

    .map {
      margin-top: 1.5rem;
      border-radius: var(--radius-md);
      overflow: hidden;
      aspect-ratio: 16/7;
      background:
        linear-gradient(135deg, rgba(26,60,110,0.85), rgba(14,124,74,0.85)),
        repeating-linear-gradient(45deg, rgba(255,255,255,0.05) 0 6px, transparent 6px 14px),
        repeating-linear-gradient(-45deg, rgba(255,255,255,0.05) 0 6px, transparent 6px 14px);
      display: grid;
      place-items: center;
      color: #fff;
      position: relative;
      text-align: center;
    }
    .map__pin {
      width: 50px; height: 50px;
      border-radius: 50% 50% 50% 0;
      background: var(--c-gold);
      color: var(--c-navy);
      display: grid;
      place-items: center;
      transform: rotate(-45deg);
      box-shadow: 0 8px 20px rgba(0,0,0,0.3);
      margin-bottom: .75rem;
    }
    .map__pin i { transform: rotate(45deg); }
    .map small { display: block; color: rgba(255,255,255,0.85); margin-top: .25rem; font-size: .85rem; }

    /* Form */
    .form {
      background: #fff;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      box-shadow: var(--shadow-md);
    }
    .form h3 { margin-bottom: .35rem; }
    .form p.muted { color: var(--c-muted); margin-bottom: 1.5rem; }
    .form__row { display: grid; gap: 1rem; grid-template-columns: 1fr 1fr; }
    .field { margin-bottom: 1rem; display: flex; flex-direction: column; gap: .35rem; }
    .field label { font-weight: 600; font-size: .9rem; color: var(--c-navy); font-family: var(--font-display); }
    .field input, .field select, .field textarea {
      padding: .85rem 1rem;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-sm);
      background: var(--c-bg);
      color: var(--c-ink);
      transition: border-color .2s var(--ease), box-shadow .2s var(--ease), background .2s var(--ease);
      width: 100%;
      font-family: var(--font-body);
    }
    .field textarea { min-height: 130px; resize: vertical; }
    .field input:focus, .field select:focus, .field textarea:focus {
      outline: none;
      border-color: var(--c-green);
      background: #fff;
      box-shadow: 0 0 0 4px rgba(14,124,74,0.12);
    }
    .field--error input,
    .field--error select,
    .field--error textarea { border-color: #C0392B; }
    .field__error { color: #C0392B; font-size: .82rem; min-height: 1.1em; }
    .form .btn { width: 100%; justify-content: center; }
    .form__notice {
      display: none;
      margin-top: 1rem;
      padding: .9rem 1rem;
      background: rgba(14,124,74,0.1);
      color: var(--c-green);
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: .92rem;
      border-left: 4px solid var(--c-green);
    }
    .form__notice.is-visible { display: block; }

    /* ---------- Footer ---------- */
    .footer {
      background: #0F1E36;
      color: rgba(255,255,255,0.82);
      padding: 4rem 0 1.5rem;
      font-size: .94rem;
    }
    .footer h4 { color: #fff; font-family: var(--font-display); font-size: 1.05rem; margin-bottom: 1rem; }
    .footer__grid {
      display: grid;
      grid-template-columns: 1.4fr 1fr 1fr 1.2fr;
      gap: 2.5rem;
      padding-bottom: 2.5rem;
      border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    .footer__brand { display: flex; gap: .75rem; align-items: center; margin-bottom: 1rem; }
    .footer__logo {
      height: 50px;
      width: auto;
      border-radius: 8px;
      background: #fff;
      padding: 6px;
    }
    .footer__brand-text {
      font-family: var(--font-display);
      font-weight: 700;
      color: #fff;
      font-size: 1rem;
      line-height: 1.2;
    }
    .footer__brand-text small {
      display: block;
      font-weight: 500;
      font-size: .7rem;
      letter-spacing: .14em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.7);
    }
    .footer p { color: rgba(255,255,255,0.75); margin-bottom: 1rem; }
    .footer ul { list-style: none; padding: 0; margin: 0; display: grid; gap: .55rem; }
    .footer ul a { color: rgba(255,255,255,0.78); }
    .footer ul a:hover { color: var(--c-gold); }
    .footer__socials { display: flex; gap: .55rem; margin-top: 1rem; }
    .footer__socials a {
      width: 36px; height: 36px;
      border-radius: 50%;
      background: rgba(255,255,255,0.08);
      display: grid;
      place-items: center;
      color: #fff;
      transition: background .2s var(--ease), color .2s var(--ease), transform .2s var(--ease);
    }
    .footer__socials a:hover { background: var(--c-gold); color: var(--c-navy); transform: translateY(-2px); }
    .footer__newsletter { display: flex; gap: .5rem; margin-top: .5rem; }
    .footer__newsletter input {
      flex: 1;
      padding: .75rem 1rem;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(255,255,255,0.18);
      background: rgba(255,255,255,0.06);
      color: #fff;
      font-family: var(--font-body);
    }
    .footer__newsletter input::placeholder { color: rgba(255,255,255,0.55); }
    .footer__newsletter input:focus {
      outline: none;
      border-color: var(--c-gold);
      box-shadow: 0 0 0 3px rgba(240,165,0,0.2);
    }
    .footer__newsletter button {
      padding: .75rem 1.1rem;
      border-radius: var(--radius-pill);
      border: 0;
      background: var(--c-gold);
      color: var(--c-navy);
      font-weight: 700;
      font-family: var(--font-display);
      cursor: pointer;
      transition: transform .2s var(--ease), background .2s var(--ease);
    }
    .footer__newsletter button:hover { transform: translateY(-2px); background: #FFB627; }
    .footer__bottom {
      padding-top: 1.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      justify-content: space-between;
      color: rgba(255,255,255,0.6);
      font-size: .85rem;
    }
    .footer__bottom a { color: rgba(255,255,255,0.7); }
    .footer__bottom a:hover { color: var(--c-gold); }

    /* ---------- Reveal animations ---------- */
    .reveal {
      opacity: 0;
      transform: translateY(28px);
      transition: opacity .8s var(--ease), transform .8s var(--ease);
      will-change: opacity, transform;
    }
    .reveal.is-visible { opacity: 1; transform: translateY(0); }
    .reveal[data-delay="1"] { transition-delay: .08s; }
    .reveal[data-delay="2"] { transition-delay: .16s; }
    .reveal[data-delay="3"] { transition-delay: .24s; }
    .reveal[data-delay="4"] { transition-delay: .32s; }

    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after { animation: none !important; transition: none !important; }
      .reveal { opacity: 1; transform: none; }
      html { scroll-behavior: auto; }
    }

    /* ---------- Responsive ---------- */
    @media (max-width: 1024px) {
      .hero__grid { grid-template-columns: 1fr; gap: 2.5rem; }
      .nav__menu a { padding: .5rem .7rem; font-size: .9rem; }
      .hero__visual { order: -1; }
      .hero__card { max-width: 380px; }
      .stats__grid { grid-template-columns: repeat(2, 1fr); }
      .about__grid { grid-template-columns: 1fr; }
      .services__grid { grid-template-columns: repeat(2, 1fr); }
      .why__grid { grid-template-columns: repeat(2, 1fr); }
      .blog__grid { grid-template-columns: repeat(2, 1fr); }
      .contact__grid { grid-template-columns: 1fr; }
      .footer__grid { grid-template-columns: 1fr 1fr; gap: 2rem; }
    }
    @media (max-width: 900px) {
      .nav__menu {
        position: fixed;
        inset: var(--nav-h) 0 auto 0;
        background: #fff;
        flex-direction: column;
        align-items: stretch;
        padding: 1rem;
        gap: .25rem;
        box-shadow: var(--shadow-lg);
        transform: translateY(-100%);
        opacity: 0;
        visibility: hidden;
        transition: transform .3s var(--ease), opacity .3s var(--ease), visibility .3s;
        z-index: 99;
        max-height: calc(100vh - var(--nav-h));
        overflow-y: auto;
        top: var(--nav-h);
      }
      .nav__menu.is-open { opacity: 1; visibility: visible; }
      .nav__menu.is-open { transform: translateY(0); opacity: 1; visibility: visible; }
      .nav__menu a { color: var(--c-navy); padding: .85rem 1rem; }
      .nav__menu a:hover { background: var(--c-bg); }
      .nav__cta { margin: .5rem 0 0; text-align: center; }
      .nav__toggle { display: inline-flex; }
      .nav__brand-text small { display: none; }

    }
    @media (max-width: 767px) {
      .services__grid, .blog__grid { grid-template-columns: 1fr; }
      .why__grid { grid-template-columns: 1fr; }
      .form__row { grid-template-columns: 1fr; }
      .contact__info, .form { padding: 1.75rem; }
      .testimonial__card { padding: 1.75rem; }
      .footer__grid { grid-template-columns: 1fr; }
    }
    @media (max-width: 479px) {
      .stats__grid { grid-template-columns: 1fr 1fr; padding: 1.5rem; gap: .75rem; }
      .hero { padding: calc(var(--nav-h) + 2rem) 0 4rem; }
      .hero__actions .btn { width: 100%; justify-content: center; }
      .hero__trust { gap: .75rem 1.25rem; font-size: .85rem; }
    }
    @media (min-width: 1440px) {
      .container { width: min(100% - 3rem, 1280px); }
      h1 { font-size: 4rem; }
    }

    /* Focus visibility */
    a:focus-visible, button:focus-visible, input:focus-visible, textarea:focus-visible, select:focus-visible {
      outline: 2px solid var(--c-gold);
      outline-offset: 2px;
    }

    /* Skip link */
    .skip-link {
      position: absolute;
      left: 1rem; top: 1rem;
      background: var(--c-navy);
      color: #fff;
      padding: .55rem .9rem;
      border-radius: 6px;
      transform: translateY(-200%);
      z-index: 1000;
      transition: transform .2s var(--ease);
    }
    .skip-link:focus { transform: translateY(0); color: #fff; }
  </style>
</head>
<body>
  <a href="#main" class="skip-link">Skip to content</a>

  <!-- ===================== NAV ===================== -->
  <header class="nav" id="nav" role="banner">
    <div class="container nav__inner">
      <a href="#hero" class="nav__brand" aria-label="EDU-FIN PROCONSULT SERVICES — home">
        <img src="__LOGO__" alt="EDU-FIN PROCONSULT SERVICES logo" class="nav__logo" width="44" height="44" />
        <span class="nav__brand-text">EDU-FIN PROCONSULT
          <small>Services</small>
        </span>
      </a>

      <nav aria-label="Primary">
        <ul class="nav__menu" id="navMenu">
          <li><a href="#about">About</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#why">Why Us</a></li>
          <li><a href="#testimonials">Testimonials</a></li>
          <li><a href="#blog">Insights</a></li>
          <li><a href="#contact">Contact</a></li>
          <li class="nav__cta"><a href="#contact" class="btn btn--primary"><i class="fa-solid fa-paper-plane" aria-hidden="true"></i> Book a Consultation</a></li>
        </ul>
      </nav>

      <button class="nav__toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="navMenu">
        <span class="bar" aria-hidden="true"></span>
      </button>
    </div>
  </header>

  <main id="main">

    <!-- ===================== HERO ===================== -->
    <section class="hero" id="hero" aria-labelledby="heroTitle">
      <span class="shape shape--1" aria-hidden="true"></span>
      <span class="shape shape--2" aria-hidden="true"></span>
      <span class="shape shape--3" aria-hidden="true"></span>
      <span class="shape shape--4" aria-hidden="true"></span>

      <div class="container hero__grid">
        <div class="hero__copy reveal">
          <span class="eyebrow" style="color: var(--c-gold);">Educational • Financial • Business Consulting</span>
          <h1 id="heroTitle">Smart guidance for <span class="accent">students</span>, <br/>steady growth for <span class="accent">businesses</span>.</h1>
          <p class="lead">EDU-FIN PROCONSULT SERVICES partners with students, entrepreneurs, and organizations across Nigeria and Africa — helping you make confident education choices, manage money wisely, and build businesses that last.</p>
          <div class="hero__actions">
            <a href="#contact" class="btn btn--primary"><i class="fa-solid fa-calendar-check" aria-hidden="true"></i> Book a Free Consultation</a>
            <a href="#services" class="btn btn--ghost">Explore Our Services <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          </div>
          <div class="hero__trust" aria-label="Trust indicators">
            <span><i class="fa-solid fa-shield-halved" aria-hidden="true"></i> Trusted by 500+ clients</span>
            <span><i class="fa-solid fa-earth-africa" aria-hidden="true"></i> Nigeria &amp; pan-African reach</span>
            <span><i class="fa-solid fa-circle-check" aria-hidden="true"></i> Practical, results-driven</span>
          </div>
        </div>

        <div class="hero__visual reveal" data-delay="2">
          <div class="hero__card">
            <div class="hero__card-logo">
              <img src="__LOGO__" alt="EDU-FIN PROCONSULT SERVICES brand mark" />
            </div>
            <h3>From classroom to boardroom</h3>
            <p>One trusted partner for scholarships, study abroad, financial literacy, business planning, and SME growth.</p>
            <div class="hero__card-meta">
              <div>
                <strong>12+</strong>
                <span>Years of experience</span>
              </div>
              <div>
                <strong>500+</strong>
                <span>Clients served</span>
              </div>
              <div>
                <strong>15</strong>
                <span>African countries</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== STATS / COUNTERS ===================== -->
    <section class="container stats" aria-label="Key statistics">
      <div class="stats__grid reveal">
        <div class="stat">
          <span class="stat__num" data-count="500" data-suffix="+">0</span>
          <span class="stat__label">Clients empowered</span>
        </div>
        <div class="stat">
          <span class="stat__num" data-count="12" data-suffix="+">0</span>
          <span class="stat__label">Years of expertise</span>
        </div>
        <div class="stat">
          <span class="stat__num" data-count="95" data-suffix="%">0</span>
          <span class="stat__label">Client satisfaction</span>
        </div>
        <div class="stat">
          <span class="stat__num" data-count="15" data-suffix="">0</span>
          <span class="stat__label">Countries reached</span>
        </div>
      </div>
    </section>

    <!-- ===================== ABOUT ===================== -->
    <section class="section" id="about" aria-labelledby="aboutTitle">
      <div class="container">
        <div class="about__grid">
          <div class="about__media reveal">
            <div class="about__media-card">
              <img src="__LOGO__" alt="EDU-FIN PROCONSULT SERVICES" />
              <h4>Education + Finance, in one place</h4>
              <p>A consulting partner that understands the realities of African students, families, and small businesses.</p>
            </div>
          </div>

          <div class="reveal" data-delay="1">
            <span class="eyebrow">About Us</span>
            <h2 id="aboutTitle">Practical advisory for <span class="gradient-text">real African ambitions</span>.</h2>
            <p>EDU-FIN PROCONSULT SERVICES was founded to close a simple gap: too many students and entrepreneurs across Nigeria and Africa work hard but lack trusted guidance on education pathways, money, and business decisions. We bridge that gap with clear, ethical, and locally-grounded advice.</p>

            <div class="about__pills">
              <span class="pill"><i class="fa-solid fa-graduation-cap" aria-hidden="true"></i> Education</span>
              <span class="pill"><i class="fa-solid fa-coins" aria-hidden="true"></i> Personal Finance</span>
              <span class="pill"><i class="fa-solid fa-briefcase" aria-hidden="true"></i> Business Advisory</span>
              <span class="pill"><i class="fa-solid fa-chart-line" aria-hidden="true"></i> Growth Strategy</span>
            </div>

            <ul class="about__points">
              <li>
                <i class="fa-solid fa-bullseye" aria-hidden="true"></i>
                <span><strong>Our mission</strong> — equip every learner, entrepreneur, and organization with clear knowledge and a confident plan.</span>
              </li>
              <li>
                <i class="fa-solid fa-eye" aria-hidden="true"></i>
                <span><strong>Our vision</strong> — to be Africa&rsquo;s most trusted partner where education and finance meet purpose and progress.</span>
              </li>
              <li>
                <i class="fa-solid fa-handshake" aria-hidden="true"></i>
                <span><strong>Our values</strong> — integrity first, practical solutions, lasting relationships, and community-focused growth.</span>
              </li>
            </ul>

            <a href="#contact" class="btn btn--solid">Talk to an advisor <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== SERVICES ===================== -->
    <section class="section section--alt" id="services" aria-labelledby="servicesTitle">
      <div class="container">
        <div class="section-title reveal">
          <span class="eyebrow">What We Do</span>
          <h2 id="servicesTitle">Services built around <span class="gradient-text">your next step</span>.</h2>
          <p>Whether you&rsquo;re applying to university, learning to budget, or scaling a small business, our team gives you a clear roadmap and walks the journey with you.</p>
        </div>

        <div class="services__grid">

          <article class="service reveal" data-delay="1">
            <div class="service__icon" aria-hidden="true">
              <!-- Graduation cap icon -->
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 10l10-5 10 5-10 5L2 10z"/><path d="M6 12v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/><path d="M22 10v6"/></svg>
            </div>
            <h3>Educational Consulting</h3>
            <p>Guidance for students, parents, and schools — from course choice to global opportunities.</p>
            <ul>
              <li>University &amp; programme selection</li>
              <li>Scholarship search &amp; applications</li>
              <li>Study abroad &amp; visa support</li>
              <li>Career planning for students</li>
            </ul>
          </article>

          <article class="service reveal" data-delay="2">
            <div class="service__icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 6H9.5a3.5 3.5 0 1 0 0 7H14a3.5 3.5 0 1 1 0 7H6"/></svg>
            </div>
            <h3>Financial Advisory</h3>
            <p>Make confident money decisions with practical tools and ethical, plain-English advice.</p>
            <ul>
              <li>Personal budgeting &amp; savings plans</li>
              <li>Investment &amp; portfolio guidance</li>
              <li>Family financial planning</li>
              <li>Financial literacy workshops</li>
            </ul>
          </article>

          <article class="service reveal" data-delay="3">
            <div class="service__icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/></svg>
            </div>
            <h3>Business Consulting</h3>
            <p>Build, formalise, and grow your business with structured plans that match local realities.</p>
            <ul>
              <li>Business plan &amp; model design</li>
              <li>CAC registration &amp; compliance</li>
              <li>Market entry &amp; positioning</li>
              <li>Operations &amp; team setup</li>
            </ul>
          </article>

          <article class="service reveal" data-delay="1">
            <div class="service__icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 15l4-4 4 4 5-7"/></svg>
            </div>
            <h3>SME Growth &amp; Strategy</h3>
            <p>Move beyond survival mode. Sharpen pricing, sales, and systems so your business scales.</p>
            <ul>
              <li>Sales &amp; marketing playbooks</li>
              <li>Pricing &amp; revenue strategy</li>
              <li>Financial controls for SMEs</li>
              <li>Access-to-funding readiness</li>
            </ul>
          </article>

          <article class="service reveal" data-delay="2">
            <div class="service__icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-8 0v2"/><circle cx="12" cy="7" r="4"/><path d="M2 21v-1a5 5 0 0 1 5-5"/><path d="M22 21v-1a5 5 0 0 0-5-5"/></svg>
            </div>
            <h3>Training &amp; Workshops</h3>
            <p>Practical training for schools, companies, and community groups — delivered in person or online.</p>
            <ul>
              <li>Financial literacy bootcamps</li>
              <li>Entrepreneurship masterclasses</li>
              <li>Career readiness sessions</li>
              <li>Corporate &amp; NGO training</li>
            </ul>
          </article>

          <article class="service reveal" data-delay="3">
            <div class="service__icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 18 0 9 9 0 1 0-18 0"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18"/><path d="M12 3a14 14 0 0 0 0 18"/></svg>
            </div>
            <h3>Organisational Advisory</h3>
            <p>Support for NGOs, cooperatives, and institutions seeking sustainable impact and good governance.</p>
            <ul>
              <li>Strategy &amp; programme design</li>
              <li>Grant &amp; proposal writing</li>
              <li>Monitoring &amp; evaluation</li>
              <li>Capacity building</li>
            </ul>
          </article>

        </div>
      </div>
    </section>

    <!-- ===================== WHY US ===================== -->
    <section class="section why" id="why" aria-labelledby="whyTitle">
      <div class="container">
        <div class="section-title reveal">
          <span class="eyebrow">Why Choose Us</span>
          <h2 id="whyTitle">Africa-rooted expertise. Practical, ethical, and unrushed.</h2>
          <p>We&rsquo;re not a faceless consultancy. We&rsquo;re a team that listens, plans with you, and stays with you long after the first decision is made.</p>
        </div>

        <div class="why__grid">
          <div class="why__card reveal" data-delay="1">
            <div class="why__card-icon"><i class="fa-solid fa-user-tie" aria-hidden="true"></i></div>
            <h3>Experienced advisors</h3>
            <p>A blended team of educators, finance professionals, and entrepreneurs with on-the-ground African experience.</p>
          </div>
          <div class="why__card reveal" data-delay="2">
            <div class="why__card-icon"><i class="fa-solid fa-compass" aria-hidden="true"></i></div>
            <h3>Tailored, never templated</h3>
            <p>Every plan is built around your reality — income, family, location, goals — not a copy-and-paste framework.</p>
          </div>
          <div class="why__card reveal" data-delay="3">
            <div class="why__card-icon"><i class="fa-solid fa-shield-halved" aria-hidden="true"></i></div>
            <h3>Trust &amp; transparency</h3>
            <p>Clear fees, honest advice, and zero pressure. We tell you when something isn&rsquo;t the right move.</p>
          </div>
          <div class="why__card reveal" data-delay="1">
            <div class="why__card-icon"><i class="fa-solid fa-people-arrows" aria-hidden="true"></i></div>
            <h3>End-to-end support</h3>
            <p>From the first consultation to long-term check-ins, we walk with you across every stage.</p>
          </div>
          <div class="why__card reveal" data-delay="2">
            <div class="why__card-icon"><i class="fa-solid fa-language" aria-hidden="true"></i></div>
            <h3>Locally grounded</h3>
            <p>We understand Nigerian regulation, local banking, and pan-African realities — and explain them simply.</p>
          </div>
          <div class="why__card reveal" data-delay="3">
            <div class="why__card-icon"><i class="fa-solid fa-rocket" aria-hidden="true"></i></div>
            <h3>Outcome focused</h3>
            <p>We measure success in admissions secured, businesses launched, debts cleared, and goals reached.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== TESTIMONIALS ===================== -->
    <section class="section" id="testimonials" aria-labelledby="testimonialsTitle">
      <div class="container">
        <div class="section-title reveal">
          <span class="eyebrow">What Clients Say</span>
          <h2 id="testimonialsTitle">Stories from people we&rsquo;ve walked with.</h2>
          <p>Students, founders, and community leaders across Nigeria and Africa share how EDU-FIN PROCONSULT SERVICES helped them move forward with confidence.</p>
        </div>

        <div class="testimonials reveal" data-delay="1">
          <div class="testimonials__viewport">
            <div class="testimonials__track" id="testTrack" aria-live="polite">

              <div class="testimonial">
                <div class="testimonial__card">
                  <div class="testimonial__quote-icon" aria-hidden="true"><i class="fa-solid fa-quote-left"></i></div>
                  <p class="testimonial__text">&ldquo;I came in confused about which university to apply to and how to fund it. The team walked me through every step, helped me apply for two scholarships, and today I&rsquo;m studying abroad on a full grant. Life-changing.&rdquo;</p>
                  <div class="testimonial__author">
                    <div class="testimonial__avatar">AO</div>
                    <div class="testimonial__meta">
                      <span class="testimonial__name">Adaeze O.</span>
                      <span class="testimonial__role">Postgraduate Student • Lagos, Nigeria</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="testimonial">
                <div class="testimonial__card">
                  <div class="testimonial__quote-icon" aria-hidden="true"><i class="fa-solid fa-quote-left"></i></div>
                  <p class="testimonial__text">&ldquo;My fashion business was busy but barely profitable. EDU-FIN helped me rework pricing, set up proper books, and register the company. Six months later, profit margins doubled and I hired my first two staff.&rdquo;</p>
                  <div class="testimonial__author">
                    <div class="testimonial__avatar">CN</div>
                    <div class="testimonial__meta">
                      <span class="testimonial__name">Chinwe N.</span>
                      <span class="testimonial__role">Founder, Lumière Apparel • Abuja</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="testimonial">
                <div class="testimonial__card">
                  <div class="testimonial__quote-icon" aria-hidden="true"><i class="fa-solid fa-quote-left"></i></div>
                  <p class="testimonial__text">&ldquo;Their financial literacy workshop for our staff was the most practical training we&rsquo;ve ever paid for. People left with budgets, savings goals, and a plan. We bring them back every year now.&rdquo;</p>
                  <div class="testimonial__author">
                    <div class="testimonial__avatar">KM</div>
                    <div class="testimonial__meta">
                      <span class="testimonial__name">Kwame M.</span>
                      <span class="testimonial__role">HR Director • Accra, Ghana</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="testimonial">
                <div class="testimonial__card">
                  <div class="testimonial__quote-icon" aria-hidden="true"><i class="fa-solid fa-quote-left"></i></div>
                  <p class="testimonial__text">&ldquo;As an NGO we needed structure. EDU-FIN PROCONSULT helped us design a three-year strategy, sharpened our grant proposals, and we secured our first major international funder within seven months.&rdquo;</p>
                  <div class="testimonial__author">
                    <div class="testimonial__avatar">FA</div>
                    <div class="testimonial__meta">
                      <span class="testimonial__name">Folake A.</span>
                      <span class="testimonial__role">Executive Director, BrightFutures NGO • Ibadan</span>
                    </div>
                  </div>
                </div>
              </div>

              <div class="testimonial">
                <div class="testimonial__card">
                  <div class="testimonial__quote-icon" aria-hidden="true"><i class="fa-solid fa-quote-left"></i></div>
                  <p class="testimonial__text">&ldquo;I was drowning in small loans. They didn&rsquo;t judge — they built me a clear payoff plan and helped me start saving for the first time in years. I&rsquo;m now debt-free and have an emergency fund.&rdquo;</p>
                  <div class="testimonial__author">
                    <div class="testimonial__avatar">BE</div>
                    <div class="testimonial__meta">
                      <span class="testimonial__name">Bayo E.</span>
                      <span class="testimonial__role">Civil Servant • Port Harcourt</span>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>

          <div class="testimonials__nav" role="group" aria-label="Testimonial controls">
            <button class="testimonials__arrow" id="testPrev" aria-label="Previous testimonial"><i class="fa-solid fa-arrow-left" aria-hidden="true"></i></button>
            <div class="testimonials__dots" id="testDots" role="tablist" aria-label="Select testimonial"></div>
            <button class="testimonials__arrow" id="testNext" aria-label="Next testimonial"><i class="fa-solid fa-arrow-right" aria-hidden="true"></i></button>
          </div>
        </div>
      </div>
    </section>

    <!-- ===================== BLOG ===================== -->
    <section class="section section--alt" id="blog" aria-labelledby="blogTitle">
      <div class="container">
        <div class="section-title reveal">
          <span class="eyebrow">Insights &amp; Resources</span>
          <h2 id="blogTitle">Latest from the <span class="gradient-text">EDU-FIN journal</span>.</h2>
          <p>Practical reads on education, money, and business — written for African readers, in plain language.</p>
        </div>

        <div class="blog__grid">
          <article class="post reveal" data-delay="1">
            <div class="post__media post--a" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M2 10l10-5 10 5-10 5L2 10z"/><path d="M6 12v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/></svg>
            </div>
            <div class="post__body">
              <span class="post__tag">Education</span>
              <h3>10 fully-funded scholarships Nigerian students can apply to in 2025</h3>
              <p>A curated list of legitimate, fully-funded scholarship opportunities — with realistic eligibility notes and deadlines.</p>
              <div class="post__meta">
                <span><i class="fa-regular fa-calendar" aria-hidden="true"></i> 12 Feb 2025 · 6 min</span>
                <a href="#" class="post__link">Read <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
              </div>
            </div>
          </article>

          <article class="post post--b reveal" data-delay="2">
            <div class="post__media" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 2v20"/><path d="M17 6H9.5a3.5 3.5 0 1 0 0 7H14a3.5 3.5 0 1 1 0 7H6"/></svg>
            </div>
            <div class="post__body">
              <span class="post__tag">Finance</span>
              <h3>How to build your first emergency fund on a Nigerian income</h3>
              <p>A step-by-step plan to save your first 3 months of expenses, even when prices keep changing and income is irregular.</p>
              <div class="post__meta">
                <span><i class="fa-regular fa-calendar" aria-hidden="true"></i> 28 Jan 2025 · 5 min</span>
                <a href="#" class="post__link">Read <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
              </div>
            </div>
          </article>

          <article class="post post--c reveal" data-delay="3">
            <div class="post__media" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3 3v18h18"/><path d="M7 15l4-4 4 4 5-7"/></svg>
            </div>
            <div class="post__body">
              <span class="post__tag">Business</span>
              <h3>From side hustle to registered SME: a 90-day roadmap</h3>
              <p>The structure, paperwork, and pricing decisions that separate a hustle from a real, fundable business.</p>
              <div class="post__meta">
                <span><i class="fa-regular fa-calendar" aria-hidden="true"></i> 14 Jan 2025 · 8 min</span>
                <a href="#" class="post__link">Read <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
              </div>
            </div>
          </article>
        </div>

        <div style="text-align:center; margin-top: 2.5rem;">
          <a href="#" class="btn btn--solid">Browse all insights <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>
        </div>
      </div>
    </section>

    <!-- ===================== CONTACT ===================== -->
    <section class="section" id="contact" aria-labelledby="contactTitle">
      <div class="container">
        <div class="section-title reveal">
          <span class="eyebrow">Get in Touch</span>
          <h2 id="contactTitle">Let&rsquo;s plan your next confident step.</h2>
          <p>Tell us what you&rsquo;re working on — education, finance, or business — and we&rsquo;ll get back within one working day.</p>
        </div>

        <div class="contact__grid">
          <div class="contact__info reveal">
            <h3>Talk to EDU-FIN PROCONSULT</h3>
            <p>Reach us through the channel that works best for you. Consultations are available in person, online, and on-site for organisations.</p>

            <ul class="contact__list">
              <li>
                <i class="fa-solid fa-location-dot" aria-hidden="true"></i>
                <div>
                  <strong>Visit us</strong>
                  <span>Lagos &amp; Abuja, Nigeria — with partners across West Africa.</span>
                </div>
              </li>
              <li>
                <i class="fa-solid fa-phone" aria-hidden="true"></i>
                <div>
                  <strong>Call or WhatsApp</strong>
                  <span><a href="tel:+2348000000000">+234 800 000 0000</a></span>
                </div>
              </li>
              <li>
                <i class="fa-solid fa-envelope" aria-hidden="true"></i>
                <div>
                  <strong>Email</strong>
                  <span><a href="mailto:hello@edufinproconsult.com">hello@edufinproconsult.com</a></span>
                </div>
              </li>
              <li>
                <i class="fa-regular fa-clock" aria-hidden="true"></i>
                <div>
                  <strong>Working hours</strong>
                  <span>Mon &ndash; Fri, 9:00 AM &ndash; 6:00 PM WAT</span>
                </div>
              </li>
            </ul>

            <div class="contact__socials" aria-label="Social profiles">
              <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i></a>
              <a href="#" aria-label="X / Twitter"><i class="fa-brands fa-x-twitter" aria-hidden="true"></i></a>
              <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a>
              <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f" aria-hidden="true"></i></a>
              <a href="#" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></a>
            </div>

            <div class="map" role="img" aria-label="Map placeholder showing Lagos, Nigeria office location">
              <div>
                <div class="map__pin"><i class="fa-solid fa-location-dot" aria-hidden="true"></i></div>
                <strong>EDU-FIN PROCONSULT HQ</strong>
                <small>Lagos &amp; Abuja, Nigeria</small>
              </div>
            </div>
          </div>

          <form class="form reveal" data-delay="1" id="contactForm" novalidate>
            <h3>Send us a message</h3>
            <p class="muted">Fill in the form and our team will reach out shortly.</p>

            <div class="form__row">
              <div class="field">
                <label for="firstName">First name</label>
                <input type="text" id="firstName" name="firstName" autocomplete="given-name" required />
                <span class="field__error" id="err-firstName"></span>
              </div>
              <div class="field">
                <label for="lastName">Last name</label>
                <input type="text" id="lastName" name="lastName" autocomplete="family-name" required />
                <span class="field__error" id="err-lastName"></span>
              </div>
            </div>

            <div class="form__row">
              <div class="field">
                <label for="email">Email address</label>
                <input type="email" id="email" name="email" autocomplete="email" required />
                <span class="field__error" id="err-email"></span>
              </div>
              <div class="field">
                <label for="phone">Phone (optional)</label>
                <input type="tel" id="phone" name="phone" autocomplete="tel" />
                <span class="field__error" id="err-phone"></span>
              </div>
            </div>

            <div class="field">
              <label for="service">Which service interests you?</label>
              <select id="service" name="service" required>
                <option value="">Choose a service...</option>
                <option>Educational Consulting</option>
                <option>Financial Advisory</option>
                <option>Business Consulting</option>
                <option>SME Growth &amp; Strategy</option>
                <option>Training &amp; Workshops</option>
                <option>Organisational Advisory</option>
                <option>Not sure yet</option>
              </select>
              <span class="field__error" id="err-service"></span>
            </div>

            <div class="field">
              <label for="message">How can we help?</label>
              <textarea id="message" name="message" placeholder="Briefly describe your goal or question..." required></textarea>
              <span class="field__error" id="err-message"></span>
            </div>

            <button type="submit" class="btn btn--primary"><i class="fa-solid fa-paper-plane" aria-hidden="true"></i> Send message</button>
            <div class="form__notice" id="formNotice" role="status">Thanks! Your message has been received. We&rsquo;ll be in touch within one working day.</div>
          </form>
        </div>
      </div>
    </section>
  </main>

  <!-- ===================== FOOTER ===================== -->
  <footer class="footer" role="contentinfo">
    <div class="container">
      <div class="footer__grid">
        <div>
          <div class="footer__brand">
            <img src="__LOGO__" alt="EDU-FIN PROCONSULT SERVICES" class="footer__logo" width="50" height="50" />
            <span class="footer__brand-text">EDU-FIN PROCONSULT
              <small>Services</small>
            </span>
          </div>
          <p>Educational, financial, and business consulting for students, entrepreneurs, and organisations across Nigeria and the wider African continent.</p>
          <div class="footer__socials" aria-label="Social profiles">
            <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in" aria-hidden="true"></i></a>
            <a href="#" aria-label="X / Twitter"><i class="fa-brands fa-x-twitter" aria-hidden="true"></i></a>
            <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram" aria-hidden="true"></i></a>
            <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f" aria-hidden="true"></i></a>
            <a href="#" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp" aria-hidden="true"></i></a>
          </div>
        </div>

        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="#about">About us</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#why">Why choose us</a></li>
            <li><a href="#testimonials">Testimonials</a></li>
            <li><a href="#blog">Insights</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div>

        <div>
          <h4>Services</h4>
          <ul>
            <li><a href="#services">Educational consulting</a></li>
            <li><a href="#services">Financial advisory</a></li>
            <li><a href="#services">Business consulting</a></li>
            <li><a href="#services">SME growth &amp; strategy</a></li>
            <li><a href="#services">Training &amp; workshops</a></li>
            <li><a href="#services">Organisational advisory</a></li>
          </ul>
        </div>

        <div>
          <h4>Stay in the loop</h4>
          <p>Get monthly insights on education opportunities, money tips, and SME growth.</p>
          <form class="footer__newsletter" id="newsletter" novalidate>
            <label for="newsletter-email" class="sr-only" style="position:absolute;left:-9999px;">Email address</label>
            <input type="email" id="newsletter-email" placeholder="Your email address" required />
            <button type="submit" aria-label="Subscribe">Join</button>
          </form>
          <p style="margin-top: .75rem; font-size: .82rem; color: rgba(255,255,255,0.6);">We respect your inbox. No spam, unsubscribe anytime.</p>
        </div>
      </div>

      <div class="footer__bottom">
        <span>&copy; <span id="year"></span> EDU-FIN PROCONSULT SERVICES. All rights reserved.</span>
        <span><a href="#">Privacy policy</a> &middot; <a href="#">Terms of service</a> &middot; <a href="#">Cookie preferences</a></span>
      </div>
    </div>
  </footer>

  <script>
    (function () {
      'use strict';

      // ----- Footer year -----
      var yearEl = document.getElementById('year');
      if (yearEl) yearEl.textContent = new Date().getFullYear();

      // ----- Sticky nav state -----
      var nav = document.getElementById('nav');
      var setNavState = function () {
        if (window.scrollY > 24) nav.classList.add('is-scrolled');
        else nav.classList.remove('is-scrolled');
      };
      setNavState();
      window.addEventListener('scroll', setNavState, { passive: true });

      // ----- Hamburger menu -----
      var toggle = document.getElementById('navToggle');
      var menu = document.getElementById('navMenu');
      var closeMenu = function () {
        menu.classList.remove('is-open');
        toggle.classList.remove('is-active');
        toggle.setAttribute('aria-expanded', 'false');
      };
      toggle.addEventListener('click', function () {
        var open = menu.classList.toggle('is-open');
        toggle.classList.toggle('is-active', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      menu.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', closeMenu);
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeMenu();
      });

      // ----- Intersection Observer reveal -----
      var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var revealEls = document.querySelectorAll('.reveal');
      if (prefersReduced || !('IntersectionObserver' in window)) {
        revealEls.forEach(function (el) { el.classList.add('is-visible'); });
      } else {
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible');
              io.unobserve(entry.target);
            }
          });
        }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
        revealEls.forEach(function (el) { io.observe(el); });
      }

      // ----- Counter animation -----
      var counters = document.querySelectorAll('[data-count]');
      var animateCounter = function (el) {
        var target = parseInt(el.getAttribute('data-count'), 10) || 0;
        var suffix = el.getAttribute('data-suffix') || '';
        var duration = 1800;
        var start = performance.now();
        var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
        var step = function (now) {
          var t = Math.min(1, (now - start) / duration);
          var val = Math.round(target * ease(t));
          el.textContent = val.toLocaleString() + suffix;
          if (t < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      };
      if (prefersReduced || !('IntersectionObserver' in window)) {
        counters.forEach(function (c) {
          c.textContent = (parseInt(c.getAttribute('data-count'),10) || 0).toLocaleString() + (c.getAttribute('data-suffix') || '');
        });
      } else {
        var cio = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              animateCounter(entry.target);
              cio.unobserve(entry.target);
            }
          });
        }, { threshold: 0.5 });
        counters.forEach(function (c) { cio.observe(c); });
      }

      // ----- Testimonial carousel -----
      var track = document.getElementById('testTrack');
      var prevBtn = document.getElementById('testPrev');
      var nextBtn = document.getElementById('testNext');
      var dotsWrap = document.getElementById('testDots');
      var slides = track ? track.children : [];
      var index = 0;
      var autoTimer = null;
      var goTo = function (i) {
        index = (i + slides.length) % slides.length;
        track.style.transform = 'translateX(' + (-index * 100) + '%)';
        Array.prototype.forEach.call(dotsWrap.children, function (d, n) {
          d.classList.toggle('is-active', n === index);
          d.setAttribute('aria-selected', n === index ? 'true' : 'false');
        });
      };
      var startAuto = function () {
        if (prefersReduced) return;
        stopAuto();
        autoTimer = setInterval(function () { goTo(index + 1); }, 6000);
      };
      var stopAuto = function () { if (autoTimer) { clearInterval(autoTimer); autoTimer = null; } };
      if (track && slides.length) {
        for (var i = 0; i < slides.length; i++) {
          (function (idx) {
            var dot = document.createElement('button');
            dot.className = 'testimonials__dot';
            dot.type = 'button';
            dot.setAttribute('role', 'tab');
            dot.setAttribute('aria-label', 'Show testimonial ' + (idx + 1));
            dot.addEventListener('click', function () { goTo(idx); startAuto(); });
            dotsWrap.appendChild(dot);
          })(i);
        }
        goTo(0);
        prevBtn.addEventListener('click', function () { goTo(index - 1); startAuto(); });
        nextBtn.addEventListener('click', function () { goTo(index + 1); startAuto(); });
        startAuto();
        // Pause on hover/focus
        var pauseEls = [track, prevBtn, nextBtn, dotsWrap];
        pauseEls.forEach(function (el) {
          el.addEventListener('mouseenter', stopAuto);
          el.addEventListener('mouseleave', startAuto);
          el.addEventListener('focusin', stopAuto);
          el.addEventListener('focusout', startAuto);
        });
        // Touch swipe
        var touchStart = null;
        track.addEventListener('touchstart', function (e) { touchStart = e.touches[0].clientX; stopAuto(); }, { passive: true });
        track.addEventListener('touchend', function (e) {
          if (touchStart === null) return;
          var dx = e.changedTouches[0].clientX - touchStart;
          if (Math.abs(dx) > 40) goTo(index + (dx < 0 ? 1 : -1));
          touchStart = null;
          startAuto();
        });
      }

      // ----- Contact form validation -----
      var form = document.getElementById('contactForm');
      var notice = document.getElementById('formNotice');
      var setError = function (id, msg) {
        var input = document.getElementById(id);
        var err = document.getElementById('err-' + id);
        if (input && err) {
          err.textContent = msg || '';
          input.closest('.field').classList.toggle('field--error', !!msg);
        }
      };
      var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (form) {
        form.addEventListener('submit', function (e) {
          e.preventDefault();
          var ok = true;
          var get = function (id) { return (document.getElementById(id).value || '').trim(); };
          if (!get('firstName')) { setError('firstName', 'Please enter your first name.'); ok = false; } else setError('firstName', '');
          if (!get('lastName'))  { setError('lastName',  'Please enter your last name.');  ok = false; } else setError('lastName', '');
          if (!emailRe.test(get('email'))) { setError('email', 'Please enter a valid email.'); ok = false; } else setError('email', '');
          if (!get('service'))   { setError('service',   'Please choose a service.');        ok = false; } else setError('service', '');
          if (get('message').length < 10) { setError('message', 'Please share a few more details (10+ characters).'); ok = false; } else setError('message', '');
          if (ok) {
            notice.classList.add('is-visible');
            form.reset();
            setTimeout(function () { notice.classList.remove('is-visible'); }, 6000);
          }
        });
      }

      // ----- Newsletter -----
      var news = document.getElementById('newsletter');
      if (news) {
        news.addEventListener('submit', function (e) {
          e.preventDefault();
          var input = document.getElementById('newsletter-email');
          if (emailRe.test((input.value || '').trim())) {
            input.value = '';
            input.setAttribute('placeholder', 'Thanks — you\u2019re subscribed!');
            input.style.borderColor = 'var(--c-gold)';
            setTimeout(function () {
              input.setAttribute('placeholder', 'Your email address');
              input.style.borderColor = '';
            }, 4000);
          } else {
            input.style.borderColor = '#C0392B';
            input.focus();
          }
        });
      }
    })();
  </script>
</body>
</html>
"""

OUT = HTML.replace("__LOGO__", LOGO_DATA_URI)
(ROOT / "index.html").write_text(OUT)
print(f"Wrote index.html — {len(OUT):,} bytes")

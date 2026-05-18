---
layout: null
---

<style>
:root {
  --bg: #050505;
  --bg-soft: #0b0b10;
  --paper: #f4f3ef;
  --paper-2: #ece9e3;
  --ink: #f5f5f5;
  --ink-dark: #1f1f1f;
  --muted: rgba(245, 245, 245, 0.68);
  --muted-dark: rgba(31, 31, 31, 0.68);
  --line: rgba(255, 255, 255, 0.1);
  --line-dark: rgba(31, 31, 31, 0.1);
  --accent-a: #ff4f75;
  --accent-b: #9b5cff;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans KR", "Apple SD Gothic Neo", sans-serif;
  line-height: 1.65;
  overflow-x: hidden;
}

* {
  box-sizing: border-box;
}

a {
  color: inherit;
  text-decoration: none;
}

img {
  display: block;
  max-width: 100%;
}

.page-shell {
  width: min(1440px, calc(100% - 40px));
  margin: 0 auto;
}

.site-nav {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(5, 5, 5, 0.76);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 18px 0;
}

.brand {
  font-weight: 800;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-size: 0.82rem;
}

.nav-links {
  display: flex;
  flex-wrap: wrap;
  gap: 22px;
  justify-content: flex-end;
  color: var(--muted);
  font-size: 0.95rem;
}

.nav-links a:hover {
  color: var(--ink);
}

.hero {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  display: flex;
  align-items: center;
  background:
    radial-gradient(circle at 18% 18%, rgba(255, 79, 117, 0.15), transparent 28%),
    radial-gradient(circle at 82% 18%, rgba(155, 92, 255, 0.18), transparent 30%),
    url("./image/go2_whole.png"),
    linear-gradient(180deg, #101014 0%, #050505 100%);
  background-repeat: no-repeat, no-repeat, no-repeat, no-repeat;
  background-position: left top, right top, right bottom, center;
  background-size: auto, auto, min(58vw, 900px), cover;
}

.hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(180deg, rgba(5, 5, 5, 0.18), rgba(5, 5, 5, 0.72)),
    linear-gradient(90deg, rgba(5, 5, 5, 0.18), rgba(5, 5, 5, 0.12) 35%, rgba(5, 5, 5, 0.42) 100%);
  z-index: 1;
}

.hero-inner {
  position: relative;
  z-index: 2;
  width: 100%;
  padding: 110px 0 120px;
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0;
  align-items: start;
  max-width: none;
  width: 100%;
  padding-inline: clamp(16px, 4vw, 64px);
}

.kicker {
  margin: 0 0 18px;
  text-transform: uppercase;
  letter-spacing: 0.22em;
  font-size: 0.82rem;
  color: rgba(245, 245, 245, 0.72);
}

.hero h1 {
  margin: 0;
  max-width: none;
  font-size: clamp(2.35rem, 4.8vw, 5.2rem);
  line-height: 0.94;
  letter-spacing: -0.05em;
  background: linear-gradient(90deg, var(--accent-a), var(--accent-b));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hero-lead {
  margin: 26px 0 0;
  max-width: 88ch;
  color: rgba(245, 245, 245, 0.82);
  font-size: 1rem;
}

.hero-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 28px;
}

.pill {
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 999px;
  padding: 8px 12px;
  background: rgba(255, 255, 255, 0.04);
  color: rgba(245, 245, 245, 0.92);
  font-size: 0.92rem;
}

.hero-cta {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 30px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 18px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease;
}

.btn.primary {
  background: linear-gradient(90deg, var(--accent-a), var(--accent-b));
  color: #fff;
  border-color: transparent;
}

.btn:hover {
  transform: translateY(-1px);
  border-color: rgba(255, 255, 255, 0.3);
}

.section {
  padding: 92px 0;
}

.section.light {
  background: var(--bg);
  color: var(--ink);
}

.section.dark {
  background: var(--bg);
  color: var(--ink);
}

main > section {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.section-head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 30px;
}

.section-head h2 {
  margin: 0;
  font-size: clamp(2rem, 4vw, 3.6rem);
  line-height: 1;
  letter-spacing: -0.04em;
}

.section-head p {
  margin: 0;
  max-width: 56ch;
  color: var(--muted);
}

.light .section-head p {
  color: var(--muted);
}

.split {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 34px;
  align-items: center;
}

.card-shell {
  border: 1px solid var(--line-dark);
  background: rgba(255, 255, 255, 0.72);
  overflow: hidden;
}

.dark .card-shell {
  border-color: var(--line);
  background: rgba(255, 255, 255, 0.03);
}

.light .card-shell {
  border-color: var(--line);
  background: rgba(255, 255, 255, 0.03);
}

.media {
  position: relative;
  min-height: 420px;
}

.media.tall {
  min-height: 520px;
}

.media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center center;
}

.copy h3 {
  margin: 0 0 14px;
  font-size: clamp(1.5rem, 2.5vw, 2.4rem);
  letter-spacing: -0.03em;
}

.copy p {
  margin: 0 0 16px;
  color: rgba(245, 245, 245, 0.78);
}

.light .copy p {
  color: rgba(245, 245, 245, 0.78);
}

.copy p:last-child {
  margin-bottom: 0;
}

.feature-grid,
.hardware-grid,
.timeline-grid,
.stack-grid,
.contact-grid,
.refs-grid {
  display: grid;
  gap: 18px;
}

.feature-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
  margin-top: 28px;
}

.mini-card {
  border: 1px solid rgba(31, 31, 31, 0.09);
  background: rgba(255, 255, 255, 0.78);
  padding: 18px 18px 20px;
  min-height: 180px;
}

.dark .mini-card {
  border-color: rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.04);
}

.light .mini-card {
  border-color: rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.04);
}

.mini-card h4 {
  margin: 0 0 10px;
  font-size: 1.05rem;
}

.mini-card p {
  margin: 0;
  color: inherit;
  opacity: 0.78;
  font-size: 0.95rem;
}

.hardware-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.hardware-card {
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.04);
  overflow: hidden;
  transition: transform 0.18s ease, border-color 0.18s ease;
  color: var(--ink);
}

.hardware-card:hover {
  transform: translateY(-2px);
  border-color: rgba(255, 79, 117, 0.4);
}

.hardware-card figure {
  margin: 0;
  height: 240px;
  background: #0f0f13;
}

.hardware-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center center;
}

.hardware-card .body {
  padding: 18px;
}

.hardware-card .body h3 {
  margin: 0 0 8px;
  font-size: 1.1rem;
}

.hardware-card .body p {
  margin: 0;
  color: rgba(245, 245, 245, 0.72);
  font-size: 0.94rem;
}

.arch-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
  gap: 30px;
  align-items: stretch;
}

.placeholder-arch {
  min-height: 520px;
  background: var(--bg);
}

.dark .placeholder-arch {
  background: var(--bg);
}

.placeholder-arch img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.arch-list {
  margin: 18px 0 0;
  padding-left: 18px;
  display: grid;
  gap: 10px;
  color: inherit;
  opacity: 0.9;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 16px;
}

.team-card {
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.04);
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-height: 260px;
}

.light .team-card {
  border-color: rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.04);
}

.avatar {
  width: 100%;
  aspect-ratio: 1 / 1;
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  overflow: hidden;
  background: #0f0f13;
}

.light .avatar {
  border-color: rgba(255, 255, 255, 0.12);
}

.avatar img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center center;
}

.team-card h3 {
  margin: 0;
  font-size: 1.02rem;
}

.team-card .role {
  margin: 0;
  color: inherit;
  opacity: 0.65;
  font-size: 0.92rem;
  min-height: 1.4em;
}

.team-card .gh {
  margin-top: auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  align-self: flex-start;
  min-height: 38px;
  padding: 0 14px 0 12px;
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.04);
  font-size: 0.88rem;
  font-weight: 600;
  color: inherit;
  opacity: 0.92;
  gap: 8px;
  transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease;
}

.team-card .gh svg {
  width: 15px;
  height: 15px;
  flex: 0 0 auto;
  fill: currentColor;
}

.light .team-card .gh {
  border-color: rgba(255, 255, 255, 0.14);
  background: rgba(255, 255, 255, 0.04);
}

.team-card .gh:hover {
  transform: translateY(-1px);
  border-color: rgba(255, 79, 117, 0.45);
  background: linear-gradient(90deg, rgba(255, 79, 117, 0.12), rgba(155, 92, 255, 0.12));
}

.team-card .gh:focus-visible {
  outline: 2px solid rgba(155, 92, 255, 0.7);
  outline-offset: 2px;
}

.timeline-section {
  background: var(--bg);
  color: var(--ink);
}

.timeline-shell {
  padding-top: 8px;
}

.timeline-head {
  display: grid;
  justify-items: center;
  text-align: center;
  gap: 10px;
  margin-bottom: 44px;
}

.timeline-kicker {
  margin: 0;
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: rgba(155, 92, 255, 0.86);
}

.timeline-head h2 {
  margin: 0;
  font-size: clamp(2.2rem, 3.8vw, 3.8rem);
  line-height: 0.98;
  letter-spacing: -0.045em;
  color: var(--ink);
  font-weight: 800;
}

.timeline-head p {
  margin: 0;
  max-width: 60ch;
  color: var(--muted);
}

.timeline-stage {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 100px minmax(0, 1fr);
  grid-template-rows: repeat(3, auto);
  row-gap: 88px;
  padding: 12px 0 42px;
}

.timeline-axis {
  position: absolute;
  top: 0;
  bottom: 22px;
  left: 50%;
  width: 2px;
  transform: translateX(-50%);
  background: linear-gradient(180deg, rgba(255, 91, 138, 0.14), rgba(255, 91, 138, 0.82), rgba(155, 92, 255, 0.82), rgba(155, 92, 255, 0.14));
}

.timeline-node {
  position: relative;
  z-index: 2;
  justify-self: center;
  width: 12px;
  height: 12px;
  margin-top: 16px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent-a), var(--accent-b));
  box-shadow: 0 0 0 4px rgba(255, 91, 138, 0.07), 0 0 12px rgba(155, 92, 255, 0.14);
}

.timeline-node-1 {
  grid-column: 2;
  grid-row: 1;
}

.timeline-node-2 {
  grid-column: 2;
  grid-row: 2;
}

.timeline-node-3 {
  grid-column: 2;
  grid-row: 3;
}

.timeline-entry {
  position: relative;
  max-width: 440px;
  padding: 0;
  border: 0;
  background: transparent;
  box-shadow: none;
}

.timeline-entry-1,
.timeline-entry-3 {
  justify-self: end;
  text-align: left;
  padding-right: 30px;
}

.timeline-entry-2 {
  justify-self: start;
  text-align: left;
  padding-left: 30px;
}

.timeline-entry-1 {
  grid-column: 1;
  grid-row: 1;
}

.timeline-entry-2 {
  grid-column: 3;
  grid-row: 2;
}

.timeline-entry-3 {
  grid-column: 1;
  grid-row: 3;
}

.timeline-entry::after {
  content: "";
  position: absolute;
  top: 22px;
  height: 1px;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0), rgba(255, 91, 138, 0.8), rgba(155, 92, 255, 0.8));
}

.timeline-entry-1::after,
.timeline-entry-3::after {
  right: -20px;
  width: 44px;
}

.timeline-entry-2::after {
  left: -20px;
  width: 44px;
  background: linear-gradient(90deg, rgba(255, 91, 138, 0.8), rgba(155, 92, 255, 0.8), rgba(255, 255, 255, 0));
}

.timeline-entry-inner {
  display: grid;
  gap: 12px;
}

.timeline-entry h3 {
  margin: 0;
  display: inline-grid;
  gap: 10px;
  font-size: 1.18rem;
  font-weight: 800;
  letter-spacing: -0.035em;
  color: var(--ink);
}

.timeline-title-row {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.timeline-title-row svg {
  width: 13px;
  height: 13px;
  fill: currentColor;
  opacity: 0.85;
  flex: 0 0 auto;
}

.timeline-entry h3::after {
  content: "";
  width: 100%;
  height: 1px;
  border-radius: 999px;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.14), rgba(255, 91, 138, 0.58), rgba(155, 92, 255, 0.58));
}

.timeline-entry-3 h3 {
  color: var(--accent-b);
}

.timeline-entry-3 h3::after {
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.12), rgba(255, 91, 138, 0.52), rgba(155, 92, 255, 0.72));
}

.timeline-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 9px;
  color: rgba(245, 245, 245, 0.84);
}

.timeline-list li {
  position: relative;
  padding-left: 16px;
  line-height: 1.55;
}

.timeline-list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.78em;
  width: 5px;
  height: 5px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent-a), var(--accent-b));
  transform: translateY(-50%);
}

.timeline-entry-3 .timeline-list li::before {
  background: linear-gradient(90deg, var(--accent-b), var(--accent-a));
}

.timeline-arrow {
  position: absolute;
  left: 50%;
  bottom: 0;
  width: 14px;
  height: 14px;
  border-right: 2px solid rgba(255, 255, 255, 0.25);
  border-bottom: 2px solid rgba(255, 255, 255, 0.25);
  transform: translateX(-50%) rotate(45deg);
}

@media (max-width: 900px) {
  .timeline-head {
    justify-items: start;
    text-align: left;
  }

  .timeline-stage {
    grid-template-columns: 26px 1fr;
    grid-template-rows: auto auto auto;
    row-gap: 34px;
    padding-left: 0;
  }

  .timeline-axis {
    left: 12px;
    transform: none;
  }

  .timeline-node {
    justify-self: start;
    margin-top: 14px;
  }

  .timeline-node-1 {
    grid-column: 1;
    grid-row: 1;
  }

  .timeline-node-2 {
    grid-column: 1;
    grid-row: 2;
  }

  .timeline-node-3 {
    grid-column: 1;
    grid-row: 3;
  }

  .timeline-entry,
  .timeline-entry-1,
  .timeline-entry-2,
  .timeline-entry-3 {
    grid-column: 2;
    justify-self: stretch;
    max-width: none;
    padding-left: 18px;
    padding-right: 0;
  }

  .timeline-entry-1,
  .timeline-entry-3 {
    text-align: left;
  }

  .timeline-entry::after {
    left: -18px;
    right: auto;
    width: 26px;
  }

  .timeline-arrow {
    left: 12px;
  }
}.stack-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.stack-list {
  margin: 12px 0 0;
  padding-left: 18px;
  display: grid;
  gap: 8px;
  color: inherit;
  opacity: 0.86;
}

.contact-grid {
  grid-template-columns: 1.15fr 0.85fr 0.85fr;
}

.refs-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.ref-card a {
  color: inherit;
  text-decoration: underline;
  text-decoration-color: rgba(255, 79, 117, 0.55);
  text-underline-offset: 3px;
}

.impact-grid {
  display: grid;
  gap: 18px;
}

.impact-card h3 {
  margin-bottom: 12px;
}

.footer {
  padding: 30px 0 46px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  background: var(--bg);
  color: var(--ink);
}

.footer-inner {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
  align-items: center;
  color: rgba(245, 245, 245, 0.68);
}

.footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.footer-links a {
  color: inherit;
}

@media (max-width: 1200px) {
  .feature-grid,
  .hardware-grid,
  .timeline-grid,
  .contact-grid,
  .refs-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .team-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (max-width: 860px) {
  .nav-inner,
  .section-head,
  .split,
  .arch-grid {
    grid-template-columns: 1fr;
    display: grid;
  }

  .nav-inner {
    gap: 12px;
  }

  .nav-links {
    justify-content: flex-start;
    gap: 16px;
  }

  .hero-grid {
    grid-template-columns: 1fr;
    align-items: start;
  }

  .hero {
    min-height: auto;
  }

  .hero-inner {
    padding: 72px 0 78px;
  }

  .hero-robot {
    display: none;
  }

  .section {
    padding: 72px 0;
  }

  .feature-grid,
  .hardware-grid,
  .timeline-grid,
  .stack-grid,
  .contact-grid,
  .refs-grid {
    grid-template-columns: 1fr;
  }

  .timeline-grid {
    padding-left: 26px;
    padding-right: 0;
    grid-template-columns: 1fr;
    grid-template-rows: none;
    gap: 28px;
  }

  .timeline-grid::before {
    left: 14px;
    transform: none;
  }

  .timeline-card,
  .timeline-card:nth-child(odd),
  .timeline-card:nth-child(even) {
    grid-column: auto;
    grid-row: auto;
    justify-self: stretch;
    text-align: left;
    max-width: none;
  }

  .timeline-card::before,
  .timeline-card:nth-child(odd)::before,
  .timeline-card:nth-child(even)::before {
    left: -23px;
    right: auto;
  }

  .timeline-card::after,
  .timeline-card:nth-child(odd)::after,
  .timeline-card:nth-child(even)::after {
    left: -21px;
    right: auto;
    width: 24px;
  }

  .timeline-card:nth-child(odd) .timeline-list {
    padding-right: 0;
    padding-left: 18px;
    list-style-position: outside;
  }

  .timeline-card:nth-child(odd) .timeline-list li {
    text-align: left;
  }

  .team-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 560px) {
  .page-shell {
    width: min(100% - 28px, 1440px);
  }

  .team-grid {
    grid-template-columns: 1fr;
  }

  .hero h1 {
    max-width: none;
    font-size: clamp(2.2rem, 10vw, 3.8rem);
  }

  .hero-lead {
    font-size: 1rem;
  }

  .pill {
    font-size: 0.86rem;
  }

  .media,
  .media.tall {
    min-height: 300px;
  }

  .placeholder-arch {
    min-height: 360px;
  }
}
</style>

<nav class="site-nav" id="home">
  <div class="page-shell nav-inner">
    <a class="brand" href="#home">CAPSTONE 41</a>
    <div class="nav-links">
      <a href="#home">Home</a>
      <a href="#overview">Overview</a>
      <a href="#demo">Demo</a>
      <a href="#architecture">Architecture</a>
      <a href="#hardware">Hardware</a>
      <a href="#team">Team</a>
      <a href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub</a>
    </div>
  </div>
</nav>

<header class="hero">
  <div class="hero-inner">
    <div class="page-shell hero-grid">
      <div>
        <p class="kicker">Vision-Language-Action 夷?Robotics Capstone Project</p>
        <h1>VLA 疫꿸퀡而?????嚥≪뮆?????? ?癒?몛 ??뽯뮞??/h1>
        <p class="hero-lead">
          癰??袁⑥쨮??븍뱜??<strong>Unitree Go2</strong> ????癰귣똾六?嚥≪뮆???筌ㅼ뮇??Vision-Language-Action(VLA) 筌뤴뫀???<strong>InternVLA-N1-DualVLN</strong>????곷뻼??뤿연, ?????筌띾?釉???癒?염??筌뤿굝議?"??륁쁽嚥?揶쎛", "?? ??????怨뺤뵬揶쎛")筌띾슣?앮에?嚥≪뮆?????볦퍟 ?類ｋ궖????곴퐤??랁???쇱젫 ??띻펾???癒?몛 雅뚯눛六??롫즲嚥??닌뗭겱???袁⑥쨮??븍뱜??
        </p>
        <p class="hero-lead">
          疫꿸퀣??VLA 筌뤴뫀???? ??筌ｋ?以?????紐꾩뵠??볧닋 ??뽰젎??援??⑥쥚萸뱄쭪?燁삳?李????띻펾???袁⑹젫嚥?筌띾슢諭??곸죬 ??됰선, ?臾? ????嚥≪뮆?몌㎗?롮쓥 癰귣챷猿쒎첎? ??삘뀲 ??띻펾??域밸챶?嚥???由곤쭖??源낅뮟????λ선筌욊쑬?? ?怨뺚봺 ???? ?????<strong>嚥≪뮆??癰귣챷猿쒑퉪???띻펾 筌△뫁??/strong>??癰귣똻???띾┛ ?袁る퉸 LOVON????? ?닌듼쒐몴?InternVLA??野껉퀬鍮??랁? ROSA ?癒?뵠?袁る뱜嚥?筌뤿굝議???브쑵鍮??롫뮉 ????뽯뮞????덇볼??揶쏆뮇苑???酉六??
        </p>
        <div class="hero-meta">
          <span class="pill">Unitree Go2</span>
          <span class="pill">InternVLA-N1-DualVLN</span>
          <span class="pill">ROSA Agent</span>
          <span class="pill">LiDAR SLAM</span>
        </div>
        <div class="hero-cta">
          <a class="btn primary" href="#overview">Explore Overview</a>
          <a class="btn" href="#architecture">View Architecture</a>
        </div>
      </div>
    </div>
  </div>
</header>

<main>
<section class="section dark" id="impact">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Project Significance</h2>
        </div>
      </div>
      <div class="impact-grid">
        <article class="impact-card">
          <h3>1. ??곗굨 ????嚥≪뮆????띻펾??????VLA Foundation Model???怨몄벓</h3>
          <p>??域뱀뮆???????됱뵠???怨쀬뵠?怨뺤쨮 ??덈뮸??筌ㅼ뮇??VLA Foundation Model?? ??곗뺘?怨몄몵嚥?????紐꾩뵠??볧닋 ??뽰젎??援??⑥쥚萸뱄쭪?RGB-D ??띻펾??揶쎛?類λ릭疫?????? ??뽰젎 ?誘れ뵠揶쎛 ????燁삳?李????堉????쀫립????곗굨 ????嚥≪뮆???域밸챶?嚥?獄쏄퀬猷??롢늺 ?源낅뮟??????롫┷??癰귣챷彛????볧롧몴?筌왖???뼄. 癰??袁⑥쨮??븍뱜??LOVON?????뼎 筌뤴뫀諭??InternVLA-N1-DualVLN ??????醫뤾문?怨몄몵嚥???????μ몵嚥≪뮇?? <strong>Foundation Model?????럮嚥???釉???릭筌왖 ??꾪????곗굨 ????嚥≪뮆??癰귣챷猿???怨몄벓(domain adaptation)??쀪텕????쇱뒠??野껋럥以?/strong>????뽯뻻??덈뼄. ????筌ㅼ뮇????域뱀뮆??VLA 筌뤴뫀???????쑴??嚥≪뮆?????삸??깅퓠 ??곷뻼??롮젻???袁⑸꺗 ?怨뚮럡夷뚦첎?뺤뻣??筌욊낯????뽰뒠 揶쎛?館釉?獄쎻뫖苡욘에醫롮읅 疫꿸퀣肉ф에??????뺣뼄.</p>
        </article>
        <article class="impact-card">
          <h3>2. ??μ뵬 task ??뽯염????뤿선??筌렺?怨좉묶??쎄쾿 ???? ???뵠?袁⑥뵬??/h3>
          <p>??쎈탞???뮞 InternVLA???⑤벀而???뽯염????μ뵬 navigation task???믩챶窺????덈뮉 野껉퍒?????? 癰???뽯뮞??? <strong>Navigation, Pointing, Following, Backtracking 4??task??ROSA 疫꿸퀡而?LLM ?癒?뵠?袁る뱜 ?袁⑸퓠 ??μ뵬 ???뵠?袁⑥뵬?紐꾩몵嚥?????</strong>??덈뼄. ?諭곸뿳 LiDAR SLAM closed-loop 疫꿸퀡而??癒?몛 獄쏄퉲???묎때?? InternVLA揶쎛 癰귣챶????삼펷筌왖 ??낅뮉 疫꿸퀡?????뽯뮞????덇볼?癒?퐣 ?類ㅼ삢?????嚥? foundation model???臾믪뒠 task嚥??類ㅼ삢??롫뮉 ?닌딄퍥????블???됰뻻????볥궗??뺣뼄.</p>
        </article>
        <article class="impact-card">
          <h3>3. ?癒?염??疫꿸퀡而??癒?봄 嚥≪뮆????곸뒠 ?紐낃숲??륁뵠??/h3>
          <p>?癒?퍥 揶쏆뮆而??<strong>Go2 Monitor ???紐낃숲??륁뵠??/strong>?? <strong>Zenoh-bridge 疫꿸퀡而??얜똻苑?ROS2 ???뻿 ??쎄문</strong>??野껉퀬鍮??μ몵嚥≪뮇?? <strong>?紐낃숲???怨뚭퍙筌???됱몵筌??癒?봄筌왖?癒?퐣??嚥≪뮆?????쇰뻻揶?燁삳?李????곕굡???類ㅼ뵥??랁??癒?염??筌뤿굝議???袁⑸꽊夷??쎈뻬</strong>??쀪텢 ????덈뮉 ?닌듼쒐몴??袁⑷쉐??덈뼄. ????????嚥≪뮆?????뽰뒠 甕곕뗄?욅몴??怨뚮럡???怨뺛걟????뤿선 <strong>?????筌욊낯???臾롫젏????쀫립??롫뮉 ?癒?봄筌왖夷?袁る퓮 ??띻펾夷뚩눧?곸뵥 ??뽮퐬</strong> ????쇱젫 ??곸뒠 ??뺢돌?귐딆궎嚥??類ㅼ삢??????덈뮉 疫꿸퀡而????볥궗??렽? ??쑴?얕눧硫????癒?염??彛??곗쨮 嚥≪뮆?????곸뒠??????덈뼄???癒?퓠??HRI(Human-Robot Interaction) 筌γ볝늺??筌욊쑴???貫瑗????苡?????疫꿸퀣肉ф에??????뺣뼄.</p>
        </article>
      </div>
    </div>
  </section>

<section class="section light" id="overview">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Overview</h2>
        </div>
      </div>
      <div class="split">
        <figure class="card-shell media tall">
          <img src="./image/go2_front.png" alt="Unitree Go2 front view">
        </figure>
        <div class="copy">
          <h3>?癒?염??筌뤿굝議??곗쨮 ??筌욊낯???VLA 疫꿸퀡而?????嚥≪뮆??/h3>
          <p>癰??袁⑥쨮??븍뱜??<strong>Unitree Go2</strong> ????癰귣똾六?嚥≪뮆???筌ㅼ뮇??Vision-Language-Action(VLA) 筌뤴뫀???<strong>InternVLA-N1-DualVLN</strong>????곷뻼??뤿연, ?????筌띾?釉???癒?염??筌뤿굝議?"??륁쁽嚥?揶쎛", "?? ??????怨뺤뵬揶쎛")筌띾슣?앮에?嚥≪뮆?????볦퍟 ?類ｋ궖????곴퐤??랁???쇱젫 ??띻펾???癒?몛 雅뚯눛六??롫즲嚥??닌뗭겱???袁⑥쨮??븍뱜??</p>
          <p>疫꿸퀣??VLA 筌뤴뫀???? ??筌ｋ?以?????紐꾩뵠??볧닋 ??뽰젎??援??⑥쥚萸뱄쭪?燁삳?李????띻펾???袁⑹젫嚥?筌띾슢諭??곸죬 ??됰선, ?臾? ????嚥≪뮆?몌㎗?롮쓥 癰귣챷猿쒎첎? ??삘뀲 ??띻펾??域밸챶?嚥???由곤쭖??源낅뮟????λ선筌욊쑬?? ?怨뺚봺 ???? ?????<strong>嚥≪뮆??癰귣챷猿쒑퉪???띻펾 筌△뫁??/strong>??癰귣똻???띾┛ ?袁る퉸 LOVON????? ?닌듼쒐몴?InternVLA??野껉퀬鍮??랁? ROSA ?癒?뵠?袁る뱜嚥?筌뤿굝議???브쑵鍮??롫뮉 ????뽯뮞????덇볼??揶쏆뮇苑???酉六??</p>
          <div class="hero-cta" style="margin-top:24px;">
            <a class="btn" href="#hardware">Hardware</a>
            <a class="btn" href="#demo">Demo</a>
            <a class="btn" href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub</a>
          </div>
        </div>
      </div>

      <div class="feature-grid" aria-label="4揶쎛筌왖 ???뼎 疫꿸퀡??>
        <article class="mini-card">
          <h4>Navigation</h4>
          <p>?癒?염??筌뤿굝議??獄쏆룇釉???띻펾 ??筌뤴뫚紐?筌왖?癒?돱筌왖 ?癒?몛 雅뚯눛六??뺣뼄. InternVLA-N1-DualVLN??燁삳?李?????筌왖?? 筌뤿굝議????덈뻻????곴퐤??pixel goal???곗뮆???롢늺, 嚥≪뮆???域밸챷肉?筌띿쉸????猷??뺣뼄.</p>
        </article>
        <article class="mini-card">
          <h4>Pointing</h4>
          <p>???筌왖 ???諭??揶쏆빘猿쒐몴?筌왖??쀫릭筌?嚥≪뮆???????揶쏆빘猿쒏에??館釉?? 揶쏆빘猿?筌왖???類ｋ궖??pixel goal嚥?癰궰??묐퉸 InternVLA???袁⑤뼎??롫뮉 獄쎻뫗?????</p>
        </article>
        <article class="mini-card">
          <h4>Following</h4>
          <p>?????援??얠눘猿쒐몴?筌왖??우읅??곗쨮 ?곕뗄伊??뺣뼄. YOLO 揶쏆빘猿?野꺜??野껉퀗?든몴?pixel goal ??낆젾??곗쨮 ?????렽? LOVON????? ?닌듼쒐몴?筌△뫁???筌뤴뫁???됰뗀??쮯?????곕뗄伊???띻펾?癒?퐣????됱젟?怨몄몵嚥???덉삂??롫즲嚥?揶쏆뮇苑??덈뼄.</p>
        </article>
        <article class="mini-card">
          <h4>Backtracking</h4>
          <p>LiDAR SLAM 疫꿸퀡而?closed-loop ??뽯선嚥??⑥눊援??筌왖??륁궔 野껋럥以덄몴??癒?짗??곗쨮 ??륁??????툡??ㅻ뼄.</p>
        </article>
      </div>
    </div>
  </section>

<section class="section light" id="demo">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Demo</h2>
        </div>
      </div>
      <div class="split">
        <figure class="card-shell media tall">
          <video controls playsinline preload="metadata" poster="./image/go2_front.png">
            <source src="./video/demo.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </figure>
        <div class="copy">
          <h3>Demo Video Placeholder</h3>
          <p>Add the demo video later at <code>./video/demo.mp4</code>.</p>
          <p>This section is ready for a recorded demo, teaser clip, or walkthrough.</p>
        </div>
      </div>
    </div>
  </section>

<section class="section dark" id="architecture">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Architecture</h2>
        </div>
      </div>
      <div class="arch-grid">
        <div class="placeholder-arch">
          <img src="./image/Architecture dark.png" alt="Architecture diagram">
        </div>
        <div class="copy">
          <h3>??뽯뮞???袁り텕??우퓗</h3>
          <ul class="arch-list">
            <li><strong>甕곗쥙???筌뤴뫀????InternVLA-N1-DualVLN</strong>: System1(????? ??뽯선) + System2(?⑥쥙?붶빳? ??뤾텢野껉퀣????dual-system ?닌듼쒐몴?揶쎛筌?VLA foundation model??域밸챶?嚥???뽰뒠??뺣뼄.</li>
            <li><strong>LOVON ?봔??野껉퀬鍮</strong>: LOVON 筌뤴뫀???袁⑷퍥?????럮嚥??????? ??꾪? ??? ?닌듼?? 筌뤴뫀?쏙쭕?筌△뫁???InternVLA ???????깆뜖 ?節뚮선 筌뤴뫁???됰뗀??쮯??????띻펾?癒?퐣???곕뗄伊??源낅뮟??揶쏆뮇苑??덈뼄.</li>
            <li><strong>LiDAR SLAM Runner</strong>: ??쇰뻻揶?SLAM 疫꿸퀡而?closed-loop ??뽯선嚥???됱읈???癒?몛 獄쏄퉲???묎때????볥궗??뺣뼄.</li>
            <li><strong>ROSA Agent + Qwen3.5-4B</strong>: ?癒?염??筌뤿굝議??tool ??μ맄嚥??브쑵鍮??랁? 4??疫꿸퀡????怨뱀넺??筌띿쉳苡??紐꾪뀱??롫뮉 LLM ?癒?뵠?袁る뱜??</li>
            <li><strong>YOLO ??낆젾??/strong>: VLA?????럮嚥???釉???릭筌왖 ??꾪???醫됲뇣 task???곕떽???????덈즲嚥?揶쏆빘猿?野꺜??野껉퀗?든몴?pixel goal ?類κ묶嚥?筌뤴뫀???雅뚯눘???뺣뼄.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>


<section class="section dark" id="stack">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Tech Stack</h2>
        </div>
      </div>
      <div class="section-head" id="hardware">
        <div>
          <h2>Hardware</h2>
        </div>
      </div>
      <div class="hardware-grid">
        <article class="hardware-card">
          <figure>
            <img src="./image/go2_whole.png" alt="Unitree Go2">
          </figure>
          <div class="body">
            <h3>Unitree Go2</h3>
            <p>4議?蹂댄뻾 濡쒕큸, ?댁옣 Jetson Orin / ?댁옣 LiDAR</p>
          </div>
        </article>
        <article class="hardware-card">
          <figure>
            <img src="./image/realsense.png" alt="Intel RealSense D435">
          </figure>
          <div class="body">
            <h3>Intel RealSense D435</h3>
            <p>RGB-D 移대찓??/p>
          </div>
        </article>
        <article class="hardware-card">
          <figure>
            <img src="./image/rtx_3090.png" alt="RTX 3090">
          </figure>
          <div class="body">
            <h3>RTX 3090</h3>
            <p>紐⑤뜽 異붾줎 諛??ㅽ뿕 ?섍꼍</p>
          </div>
        </article>
        <article class="hardware-card">
          <figure>
            <img src="./image/go2_lidar.png" alt="LiDAR on Unitree Go2">
          </figure>
          <div class="body">
            <h3>LiDAR</h3>
            <p>?먯쑉 諛깊듃?섑궧怨??섍꼍 ?몄?瑜??꾪븳 嫄곕━ ?쇱꽌</p>
          </div>
        </article>
      </div>
      <div class="stack-grid">
        <article class="stack-card">
          <h3>??롫굡??λ선</h3>
          <ul class="stack-list">
            <li>Unitree Go2 (4鈺?癰귣똾六?嚥≪뮆?? ??곸삢 Jetson Orin / ??곸삢 LiDAR)</li>
            <li>Intel RealSense D435 (RGB-D 燁삳?李??</li>
            <li>RTX 3090</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>筌뤴뫀?쎌쮯AI</h3>
          <ul class="stack-list">
            <li>InternVLA-N1-DualVLN (筌롫뗄??VLA)</li>
            <li>LOVON (??? ?닌듼?筌△뫁??</li>
            <li>Qwen3.5-4B (vLLM ??뺥뒅, ROSA agent??LLM)</li>
            <li>YOLO (揶쏆빘猿?野꺜??</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>??곕늄?紐꾩띃??/h3>
          <ul class="stack-list">
            <li>Python + PyTorch ??筌롫뗄??揶쏆뮆而??紐꾨선 獄?InternVLA夷똋OVON ?곕뗀以??袁⑥쟿?袁⑹뜖??/li>
            <li>vLLM ??Qwen3.5-4B LLM ??뺥뒅</li>
            <li>OpenCV / NumPy ?????筌왖 筌ｌ꼶?곸쮯?遺얩닜??彛낆쮯SLAM ?袁⑹퓗??猷뱀쪝???怨쀪텦</li>
            <li>ROS 2 ??嚥≪뮆??沃섎챶諭??λ선 (?紐껊굡 揶??醫뤿동夷??뺥돩?????뻿)</li>
            <li>TensorRT ??System1 ?곕뗀以???얜즲(雅뚯눊由? ?關湲?/li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>沃섎챶諭??λ선夷뚧에?뺥겦 ??뽯선</h3>
          <ul class="stack-list">
            <li>Zenoh-bridge ROS2 DDS (?얜똻苑????뻿 ?됰슢?몌쭪?)</li>
            <li>Unitree API</li>
            <li>LiDAR SLAM Runner (?癒?퍥 closed-loop 獄쏄퉲???묎때)</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>?????됱뵠??뺣；??/h3>
          <ul class="stack-list">
            <li>NVIDIA Isaac Sim (Embodiment gap 野꺜筌?</li>
            <li>3D ?袁ⓥ뵛??(RealSense 筌띾뜆???</li>
          </ul>
        </article>
      </div>
    </div>
  </section>

<section class="section light timeline-section" id="timeline">
    <div class="page-shell timeline-shell">
      <div class="timeline-head">
        <p class="timeline-kicker">Timeline</p>
        <h2>筌╈돦???揶쏆뮆而????袁⑥뵬??/h2>
        <p>3?遺???5?遺쏀돱筌왖??雅뚯눘??揶쏆뮆而??④쑵?룡?筌욊쑵六??⑥눘??/p>
      </div>

      <div class="timeline-stage" aria-label="筌╈돦???揶쏆뮆而????袁⑥뵬??>
        <span class="timeline-axis" aria-hidden="true"></span>
        <span class="timeline-node timeline-node-1" aria-hidden="true"></span>
        <span class="timeline-node timeline-node-2" aria-hidden="true"></span>
        <span class="timeline-node timeline-node-3" aria-hidden="true"></span>

        <article class="timeline-entry timeline-entry-1">
          <div class="timeline-entry-inner">
            <h3>
              <span class="timeline-title-row">
                <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                  <path d="M4 0a1 1 0 0 1 1 1v1h6V1a1 1 0 1 1 2 0v1h1.5A1.5 1.5 0 0 1 16 3.5v11A1.5 1.5 0 0 1 14.5 16h-13A1.5 1.5 0 0 1 0 14.5v-11A1.5 1.5 0 0 1 1.5 2H3V1a1 1 0 0 1 1-1Zm-2 6v8.5c0 .28.22.5.5.5h11c.28 0 .5-.22.5-.5V6H2Zm12-2V3.5a.5.5 0 0 0-.5-.5H14v1a1 1 0 1 1-2 0V3H4v1a1 1 0 1 1-2 0V3h-.5a.5.5 0 0 0-.5.5V4h13Z"/>
                </svg>
                <span>3??/span>
              </span>
            </h3>
            <ul class="timeline-list">
              <li>獄쎻뫚堉??野껉퀣??/li>
              <li>ROS2 / Zenoh</li>
              <li>InternVLA / LOVON ????/li>
              <li>1筌???뽯염</li>
            </ul>
          </div>
        </article>

        <article class="timeline-entry timeline-entry-2">
          <div class="timeline-entry-inner">
            <h3>
              <span class="timeline-title-row">
                <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                  <path d="M4 0a1 1 0 0 1 1 1v1h6V1a1 1 0 1 1 2 0v1h1.5A1.5 1.5 0 0 1 16 3.5v11A1.5 1.5 0 0 1 14.5 16h-13A1.5 1.5 0 0 1 0 14.5v-11A1.5 1.5 0 0 1 1.5 2H3V1a1 1 0 0 1 1-1Zm-2 6v8.5c0 .28.22.5.5.5h11c.28 0 .5-.22.5-.5V6H2Zm12-2V3.5a.5.5 0 0 0-.5-.5H14v1a1 1 0 1 1-2 0V3H4v1a1 1 0 1 1-2 0V3h-.5a.5.5 0 0 0-.5.5V4h13Z"/>
                </svg>
                <span>4??/span>
              </span>
            </h3>
            <ul class="timeline-list">
              <li>Following 野껉퀬鍮</li>
              <li>LOVON ??? ?닌듼?筌△뫁??/li>
              <li>?遺얩닜??彛?/li>
              <li>LiDAR SLAM</li>
              <li>Backtracking</li>
            </ul>
          </div>
        </article>

        <article class="timeline-entry timeline-entry-3">
          <div class="timeline-entry-inner">
            <h3>
              <span class="timeline-title-row">
                <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">
                  <path d="M4 0a1 1 0 0 1 1 1v1h6V1a1 1 0 1 1 2 0v1h1.5A1.5 1.5 0 0 1 16 3.5v11A1.5 1.5 0 0 1 14.5 16h-13A1.5 1.5 0 0 1 0 14.5v-11A1.5 1.5 0 0 1 1.5 2H3V1a1 1 0 0 1 1-1Zm-2 6v8.5c0 .28.22.5.5.5h11c.28 0 .5-.22.5-.5V6H2Zm12-2V3.5a.5.5 0 0 0-.5-.5H14v1a1 1 0 1 1-2 0V3H4v1a1 1 0 1 1-2 0V3h-.5a.5.5 0 0 0-.5.5V4h13Z"/>
                </svg>
                <span>5??/span>
              </span>
            </h3>
            <ul class="timeline-list">
              <li>Pointing ?곕떽?</li>
              <li>?袁⑷퍥 ?꾨뗀諭?癰귣쵑鍮</li>
              <li>ROSA + Qwen3.5-4B ?怨뚭퍙</li>
              <li>ROS2 ?袁㏓럡 揶쏆뮇苑?/li>
              <li>Task Planner ????</li>
              <li>?類ｌ쎗 ???</li>
              <li>??겆??λ뜆釉?/li>
            </ul>
          </div>
        </article>

        <div class="timeline-arrow" aria-hidden="true"></div>
      </div>
    </div>
  </section>

<section class="section dark" id="team">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Team</h2>
        </div>
      </div>
      <div class="team-grid">
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/?袁???png" alt="?袁???profile photo">
          </div>
          <h3>?袁???/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/dla020501" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/鈺곌퀣???png" alt="鈺곌퀣???profile photo">
          </div>
          <h3>鈺곌퀣???/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/Reveroftrillion" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/?類ㅼ?筌?jpg" alt="?類ㅼ?筌?profile photo">
          </div>
          <h3>?類ㅼ?筌?/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/alicex-x02" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/?源놁삺??jpg" alt="?源놁삺??profile photo">
          </div>
          <h3>?源놁삺??/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/Sung-Jae-Seong" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/鈺곌퀣???png" alt="鈺곌퀣???profile photo">
          </div>
          <h3>鈺곌퀣???/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/yubincho3" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/?醫듼봺??jpg" alt="?醫듼봺??profile photo">
          </div>
          <h3>?醫듼봺??/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/ryurian001" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
      </div>
    </div>
  </section>

<section class="section light" id="references">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>References</h2>
        </div>
      </div>
      <article class="ref-card">
        <h3>Core References</h3>
        <p>[1] M. Wei, C. Wan, J. Peng, *et al.*, "Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation," *arXiv preprint* arXiv:2512.08186, 2025. <a href="https://arxiv.org/abs/2512.08186" target="_blank" rel="noreferrer">arXiv</a> <a href="https://huggingface.co/InternRobotics/InternVLA-N1-DualVLN" target="_blank" rel="noreferrer">HuggingFace</a></p>
        <p>[2] D. Peng, J. Cao, Q. Zhang, and J. Ma, "LOVON: Legged Open-Vocabulary Object Navigator," *arXiv preprint* arXiv:2507.06747, July 2025. <a href="https://arxiv.org/abs/2507.06747" target="_blank" rel="noreferrer">arXiv</a></p>
        <p>[3] R. Royce, M. Kaufmann, J. Becktor, *et al.*, "Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent," *arXiv preprint* arXiv:2410.06472, October 2024. <a href="https://arxiv.org/abs/2410.06472" target="_blank" rel="noreferrer">arXiv</a> <a href="https://github.com/nasa-jpl/rosa" target="_blank" rel="noreferrer">GitHub</a></p>
        <p>[4] Qwen Team, "Qwen3.5: Towards Native Multimodal Agents," *Qwen Blog*, February 2026. <a href="https://qwen.ai/blog?id=qwen3.5" target="_blank" rel="noreferrer">Blog</a> <a href="https://huggingface.co/Qwen/Qwen3.5-4B" target="_blank" rel="noreferrer">HuggingFace</a></p>
      </article>
    </div>
  </section>
</main>

<footer class="footer" id="contact">
  <div class="page-shell footer-inner">
    <div>
      <strong>VLA 疫꿸퀡而?????嚥≪뮆?????? ?癒?몛 ??뽯뮞??/strong>
      <div style="margin-top:8px;">GitHub Pages 夷?Kookmin SW Capstone 2026</div>
    </div>
    <div class="footer-links">
      <a href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub Repository</a>
      <a href="#overview">Overview</a>
      <a href="#hardware">Hardware</a>
      <a href="#team">Team</a>
    </div>
    <div>
      <div>Contact: TBD</div>
      <div>Images use relative paths like <code>./image/...</code></div>
    </div>
  </div>
</footer>
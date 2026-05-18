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
  background: linear-gradient(180deg, #f5f4f0 0%, #efede8 100%);
  color: var(--ink-dark);
}

.section.dark {
  background: var(--bg);
  color: var(--ink);
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
  color: var(--muted-dark);
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

.media video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: #000;
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
  color: rgba(31, 31, 31, 0.74);
}

.copy p:last-child {
  margin-bottom: 0;
}

.stack-subhead {
  margin: 0 0 18px;
}

.stack-subhead h3 {
  margin: 0;
  font-size: clamp(1.35rem, 2.4vw, 2rem);
  letter-spacing: -0.03em;
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
  border: 1px solid rgba(31, 31, 31, 0.1);
  background: #f6f3ed;
  overflow: hidden;
  transition: transform 0.18s ease, border-color 0.18s ease;
  color: var(--ink-dark);
}

.hardware-card:hover {
  transform: translateY(-2px);
  border-color: rgba(255, 79, 117, 0.4);
}

.hardware-card figure {
  margin: 0;
  height: 240px;
  background: #fff;
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
  color: rgba(31, 31, 31, 0.72);
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
  border: 1px dashed rgba(31, 31, 31, 0.22);
  background:
    linear-gradient(135deg, rgba(255, 79, 117, 0.08), rgba(155, 92, 255, 0.08)),
    repeating-linear-gradient(
      45deg,
      rgba(31, 31, 31, 0.03) 0,
      rgba(31, 31, 31, 0.03) 12px,
      transparent 12px,
      transparent 24px
    );
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 32px;
  color: var(--ink-dark);
}

.dark .placeholder-arch {
  border-color: rgba(255, 255, 255, 0.18);
  background:
    linear-gradient(135deg, rgba(255, 79, 117, 0.12), rgba(155, 92, 255, 0.12)),
    repeating-linear-gradient(
      45deg,
      rgba(255, 255, 255, 0.05) 0,
      rgba(255, 255, 255, 0.05) 12px,
      transparent 12px,
      transparent 24px
    );
  color: var(--ink);
}

.placeholder-arch strong {
  display: block;
  margin-bottom: 6px;
  font-size: 1.1rem;
}

.placeholder-arch code {
  font-size: 0.9rem;
  opacity: 0.82;
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
  border-color: rgba(31, 31, 31, 0.1);
  background: #fff;
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
  border-color: rgba(31, 31, 31, 0.08);
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
  border-color: rgba(31, 31, 31, 0.12);
  background: rgba(31, 31, 31, 0.02);
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
  background: linear-gradient(180deg, #f8f6f2 0%, #f4f1eb 100%);
  color: var(--ink-dark);
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
  color: var(--ink-dark);
  font-weight: 800;
}

.timeline-head p {
  margin: 0;
  max-width: 60ch;
  color: var(--muted-dark);
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
  background: linear-gradient(90deg, rgba(255, 91, 138, 0), rgba(255, 91, 138, 0.8), rgba(155, 92, 255, 0.8));
}

.timeline-entry-1::after,
.timeline-entry-3::after {
  right: -20px;
  width: 44px;
}

.timeline-entry-2::after {
  left: -20px;
  width: 44px;
  background: linear-gradient(90deg, rgba(255, 91, 138, 0.8), rgba(155, 92, 255, 0.8), rgba(155, 92, 255, 0));
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
  color: var(--ink-dark);
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
  background: linear-gradient(90deg, rgba(15, 27, 45, 0.18), rgba(255, 91, 138, 0.58), rgba(155, 92, 255, 0.58));
}

.timeline-entry-3 h3 {
  color: var(--accent-b);
}

.timeline-entry-3 h3::after {
  background: linear-gradient(90deg, rgba(15, 27, 45, 0.14), rgba(255, 91, 138, 0.52), rgba(155, 92, 255, 0.72));
}

.timeline-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 9px;
  color: rgba(31, 31, 31, 0.84);
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
  border-right: 2px solid rgba(15, 27, 45, 0.25);
  border-bottom: 2px solid rgba(15, 27, 45, 0.25);
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
      <a href="#stack">Tech Stack</a>
      <a href="#team">Team</a>
      <a href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub</a>
    </div>
  </div>
</nav>

<header class="hero">
  <div class="hero-inner">
    <div class="page-shell hero-grid">
      <div>
        <p class="kicker">Vision-Language-Action 쨌 Robotics Capstone Project</p>
        <h1>VLA 湲곕컲 ?ъ” 濡쒕큸 ?듯빀 ?먯쑉 ?쒖뒪??/h1>
        <p class="hero-lead">
          蹂??꾨줈?앺듃??<strong>Unitree Go2</strong> ?ъ” 蹂댄뻾 濡쒕큸??理쒖떊 Vision-Language-Action(VLA) 紐⑤뜽??<strong>InternVLA-N1-DualVLN</strong>???댁떇?섏뿬, ?щ엺??留먰븯???먯뿰??紐낅졊("?섏옄濡?媛", "? ?щ엺???곕씪媛")留뚯쑝濡?濡쒕큸???쒓컖 ?뺣낫瑜??댁꽍?섍퀬 ?ㅼ젣 ?섍꼍???먯쑉 二쇳뻾?섎룄濡?援ы쁽???꾨줈?앺듃??
        </p>
        <p class="hero-lead">
          湲곗〈 VLA 紐⑤뜽?ㅼ? ?泥대줈 ?대㉧?몄씠?쒓툒 ?쒖젏?대굹 怨좏뭹吏?移대찓???섍꼍???꾩젣濡?留뚮뱾?댁졇 ?덉뼱, ?묒? ?ъ” 濡쒕큸泥섎읆 蹂몄껜媛 ?ㅻⅨ ?섍꼍??洹몃?濡???린硫??깅뒫???⑥뼱吏꾨떎. ?곕━ ?? ?대윭??<strong>濡쒕큸 蹂몄껜蹂??섍꼍 李⑥씠</strong>瑜?蹂댁젙?섍린 ?꾪빐 LOVON???쇰? 援ъ“瑜?InternVLA??寃고빀?섍퀬, ROSA ?먯씠?꾪듃濡?紐낅졊??遺꾪빐?섎뒗 ???쒖뒪???덈꺼??媛쒖꽑???뷀뻽??
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
          <h2>?꾨줈?앺듃???섏쓽</h2>
        </div>
      </div>
      <div class="impact-grid">
        <article class="impact-card">
          <h3>1. ?뚰삎 ?ъ” 濡쒕큸 ?섍꼍?????VLA Foundation Model???곸쓳</h3>
          <p>?洹쒕え ?쒕??덉씠???곗씠?곕줈 ?숈뒿??理쒖떊 VLA Foundation Model? ?쇰컲?곸쑝濡??대㉧?몄씠?쒓툒 ?쒖젏?대굹 怨좏뭹吏?RGB-D ?섍꼍??媛?뺥븯湲??뚮Ц?? ?쒖젏 ?믪씠媛 ??퀬 移대찓???ъ뼇???쒗븳???뚰삎 ?ъ” 濡쒕큸??洹몃?濡?諛고룷?섎㈃ ?깅뒫????섎릺??蹂몄쭏???쒓퀎瑜?吏?뚮떎. 蹂??꾨줈?앺듃??LOVON???듭떖 紐⑤뱢??InternVLA-N1-DualVLN ?대????좏깮?곸쑝濡??듯빀?⑥쑝濡쒖뜥, <strong>Foundation Model???듭㎏濡??ы븰?듯븯吏 ?딄퀬???뚰삎 ?ъ” 濡쒕큸 蹂몄껜???곸쓳(domain adaptation)?쒗궎???ㅼ슜??寃쎈줈</strong>瑜??쒖떆?덈떎. ?대뒗 理쒖떊 ?洹쒕え VLA 紐⑤뜽???鍮꾩슜 濡쒕큸 ?뚮옯?쇱뿉 ?댁떇?섎젮???꾩냽 ?곌뎄쨌媛쒕컻??吏곸젒 ?쒖슜 媛?ν븳 諛⑸쾿濡좎쟻 湲곗뿬濡??됯??쒕떎.</p>
        </article>
        <article class="impact-card">
          <h3>2. ?⑥씪 task ?쒖뿰???섏뼱??硫?고깭?ㅽ겕 ?듯빀 ?뚯씠?꾨씪??/h3>
          <p>?ㅽ뵂?뚯뒪 InternVLA??怨듦컻 ?쒖뿰???⑥씪 navigation task??癒몃Ъ???덈뒗 寃껉낵 ?щ━, 蹂??쒖뒪?쒖? <strong>Navigation, Pointing, Following, Backtracking 4醫?task瑜?ROSA 湲곕컲 LLM ?먯씠?꾪듃 ?꾩뿉 ?⑥씪 ?뚯씠?꾨씪?몄쑝濡??듯빀</strong>?덈떎. ?뱁엳 LiDAR SLAM closed-loop 湲곕컲 ?먯쑉 諛깊듃?섑궧? InternVLA媛 蹂몃옒 ?ㅻ（吏 ?딅뒗 湲곕뒫???쒖뒪???덈꺼?먯꽌 ?뺤옣???щ?濡? foundation model???묒슜 task濡??뺤옣?섎뒗 援ъ껜???ㅺ퀎 ?덉떆瑜??쒓났?쒕떎.</p>
        </article>
        <article class="impact-card">
          <h3>3. ?먯뿰??湲곕컲 ?먭꺽 濡쒕큸 ?댁슜 ?명꽣?섏씠??/h3>
          <p>?먯껜 媛쒕컻??<strong>Go2 Monitor ???명꽣?섏씠??/strong>? <strong>Zenoh-bridge 湲곕컲 臾댁꽑 ROS2 ?듭떊 ?ㅽ깮</strong>??寃고빀?⑥쑝濡쒖뜥, <strong>?명꽣???곌껐留??덉쑝硫??먭꺽吏?먯꽌??濡쒕큸???ㅼ떆媛?移대찓???쇰뱶瑜??뺤씤?섍퀬 ?먯뿰??紐낅졊???꾩넚쨌?ㅽ뻾</strong>?쒗궗 ???덈뒗 援ъ“瑜??꾩꽦?덈떎. ?대뒗 ?ъ” 濡쒕큸???쒖슜 踰붿쐞瑜??곌뎄???곕え瑜??섏뼱 <strong>?щ엺??吏곸젒 ?묎렐???쒗븳?섎뒗 ?먭꺽吏쨌?꾪뿕 ?섍꼍쨌臾댁씤 ?쒖꽕</strong> ???ㅼ젣 ?댁슜 ?쒕굹由ъ삤濡??뺤옣?????덈뒗 湲곕컲???쒓났?섎ŉ, 鍮꾩쟾臾멸????먯뿰?대쭔?쇰줈 濡쒕큸???댁슜?????덈떎???먯뿉??HRI(Human-Robot Interaction) 痢〓㈃??吏꾩엯 ?λ꼍???ш쾶 ??텣 湲곗뿬濡??됯??쒕떎.</p>
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
          <h3>?먯뿰??紐낅졊?쇰줈 ?吏곸씠??VLA 湲곕컲 ?ъ” 濡쒕큸</h3>
          <p>蹂??꾨줈?앺듃??<strong>Unitree Go2</strong> ?ъ” 蹂댄뻾 濡쒕큸??理쒖떊 Vision-Language-Action(VLA) 紐⑤뜽??<strong>InternVLA-N1-DualVLN</strong>???댁떇?섏뿬, ?щ엺??留먰븯???먯뿰??紐낅졊("?섏옄濡?媛", "? ?щ엺???곕씪媛")留뚯쑝濡?濡쒕큸???쒓컖 ?뺣낫瑜??댁꽍?섍퀬 ?ㅼ젣 ?섍꼍???먯쑉 二쇳뻾?섎룄濡?援ы쁽???꾨줈?앺듃??</p>
          <p>湲곗〈 VLA 紐⑤뜽?ㅼ? ?泥대줈 ?대㉧?몄씠?쒓툒 ?쒖젏?대굹 怨좏뭹吏?移대찓???섍꼍???꾩젣濡?留뚮뱾?댁졇 ?덉뼱, ?묒? ?ъ” 濡쒕큸泥섎읆 蹂몄껜媛 ?ㅻⅨ ?섍꼍??洹몃?濡???린硫??깅뒫???⑥뼱吏꾨떎. ?곕━ ?? ?대윭??<strong>濡쒕큸 蹂몄껜蹂??섍꼍 李⑥씠</strong>瑜?蹂댁젙?섍린 ?꾪빐 LOVON???쇰? 援ъ“瑜?InternVLA??寃고빀?섍퀬, ROSA ?먯씠?꾪듃濡?紐낅졊??遺꾪빐?섎뒗 ???쒖뒪???덈꺼??媛쒖꽑???뷀뻽??</p>
          <div class="hero-cta" style="margin-top:24px;">
            <a class="btn" href="#hardware">Hardware</a>
            <a class="btn" href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub</a>
          </div>
        </div>
      </div>

      <div class="feature-grid" aria-label="4媛吏 ?듭떖 湲곕뒫">
        <article class="mini-card">
          <h4>Navigation</h4>
          <p>?먯뿰??紐낅졊??諛쏆븘 ?섍꼍 ??紐⑺몴 吏?먭퉴吏 ?먯쑉 二쇳뻾?쒕떎. InternVLA-N1-DualVLN??移대찓???대?吏? 紐낅졊???숈떆???댁꽍??pixel goal??異쒕젰?섎㈃, 濡쒕큸??洹몄뿉 留욎떠 ?대룞?쒕떎.</p>
        </article>
        <article class="mini-card">
          <h4>Pointing</h4>
          <p>?대?吏 ???뱀젙 媛앹껜瑜?吏?쒗븯硫?濡쒕큸???대떦 媛앹껜濡??ν븳?? 媛앹껜 吏???뺣낫瑜?pixel goal濡?蹂?섑빐 InternVLA???꾨떖?섎뒗 諛⑹떇?대떎.</p>
        </article>
        <article class="mini-card">
          <h4>Following</h4>
          <p>?щ엺?대굹 臾쇱껜瑜?吏?띿쟻?쇰줈 異붿쥌?쒕떎. YOLO 媛앹껜 寃異?寃곌낵瑜?pixel goal ?낅젰?쇰줈 ?ъ슜?섎ŉ, LOVON???쇰? 援ъ“瑜?李⑥슜??紐⑥뀡 釉붾윭쨌???異붿쥌 ?섍꼍?먯꽌???덉젙?곸쑝濡??숈옉?섎룄濡?媛쒖꽑?덈떎.</p>
        </article>
        <article class="mini-card">
          <h4>Backtracking</h4>
          <p>LiDAR SLAM 湲곕컲 closed-loop ?쒖뼱濡?怨쇨굅??吏?섏삩 寃쎈줈瑜??먮룞?쇰줈 ?섏쭦???뚯븘?⑤떎.</p>
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
          <h3>Project Demo Video</h3>
          <p>?ш린???곕え ?곸긽???ｌ쓣 ???덉뒿?덈떎. <code>./video/demo.mp4</code> 寃쎈줈???ㅼ젣 ?뚯씪???먮㈃ 諛붾줈 ?ъ깮?⑸땲??</p>
          <p>?쒖뿰?먯꽌??VLA navigation, pointing, following, backtracking ?먮쫫??蹂댁뿬二쇰뒗 援ъ꽦?????댁슱由쎈땲??</p>
        </div>
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
            <img src="./profile/?꾨???png" alt="?꾨???profile photo">
          </div>
          <h3>?꾨???/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/dla020501" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/議곗썝??png" alt="議곗썝??profile photo">
          </div>
          <h3>議곗썝??/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/Reveroftrillion" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/?뺤쑀吏?jpg" alt="?뺤쑀吏?profile photo">
          </div>
          <h3>?뺤쑀吏?/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/alicex-x02" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/?깆옱??jpg" alt="?깆옱??profile photo">
          </div>
          <h3>?깆옱??/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/Sung-Jae-Seong" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/議곗쑀鍮?png" alt="議곗쑀鍮?profile photo">
          </div>
          <h3>議곗쑀鍮?/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/yubincho3" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/?좊━??jpg" alt="?좊━??profile photo">
          </div>
          <h3>?좊━??/h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/ryurian001" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
      </div>
    </div>
  </section>

    <section class="section light timeline-section" id="timeline">
    <div class="page-shell timeline-shell">
      <div class="timeline-head">
        <p class="timeline-kicker">Timeline</p>
        <h2>罹≪뒪??媛쒕컻 ??꾨씪??/h2>
        <p>3?붾???5?붽퉴吏??二쇱슂 媛쒕컻 怨꾪쉷怨?吏꾪뻾 怨쇱젣</p>
      </div>

      <div class="timeline-stage" aria-label="罹≪뒪??媛쒕컻 ??꾨씪??>
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
              <li>諛⑺뼢??寃곗젙</li>
              <li>ROS2 / Zenoh</li>
              <li>InternVLA / LOVON ?ы쁽</li>
              <li>1李??쒖뿰</li>
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
              <li>Following 寃고빀</li>
              <li>LOVON ?쇰? 援ъ“ 李⑥슜</li>
              <li>?붾툝?щ쭅</li>
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
              <li>Pointing 異붽?</li>
              <li>?꾩껜 肄붾뱶 蹂묓빀</li>
              <li>ROSA + Qwen3.5-4B ?곌껐</li>
              <li>ROS2 ?꾧뎄 媛쒖꽑</li>
              <li>Task Planner ?듯빀</li>
              <li>?뺣웾 ?됯?</li>
              <li>?쇰Ц 珥덉븞</li>
            </ul>
          </div>
        </article>

        <div class="timeline-arrow" aria-hidden="true"></div>
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
      <div class="stack-subhead" id="hardware">
        <h3>Hardware</h3>
      </div>
      <div class="hardware-grid">
        <article class="hardware-card">
          <figure>
            <img src="./image/go2_whole.png" alt="Unitree Go2">
          </figure>
          <div class="body">
            <h3>Unitree Go2</h3>
            <p>4諛?蹂댄뻾 濡쒕큸, ?댁옣 Jetson Orin / ?댁옣 LiDAR</p>
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
            <p>二쇳뻾 ?덉젙?깃낵 ?섍꼍 ?몄?瑜??꾪븳 嫄곕━ ?쇱꽌</p>
          </div>
        </article>
      </div>

      <div class="stack-subhead" style="margin-top:34px;">
        <h3>Software / Models</h3>
      </div>
      <div class="stack-grid">
        <article class="stack-card">
          <h3>Models / AI</h3>
          <ul class="stack-list">
            <li>InternVLA-N1-DualVLN</li>
            <li>LOVON</li>
            <li>Qwen3.5-4B</li>
            <li>YOLO</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>Software</h3>
          <ul class="stack-list">
            <li>Python + PyTorch</li>
            <li>OpenCV / NumPy</li>
            <li>ROS 2</li>
            <li>TensorRT</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>Middleware / Robot Control</h3>
          <ul class="stack-list">
            <li>Zenoh-bridge ROS2 DDS</li>
            <li>Unitree API</li>
            <li>LiDAR SLAM Runner</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>Simulation</h3>
          <ul class="stack-list">
            <li>NVIDIA Isaac Sim</li>
            <li>3D printing / RealSense mounting</li>
          </ul>
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
      <strong>VLA 湲곕컲 ?ъ” 濡쒕큸 ?듯빀 ?먯쑉 ?쒖뒪??/strong>
      <div style="margin-top:8px;">GitHub Pages 쨌 Kookmin SW Capstone 2026</div>
    </div>
    <div class="footer-links">
      <a href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub Repository</a>
      <a href="#overview">Overview</a>
      <a href="#demo">Demo</a>
      <a href="#stack">Tech Stack</a>
      <a href="#team">Team</a>
    </div>
    <div>
      <div>Contact: TBD</div>
      <div>Images use relative paths like <code>./image/...</code></div>
    </div>
  </div>
</footer>



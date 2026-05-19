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
  margin: 0;
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

#overview .copy h3 {
  max-width: 100%;
  font-size: clamp(2rem, 2.8vw, 3.2rem);
  line-height: 1.25;
  word-break: keep-all;
  overflow-wrap: normal;
}

#overview .split {
  grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
  gap: 56px;
}

#overview .media.tall {
  min-height: 480px;
}

#overview .media img {
  object-fit: cover;
  object-position: center center;
  transform: scale(1.1);
}

#overview .feature-grid {
  margin-top: 52px;
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

.demo-note {
  margin: -8px 0 0;
  color: rgba(245, 245, 245, 0.62);
  font-size: 0.95rem;
}

.demo-grid {
  display: grid;
  grid-template-columns: 0.88fr 1fr 1fr;
  gap: 18px;
  margin-top: 24px;
  grid-auto-flow: dense;
  align-items: stretch;
}

.demo-card {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 14px;
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.03);
  min-height: 0;
}

.demo-card h3 {
  margin: 0;
  min-height: 1.4em;
  font-size: 0.98rem;
  line-height: 1.35;
  letter-spacing: -0.03em;
  word-break: keep-all;
}

.demo-card video {
  display: block;
  width: 100%;
  height: auto;
  object-fit: cover;
  background: #000;
}

.demo-card.portrait {
  grid-row: span 2;
}

.demo-card.portrait video {
  flex: 1;
  min-height: 0;
  height: 100%;
  aspect-ratio: 9 / 15;
}

.demo-card.landscape video {
  aspect-ratio: 16 / 9;
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

@media (max-width: 1100px) {
  .demo-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .demo-card.portrait {
    grid-row: auto;
  }

  .demo-card.portrait video {
    aspect-ratio: 16 / 9;
  }
}

@media (max-width: 720px) {
  .demo-grid {
    grid-template-columns: 1fr;
  }
}

.mini-card h4 {
  margin: 0 0 14px;
  padding-bottom: 10px;
  font-size: 1.28rem;
  line-height: 1.25;
  position: relative;
}

.mini-card h4::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent-a), var(--accent-b));
  box-shadow: 0 0 12px rgba(255, 79, 117, 0.35), 0 0 16px rgba(155, 92, 255, 0.22);
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
  align-items: center;
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

#architecture .placeholder-arch {
  display: flex;
  align-items: center;
}

#architecture .copy {
  align-self: center;
}

#architecture .arch-list {
  margin-top: 0;
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
  background:
    radial-gradient(circle at 24% 48%, rgba(255, 79, 117, 0.08), transparent 28%),
    radial-gradient(circle at 78% 48%, rgba(155, 92, 255, 0.08), transparent 30%),
    var(--bg);
  color: var(--ink);
}

.timeline-shell {
  padding-top: 8px;
}

.timeline-head {
  display: grid;
  justify-items: start;
  text-align: left;
  gap: 10px;
  margin-bottom: 36px;
}

.timeline-head h2 {
  margin: 0;
  font-size: clamp(2rem, 4vw, 3.6rem);
  line-height: 1;
  letter-spacing: -0.04em;
  color: var(--ink);
}

.timeline-head p {
  margin: 0;
  max-width: 60ch;
  color: var(--muted);
}

.timeline-stage {
  position: relative;
  min-height: 590px;
  padding: 18px 0 28px;
}

.timeline-axis {
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  height: 2px;
  transform: translateY(-50%);
  background: linear-gradient(90deg, rgba(255, 79, 117, 0.05), rgba(255, 79, 117, 0.88), rgba(155, 92, 255, 0.9), rgba(155, 92, 255, 0.05));
  box-shadow: 0 0 18px rgba(255, 79, 117, 0.35), 0 0 28px rgba(155, 92, 255, 0.25);
}

.timeline-node {
  position: absolute;
  top: 50%;
  z-index: 2;
  width: 18px;
  height: 18px;
  border-radius: 999px;
  background: linear-gradient(135deg, var(--accent-a), var(--accent-b));
  border: 3px solid rgba(255, 255, 255, 0.78);
  box-shadow: 0 0 0 8px rgba(255, 79, 117, 0.14), 0 0 26px rgba(155, 92, 255, 0.5);
  transform: translate(-50%, -50%);
}

.timeline-node::after {
  content: "";
  position: absolute;
  left: 50%;
  width: 1px;
  height: 54px;
  transform: translateX(-50%);
  background: linear-gradient(180deg, rgba(255, 79, 117, 0.85), rgba(155, 92, 255, 0.3));
}

.timeline-node-1 {
  left: 18%;
}

.timeline-node-2 {
  left: 50%;
}

.timeline-node-3 {
  left: 82%;
}

.timeline-node-1::after,
.timeline-node-3::after {
  top: 100%;
}

.timeline-node-2::after {
  bottom: 100%;
  background: linear-gradient(0deg, rgba(255, 79, 117, 0.85), rgba(155, 92, 255, 0.3));
}

.timeline-entry {
  position: absolute;
  z-index: 3;
  width: min(330px, 28vw);
  padding: 0;
  border: 0;
  background: transparent;
  box-shadow: none;
}

.timeline-entry-1 {
  left: 9%;
  top: calc(50% + 70px);
}

.timeline-entry-2 {
  left: 50%;
  bottom: calc(50% + 70px);
  transform: translateX(-50%);
}

.timeline-entry-3 {
  right: 7%;
  top: calc(50% + 70px);
}

.timeline-entry-inner {
  display: grid;
  gap: 14px;
}

.timeline-entry h3 {
  margin: 0;
  display: grid;
  gap: 12px;
  font-size: clamp(1.45rem, 2.4vw, 2.2rem);
  font-weight: 600;
  line-height: 1;
  letter-spacing: -0.03em;
  color: var(--ink);
}

.timeline-title-row {
  display: inline-flex;
  align-items: center;
  gap: 12px;
}

.timeline-title-row svg {
  width: 26px;
  height: 26px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.6;
  color: var(--accent-a);
  filter: drop-shadow(0 0 7px rgba(255, 79, 117, 0.5));
  flex: 0 0 auto;
}

.timeline-entry h3::after {
  content: "";
  width: 100%;
  height: 2px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent-a), var(--accent-b));
  box-shadow: 0 0 12px rgba(155, 92, 255, 0.25);
}

.timeline-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 8px;
  color: rgba(245, 245, 245, 0.84);
  font-size: clamp(0.92rem, 1.1vw, 1rem);
}

.timeline-list li {
  position: relative;
  padding-left: 18px;
  line-height: 1.5;
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
  box-shadow: 0 0 8px rgba(255, 79, 117, 0.45);
}

.timeline-entry-2 .timeline-title-row svg {
  color: var(--accent-b);
}

@media (max-width: 900px) {
  .timeline-stage {
    display: grid;
    gap: 28px;
    min-height: auto;
    padding: 8px 0 0;
  }

  .timeline-axis,
  .timeline-node {
    display: none;
  }

  .timeline-entry,
  .timeline-entry-1,
  .timeline-entry-2,
  .timeline-entry-3 {
    position: static;
    width: 100%;
    max-width: none;
    transform: none;
    padding: 0 0 0 18px;
    border-left: 1px solid rgba(255, 79, 117, 0.38);
  }
}

.stack-grid {
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

.impact-layout {
  display: grid;
  grid-template-columns: minmax(0, 1.35fr) minmax(320px, 0.65fr);
  gap: 36px;
  align-items: start;
}

.impact-copy {
  display: grid;
  gap: 18px;
}

.impact-image {
  margin: 0;
  border: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.03);
  overflow: hidden;
}

.impact-image img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center center;
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

  .impact-layout {
    grid-template-columns: 1fr;
  }

  .nav-inner {
    gap: 12px;
  }

  .nav-links {
    justify-content: flex-start;
    gap: 16px;
  }

  #overview .split {
    grid-template-columns: 1fr;
    gap: 34px;
  }

  #overview .media img {
    transform: none;
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
      <a href="#stack">Hardware</a>
      <a href="#team">Team</a>
      <a href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub</a>
    </div>
  </div>
</nav>

<header class="hero">
  <div class="hero-inner">
    <div class="page-shell hero-grid">
      <div>
        <p class="kicker">Vision-Language-Action · Robotics Capstone Project</p>
        <h1>원격지에서의 자율적인 사족보행 로봇 구현</h1>
        <p class="hero-lead">
          본 프로젝트는 <strong>Unitree Go2</strong> 사족 보행 로봇에 최신 Vision-Language-Action(VLA) 기반 내비게이션 모델인 <strong>InternVLA-N1-DualVLN</strong>을 이식하여, 자연어 명령만으로 실제 환경을 인식하고 자율 주행하는 로봇 시스템을 구현합니다.
        </p>
        <p class="hero-lead">
          또한 사족 보행 로봇의 낮은 카메라 시점과 실제 환경 차이로 인한 성능 저하를 줄이기 위해, <strong>LOVON의 객체 탐지 기반 보정 구조</strong>와 <strong>ROSA 에이전트 기반 명령 분해</strong>를 결합하여 보다 안정적인 자연어 기반 자율 주행 파이프라인을 구축했습니다.
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
      <div class="impact-layout">
        <div class="impact-copy">
          <article class="impact-card">
            <h3>1. 소형 사족 로봇 환경에 대한 VLA 모델 적응</h3>
            <p>
              사람에 가까운 카메라 시점과 고품질 센서 환경을 전제로 한 기존 VLA 모델은
              소형 사족 로봇에 그대로 적용할 경우 성능 저하가 발생할 수 있습니다.
              본 프로젝트는 <strong>InternVLA-N1-DualVLN</strong>에
              <strong>LOVON 기반 객체 탐지 및 목표 보정 구조</strong>를 결합하여,
              모델 전체를 재학습하지 않고도 Unitree Go2 환경에 적응할 수 있도록 구성했습니다.
            </p>
          </article>

          <article class="impact-card">
            <h3>2. 멀티태스크 VLA 파이프라인 구축</h3>
            <p>
              <strong>Navigation, Pointing, Following, Backtracking</strong> 기능을
              <strong>ROSA 기반 LLM 에이전트</strong> 위에 통합하여,
              자연어 명령에 따라 필요한 기능을 선택적으로 실행하는 구조를 구현했습니다.
              특히 LiDAR SLAM 기반 자율 백트래킹을 추가해 기존 내비게이션 중심 기능을 확장했습니다.
            </p>
          </article>

          <article class="impact-card">
            <h3>3. 자연어 기반 원격 로봇 운용</h3>
            <p>
              <strong>Go2 Monitor 웹 인터페이스</strong>와
              <strong>Zenoh-bridge 기반 무선 ROS2 통신</strong>을 통해,
              원격에서도 실시간 카메라 피드를 확인하고 자연어 명령을 전송할 수 있도록 구성했습니다.
              이를 통해 비전문가도 로봇을 쉽게 운용할 수 있는 기반을 마련했습니다.
            </p>
          </article>
        </div>

        <figure class="impact-image">
          <img src="./image/go2_crazy.jpg" alt="Unitree Go2">
        </figure>
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
          <img src="./image/go2_standing.png" alt="Unitree Go2 standing view">
        </figure>
        <div class="copy">
          <h3>자연어 명령 기반 VLA 사족 로봇</h3>
          <p>
            <strong>Unitree Go2</strong>가 사용자의 자연어 명령을 이해하고,
            시각 정보를 바탕으로 목표 대상을 찾아 실제 환경에서 자율 주행하도록 구현한 프로젝트입니다.
          </p>
          <p>
            사족 보행 로봇의 카메라 시점 차이와 실제 환경에서의 인식 오차를 보완하기 위해
            <strong>LOVON 기반 객체 탐지 보정</strong>과
            <strong>ROSA 에이전트 기반 명령 분해</strong>를 결합하여 안정적인 VLA 파이프라인을 구성했습니다.
          </p>
          <div class="hero-cta" style="margin-top:24px;">
            <a class="btn" href="#stack">Tech Stack</a>
            <a class="btn" href="#demo">Demo</a>
            <a class="btn" href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub</a>
          </div>
        </div>
      </div>

      <div class="feature-grid" aria-label="4가지 핵심 기능">
        <article class="mini-card">
          <h4>Navigation</h4>
          <p>자연어 명령을 받아 환경 내 목표 지점까지 자율 주행한다. InternVLA-N1-DualVLN이 카메라 이미지와 명령을 동시에 해석해 pixel goal을 출력하면, 로봇이 그에 맞춰 이동한다.</p>
        </article>
        <article class="mini-card">
          <h4>Pointing</h4>
          <p>이미지 위 특정 객체를 지시하면 로봇이 해당 객체로 향한다. 객체 지시 정보를 pixel goal로 변환해 InternVLA에 전달하는 방식이다.</p>
        </article>
        <article class="mini-card">
          <h4>Following</h4>
          <p>사람이나 물체를 지속적으로 추종한다. YOLO 객체 검출 결과를 pixel goal 입력으로 사용하며, LOVON의 일부 구조를 차용해 모션 블러·저속 추종 환경에서도 안정적으로 동작하도록 개선했다.</p>
        </article>
        <article class="mini-card">
          <h4>Backtracking</h4>
          <p>LiDAR SLAM 기반 closed-loop 제어로 과거에 지나온 경로를 자동으로 되짚어 돌아온다.</p>
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
      <p class="demo-note">Note: All demo videos are muted and shown at 2× playback speed.</p>
      <div class="demo-grid" aria-label="Demo videos">
        <article class="demo-card portrait">
          <h3>Follow the person</h3>
          <video controls autoplay loop playsinline preload="metadata" muted>
            <source src="./video/follow%20the%20person.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </article>
        <article class="demo-card landscape">
          <h3>Go to the backpack and return to the starting position</h3>
          <video controls autoplay loop playsinline preload="metadata" muted>
            <source src="./video/go%20to%20the%20backpack%20and%20return%20to%20the%20starting%20position.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </article>
        <article class="demo-card landscape">
          <h3>Go to the person and go to the chair</h3>
          <video controls autoplay loop playsinline preload="metadata" muted>
            <source src="./video/go%20to%20the%20person%20and%20go%20to%20the%20chair.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </article>
        <article class="demo-card landscape">
          <h3>Go to the sports ball</h3>
          <video controls autoplay loop playsinline preload="metadata" muted>
            <source src="./video/go%20to%20the%20sports%20ball.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </article>
        <article class="demo-card landscape">
          <h3>Turn right and go to the sports ball</h3>
          <video controls autoplay loop playsinline preload="metadata" muted>
            <source src="./video/turn%20right%20and%20go%20to%20the%20sports%20ball.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </article>
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
          <ul class="arch-list">
          <li><strong>Base Model-InternVLA-N1-DualVLN</strong>: System1의 저수준 제어와 System2의 고수준 의사결정을 결합한 dual-system 기반 VLA foundation model을 사용</li>

          <li><strong>LOVON 기반 구조 결합</strong>: LOVON의 객체 탐지 및 목표 보정 구조를 InternVLA 파이프라인에 결합하여 저속 주행·모션 블러 환경에서의 추종 안정성을 개선</li>

          <li><strong>LiDAR SLAM Runner</strong>: 실시간 SLAM 기반 closed-loop 제어를 통해 이동 경로를 추적하고, 필요 시 안전한 자율 백트래킹을 수행하도록 구성</li>

          <li><strong>ROSA Agent + Qwen3.5-4B</strong>: 자연어 명령을 세부 작업 단위로 분해하고, 상황에 맞는 기능을 선택적으로 호출하는 LLM 기반 에이전트</li>

          <li><strong>YOLO 입력단</strong>: VLA 모델을 전체 재학습하지 않고도 객체 기반 task를 확장할 수 있도록, YOLO 검출 결과를 pixel goal 형태로 변환해 입력에 주입</li>
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
      <h3>Hardware</h3>

<div class="hardware-grid">
        <article class="hardware-card">
          <figure>
            <img src="./image/go2_whole.png" alt="Unitree Go2">
          </figure>
          <div class="body">
            <h3>Unitree Go2</h3>
            <p>4족 보행 로봇, 내장 Jetson Orin / 내장 LiDAR</p>
          </div>
        </article>
        <article class="hardware-card">
          <figure>
            <img src="./image/realsense.png" alt="Intel RealSense D435i">
          </figure>
          <div class="body">
            <h3>Intel RealSense D435i</h3>
            <p>RGB-D 카메라</p>
          </div>
        </article>
        <article class="hardware-card">
          <figure>
            <img src="./image/rtx_3090.png" alt="RTX 3090">
          </figure>
          <div class="body">
            <h3>RTX 3090</h3>
            <p>모델 추론 및 실험 환경</p>
          </div>
        </article>
        <article class="hardware-card">
          <figure>
            <img src="./image/go2_lidar.png" alt="LiDAR on Unitree Go2">
          </figure>
          <div class="body">
            <h3>LiDAR</h3>
            <p>자율 백트래킹과 환경 인지를 위한 거리 센서</p>
          </div>
        </article>
      </div>

      <div class="stack-grid">
        <article class="stack-card">
          <h3>Models & AI</h3>
          <ul class="stack-list">
            <li>InternVLA-N1-DualVLN (메인 VLA)</li>
            <li>LOVON (일부 구조 차용)</li>
            <li>Qwen3.5-4B (vLLM 서빙, ROSA agent의 LLM)</li>
            <li>YOLO (객체 검출)</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>Software</h3>
          <ul class="stack-list">
            <li>Python + PyTorch: 메인 개발 언어 및 InternVLA·LOVON 추론 프레임워크</li>
            <li>vLLM: Qwen3.5-4B LLM 서빙</li>
            <li>OpenCV / NumPy: 이미지 처리·디블러링·SLAM 후처리·좌표 연산</li>
            <li>ROS 2: 로봇 미들웨어 (노드 간 토픽·서비스 통신)</li>
            <li>TensorRT: System1 추론 속도(주기) 향상</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>Middleware & Robot Control</h3>
          <ul class="stack-list">
            <li>Zenoh-bridge ROS2 DDS (무선 통신 브릿지)</li>
            <li>Unitree API</li>
            <li>LiDAR SLAM Runner (자체 closed-loop 백트래킹)</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>Simulation & Tools</h3>
          <ul class="stack-list">
            <li>NVIDIA Isaac Sim (Embodiment gap 검증)</li>
            <li>3D 프린팅 (RealSense 마운트)</li>
          </ul>
        </article>
      </div>
    </div>
  </section>

<section class="section light timeline-section" id="timeline">
    <div class="page-shell timeline-shell">
      <div class="timeline-head">
        <h2>Timeline</h2>
      </div>

      <div class="timeline-stage" aria-label="캡스톤 개발 타임라인">
        <span class="timeline-axis" aria-hidden="true"></span>
        <span class="timeline-node timeline-node-1" aria-hidden="true"></span>
        <span class="timeline-node timeline-node-2" aria-hidden="true"></span>
        <span class="timeline-node timeline-node-3" aria-hidden="true"></span>

        <article class="timeline-entry timeline-entry-1">
          <div class="timeline-entry-inner">
            <h3>
              <span class="timeline-title-row">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                  <rect x="4" y="5" width="16" height="15" rx="2"></rect>
                  <path d="M8 3v4M16 3v4M4 10h16"></path>
                </svg>
                <span>March</span>
              </span>
            </h3>
            <ul class="timeline-list">
              <li>주제 : 원격지에서의 자율적인 사족보행 로봇 구현</li>
              <li>ROS2 / Zenoh</li>
              <li>InternVLA / LOVON 재현</li>
              <li>1차 시연</li>
            </ul>
          </div>
        </article>

        <article class="timeline-entry timeline-entry-2">
          <div class="timeline-entry-inner">
            <h3>
              <span class="timeline-title-row">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                  <rect x="4" y="5" width="16" height="15" rx="2"></rect>
                  <path d="M8 3v4M16 3v4M4 10h16"></path>
                </svg>
                <span>April</span>
              </span>
            </h3>
            <ul class="timeline-list">
              <li>Following 결합</li>
              <li>LOVON 일부 구조 차용</li>
              <li>디블러링</li>
              <li>LiDAR SLAM</li>
              <li>Backtracking</li>
            </ul>
          </div>
        </article>

        <article class="timeline-entry timeline-entry-3">
          <div class="timeline-entry-inner">
            <h3>
              <span class="timeline-title-row">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                  <rect x="4" y="5" width="16" height="15" rx="2"></rect>
                  <path d="M8 3v4M16 3v4M4 10h16"></path>
                </svg>
                <span>May</span>
              </span>
            </h3>
            <ul class="timeline-list">
              <li>Pointing 추가</li>
              <li>ROSA + Qwen3.5-4B 연결</li>
              <li>ROS2 도구 개선</li>
              <li>Task Planner 통합</li>
              <li>정량 평가</li>
              <li>논문 초안</li>
            </ul>
          </div>
        </article>
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
            <img src="./profile/임민석.png" alt="임민석 profile photo">
          </div>
          <h3>임민석</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/dla020501" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/조원영.png" alt="조원영 profile photo">
          </div>
          <h3>조원영</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/Reveroftrillion" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/정유진.jpg" alt="정유진 profile photo">
          </div>
          <h3>정유진</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/alicex-x02" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/성재승.jpg" alt="성재승 profile photo">
          </div>
          <h3>성재승</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/Sung-Jae-Seong" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/조유빈.png" alt="조유빈 profile photo">
          </div>
          <h3>조유빈</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="https://github.com/yubincho3" target="_blank" rel="noreferrer">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.5-1.07-1.76-.2-3.62-.88-3.62-3.91 0-.86.31-1.57.82-2.13-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.65 7.65 0 0 1 2-.27c.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.26.82 2.13 0 3.04-1.86 3.7-3.63 3.9.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>
            <span>GitHub</span>
          </a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <img src="./profile/유리안.jpg" alt="유리안 profile photo">
          </div>
          <h3>유리안</h3>
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
      <strong>원격지에서의 자율적인 사족보행 로봇 구현</strong>
      <div style="margin-top:8px;">GitHub Pages · Kookmin SW Capstone 2026</div>
    </div>
    <div class="footer-links">
      <a href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub Repository</a>
      <a href="#overview">Overview</a>
      <a href="#stack">Hardware</a>
      <a href="#team">Team</a>
    </div>
    <div>
      <div>Contact: TBD</div>
      <div>Images use relative paths like <code>./image/...</code></div>
    </div>
  </div>
</footer>

<script>
(function () {
  var videos = document.querySelectorAll('.demo-grid video');
  if (!videos.length) return;

  function tryPlay(video) {
    var result = video.play();
    if (result && typeof result.catch === 'function') {
      result.catch(function () {});
    }
  }

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          tryPlay(entry.target);
        } else {
          entry.target.pause();
        }
      });
    }, { threshold: 0.5 });

    videos.forEach(function (video) {
      video.loop = true;
      video.muted = true;
      video.playsInline = true;
      observer.observe(video);
    });
  } else {
    videos.forEach(function (video) {
      video.loop = true;
      video.muted = true;
      video.playsInline = true;
      tryPlay(video);
    });
  }
})();
</script>

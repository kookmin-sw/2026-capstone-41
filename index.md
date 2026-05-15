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
    linear-gradient(180deg, #101014 0%, #050505 100%);
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

.hero-robot {
  position: absolute;
  right: 0;
  bottom: 0;
  width: min(58vw, 860px);
  max-height: 92vh;
  object-fit: contain;
  object-position: right bottom;
  opacity: 0.28;
  filter: grayscale(0.05) contrast(1.04);
}

.hero-inner {
  position: relative;
  z-index: 2;
  width: 100%;
  padding: 88px 0 96px;
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(280px, 0.85fr);
  gap: 36px;
  align-items: end;
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
  max-width: 10ch;
  font-size: clamp(3rem, 7vw, 6.8rem);
  line-height: 0.94;
  letter-spacing: -0.05em;
  background: linear-gradient(90deg, var(--accent-a), var(--accent-b));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hero-lead {
  margin: 26px 0 0;
  max-width: 58ch;
  color: rgba(245, 245, 245, 0.82);
  font-size: 1.05rem;
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

.avatar svg {
  width: 100%;
  height: 100%;
  display: block;
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
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 12px;
  font-size: 0.92rem;
  color: inherit;
  opacity: 0.84;
}

.light .team-card .gh {
  border-color: rgba(31, 31, 31, 0.08);
}

.team-note {
  margin-top: 14px;
  color: rgba(245, 245, 245, 0.68);
  font-size: 0.92rem;
}

.light .team-note {
  color: rgba(31, 31, 31, 0.58);
}

.timeline-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.timeline-card,
.stack-card,
.contact-card,
.ref-card,
.impact-card {
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.03);
  padding: 22px;
}

.light .timeline-card,
.light .stack-card,
.light .contact-card,
.light .ref-card,
.light .impact-card {
  border-color: rgba(31, 31, 31, 0.1);
  background: #fff;
}

.timeline-card h3,
.stack-card h3,
.contact-card h3,
.ref-card h3,
.impact-card h3 {
  margin: 0 0 10px;
  font-size: 1.15rem;
}

.timeline-card p,
.stack-card p,
.contact-card p,
.ref-card p,
.impact-card p {
  margin: 0;
  color: inherit;
  opacity: 0.78;
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
    right: -9vw;
    width: min(86vw, 620px);
    opacity: 0.2;
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
      <a href="#hardware">Hardware</a>
      <a href="#architecture">Architecture</a>
      <a href="#team">Team</a>
      <a href="https://github.com/kookmin-sw/2026-capstone-41" target="_blank" rel="noreferrer">GitHub</a>
    </div>
  </div>
</nav>

<header class="hero">
  <img class="hero-robot" src="./image/go2_whole.png" alt="Unitree Go2 robot">
  <div class="hero-inner">
    <div class="page-shell hero-grid">
      <div>
        <p class="kicker">Vision-Language-Action · Robotics Capstone Project</p>
        <h1>VLA 기반 사족 로봇 통합 자율 시스템</h1>
        <p class="hero-lead">
          본 프로젝트는 <strong>Unitree Go2</strong> 사족 보행 로봇에 최신 Vision-Language-Action(VLA) 모델인 <strong>InternVLA-N1-DualVLN</strong>을 이식하여, 사람이 말하는 자연어 명령("의자로 가", "저 사람을 따라가")만으로 로봇이 시각 정보를 해석하고 실제 환경을 자율 주행하도록 구현한 프로젝트다.
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
      <div>
        <p class="hero-lead" style="margin-top:0;">
          기존 VLA 모델들은 대체로 휴머노이드급 시점이나 고품질 카메라 환경을 전제로 만들어져 있어, 작은 사족 로봇처럼 본체가 다른 환경에 그대로 옮기면 성능이 떨어진다. 우리 팀은 이러한 <strong>로봇 본체별 환경 차이</strong>를 보정하기 위해 LOVON의 일부 구조를 InternVLA에 결합하고, ROSA 에이전트로 명령을 분해하는 등 시스템 레벨의 개선을 더했다.
        </p>
      </div>
    </div>
  </div>
</header>

<main>
  <section class="section light" id="overview">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>프로젝트 개요</h2>
          <p>PDF 5페이지처럼 큰 이미지와 텍스트를 좌우로 배치한 구조로, 기존 프로젝트 소개를 그대로 살려 재구성했다.</p>
        </div>
      </div>
      <div class="split">
        <figure class="card-shell media tall">
          <img src="./image/go2_front.png" alt="Unitree Go2 front view">
        </figure>
        <div class="copy">
          <h3>자연어 명령으로 움직이는 VLA 기반 사족 로봇</h3>
          <p>본 프로젝트는 <strong>Unitree Go2</strong> 사족 보행 로봇에 최신 Vision-Language-Action(VLA) 모델인 <strong>InternVLA-N1-DualVLN</strong>을 이식하여, 사람이 말하는 자연어 명령("의자로 가", "저 사람을 따라가")만으로 로봇이 시각 정보를 해석하고 실제 환경을 자율 주행하도록 구현한 프로젝트다.</p>
          <p>기존 VLA 모델들은 대체로 휴머노이드급 시점이나 고품질 카메라 환경을 전제로 만들어져 있어, 작은 사족 로봇처럼 본체가 다른 환경에 그대로 옮기면 성능이 떨어진다. 우리 팀은 이러한 <strong>로봇 본체별 환경 차이</strong>를 보정하기 위해 LOVON의 일부 구조를 InternVLA에 결합하고, ROSA 에이전트로 명령을 분해하는 등 시스템 레벨의 개선을 더했다.</p>
          <div class="hero-cta" style="margin-top:24px;">
            <a class="btn" href="#hardware">Hardware</a>
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

  <section class="section dark" id="hardware">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Hardware</h2>
          <p>사용한 하드웨어를 카드형으로 정리했다. 얇은 경계선과 절제된 hover 효과만 적용해 과한 랜딩페이지 느낌을 피했다.</p>
        </div>
      </div>
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
            <img src="./image/realsense.png" alt="Intel RealSense D435">
          </figure>
          <div class="body">
            <h3>Intel RealSense D435</h3>
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
    </div>
  </section>

  <section class="section light" id="architecture">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Architecture</h2>
          <p>아직 최종 아키텍처 이미지가 없어, 나중에 쉽게 교체할 수 있는 placeholder 박스를 먼저 넣어두었다.</p>
        </div>
      </div>
      <div class="arch-grid">
        <div class="placeholder-arch">
          <!-- Replace this block with <img src="./image/architecture-placeholder.png" alt="Architecture diagram"> when ready. -->
          <strong>Architecture image will be updated</strong>
          <code>./image/architecture-placeholder.png</code>
        </div>
        <div class="copy">
          <h3>시스템 아키텍처</h3>
          <p>아키텍처 섹션은 현재는 텍스트와 placeholder로 구성했지만, 완성된 다이어그램이 들어오면 그대로 교체할 수 있게 단순한 구조로 유지했다.</p>
          <ul class="arch-list">
            <li><strong>베이스 모델 — InternVLA-N1-DualVLN</strong>: System1(저수준 제어) + System2(고수준 의사결정)의 dual-system 구조를 가진 VLA foundation model을 그대로 활용한다.</li>
            <li><strong>LOVON 부분 결합</strong>: LOVON 모델 전체를 통째로 사용하지 않고, 일부 구조와 모델만 차용해 InternVLA 내부에 끼워 넣어 모션 블러·저속 환경에서의 추종 성능을 개선했다.</li>
            <li><strong>LiDAR SLAM Runner</strong>: 실시간 SLAM 기반 closed-loop 제어로 안전한 자율 백트래킹을 제공한다.</li>
            <li><strong>ROSA Agent + Qwen3.5-4B</strong>: 자연어 명령을 tool 단위로 분해하고, 4종 기능을 상황에 맞게 호출하는 LLM 에이전트다.</li>
            <li><strong>YOLO 입력단</strong>: VLA를 통째로 재학습하지 않고도 신규 task를 추가할 수 있도록 객체 검출 결과를 pixel goal 형태로 모델에 주입한다.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section dark" id="team">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>Team</h2>
          <p>기존 index.md에 있던 팀원 이름은 유지했고, 역할과 GitHub 링크는 나중에 바로 채울 수 있도록 placeholder로 남겼다.</p>
        </div>
      </div>
      <div class="team-grid">
        <article class="team-card">
          <div class="avatar">
            <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Member placeholder avatar">
              <defs>
                <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#ff4f75" stop-opacity="0.95" />
                  <stop offset="100%" stop-color="#9b5cff" stop-opacity="0.95" />
                </linearGradient>
              </defs>
              <rect width="400" height="400" fill="#0f0f13"/>
              <circle cx="200" cy="150" r="76" fill="url(#g1)" opacity="0.35"/>
              <circle cx="200" cy="186" r="48" fill="#f5f5f5" opacity="0.92"/>
              <path d="M96 344c14-68 68-102 104-102s90 34 104 102" fill="#f5f5f5" opacity="0.92"/>
              <path d="M104 132h192" stroke="url(#g1)" stroke-width="6" opacity="0.45"/>
              <circle cx="136" cy="122" r="7" fill="#f5f5f5"/>
              <circle cx="264" cy="122" r="7" fill="#f5f5f5"/>
            </svg>
          </div>
          <h3>임민석</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="#">GitHub</a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Member placeholder avatar">
              <defs>
                <linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#ff8a4c" stop-opacity="0.95" />
                  <stop offset="100%" stop-color="#ff4f75" stop-opacity="0.95" />
                </linearGradient>
              </defs>
              <rect width="400" height="400" fill="#0f0f13"/>
              <circle cx="200" cy="150" r="76" fill="url(#g2)" opacity="0.35"/>
              <circle cx="200" cy="186" r="48" fill="#f5f5f5" opacity="0.92"/>
              <path d="M96 344c14-68 68-102 104-102s90 34 104 102" fill="#f5f5f5" opacity="0.92"/>
              <path d="M104 132h192" stroke="url(#g2)" stroke-width="6" opacity="0.45"/>
              <circle cx="136" cy="122" r="7" fill="#f5f5f5"/>
              <circle cx="264" cy="122" r="7" fill="#f5f5f5"/>
            </svg>
          </div>
          <h3>조원영</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="#">GitHub</a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Member placeholder avatar">
              <defs>
                <linearGradient id="g3" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#9b5cff" stop-opacity="0.95" />
                  <stop offset="100%" stop-color="#5ec3ff" stop-opacity="0.95" />
                </linearGradient>
              </defs>
              <rect width="400" height="400" fill="#0f0f13"/>
              <circle cx="200" cy="150" r="76" fill="url(#g3)" opacity="0.35"/>
              <circle cx="200" cy="186" r="48" fill="#f5f5f5" opacity="0.92"/>
              <path d="M96 344c14-68 68-102 104-102s90 34 104 102" fill="#f5f5f5" opacity="0.92"/>
              <path d="M104 132h192" stroke="url(#g3)" stroke-width="6" opacity="0.45"/>
              <circle cx="136" cy="122" r="7" fill="#f5f5f5"/>
              <circle cx="264" cy="122" r="7" fill="#f5f5f5"/>
            </svg>
          </div>
          <h3>정유진</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="#">GitHub</a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Member placeholder avatar">
              <defs>
                <linearGradient id="g4" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#4fd1c5" stop-opacity="0.95" />
                  <stop offset="100%" stop-color="#9b5cff" stop-opacity="0.95" />
                </linearGradient>
              </defs>
              <rect width="400" height="400" fill="#0f0f13"/>
              <circle cx="200" cy="150" r="76" fill="url(#g4)" opacity="0.35"/>
              <circle cx="200" cy="186" r="48" fill="#f5f5f5" opacity="0.92"/>
              <path d="M96 344c14-68 68-102 104-102s90 34 104 102" fill="#f5f5f5" opacity="0.92"/>
              <path d="M104 132h192" stroke="url(#g4)" stroke-width="6" opacity="0.45"/>
              <circle cx="136" cy="122" r="7" fill="#f5f5f5"/>
              <circle cx="264" cy="122" r="7" fill="#f5f5f5"/>
            </svg>
          </div>
          <h3>성재승</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="#">GitHub</a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Member placeholder avatar">
              <defs>
                <linearGradient id="g5" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#ff4f75" stop-opacity="0.95" />
                  <stop offset="100%" stop-color="#4fd1c5" stop-opacity="0.95" />
                </linearGradient>
              </defs>
              <rect width="400" height="400" fill="#0f0f13"/>
              <circle cx="200" cy="150" r="76" fill="url(#g5)" opacity="0.35"/>
              <circle cx="200" cy="186" r="48" fill="#f5f5f5" opacity="0.92"/>
              <path d="M96 344c14-68 68-102 104-102s90 34 104 102" fill="#f5f5f5" opacity="0.92"/>
              <path d="M104 132h192" stroke="url(#g5)" stroke-width="6" opacity="0.45"/>
              <circle cx="136" cy="122" r="7" fill="#f5f5f5"/>
              <circle cx="264" cy="122" r="7" fill="#f5f5f5"/>
            </svg>
          </div>
          <h3>유리안</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="#">GitHub</a>
        </article>
        <article class="team-card">
          <div class="avatar">
            <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Member placeholder avatar">
              <defs>
                <linearGradient id="g6" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#f6c95d" stop-opacity="0.95" />
                  <stop offset="100%" stop-color="#ff4f75" stop-opacity="0.95" />
                </linearGradient>
              </defs>
              <rect width="400" height="400" fill="#0f0f13"/>
              <circle cx="200" cy="150" r="76" fill="url(#g6)" opacity="0.35"/>
              <circle cx="200" cy="186" r="48" fill="#f5f5f5" opacity="0.92"/>
              <path d="M96 344c14-68 68-102 104-102s90 34 104 102" fill="#f5f5f5" opacity="0.92"/>
              <path d="M104 132h192" stroke="url(#g6)" stroke-width="6" opacity="0.45"/>
              <circle cx="136" cy="122" r="7" fill="#f5f5f5"/>
              <circle cx="264" cy="122" r="7" fill="#f5f5f5"/>
            </svg>
          </div>
          <h3>조유빈</h3>
          <p class="role">Role TBD</p>
          <a class="gh" href="#">GitHub</a>
        </article>
      </div>
      <div class="team-note">역할과 GitHub 링크는 나중에 바로 채울 수 있도록 비워두었다.</div>
    </div>
  </section>

  <section class="section light" id="timeline">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>진행 타임라인</h2>
          <p>기존 index.md의 일정 설명을 그대로 유지하면서, PDF 9페이지처럼 grid 느낌으로 정리했다.</p>
        </div>
      </div>
      <div class="timeline-grid">
        <article class="timeline-card">
          <h3>3월</h3>
          <p>프로젝트 방향성 결정, ROS2/Zenoh 무선 통신 셋업, InternVLA·LOVON 재현, 1차 시연 발표를 진행했다.</p>
        </article>
        <article class="timeline-card">
          <h3>4월</h3>
          <p>InternVLA에 Following을 결합하는 방향성을 확정하고, LOVON 일부 구조 차용·디블러링·LiDAR SLAM 기반 자율 Backtracking을 구현했다.</p>
        </article>
        <article class="timeline-card">
          <h3>5월</h3>
          <p>Pointing 기능 추가, 전체 코드 병합, ROSA에 Qwen3.5-4B 연결, ROS2 도구 개선, Task Planner 통합 후 정량 평가와 논문 초안 작성에 들어갔다.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section dark" id="stack">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>기술 스택</h2>
          <p>기존 파일의 하드웨어, 모델, 소프트웨어, 미들웨어, 시뮬레이션 항목을 빠짐없이 유지했다.</p>
        </div>
      </div>
      <div class="stack-grid">
        <article class="stack-card">
          <h3>하드웨어</h3>
          <ul class="stack-list">
            <li>Unitree Go2 (4족 보행 로봇, 내장 Jetson Orin / 내장 LiDAR)</li>
            <li>Intel RealSense D435 (RGB-D 카메라)</li>
            <li>RTX 3090</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>모델·AI</h3>
          <ul class="stack-list">
            <li>InternVLA-N1-DualVLN (메인 VLA)</li>
            <li>LOVON (일부 구조 차용)</li>
            <li>Qwen3.5-4B (vLLM 서빙, ROSA agent의 LLM)</li>
            <li>YOLO (객체 검출)</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>소프트웨어</h3>
          <ul class="stack-list">
            <li>Python + PyTorch — 메인 개발 언어 및 InternVLA·LOVON 추론 프레임워크</li>
            <li>vLLM — Qwen3.5-4B LLM 서빙</li>
            <li>OpenCV / NumPy — 이미지 처리·디블러링·SLAM 후처리·좌표 연산</li>
            <li>ROS 2 — 로봇 미들웨어 (노드 간 토픽·서비스 통신)</li>
            <li>TensorRT — System1 추론 속도(주기) 향상</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>미들웨어·로봇 제어</h3>
          <ul class="stack-list">
            <li>Zenoh-bridge ROS2 DDS (무선 통신 브릿지)</li>
            <li>Unitree API</li>
            <li>LiDAR SLAM Runner (자체 closed-loop 백트래킹)</li>
          </ul>
        </article>
        <article class="stack-card">
          <h3>시뮬레이션·툴</h3>
          <ul class="stack-list">
            <li>NVIDIA Isaac Sim (Embodiment gap 검증)</li>
            <li>3D 프린팅 (RealSense 마운트)</li>
          </ul>
        </article>
      </div>
    </div>
  </section>

  <section class="section light" id="references">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>레퍼런스</h2>
          <p>본 프로젝트의 핵심 기반이 된 4개의 논문 및 기술 문서를 유지했다.</p>
        </div>
      </div>
      <div class="refs-grid">
        <article class="ref-card">
          <h3>[1] InternVLA-N1-DualVLN</h3>
          <p>M. Wei, C. Wan, J. Peng, *et al.*, "Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation," *arXiv preprint* arXiv:2512.08186, 2025. <a href="https://arxiv.org/abs/2512.08186" target="_blank" rel="noreferrer">arXiv</a> <a href="https://huggingface.co/InternRobotics/InternVLA-N1-DualVLN" target="_blank" rel="noreferrer">HuggingFace</a></p>
        </article>
        <article class="ref-card">
          <h3>[2] LOVON</h3>
          <p>D. Peng, J. Cao, Q. Zhang, and J. Ma, "LOVON: Legged Open-Vocabulary Object Navigator," *arXiv preprint* arXiv:2507.06747, July 2025. <a href="https://arxiv.org/abs/2507.06747" target="_blank" rel="noreferrer">arXiv</a></p>
        </article>
        <article class="ref-card">
          <h3>[3] ROSA</h3>
          <p>R. Royce, M. Kaufmann, J. Becktor, *et al.*, "Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent," *arXiv preprint* arXiv:2410.06472, October 2024. <a href="https://arxiv.org/abs/2410.06472" target="_blank" rel="noreferrer">arXiv</a> <a href="https://github.com/nasa-jpl/rosa" target="_blank" rel="noreferrer">GitHub</a></p>
        </article>
        <article class="ref-card">
          <h3>[4] Qwen3.5</h3>
          <p>Qwen Team, "Qwen3.5: Towards Native Multimodal Agents," *Qwen Blog*, February 2026. <a href="https://qwen.ai/blog?id=qwen3.5" target="_blank" rel="noreferrer">Blog</a> <a href="https://huggingface.co/Qwen/Qwen3.5-4B" target="_blank" rel="noreferrer">HuggingFace</a></p>
        </article>
      </div>
    </div>
  </section>

  <section class="section dark" id="impact">
    <div class="page-shell">
      <div class="section-head">
        <div>
          <h2>프로젝트의 의의</h2>
          <p>기존 index.md의 마지막 해설 문단도 누락하지 않고 그대로 유지했다.</p>
        </div>
      </div>
      <div class="impact-grid">
        <article class="impact-card">
          <h3>1. 소형 사족 로봇 환경에 대한 VLA Foundation Model의 적응</h3>
          <p>대규모 시뮬레이션 데이터로 학습된 최신 VLA Foundation Model은 일반적으로 휴머노이드급 시점이나 고품질 RGB-D 환경을 가정하기 때문에, 시점 높이가 낮고 카메라 사양이 제한된 소형 사족 로봇에 그대로 배포하면 성능이 저하되는 본질적 한계를 지닌다. 본 프로젝트는 LOVON의 핵심 모듈을 InternVLA-N1-DualVLN 내부에 선택적으로 통합함으로써, <strong>Foundation Model을 통째로 재학습하지 않고도 소형 사족 로봇 본체에 적응(domain adaptation)시키는 실용적 경로</strong>를 제시했다. 이는 최신 대규모 VLA 모델을 저비용 로봇 플랫폼에 이식하려는 후속 연구·개발에 직접 활용 가능한 방법론적 기여로 평가된다.</p>
        </article>
        <article class="impact-card">
          <h3>2. 단일 task 시연을 넘어선 멀티태스크 통합 파이프라인</h3>
          <p>오픈소스 InternVLA의 공개 시연이 단일 navigation task에 머물러 있는 것과 달리, 본 시스템은 <strong>Navigation, Pointing, Following, Backtracking 4종 task를 ROSA 기반 LLM 에이전트 위에 단일 파이프라인으로 통합</strong>했다. 특히 LiDAR SLAM closed-loop 기반 자율 백트래킹은 InternVLA가 본래 다루지 않는 기능을 시스템 레벨에서 확장한 사례로, foundation model을 응용 task로 확장하는 구체적 설계 예시를 제공한다.</p>
        </article>
        <article class="impact-card">
          <h3>3. 자연어 기반 원격 로봇 운용 인터페이스</h3>
          <p>자체 개발한 <strong>Go2 Monitor 웹 인터페이스</strong>와 <strong>Zenoh-bridge 기반 무선 ROS2 통신 스택</strong>을 결합함으로써, <strong>인터넷 연결만 있으면 원격지에서도 로봇의 실시간 카메라 피드를 확인하고 자연어 명령을 전송·실행</strong>시킬 수 있는 구조를 완성했다. 이는 사족 로봇의 활용 범위를 연구실 데모를 넘어 <strong>사람의 직접 접근이 제한되는 원격지·위험 환경·무인 시설</strong> 등 실제 운용 시나리오로 확장할 수 있는 기반을 제공하며, 비전문가도 자연어만으로 로봇을 운용할 수 있다는 점에서 HRI(Human-Robot Interaction) 측면의 진입 장벽을 크게 낮춘 기여로 평가된다.</p>
        </article>
      </div>
    </div>
  </section>
</main>

<footer class="footer" id="contact">
  <div class="page-shell footer-inner">
    <div>
      <strong>VLA 기반 사족 로봇 통합 자율 시스템</strong>
      <div style="margin-top:8px;">GitHub Pages · Kookmin SW Capstone 2026</div>
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

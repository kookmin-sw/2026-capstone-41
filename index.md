---
title: Capstone 41
---

<style>
  :root {
    --bg: #eef3f8;
    --bg-2: #f7fafc;
    --panel: rgba(255, 255, 255, 0.82);
    --panel-strong: #ffffff;
    --text: #101828;
    --muted: #5b6475;
    --line: rgba(16, 24, 40, 0.09);
    --accent: #2457ff;
    --accent-2: #10b981;
    --accent-3: #f59e0b;
    --shadow: 0 24px 60px rgba(15, 23, 42, 0.10);
    --radius-xl: 30px;
    --radius-lg: 22px;
    --radius-md: 18px;
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    background:
      radial-gradient(circle at top left, rgba(36, 87, 255, 0.13), transparent 28%),
      radial-gradient(circle at top right, rgba(16, 185, 129, 0.13), transparent 26%),
      linear-gradient(180deg, #f7fafc 0%, #eef3f8 40%, #f9fbfd 100%);
    color: var(--text);
    font-family: "Pretendard", "Noto Sans KR", "Apple SD Gothic Neo", "Segoe UI", sans-serif;
  }

  html,
  body {
    width: 100%;
    margin: 0;
    padding: 0;
  }

  /* Override the Slate theme's centered content column. */
  #main_content_wrap,
  #main_content_wrap .inner,
  #main_content,
  .inner,
  .wrapper,
  .outer {
    max-width: none !important;
    width: 100% !important;
  }

  #main_content_wrap .inner,
  #main_content {
    padding-left: 0 !important;
    padding-right: 0 !important;
    margin: 0 !important;
  }

  .page-shell {
    width: 100%;
    max-width: none;
    margin: 0;
    padding: 0;
  }

  .hero {
    position: relative;
    overflow: hidden;
    display: grid;
    grid-template-columns: minmax(0, 1.18fr) minmax(360px, 0.82fr);
    gap: 36px;
    align-items: center;
    padding: 44px 32px;
    border: 0;
    border-radius: 0;
    background: linear-gradient(145deg, rgba(255,255,255,0.92), rgba(255,255,255,0.72));
    box-shadow: none;
  }

  .hero::before,
  .hero::after {
    content: "";
    position: absolute;
    border-radius: 999px;
    filter: blur(8px);
    pointer-events: none;
  }

  .hero::before {
    width: 220px;
    height: 220px;
    background: rgba(36, 87, 255, 0.10);
    top: -70px;
    right: -60px;
  }

  .hero::after {
    width: 180px;
    height: 180px;
    background: rgba(16, 185, 129, 0.10);
    bottom: -60px;
    left: 22%;
  }

  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(36, 87, 255, 0.08);
    color: var(--accent);
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 0.02em;
  }

  .hero h1 {
    margin: 16px 0 14px;
    font-size: clamp(2.1rem, 5vw, 4.2rem);
    line-height: 1.03;
    letter-spacing: -0.04em;
  }

  .hero p.lead {
    margin: 0;
    max-width: 62ch;
    color: var(--muted);
    font-size: 1.04rem;
    line-height: 1.8;
  }

  .hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 24px;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 13px 18px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 700;
    transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
  }

  .btn:hover {
    transform: translateY(-2px);
  }

  .btn-primary {
    background: linear-gradient(135deg, var(--accent), #466cff);
    color: #fff;
    box-shadow: 0 16px 30px rgba(36, 87, 255, 0.28);
  }

  .btn-secondary {
    background: rgba(255, 255, 255, 0.88);
    color: var(--text);
    border: 1px solid var(--line);
  }

  .hero-stack {
    display: grid;
    gap: 14px;
  }

  .hero-card {
    border-radius: 24px;
    border: 1px solid var(--line);
    background: rgba(255, 255, 255, 0.84);
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
    overflow: hidden;
  }

  .hero-card img {
    display: block;
    width: 100%;
    height: auto;
  }

  .hero-mini-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
  }

  .hero-card,
  .mini,
  .feature,
  .device,
  .member,
  .arch-card,
  .note {
    height: 100%;
  }

  .mini {
    padding: 16px;
    border-radius: 22px;
    border: 1px solid var(--line);
    background: var(--panel);
    backdrop-filter: blur(10px);
  }

  .mini strong {
    display: block;
    margin-bottom: 6px;
    font-size: 1.02rem;
  }

  .mini span {
    color: var(--muted);
    line-height: 1.65;
    font-size: 0.96rem;
  }

  .section {
    margin-top: 16px;
    padding: 36px 32px;
    border: 0;
    border-radius: 0;
    background: var(--panel);
    box-shadow: none;
    backdrop-filter: blur(12px);
  }

  .section-head {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 18px;
    margin-bottom: 18px;
  }

  .section-head h2 {
    margin: 0;
    font-size: clamp(1.4rem, 2.4vw, 2rem);
    letter-spacing: -0.03em;
  }

  .section-head p {
    margin: 0;
    max-width: 84ch;
    color: var(--muted);
    line-height: 1.7;
  }

  .stats-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 16px;
    margin-top: 24px;
  }

  .stat {
    padding: 18px;
    border-radius: 22px;
    border: 1px solid var(--line);
    background: rgba(255, 255, 255, 0.76);
  }

  .stat .num {
    display: block;
    font-size: 1.65rem;
    font-weight: 800;
    letter-spacing: -0.03em;
  }

  .stat .label {
    margin-top: 6px;
    display: block;
    color: var(--muted);
    line-height: 1.5;
  }

  .feature-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 16px;
  }

  .feature {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid var(--line);
    background: linear-gradient(180deg, rgba(255,255,255,0.94), rgba(247,249,252,0.95));
  }

  .feature img {
    width: 100%;
    display: block;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    border-bottom: 1px solid var(--line);
  }

  .feature .body {
    padding: 18px;
  }

  .feature h3 {
    margin: 0 0 8px;
    font-size: 1.08rem;
  }

  .feature p {
    margin: 0;
    color: var(--muted);
    line-height: 1.7;
    font-size: 0.96rem;
  }

  .architecture-layout {
    display: grid;
    grid-template-columns: 1.05fr 0.95fr;
    gap: 18px;
    align-items: stretch;
  }

  .arch-card {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid var(--line);
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(244,247,252,0.98));
  }

  .arch-card img {
    width: 100%;
    display: block;
  }

  .arch-notes {
    display: grid;
    gap: 14px;
  }

  .note {
    padding: 18px;
    border-radius: 22px;
    border: 1px solid var(--line);
    background: rgba(255, 255, 255, 0.84);
  }

  .note strong {
    display: block;
    margin-bottom: 7px;
    font-size: 1.02rem;
  }

  .note span {
    color: var(--muted);
    line-height: 1.7;
  }

  .device-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
  }

  .device {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid var(--line);
    background: rgba(255,255,255,0.9);
  }

  .device img {
    width: 100%;
    display: block;
    aspect-ratio: 16 / 10;
    object-fit: cover;
    border-bottom: 1px solid var(--line);
  }

  .device .body {
    padding: 18px;
  }

  .device h3 {
    margin: 0 0 6px;
    font-size: 1.05rem;
  }

  .device p {
    margin: 0;
    color: var(--muted);
    line-height: 1.7;
    font-size: 0.96rem;
  }

  .team-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 16px;
  }

  .member {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid var(--line);
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
    display: grid;
    min-height: 100%;
  }

  .member img {
    width: 100%;
    display: block;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-bottom: 1px solid var(--line);
  }

  .member .body {
    padding: 18px;
    display: grid;
    gap: 10px;
  }

  .member h3 {
    margin: 0;
    font-size: 1.1rem;
  }

  .member .role {
    display: inline-flex;
    align-items: center;
    width: fit-content;
    padding: 6px 10px;
    border-radius: 999px;
    background: rgba(36, 87, 255, 0.08);
    color: var(--accent);
    font-size: 0.88rem;
    font-weight: 700;
  }

  .member p {
    margin: 0;
    color: var(--muted);
    line-height: 1.75;
    font-size: 0.95rem;
  }

  .member .link {
    margin-top: 4px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 10px 14px;
    border-radius: 12px;
    border: 1px solid var(--line);
    background: #fff;
    color: var(--text);
    text-decoration: none;
    font-weight: 700;
  }

  .references ol {
    margin: 0;
    padding-left: 20px;
    color: var(--muted);
    line-height: 1.8;
  }

  .footer-note {
    margin-top: 16px;
    color: var(--muted);
    font-size: 0.92rem;
    line-height: 1.7;
  }

  .overview-grid,
  .timeline-grid,
  .stack-grid,
  .impact-grid {
    display: grid;
    gap: 16px;
  }

  .overview-grid {
    grid-template-columns: minmax(0, 1.08fr) minmax(0, 0.92fr);
  }

  .timeline-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .stack-grid,
  .impact-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .stats-grid > *,
  .feature-grid > *,
  .device-grid > *,
  .team-grid > *,
  .overview-grid > *,
  .timeline-grid > *,
  .stack-grid > *,
  .impact-grid > * {
    min-height: 100%;
  }

  .text-panel {
    padding: 24px;
    border-radius: 24px;
    border: 1px solid var(--line);
    background: rgba(255, 255, 255, 0.84);
    height: 100%;
  }

  .text-panel h3 {
    margin: 0 0 10px;
    font-size: 1.08rem;
  }

  .text-panel p,
  .text-panel li {
    color: var(--muted);
    line-height: 1.8;
  }

  .text-panel ul {
    margin: 0;
    padding-left: 18px;
  }

  .timeline-month {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: fit-content;
    padding: 7px 12px;
    border-radius: 999px;
    background: rgba(36, 87, 255, 0.08);
    color: var(--accent);
    font-weight: 800;
    font-size: 0.88rem;
  }

  .text-panel .desc {
    margin-top: 10px;
  }

  @media (max-width: 1024px) {
    .hero,
    .architecture-layout {
      grid-template-columns: 1fr;
    }

    .feature-grid,
    .device-grid,
    .team-grid,
    .stats-grid,
    .overview-grid,
    .timeline-grid,
    .stack-grid,
    .impact-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 720px) {
    .page-shell {
      padding-inline: 0;
    }

    .hero,
    .section {
      padding: 20px 16px;
      border-radius: 0;
    }

    .feature-grid,
    .device-grid,
    .team-grid,
    .stats-grid,
    .hero-mini-grid,
    .overview-grid,
    .timeline-grid,
    .stack-grid,
    .impact-grid {
      grid-template-columns: 1fr;
    }

    .section-head {
      flex-direction: column;
      align-items: start;
    }
  }
</style>

<main class="page-shell">
  <section class="hero">
    <div>
      <span class="eyebrow">Capstone Project 41 · Vision-Language-Action Robotics</span>
      <h1>VLA 기반 사족 로봇<br>통합 자율 시스템</h1>
      <p class="lead">
        본 프로젝트는 <strong>Unitree Go2</strong> 사족 보행 로봇에 최신 Vision-Language-Action
        모델인 <strong>InternVLA-N1-DualVLN</strong>을 이식해, 자연어 명령만으로 로봇이
        시각 정보를 해석하고 실제 환경에서 자율 주행하도록 만드는 것을 목표로 합니다.
        기존 VLA 모델의 환경 편차를 보완하기 위해 LOVON, ROSA, LiDAR SLAM, YOLO를 함께
        엮어 하나의 통합 파이프라인으로 구성했습니다.
      </p>

      <div class="hero-actions">
        <a class="btn btn-primary" href="#overview">프로젝트 개요</a>
        <a class="btn btn-secondary" href="#architecture">시스템 아키텍처</a>
      </div>

      <div class="stats-grid">
        <div class="stat">
          <span class="num">4</span>
          <span class="label">핵심 태스크<br>Navigation, Pointing, Following, Backtracking</span>
        </div>
        <div class="stat">
          <span class="num">1</span>
          <span class="label">공통 VLA 기반<br>여러 태스크를 단일 파이프라인으로 연결</span>
        </div>
        <div class="stat">
          <span class="num">3+</span>
          <span class="label">주요 하드웨어<br>Go2, D435, LiDAR 등</span>
        </div>
        <div class="stat">
          <span class="num">100%</span>
          <span class="label">교체 가능 구조<br>이미지, 링크, 역할을 쉽게 업데이트</span>
        </div>
      </div>
    </div>

    <div class="hero-stack">
      <div class="hero-card">
        <img src="image/go2.jpg" alt="Unitree Go2 사진">
      </div>
      <div class="hero-mini-grid">
        <div class="mini">
          <strong>왜 필요한가</strong>
          <span>휴머노이드나 고정된 카메라 환경에 맞춰진 VLA 모델을 사족 로봇에 그대로 쓰면 성능이 떨어집니다.</span>
        </div>
        <div class="mini">
          <strong>어떻게 해결하나</strong>
          <span>LOVON 구조 일부와 ROSA 에이전트를 결합해 환경 편차를 줄이고 task 분해를 안정화합니다.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="overview">
    <div class="section-head">
      <div>
        <h2>프로젝트 개요</h2>
        <p>원래 소개 페이지의 핵심 내용을 더 읽기 쉽게 정리한 버전입니다. 긴 설명은 문단으로, 핵심 포인트는 카드로 나눴습니다.</p>
      </div>
    </div>

    <div class="overview-grid">
      <div class="text-panel">
        <h3>무엇을 만들었나</h3>
        <p>
          본 프로젝트는 Unitree Go2 사족 보행 로봇에 최신 VLA 모델인 InternVLA-N1-DualVLN을
          이식하여, 사람이 말하는 자연어 명령만으로 로봇이 시각 정보를 해석하고 실제 환경을
          자율 주행하도록 구현한 통합 자율 시스템입니다.
        </p>
        <p class="desc">
          단순히 모델을 붙이는 데서 끝나지 않고, ROSA 에이전트를 통해 명령을 분해하고,
          LOVON 일부 구조를 차용해 로봇 본체별 환경 차이를 줄이며, LiDAR SLAM과 YOLO를
          함께 사용해 실환경 주행 안정성을 높였습니다.
        </p>
      </div>
      <div class="text-panel">
        <h3>왜 의미가 있나</h3>
        <p>
          기존 VLA 모델들은 대체로 휴머노이드급 시점이나 고품질 카메라 환경을 전제로 만들어져 있어,
          작은 사족 로봇처럼 본체가 다른 환경에 그대로 옮기면 성능이 떨어집니다.
        </p>
        <p class="desc">
          우리는 이러한 로봇 본체별 환경 차이를 보정하기 위해 LOVON 구조를 InternVLA와
          결합하고, ROSA 에이전트를 통해 명령을 분해하는 방식으로 시스템 레벨 개선을 수행했습니다.
        </p>
      </div>
    </div>
  </section>

  <section class="section" id="features">
    <div class="section-head">
      <div>
        <h2>핵심 기능</h2>
        <p>단일 task 시연이 아니라, 네 가지 기능을 하나의 파이프라인으로 통합한 것이 핵심입니다.</p>
      </div>
    </div>

    <div class="feature-grid">
      <article class="feature">
        <img src="assets/images/feature-navigation.svg" alt="Navigation 기능 이미지">
        <div class="body">
          <h3>Navigation</h3>
          <p>자연어 명령을 받아 환경 내 목표 지점까지 자율 주행합니다. InternVLA-N1-DualVLN이 카메라 이미지와 명령을 동시에 해석해 pixel goal을 출력하면, 로봇이 그에 맞춰 이동합니다.</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-pointing.svg" alt="Pointing 기능 이미지">
        <div class="body">
          <h3>Pointing</h3>
          <p>이미지 위 특정 객체를 지시하면 로봇이 해당 객체로 향합니다. 객체 지시 정보를 pixel goal로 변환해 InternVLA에 전달하는 방식입니다.</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-following.svg" alt="Following 기능 이미지">
        <div class="body">
          <h3>Following</h3>
          <p>사람이나 물체를 지속적으로 추종합니다. YOLO 객체 검출 결과를 pixel goal 입력으로 사용하며, LOVON의 일부 구조를 차용해 모션 블러와 저속 추종 환경에서도 안정적으로 동작하도록 개선했습니다.</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-backtracking.svg" alt="Backtracking 기능 이미지">
        <div class="body">
          <h3>Backtracking</h3>
          <p>LiDAR SLAM 기반 closed-loop 제어로 과거에 지나온 경로를 자동으로 되짚어 돌아옵니다. 실내 자율주행에서 안정성을 높이는 핵심 기능입니다.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="section" id="architecture">
    <div class="section-head">
      <div>
        <h2>시스템 아키텍처</h2>
        <p>실제 아키텍처 이미지를 나중에 교체할 수 있도록 임시 자리를 마련했습니다. 오른쪽 설명은 본 프로젝트의 주요 모듈을 요약한 내용입니다.</p>
      </div>
    </div>

    <div class="architecture-layout">
      <div class="arch-card">
        <img src="assets/images/architecture-placeholder.svg" alt="시스템 아키텍처 임시 이미지">
      </div>
      <div class="arch-notes">
        <div class="note">
          <strong>베이스 모델: InternVLA-N1-DualVLN</strong>
          <span>System1(저수준 제어) + System2(고수준 의사결정)의 dual-system 구조를 가진 VLA foundation model을 활용합니다.</span>
        </div>
        <div class="note">
          <strong>LOVON 부분 결합</strong>
          <span>LOVON 모델 전체를 그대로 쓰지 않고, 구조와 모델 일부를 차용해 InternVLA 내부에 결합했습니다.</span>
        </div>
        <div class="note">
          <strong>보조 모듈</strong>
          <span>LiDAR SLAM Runner, ROSA Agent + Qwen3.5-4B, YOLO 입력단을 함께 연결해 4가지 태스크를 하나의 흐름으로 만듭니다.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>시스템 구성 요소</h2>
        <p>소개 페이지에서 가장 길고 딱딱해지기 쉬운 부분이라, 카드로 나눠서 핵심만 보이게 정리했습니다.</p>
      </div>
    </div>

    <div class="impact-grid">
      <div class="text-panel">
        <h3>베이스 모델</h3>
        <p>InternVLA-N1-DualVLN은 System1과 System2를 결합한 dual-system VLA foundation model이며, 본 프로젝트의 주된 추론 엔진입니다.</p>
      </div>
      <div class="text-panel">
        <h3>행동 분해</h3>
        <p>ROSA Agent는 자연어 명령을 tool 단위로 분해해 Navigation, Pointing, Following, Backtracking 중 필요한 기능을 호출합니다.</p>
      </div>
      <div class="text-panel">
        <h3>시각 입력</h3>
        <p>YOLO 결과를 pixel goal 형태로 주입해, VLA를 전체 재학습하지 않아도 새로운 task를 추가할 수 있도록 설계했습니다.</p>
      </div>
    </div>
  </section>

  <section class="section" id="equipment">
    <div class="section-head">
      <div>
        <h2>사용 장비와 모델</h2>
        <p>하드웨어, 모델, 프레임워크를 한 화면에 묶어 보여주면 캡스톤 소개 페이지의 설득력이 더 좋아집니다.</p>
      </div>
    </div>

    <div class="device-grid">
      <article class="device">
        <img src="image/go2.jpg" alt="Unitree Go2 사진">
        <div class="body">
          <h3>Unitree Go2</h3>
          <p>주행 플랫폼으로 사용하는 4족 보행 로봇입니다. 내장 Jetson Orin과 내장 LiDAR를 활용해 실환경 자율 주행을 수행합니다.</p>
        </div>
      </article>

      <article class="device">
        <img src="assets/images/realsense-d435-placeholder.svg" alt="Intel RealSense D435 임시 이미지">
        <div class="body">
          <h3>Intel RealSense D435</h3>
          <p>RGB-D 입력을 위한 카메라입니다. 객체 인식, 거리 추정, 시각 정보 수집, 디블러링 파이프라인에 활용됩니다.</p>
        </div>
      </article>

      <article class="device">
        <img src="assets/images/lidar-placeholder.svg" alt="LiDAR 임시 이미지">
        <div class="body">
          <h3>LiDAR / SLAM</h3>
          <p>실시간 SLAM 기반 closed-loop 제어를 통해 과거 경로를 복원하고, 자율 Backtracking 기능을 안정적으로 수행합니다.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="section" id="team">
    <div class="section-head">
      <div>
        <h2>팀 구성과 역할</h2>
        <p>팀원 사진, 담당 영역, 개인 GitHub 링크를 카드형으로 정리했습니다. 링크와 사진은 나중에 실제 정보로 바로 교체할 수 있습니다.</p>
      </div>
    </div>

    <div class="team-grid">
      <article class="member">
        <img src="assets/images/avatar-1.svg" alt="팀원 1 프로필 사진">
        <div class="body">
          <h3>임민석</h3>
          <span class="role">프로젝트 총괄</span>
          <p>전체 일정 관리, 발표 구성, 시스템 통합, 최종 정리를 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-1" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-2.svg" alt="팀원 2 프로필 사진">
        <div class="body">
          <h3>조원영</h3>
          <span class="role">로봇 제어</span>
          <p>Go2 제어, 주행 로직, 센서 연결 및 실기기 테스트를 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-2" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-3.svg" alt="팀원 3 프로필 사진">
        <div class="body">
          <h3>정유진</h3>
          <span class="role">AI / VLA</span>
          <p>VLA 모델 적용, 프롬프트 설계, 객체 인식 및 행동 생성 파트를 맡습니다.</p>
          <a class="link" href="https://github.com/your-github-id-3" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-4.svg" alt="팀원 4 프로필 사진">
        <div class="body">
          <h3>성재승</h3>
          <span class="role">SLAM / 백트래킹</span>
          <p>LiDAR SLAM, 경로 복원, 자율 Backtracking 모듈을 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-4" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-1.svg" alt="팀원 5 프로필 사진">
        <div class="body">
          <h3>유리안</h3>
          <span class="role">ROSA / LLM</span>
          <p>ROSA Agent와 Qwen3.5-4B 연동, tool 분해, 자연어 인터페이스를 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-5" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-2.svg" alt="팀원 6 프로필 사진">
        <div class="body">
          <h3>조유빈</h3>
          <span class="role">문서 / 발표 / 디자인</span>
          <p>발표 자료, 페이지 디자인, 문서 정리와 자료 아카이빙을 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-6" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>
    </div>

    <div class="footer-note">
      팀원 수가 더 많거나 역할이 바뀌면 이 카드 블록만 복제해서 바로 수정하면 됩니다. 개인 GitHub 주소도 카드별로 독립적으로 연결할 수 있습니다.
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>진행 타임라인</h2>
        <p>원본 페이지에 있던 월별 진행 내역을 조금 더 보기 좋게 정리했습니다.</p>
      </div>
    </div>

    <div class="timeline-grid">
      <div class="text-panel">
        <span class="timeline-month">3월</span>
        <h3>환경 구축 및 베이스라인 탐색</h3>
        <p class="desc">프로젝트 방향성 결정, ROS2/Zenoh 무선 통신 셋업, InternVLA·LOVON 재현, 1차 시연 발표를 진행했습니다.</p>
      </div>
      <div class="text-panel">
        <span class="timeline-month">4월</span>
        <h3>핵심 기능 구현</h3>
        <p class="desc">InternVLA에 Following을 결합하는 방향성을 확정하고, LOVON 일부 구조 차용, 디블러링, LiDAR SLAM 기반 자율 Backtracking을 구현했습니다.</p>
      </div>
      <div class="text-panel">
        <span class="timeline-month">5월</span>
        <h3>통합·평가·논문화</h3>
        <p class="desc">Pointing 기능 추가, 전체 코드 병합, ROSA에 Qwen3.5-4B 연결, ROS2 도구 개선, Task Planner 통합 후 정량 평가와 논문 초안 작성에 들어갔습니다.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>기술 스택</h2>
        <p>내용이 많아 보여도 실제로는 하드웨어, 모델, 소프트웨어, 미들웨어, 시뮬레이션 정도로 묶어서 보면 이해가 쉽습니다.</p>
      </div>
    </div>

    <div class="stack-grid">
      <div class="text-panel">
        <h3>하드웨어</h3>
        <ul>
          <li>Unitree Go2: 4족 보행 로봇, 내장 Jetson Orin / 내장 LiDAR</li>
          <li>Intel RealSense D435: RGB-D 카메라</li>
          <li>RTX 3090: 학습 및 추론용 GPU</li>
        </ul>
      </div>
      <div class="text-panel">
        <h3>모델·AI</h3>
        <ul>
          <li>InternVLA-N1-DualVLN: 메인 VLA</li>
          <li>LOVON: 일부 구조 차용</li>
          <li>Qwen3.5-4B: ROSA agent의 LLM</li>
          <li>YOLO: 객체 검출</li>
        </ul>
      </div>
      <div class="text-panel">
        <h3>소프트웨어</h3>
        <ul>
          <li>Python + PyTorch</li>
          <li>vLLM</li>
          <li>OpenCV / NumPy</li>
          <li>ROS 2</li>
          <li>TensorRT</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>프로젝트의 의의</h2>
        <p>원래 문서의 뒤쪽에 있던 논문식 설명을 소개 페이지 톤으로 다시 정리했습니다.</p>
      </div>
    </div>

    <div class="impact-grid">
      <div class="text-panel">
        <h3>1. 소형 사족 로봇 환경에 대한 적응</h3>
        <p>대규모 시뮬레이션 데이터로 학습된 VLA 모델은 대체로 휴머노이드급 시점이나 고품질 RGB-D 환경을 가정합니다. 본 프로젝트는 LOVON의 핵심 모듈을 InternVLA-N1-DualVLN 내부에 선택적으로 통합해, 소형 사족 로봇 본체에 적응하는 실용적 경로를 제시했습니다.</p>
      </div>
      <div class="text-panel">
        <h3>2. 단일 task를 넘어선 멀티태스크 통합</h3>
        <p>Navigation, Pointing, Following, Backtracking 4종 task를 ROSA 기반 LLM 에이전트 위에 하나의 파이프라인으로 묶었습니다. 이를 통해 foundation model이 실제 task에서 어떻게 확장될 수 있는지 보여줍니다.</p>
      </div>
      <div class="text-panel">
        <h3>3. 자율 로봇 시스템의 인터페이스</h3>
        <p>Go2 Monitor 인터페이스와 Zenoh-bridge 기반 무선 ROS2 통신을 결합해, 현장 연결만으로 로봇 상태를 확인하고 명령을 전송·실행할 수 있는 구조를 만들었습니다. 이는 HRI 관점에서도 중요한 기반이 됩니다.</p>
      </div>
    </div>
  </section>

  <section class="section references">
    <div class="section-head">
      <div>
        <h2>참고 문헌</h2>
        <p>핵심 논문과 기술 문서는 아래처럼 짧게 정리해 두면 소개 페이지가 덜 무거워 보입니다.</p>
      </div>
    </div>

    <ol>
      <li>M. Wei, C. Wan, J. Peng, et al., "Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation," arXiv:2512.08186, 2025.</li>
      <li>D. Peng, J. Cao, Q. Zhang, and J. Ma, "LOVON: Legged Open-Vocabulary Object Navigator," arXiv:2507.06747, July 2025.</li>
      <li>R. Royce, M. Kaufmann, J. Becktor, et al., "Enabling Novel Mission Operations and Interactions with ROSA: The Robot Operating System Agent," arXiv:2410.06472, October 2024.</li>
      <li>Qwen Team, "Qwen3.5: Towards Native Multimodal Agents," Qwen Blog, February 2026.</li>
    </ol>
  </section>
</main>

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

  .page-shell {
    max-width: 1240px;
    margin: 0 auto;
    padding: 28px 20px 84px;
  }

  .hero {
    position: relative;
    overflow: hidden;
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 28px;
    align-items: center;
    padding: 34px;
    border: 1px solid var(--line);
    border-radius: 32px;
    background: linear-gradient(145deg, rgba(255,255,255,0.92), rgba(255,255,255,0.72));
    box-shadow: var(--shadow);
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
    margin-top: 28px;
    padding: 28px;
    border: 1px solid var(--line);
    border-radius: var(--radius-xl);
    background: var(--panel);
    box-shadow: var(--shadow);
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
    max-width: 58ch;
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

  @media (max-width: 1024px) {
    .hero,
    .architecture-layout {
      grid-template-columns: 1fr;
    }

    .feature-grid,
    .device-grid,
    .team-grid,
    .stats-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 720px) {
    .page-shell {
      padding-inline: 14px;
    }

    .hero,
    .section {
      padding: 20px;
      border-radius: 22px;
    }

    .feature-grid,
    .device-grid,
    .team-grid,
    .stats-grid,
    .hero-mini-grid {
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
      <h1>캡스톤 소개 페이지를<br>조금 더 읽기 좋고, 보기 좋게</h1>
      <p class="lead">
        이 페이지는 Unitree Go2 기반 자율 로봇 프로젝트를 소개하는 랜딩 페이지입니다.
        핵심 기능, 시스템 아키텍처, 사용 장비, 팀 구성까지 한 화면에서 자연스럽게 볼 수 있도록
        카드형 레이아웃과 이미지 중심 구조로 다시 설계했습니다.
      </p>

      <div class="hero-actions">
        <a class="btn btn-primary" href="#architecture">시스템 아키텍처 보기</a>
        <a class="btn btn-secondary" href="#team">팀 구성 보기</a>
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
        <img src="assets/images/hero-robo-lab.svg" alt="프로젝트 분위기를 보여주는 로봇 일러스트">
      </div>
      <div class="hero-mini-grid">
        <div class="mini">
          <strong>한눈에 들어오는 구성</strong>
          <span>기존의 긴 텍스트 중심 페이지를 카드와 이미지 중심으로 바꿨습니다.</span>
        </div>
        <div class="mini">
          <strong>교체 쉬운 임시 이미지</strong>
          <span>아키텍처, 팀원 사진, 장비 이미지는 나중에 실사진으로 바로 교체할 수 있습니다.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="features">
    <div class="section-head">
      <div>
        <h2>핵심 기능</h2>
        <p>프로젝트가 무엇을 하는지 짧고 선명하게 보여주는 섹션입니다. 각 카드마다 이미지를 배치해서 설명이 더 빨리 읽히도록 구성했습니다.</p>
      </div>
    </div>

    <div class="feature-grid">
      <article class="feature">
        <img src="assets/images/feature-navigation.svg" alt="Navigation 기능 이미지">
        <div class="body">
          <h3>Navigation</h3>
          <p>목표 지점을 입력하면 로봇이 환경을 이해하고 목적지까지 이동합니다.</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-pointing.svg" alt="Pointing 기능 이미지">
        <div class="body">
          <h3>Pointing</h3>
          <p>특정 물체를 지목하면 해당 객체를 인식하고 관련 정보를 로봇 행동에 반영합니다.</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-following.svg" alt="Following 기능 이미지">
        <div class="body">
          <h3>Following</h3>
          <p>사람 또는 객체를 따라가며 주변 상황을 반영해 자연스럽게 주행합니다.</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-backtracking.svg" alt="Backtracking 기능 이미지">
        <div class="body">
          <h3>Backtracking</h3>
          <p>지나온 경로를 복원해 되돌아가며, 실내 자율주행 시 안정성을 높입니다.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="section" id="architecture">
    <div class="section-head">
      <div>
        <h2>시스템 아키텍처</h2>
        <p>나중에 실제 아키텍처 이미지를 넣을 수 있도록 임시 이미지를 먼저 배치했습니다. 원하는 시점에 이 이미지 파일만 교체하면 레이아웃은 그대로 유지됩니다.</p>
      </div>
    </div>

    <div class="architecture-layout">
      <div class="arch-card">
        <img src="assets/images/architecture-placeholder.svg" alt="시스템 아키텍처 임시 이미지">
      </div>
      <div class="arch-notes">
        <div class="note">
          <strong>왼쪽 큰 영역</strong>
          <span>실제 아키텍처 다이어그램을 넣는 자리입니다. 발표 자료와 같은 비율로 교체하면 바로 사용 가능합니다.</span>
        </div>
        <div class="note">
          <strong>오른쪽 보조 설명</strong>
          <span>아래 설명 박스는 모델, ROS, SLAM, LLM 연동 구조를 짧게 정리하는 용도로 쓰면 좋습니다.</span>
        </div>
        <div class="note">
          <strong>업데이트 방식</strong>
          <span>이미지 파일만 바꾸거나 SVG를 PNG로 교체해도 페이지 구조는 그대로 유지됩니다.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="equipment">
    <div class="section-head">
      <div>
        <h2>사용 장비와 모델</h2>
        <p>Unitree Go2, 카메라, LiDAR 같은 실제 하드웨어 이미지를 넣어 주면 프로젝트가 훨씬 직관적으로 보입니다.</p>
      </div>
    </div>

    <div class="device-grid">
      <article class="device">
        <img src="image/go2.jpg" alt="Unitree Go2 사진">
        <div class="body">
          <h3>Unitree Go2</h3>
          <p>주행 플랫폼으로 사용하는 4족 보행 로봇입니다. 실제 사진으로 교체하면 소개 페이지의 완성도가 크게 올라갑니다.</p>
        </div>
      </article>

      <article class="device">
        <img src="assets/images/realsense-d435-placeholder.svg" alt="Intel RealSense D435 임시 이미지">
        <div class="body">
          <h3>Intel RealSense D435</h3>
          <p>RGB-D 입력을 위한 카메라입니다. 객체 인식, 거리 추정, 시각 정보 수집에 활용됩니다.</p>
        </div>
      </article>

      <article class="device">
        <img src="assets/images/lidar-placeholder.svg" alt="LiDAR 임시 이미지">
        <div class="body">
          <h3>LiDAR / SLAM</h3>
          <p>실내 위치 추정과 경로 복원에 사용되는 핵심 센서입니다. backtracking과 연동되면 설명이 더 잘 살아납니다.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="section" id="team">
    <div class="section-head">
      <div>
        <h2>팀 구성과 역할</h2>
        <p>팀원 사진, 역할, 개인 GitHub 링크를 카드형으로 정리했습니다. 실제 이름과 링크만 바꾸면 바로 쓸 수 있게 템플릿 형태로 만들어 두었습니다.</p>
      </div>
    </div>

    <div class="team-grid">
      <article class="member">
        <img src="assets/images/avatar-1.svg" alt="팀원 1 프로필 사진">
        <div class="body">
          <h3>팀원 1</h3>
          <span class="role">프로젝트 총괄</span>
          <p>전체 일정 관리, 발표 구성, 시스템 통합을 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-1" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-2.svg" alt="팀원 2 프로필 사진">
        <div class="body">
          <h3>팀원 2</h3>
          <span class="role">로봇 제어</span>
          <p>Go2 제어, 주행 로직, 센서 연결 및 실기기 테스트를 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-2" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-3.svg" alt="팀원 3 프로필 사진">
        <div class="body">
          <h3>팀원 3</h3>
          <span class="role">AI / VLA</span>
          <p>VLA 모델 적용, 프롬프트 설계, 객체 인식 및 행동 생성 파트를 맡습니다.</p>
          <a class="link" href="https://github.com/your-github-id-3" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-4.svg" alt="팀원 4 프로필 사진">
        <div class="body">
          <h3>팀원 4</h3>
          <span class="role">디자인 / 문서</span>
          <p>페이지 디자인, 발표 자료 시각화, 문서 정리와 자료 아카이빙을 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-4" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>
    </div>

    <div class="footer-note">
      팀원이 4명보다 많으면 이 카드 블록을 복제해서 추가하면 됩니다. 사진은 같은 형식의 SVG를 계속 만들거나 실제 사진으로 교체할 수 있습니다.
    </div>
  </section>

  <section class="section references">
    <div class="section-head">
      <div>
        <h2>참고 문헌</h2>
        <p>논문과 모델 출처는 작게 정리해 두는 편이 소개 페이지에서는 더 깔끔합니다.</p>
      </div>
    </div>

    <ol>
      <li>InternVLA-N1-DualVLN 관련 논문 및 모델 페이지</li>
      <li>LOVON 관련 논문</li>
      <li>ROSA Agent 및 Qwen 계열 참고 자료</li>
      <li>프로젝트 내부 기술 문서 및 테스트 로그</li>
    </ol>
  </section>
</main>

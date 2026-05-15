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
    grid-template-columns: repeat(6, minmax(0, 1fr));
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
      <span class="eyebrow">Capstone Project 41 Â· Vision-Language-Action Robotics</span>
      <h1>VLA ê¸°ë°˜ ?¬ì¡± ë¡œë´‡<br>?µí•© ?ìœ¨ ?œìŠ¤??/h1>
      <p class="lead">
        ë³??„ë¡œ?íŠ¸??<strong>Unitree Go2</strong> ?¬ì¡± ë³´í–‰ ë¡œë´‡??ìµœì‹  Vision-Language-Action
        ëª¨ë¸??<strong>InternVLA-N1-DualVLN</strong>???´ì‹?? ?ì—°??ëª…ë ¹ë§Œìœ¼ë¡?ë¡œë´‡??        ?œê° ?•ë³´ë¥??´ì„?˜ê³  ?¤ì œ ?˜ê²½?ì„œ ?ìœ¨ ì£¼í–‰?˜ë„ë¡?ë§Œë“œ??ê²ƒì„ ëª©í‘œë¡??©ë‹ˆ??
        ê¸°ì¡´ VLA ëª¨ë¸???˜ê²½ ?¸ì°¨ë¥?ë³´ì™„?˜ê¸° ?„í•´ LOVON, ROSA, LiDAR SLAM, YOLOë¥??¨ê»˜
        ??–´ ?˜ë‚˜???µí•© ?Œì´?„ë¼?¸ìœ¼ë¡?êµ¬ì„±?ˆìŠµ?ˆë‹¤.
      </p>

      <div class="hero-actions">
        <a class="btn btn-primary" href="#overview">?„ë¡œ?íŠ¸ ê°œìš”</a>
        <a class="btn btn-secondary" href="#architecture">?œìŠ¤???„í‚¤?ì²˜</a>
      </div>

      <div class="stats-grid">
        <div class="stat">
          <span class="num">4</span>
          <span class="label">?µì‹¬ ?œìŠ¤??br>Navigation, Pointing, Following, Backtracking</span>
        </div>
        <div class="stat">
          <span class="num">1</span>
          <span class="label">ê³µí†µ VLA ê¸°ë°˜<br>?¬ëŸ¬ ?œìŠ¤?¬ë? ?¨ì¼ ?Œì´?„ë¼?¸ìœ¼ë¡??°ê²°</span>
        </div>
        <div class="stat">
          <span class="num">3+</span>
          <span class="label">ì£¼ìš” ?˜ë“œ?¨ì–´<br>Go2, D435, LiDAR ??/span>
        </div>
        <div class="stat">
          <span class="num">100%</span>
          <span class="label">êµì²´ ê°€??êµ¬ì¡°<br>?´ë?ì§€, ë§í¬, ??• ???½ê²Œ ?…ë°?´íŠ¸</span>
        </div>
      </div>
    </div>

    <div class="hero-stack">
      <div class="hero-card">
        <img src="image/go2.jpg" alt="Unitree Go2 ?¬ì§„">
      </div>
      <div class="hero-mini-grid">
        <div class="mini">
          <strong>???„ìš”?œê?</strong>
          <span>?´ë¨¸?¸ì´?œë‚˜ ê³ ì •??ì¹´ë©”???˜ê²½??ë§žì¶°ì§?VLA ëª¨ë¸???¬ì¡± ë¡œë´‡??ê·¸ë?ë¡??°ë©´ ?±ëŠ¥???¨ì–´ì§‘ë‹ˆ??</span>
        </div>
        <div class="mini">
          <strong>?´ë–»ê²??´ê²°?˜ë‚˜</strong>
          <span>LOVON êµ¬ì¡° ?¼ë??€ ROSA ?ì´?„íŠ¸ë¥?ê²°í•©???˜ê²½ ?¸ì°¨ë¥?ì¤„ì´ê³?task ë¶„í•´ë¥??ˆì •?”í•©?ˆë‹¤.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="overview">
    <div class="section-head">
      <div>
        <h2>?„ë¡œ?íŠ¸ ê°œìš”</h2>
        <p>?ëž˜ ?Œê°œ ?˜ì´ì§€???µì‹¬ ?´ìš©?????½ê¸° ?½ê²Œ ?•ë¦¬??ë²„ì „?…ë‹ˆ?? ê¸??¤ëª…?€ ë¬¸ë‹¨?¼ë¡œ, ?µì‹¬ ?¬ì¸?¸ëŠ” ì¹´ë“œë¡??˜ëˆ´?µë‹ˆ??</p>
      </div>
    </div>

    <div class="overview-grid">
      <div class="text-panel">
        <h3>ë¬´ì—‡??ë§Œë“¤?ˆë‚˜</h3>
        <p>
          ë³??„ë¡œ?íŠ¸??Unitree Go2 ?¬ì¡± ë³´í–‰ ë¡œë´‡??ìµœì‹  VLA ëª¨ë¸??InternVLA-N1-DualVLN??          ?´ì‹?˜ì—¬, ?¬ëžŒ??ë§í•˜???ì—°??ëª…ë ¹ë§Œìœ¼ë¡?ë¡œë´‡???œê° ?•ë³´ë¥??´ì„?˜ê³  ?¤ì œ ?˜ê²½??          ?ìœ¨ ì£¼í–‰?˜ë„ë¡?êµ¬í˜„???µí•© ?ìœ¨ ?œìŠ¤?œìž…?ˆë‹¤.
        </p>
        <p class="desc">
          ?¨ìˆœ??ëª¨ë¸??ë¶™ì´???°ì„œ ?ë‚˜ì§€ ?Šê³ , ROSA ?ì´?„íŠ¸ë¥??µí•´ ëª…ë ¹??ë¶„í•´?˜ê³ ,
          LOVON ?¼ë? êµ¬ì¡°ë¥?ì°¨ìš©??ë¡œë´‡ ë³¸ì²´ë³??˜ê²½ ì°¨ì´ë¥?ì¤„ì´ë©? LiDAR SLAMê³?YOLOë¥?          ?¨ê»˜ ?¬ìš©???¤í™˜ê²?ì£¼í–‰ ?ˆì •?±ì„ ?’ì??µë‹ˆ??
        </p>
      </div>
      <div class="text-panel">
        <h3>???˜ë?ê°€ ?ˆë‚˜</h3>
        <p>
          ê¸°ì¡´ VLA ëª¨ë¸?¤ì? ?€ì²´ë¡œ ?´ë¨¸?¸ì´?œê¸‰ ?œì ?´ë‚˜ ê³ í’ˆì§?ì¹´ë©”???˜ê²½???„ì œë¡?ë§Œë“¤?´ì ¸ ?ˆì–´,
          ?‘ì? ?¬ì¡± ë¡œë´‡ì²˜ëŸ¼ ë³¸ì²´ê°€ ?¤ë¥¸ ?˜ê²½??ê·¸ë?ë¡???¸°ë©??±ëŠ¥???¨ì–´ì§‘ë‹ˆ??
        </p>
        <p class="desc">
          ?°ë¦¬???´ëŸ¬??ë¡œë´‡ ë³¸ì²´ë³??˜ê²½ ì°¨ì´ë¥?ë³´ì •?˜ê¸° ?„í•´ LOVON êµ¬ì¡°ë¥?InternVLA?€
          ê²°í•©?˜ê³ , ROSA ?ì´?„íŠ¸ë¥??µí•´ ëª…ë ¹??ë¶„í•´?˜ëŠ” ë°©ì‹?¼ë¡œ ?œìŠ¤???ˆë²¨ ê°œì„ ???˜í–‰?ˆìŠµ?ˆë‹¤.
        </p>
      </div>
    </div>
  </section>

  <section class="section" id="features">
    <div class="section-head">
      <div>
        <h2>?µì‹¬ ê¸°ëŠ¥</h2>
        <p>?¨ì¼ task ?œì—°???„ë‹ˆ?? ??ê°€ì§€ ê¸°ëŠ¥???˜ë‚˜???Œì´?„ë¼?¸ìœ¼ë¡??µí•©??ê²ƒì´ ?µì‹¬?…ë‹ˆ??</p>
      </div>
    </div>

    <div class="feature-grid">
      <article class="feature">
        <img src="assets/images/feature-navigation.svg" alt="Navigation ê¸°ëŠ¥ ?´ë?ì§€">
        <div class="body">
          <h3>Navigation</h3>
          <p>?ì—°??ëª…ë ¹??ë°›ì•„ ?˜ê²½ ??ëª©í‘œ ì§€?ê¹Œì§€ ?ìœ¨ ì£¼í–‰?©ë‹ˆ?? InternVLA-N1-DualVLN??ì¹´ë©”???´ë?ì§€?€ ëª…ë ¹???™ì‹œ???´ì„??pixel goal??ì¶œë ¥?˜ë©´, ë¡œë´‡??ê·¸ì— ë§žì¶° ?´ë™?©ë‹ˆ??</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-pointing.svg" alt="Pointing ê¸°ëŠ¥ ?´ë?ì§€">
        <div class="body">
          <h3>Pointing</h3>
          <p>?´ë?ì§€ ???¹ì • ê°ì²´ë¥?ì§€?œí•˜ë©?ë¡œë´‡???´ë‹¹ ê°ì²´ë¡??¥í•©?ˆë‹¤. ê°ì²´ ì§€???•ë³´ë¥?pixel goalë¡?ë³€?˜í•´ InternVLA???„ë‹¬?˜ëŠ” ë°©ì‹?…ë‹ˆ??</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-following.svg" alt="Following ê¸°ëŠ¥ ?´ë?ì§€">
        <div class="body">
          <h3>Following</h3>
          <p>?¬ëžŒ?´ë‚˜ ë¬¼ì²´ë¥?ì§€?ì ?¼ë¡œ ì¶”ì¢…?©ë‹ˆ?? YOLO ê°ì²´ ê²€ì¶?ê²°ê³¼ë¥?pixel goal ?…ë ¥?¼ë¡œ ?¬ìš©?˜ë©°, LOVON???¼ë? êµ¬ì¡°ë¥?ì°¨ìš©??ëª¨ì…˜ ë¸”ëŸ¬?€ ?€??ì¶”ì¢… ?˜ê²½?ì„œ???ˆì •?ìœ¼ë¡??™ìž‘?˜ë„ë¡?ê°œì„ ?ˆìŠµ?ˆë‹¤.</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-backtracking.svg" alt="Backtracking ê¸°ëŠ¥ ?´ë?ì§€">
        <div class="body">
          <h3>Backtracking</h3>
          <p>LiDAR SLAM ê¸°ë°˜ closed-loop ?œì–´ë¡?ê³¼ê±°??ì§€?˜ì˜¨ ê²½ë¡œë¥??ë™?¼ë¡œ ?˜ì§š???Œì•„?µë‹ˆ?? ?¤ë‚´ ?ìœ¨ì£¼í–‰?ì„œ ?ˆì •?±ì„ ?’ì´???µì‹¬ ê¸°ëŠ¥?…ë‹ˆ??</p>
        </div>
      </article>
    </div>
  </section>

  <section class="section" id="architecture">
    <div class="section-head">
      <div>
        <h2>?œìŠ¤???„í‚¤?ì²˜</h2>
        <p>?¤ì œ ?„í‚¤?ì²˜ ?´ë?ì§€ë¥??˜ì¤‘??êµì²´?????ˆë„ë¡??„ì‹œ ?ë¦¬ë¥?ë§ˆë ¨?ˆìŠµ?ˆë‹¤. ?¤ë¥¸ìª??¤ëª…?€ ë³??„ë¡œ?íŠ¸??ì£¼ìš” ëª¨ë“ˆ???”ì•½???´ìš©?…ë‹ˆ??</p>
      </div>
    </div>

    <div class="architecture-layout">
      <div class="arch-card">
        <img src="assets/images/architecture-placeholder.svg" alt="?œìŠ¤???„í‚¤?ì²˜ ?„ì‹œ ?´ë?ì§€">
      </div>
      <div class="arch-notes">
        <div class="note">
          <strong>ë² ì´??ëª¨ë¸: InternVLA-N1-DualVLN</strong>
          <span>System1(?€?˜ì? ?œì–´) + System2(ê³ ìˆ˜ì¤€ ?˜ì‚¬ê²°ì •)??dual-system êµ¬ì¡°ë¥?ê°€ì§?VLA foundation model???œìš©?©ë‹ˆ??</span>
        </div>
        <div class="note">
          <strong>LOVON ë¶€ë¶?ê²°í•©</strong>
          <span>LOVON ëª¨ë¸ ?„ì²´ë¥?ê·¸ë?ë¡??°ì? ?Šê³ , êµ¬ì¡°?€ ëª¨ë¸ ?¼ë?ë¥?ì°¨ìš©??InternVLA ?´ë???ê²°í•©?ˆìŠµ?ˆë‹¤.</span>
        </div>
        <div class="note">
          <strong>ë³´ì¡° ëª¨ë“ˆ</strong>
          <span>LiDAR SLAM Runner, ROSA Agent + Qwen3.5-4B, YOLO ?…ë ¥?¨ì„ ?¨ê»˜ ?°ê²°??4ê°€ì§€ ?œìŠ¤?¬ë? ?˜ë‚˜???ë¦„?¼ë¡œ ë§Œë“­?ˆë‹¤.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>?œìŠ¤??êµ¬ì„± ?”ì†Œ</h2>
        <p>?Œê°œ ?˜ì´ì§€?ì„œ ê°€??ê¸¸ê³  ?±ë”±?´ì?ê¸??¬ìš´ ë¶€ë¶„ì´?? ì¹´ë“œë¡??˜ëˆ ???µì‹¬ë§?ë³´ì´ê²??•ë¦¬?ˆìŠµ?ˆë‹¤.</p>
      </div>
    </div>

    <div class="impact-grid">
      <div class="text-panel">
        <h3>ë² ì´??ëª¨ë¸</h3>
        <p>InternVLA-N1-DualVLN?€ System1ê³?System2ë¥?ê²°í•©??dual-system VLA foundation model?´ë©°, ë³??„ë¡œ?íŠ¸??ì£¼ëœ ì¶”ë¡  ?”ì§„?…ë‹ˆ??</p>
      </div>
      <div class="text-panel">
        <h3>?‰ë™ ë¶„í•´</h3>
        <p>ROSA Agent???ì—°??ëª…ë ¹??tool ?¨ìœ„ë¡?ë¶„í•´??Navigation, Pointing, Following, Backtracking ì¤??„ìš”??ê¸°ëŠ¥???¸ì¶œ?©ë‹ˆ??</p>
      </div>
      <div class="text-panel">
        <h3>?œê° ?…ë ¥</h3>
        <p>YOLO ê²°ê³¼ë¥?pixel goal ?•íƒœë¡?ì£¼ìž…?? VLAë¥??„ì²´ ?¬í•™?µí•˜ì§€ ?Šì•„???ˆë¡œ??taskë¥?ì¶”ê??????ˆë„ë¡??¤ê³„?ˆìŠµ?ˆë‹¤.</p>
      </div>
    </div>
  </section>

  <section class="section" id="equipment">
    <div class="section-head">
      <div>
        <h2>?¬ìš© ?¥ë¹„?€ ëª¨ë¸</h2>
        <p>?˜ë“œ?¨ì–´, ëª¨ë¸, ?„ë ˆ?„ì›Œ?¬ë? ???”ë©´??ë¬¶ì–´ ë³´ì—¬ì£¼ë©´ ìº¡ìŠ¤???Œê°œ ?˜ì´ì§€???¤ë“?¥ì´ ??ì¢‹ì•„ì§‘ë‹ˆ??</p>
      </div>
    </div>

    <div class="device-grid">
      <article class="device">
        <img src="image/go2.jpg" alt="Unitree Go2 ?¬ì§„">
        <div class="body">
          <h3>Unitree Go2</h3>
          <p>ì£¼í–‰ ?Œëž«?¼ìœ¼ë¡??¬ìš©?˜ëŠ” 4ì¡?ë³´í–‰ ë¡œë´‡?…ë‹ˆ?? ?´ìž¥ Jetson Orinê³??´ìž¥ LiDARë¥??œìš©???¤í™˜ê²??ìœ¨ ì£¼í–‰???˜í–‰?©ë‹ˆ??</p>
        </div>
      </article>

      <article class="device">
        <img src="assets/images/realsense-d435-placeholder.svg" alt="Intel RealSense D435 ?„ì‹œ ?´ë?ì§€">
        <div class="body">
          <h3>Intel RealSense D435</h3>
          <p>RGB-D ?…ë ¥???„í•œ ì¹´ë©”?¼ìž…?ˆë‹¤. ê°ì²´ ?¸ì‹, ê±°ë¦¬ ì¶”ì •, ?œê° ?•ë³´ ?˜ì§‘, ?”ë¸”?¬ë§ ?Œì´?„ë¼?¸ì— ?œìš©?©ë‹ˆ??</p>
        </div>
      </article>

      <article class="device">
        <img src="assets/images/lidar-placeholder.svg" alt="LiDAR ?„ì‹œ ?´ë?ì§€">
        <div class="body">
          <h3>LiDAR / SLAM</h3>
          <p>?¤ì‹œê°?SLAM ê¸°ë°˜ closed-loop ?œì–´ë¥??µí•´ ê³¼ê±° ê²½ë¡œë¥?ë³µì›?˜ê³ , ?ìœ¨ Backtracking ê¸°ëŠ¥???ˆì •?ìœ¼ë¡??˜í–‰?©ë‹ˆ??</p>
        </div>
      </article>
    </div>
  </section>

    <section class="section" id="team">
    <div class="section-head">
      <div>
        <h2>ÆÀ ±¸¼º°ú ¿ªÇÒ</h2>
        <p>ÆÀ¿ø »çÁø°ú GitHub ¸µÅ©¸¸ ¸ÕÀú µÎ°í, ¿ªÇÒÀº ÀÏ´Ü ºñ¿ö µÐ »óÅÂÀÔ´Ï´Ù. ³ªÁß¿¡ ¿øÇÏ´Â ¿ªÇÒ¸íÀ¸·Î ¹Ù·Î Ã¤¿ï ¼ö ÀÖ½À´Ï´Ù.</p>
      </div>
    </div>

    <div class="team-grid">
      <article class="member">
        <img src="assets/images/avatar-1.svg" alt="ÆÀ¿ø 1 ÇÁ·ÎÇÊ »çÁø">
        <div class="body">
          <h3>ÀÓ¹Î¼®</h3>
          <span class="role"></span>
          <p>ÀüÃ¼ ÀÏÁ¤ °ü¸®, ¹ßÇ¥ ±¸¼º, ½Ã½ºÅÛ ÅëÇÕ, ÃÖÁ¾ Á¤¸®¸¦ ´ã´çÇÕ´Ï´Ù.</p>
          <a class="link" href="https://github.com/your-github-id-1" target="_blank" rel="noreferrer">GitHub ¿¬µ¿</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-2.svg" alt="ÆÀ¿ø 2 ÇÁ·ÎÇÊ »çÁø">
        <div class="body">
          <h3>Á¶¿ø¿µ</h3>
          <span class="role"></span>
          <p>Go2 Á¦¾î, ÁÖÇà ·ÎÁ÷, ¼¾¼­ ¿¬°á ¹× ½Ç±â±â Å×½ºÆ®¸¦ ´ã´çÇÕ´Ï´Ù.</p>
          <a class="link" href="https://github.com/your-github-id-2" target="_blank" rel="noreferrer">GitHub ¿¬µ¿</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-3.svg" alt="ÆÀ¿ø 3 ÇÁ·ÎÇÊ »çÁø">
        <div class="body">
          <h3>Á¤À¯Áø</h3>
          <span class="role"></span>
          <p>VLA ¸ðµ¨ Àû¿ë, ÇÁ·ÒÇÁÆ® ¼³°è, °´Ã¼ ÀÎ½Ä ¹× Çàµ¿ »ý¼º ÆÄÆ®¸¦ ¸Ã½À´Ï´Ù.</p>
          <a class="link" href="https://github.com/your-github-id-3" target="_blank" rel="noreferrer">GitHub ¿¬µ¿</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-4.svg" alt="ÆÀ¿ø 4 ÇÁ·ÎÇÊ »çÁø">
        <div class="body">
          <h3>¼ºÀç½Â</h3>
          <span class="role"></span>
          <p>LiDAR SLAM, °æ·Î º¹¿ø, ÀÚÀ² Backtracking ¸ðµâÀ» ´ã´çÇÕ´Ï´Ù.</p>
          <a class="link" href="https://github.com/your-github-id-4" target="_blank" rel="noreferrer">GitHub ¿¬µ¿</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-1.svg" alt="ÆÀ¿ø 5 ÇÁ·ÎÇÊ »çÁø">
        <div class="body">
          <h3>À¯¸®¾È</h3>
          <span class="role"></span>
          <p>ROSA Agent¿Í Qwen3.5-4B ¿¬µ¿, tool ºÐÇØ, ÀÚ¿¬¾î ÀÎÅÍÆäÀÌ½º¸¦ ´ã´çÇÕ´Ï´Ù.</p>
          <a class="link" href="https://github.com/your-github-id-5" target="_blank" rel="noreferrer">GitHub ¿¬µ¿</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-2.svg" alt="ÆÀ¿ø 6 ÇÁ·ÎÇÊ »çÁø">
        <div class="body">
          <h3>Á¶À¯ºó</h3>
          <span class="role"></span>
          <p>¹ßÇ¥ ÀÚ·á, ÆäÀÌÁö µðÀÚÀÎ, ¹®¼­ Á¤¸®¿Í ÀÚ·á ¾ÆÄ«ÀÌºùÀ» ´ã´çÇÕ´Ï´Ù.</p>
          <a class="link" href="https://github.com/your-github-id-6" target="_blank" rel="noreferrer">GitHub ¿¬µ¿</a>
        </div>
      </article>
    </div>

    <div class="footer-note">
      ÆÀ¿øÀÌ ´õ ´Ã¾î³ª¸é Ä«µå¸¸ º¹Á¦ÇÏ¸é µË´Ï´Ù. °¢ Ä«µåÀÇ GitHub ¸µÅ©´Â °³ÀÎ °èÁ¤¿¡ ¸Â°Ô ¹Ù²Ù¸é ¹Ù·Î ¿¬µ¿µË´Ï´Ù.
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>ì§„í–‰ ?€?„ë¼??/h2>
        <p>?ë³¸ ?˜ì´ì§€???ˆë˜ ?”ë³„ ì§„í–‰ ?´ì—­??ì¡°ê¸ˆ ??ë³´ê¸° ì¢‹ê²Œ ?•ë¦¬?ˆìŠµ?ˆë‹¤.</p>
      </div>
    </div>

    <div class="timeline-grid">
      <div class="text-panel">
        <span class="timeline-month">3??/span>
        <h3>?˜ê²½ êµ¬ì¶• ë°?ë² ì´?¤ë¼???ìƒ‰</h3>
        <p class="desc">?„ë¡œ?íŠ¸ ë°©í–¥??ê²°ì •, ROS2/Zenoh ë¬´ì„  ?µì‹  ?‹ì—…, InternVLAÂ·LOVON ?¬í˜„, 1ì°??œì—° ë°œí‘œë¥?ì§„í–‰?ˆìŠµ?ˆë‹¤.</p>
      </div>
      <div class="text-panel">
        <span class="timeline-month">4??/span>
        <h3>?µì‹¬ ê¸°ëŠ¥ êµ¬í˜„</h3>
        <p class="desc">InternVLA??Following??ê²°í•©?˜ëŠ” ë°©í–¥?±ì„ ?•ì •?˜ê³ , LOVON ?¼ë? êµ¬ì¡° ì°¨ìš©, ?”ë¸”?¬ë§, LiDAR SLAM ê¸°ë°˜ ?ìœ¨ Backtracking??êµ¬í˜„?ˆìŠµ?ˆë‹¤.</p>
      </div>
      <div class="text-panel">
        <span class="timeline-month">5??/span>
        <h3>?µí•©Â·?‰ê?Â·?¼ë¬¸??/h3>
        <p class="desc">Pointing ê¸°ëŠ¥ ì¶”ê?, ?„ì²´ ì½”ë“œ ë³‘í•©, ROSA??Qwen3.5-4B ?°ê²°, ROS2 ?„êµ¬ ê°œì„ , Task Planner ?µí•© ???•ëŸ‰ ?‰ê??€ ?¼ë¬¸ ì´ˆì•ˆ ?‘ì„±???¤ì–´ê°”ìŠµ?ˆë‹¤.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>ê¸°ìˆ  ?¤íƒ</h2>
        <p>?´ìš©??ë§Žì•„ ë³´ì—¬???¤ì œë¡œëŠ” ?˜ë“œ?¨ì–´, ëª¨ë¸, ?Œí”„?¸ì›¨?? ë¯¸ë“¤?¨ì–´, ?œë??ˆì´???•ë„ë¡?ë¬¶ì–´??ë³´ë©´ ?´í•´ê°€ ?½ìŠµ?ˆë‹¤.</p>
      </div>
    </div>

    <div class="stack-grid">
      <div class="text-panel">
        <h3>?˜ë“œ?¨ì–´</h3>
        <ul>
          <li>Unitree Go2: 4ì¡?ë³´í–‰ ë¡œë´‡, ?´ìž¥ Jetson Orin / ?´ìž¥ LiDAR</li>
          <li>Intel RealSense D435: RGB-D ì¹´ë©”??/li>
          <li>RTX 3090: ?™ìŠµ ë°?ì¶”ë¡ ??GPU</li>
        </ul>
      </div>
      <div class="text-panel">
        <h3>ëª¨ë¸Â·AI</h3>
        <ul>
          <li>InternVLA-N1-DualVLN: ë©”ì¸ VLA</li>
          <li>LOVON: ?¼ë? êµ¬ì¡° ì°¨ìš©</li>
          <li>Qwen3.5-4B: ROSA agent??LLM</li>
          <li>YOLO: ê°ì²´ ê²€ì¶?/li>
        </ul>
      </div>
      <div class="text-panel">
        <h3>?Œí”„?¸ì›¨??/h3>
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
        <h2>?„ë¡œ?íŠ¸???˜ì˜</h2>
        <p>?ëž˜ ë¬¸ì„œ???¤ìª½???ˆë˜ ?¼ë¬¸???¤ëª…???Œê°œ ?˜ì´ì§€ ?¤ìœ¼ë¡??¤ì‹œ ?•ë¦¬?ˆìŠµ?ˆë‹¤.</p>
      </div>
    </div>

    <div class="impact-grid">
      <div class="text-panel">
        <h3>1. ?Œí˜• ?¬ì¡± ë¡œë´‡ ?˜ê²½???€???ì‘</h3>
        <p>?€ê·œëª¨ ?œë??ˆì´???°ì´?°ë¡œ ?™ìŠµ??VLA ëª¨ë¸?€ ?€ì²´ë¡œ ?´ë¨¸?¸ì´?œê¸‰ ?œì ?´ë‚˜ ê³ í’ˆì§?RGB-D ?˜ê²½??ê°€?•í•©?ˆë‹¤. ë³??„ë¡œ?íŠ¸??LOVON???µì‹¬ ëª¨ë“ˆ??InternVLA-N1-DualVLN ?´ë???? íƒ?ìœ¼ë¡??µí•©?? ?Œí˜• ?¬ì¡± ë¡œë´‡ ë³¸ì²´???ì‘?˜ëŠ” ?¤ìš©??ê²½ë¡œë¥??œì‹œ?ˆìŠµ?ˆë‹¤.</p>
      </div>
      <div class="text-panel">
        <h3>2. ?¨ì¼ taskë¥??˜ì–´??ë©€?°íƒœ?¤í¬ ?µí•©</h3>
        <p>Navigation, Pointing, Following, Backtracking 4ì¢?taskë¥?ROSA ê¸°ë°˜ LLM ?ì´?„íŠ¸ ?„ì— ?˜ë‚˜???Œì´?„ë¼?¸ìœ¼ë¡?ë¬¶ì—ˆ?µë‹ˆ?? ?´ë? ?µí•´ foundation model???¤ì œ task?ì„œ ?´ë–»ê²??•ìž¥?????ˆëŠ”ì§€ ë³´ì—¬ì¤ë‹ˆ??</p>
      </div>
      <div class="text-panel">
        <h3>3. ?ìœ¨ ë¡œë´‡ ?œìŠ¤?œì˜ ?¸í„°?˜ì´??/h3>
        <p>Go2 Monitor ?¸í„°?˜ì´?¤ì? Zenoh-bridge ê¸°ë°˜ ë¬´ì„  ROS2 ?µì‹ ??ê²°í•©?? ?„ìž¥ ?°ê²°ë§Œìœ¼ë¡?ë¡œë´‡ ?íƒœë¥??•ì¸?˜ê³  ëª…ë ¹???„ì†¡Â·?¤í–‰?????ˆëŠ” êµ¬ì¡°ë¥?ë§Œë“¤?ˆìŠµ?ˆë‹¤. ?´ëŠ” HRI ê´€?ì—?œë„ ì¤‘ìš”??ê¸°ë°˜???©ë‹ˆ??</p>
      </div>
    </div>
  </section>

  <section class="section references">
    <div class="section-head">
      <div>
        <h2>ì°¸ê³  ë¬¸í—Œ</h2>
        <p>?µì‹¬ ?¼ë¬¸ê³?ê¸°ìˆ  ë¬¸ì„œ???„ëž˜ì²˜ëŸ¼ ì§§ê²Œ ?•ë¦¬???ë©´ ?Œê°œ ?˜ì´ì§€ê°€ ??ë¬´ê±°??ë³´ìž…?ˆë‹¤.</p>
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


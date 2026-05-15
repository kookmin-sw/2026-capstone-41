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
    display: flex;
    flex-wrap: nowrap;
    gap: 12px;
    overflow-x: auto;
    padding-bottom: 10px;
    scrollbar-width: thin;
  }

    .member {
    border-radius: 24px;
    overflow: hidden;
    border: 1px solid var(--line);
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(248,250,252,0.96));
    display: grid;
    min-height: 100%;
    flex: 0 0 calc((100% - 60px) / 6);
    min-width: 180px;
  }

  .member img {
    width: 100%;
    display: block;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-bottom: 1px solid var(--line);
  }

    .member .body {
    padding: 14px;
    display: grid;
    gap: 8px;
  }

    .member h3 {
    margin: 0;
    font-size: 1rem;
  }

    .member .role {
    display: block;
    height: 0;
    margin: 0;
    padding: 0;
    border: 0;
    background: transparent;
    overflow: hidden;
  }

    .member p {
    margin: 0;
    color: var(--muted);
    line-height: 1.55;
    font-size: 0.84rem;
  }

    .member .link {
    margin-top: 2px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 8px 10px;
    border-radius: 12px;
    border: 1px solid var(--line);
    background: #fff;
    color: var(--text);
    text-decoration: none;
    font-weight: 700;
    font-size: 0.85rem;
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
      <span class="eyebrow">Capstone Project 41 쨌 Vision-Language-Action Robotics</span>
      <h1>VLA 湲곕컲 ?ъ” 濡쒕큸<br>?듯빀 ?먯쑉 ?쒖뒪??/h1>
      <p class="lead">
        蹂??꾨줈?앺듃??<strong>Unitree Go2</strong> ?ъ” 蹂댄뻾 濡쒕큸??理쒖떊 Vision-Language-Action
        紐⑤뜽??<strong>InternVLA-N1-DualVLN</strong>???댁떇?? ?먯뿰??紐낅졊留뚯쑝濡?濡쒕큸??        ?쒓컖 ?뺣낫瑜??댁꽍?섍퀬 ?ㅼ젣 ?섍꼍?먯꽌 ?먯쑉 二쇳뻾?섎룄濡?留뚮뱶??寃껋쓣 紐⑺몴濡??⑸땲??
        湲곗〈 VLA 紐⑤뜽???섍꼍 ?몄감瑜?蹂댁셿?섍린 ?꾪빐 LOVON, ROSA, LiDAR SLAM, YOLO瑜??④퍡
        ??뼱 ?섎굹???듯빀 ?뚯씠?꾨씪?몄쑝濡?援ъ꽦?덉뒿?덈떎.
      </p>

      <div class="hero-actions">
        <a class="btn btn-primary" href="#overview">?꾨줈?앺듃 媛쒖슂</a>
        <a class="btn btn-secondary" href="#architecture">?쒖뒪???꾪궎?띿쿂</a>
      </div>

      <div class="stats-grid">
        <div class="stat">
          <span class="num">4</span>
          <span class="label">?듭떖 ?쒖뒪??br>Navigation, Pointing, Following, Backtracking</span>
        </div>
        <div class="stat">
          <span class="num">1</span>
          <span class="label">怨듯넻 VLA 湲곕컲<br>?щ윭 ?쒖뒪?щ? ?⑥씪 ?뚯씠?꾨씪?몄쑝濡??곌껐</span>
        </div>
        <div class="stat">
          <span class="num">3+</span>
          <span class="label">二쇱슂 ?섎뱶?⑥뼱<br>Go2, D435, LiDAR ??/span>
        </div>
        <div class="stat">
          <span class="num">100%</span>
          <span class="label">援먯껜 媛??援ъ“<br>?대?吏, 留곹겕, ??븷???쎄쾶 ?낅뜲?댄듃</span>
        </div>
      </div>
    </div>

    <div class="hero-stack">
      <div class="hero-card">
        <img src="image/go2.jpg" alt="Unitree Go2 ?ъ쭊">
      </div>
      <div class="hero-mini-grid">
        <div class="mini">
          <strong>???꾩슂?쒓?</strong>
          <span>?대㉧?몄씠?쒕굹 怨좎젙??移대찓???섍꼍??留욎떠吏?VLA 紐⑤뜽???ъ” 濡쒕큸??洹몃?濡??곕㈃ ?깅뒫???⑥뼱吏묐땲??</span>
        </div>
        <div class="mini">
          <strong>?대뼸寃??닿껐?섎굹</strong>
          <span>LOVON 援ъ“ ?쇰?? ROSA ?먯씠?꾪듃瑜?寃고빀???섍꼍 ?몄감瑜?以꾩씠怨?task 遺꾪빐瑜??덉젙?뷀빀?덈떎.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="overview">
    <div class="section-head">
      <div>
        <h2>?꾨줈?앺듃 媛쒖슂</h2>
        <p>?먮옒 ?뚭컻 ?섏씠吏???듭떖 ?댁슜?????쎄린 ?쎄쾶 ?뺣━??踰꾩쟾?낅땲?? 湲??ㅻ챸? 臾몃떒?쇰줈, ?듭떖 ?ъ씤?몃뒗 移대뱶濡??섎댋?듬땲??</p>
      </div>
    </div>

    <div class="overview-grid">
      <div class="text-panel">
        <h3>臾댁뾿??留뚮뱾?덈굹</h3>
        <p>
          蹂??꾨줈?앺듃??Unitree Go2 ?ъ” 蹂댄뻾 濡쒕큸??理쒖떊 VLA 紐⑤뜽??InternVLA-N1-DualVLN??          ?댁떇?섏뿬, ?щ엺??留먰븯???먯뿰??紐낅졊留뚯쑝濡?濡쒕큸???쒓컖 ?뺣낫瑜??댁꽍?섍퀬 ?ㅼ젣 ?섍꼍??          ?먯쑉 二쇳뻾?섎룄濡?援ы쁽???듯빀 ?먯쑉 ?쒖뒪?쒖엯?덈떎.
        </p>
        <p class="desc">
          ?⑥닚??紐⑤뜽??遺숈씠???곗꽌 ?앸굹吏 ?딄퀬, ROSA ?먯씠?꾪듃瑜??듯빐 紐낅졊??遺꾪빐?섍퀬,
          LOVON ?쇰? 援ъ“瑜?李⑥슜??濡쒕큸 蹂몄껜蹂??섍꼍 李⑥씠瑜?以꾩씠硫? LiDAR SLAM怨?YOLO瑜?          ?④퍡 ?ъ슜???ㅽ솚寃?二쇳뻾 ?덉젙?깆쓣 ?믪??듬땲??
        </p>
      </div>
      <div class="text-panel">
        <h3>???섎?媛 ?덈굹</h3>
        <p>
          湲곗〈 VLA 紐⑤뜽?ㅼ? ?泥대줈 ?대㉧?몄씠?쒓툒 ?쒖젏?대굹 怨좏뭹吏?移대찓???섍꼍???꾩젣濡?留뚮뱾?댁졇 ?덉뼱,
          ?묒? ?ъ” 濡쒕큸泥섎읆 蹂몄껜媛 ?ㅻⅨ ?섍꼍??洹몃?濡???린硫??깅뒫???⑥뼱吏묐땲??
        </p>
        <p class="desc">
          ?곕━???대윭??濡쒕큸 蹂몄껜蹂??섍꼍 李⑥씠瑜?蹂댁젙?섍린 ?꾪빐 LOVON 援ъ“瑜?InternVLA?
          寃고빀?섍퀬, ROSA ?먯씠?꾪듃瑜??듯빐 紐낅졊??遺꾪빐?섎뒗 諛⑹떇?쇰줈 ?쒖뒪???덈꺼 媛쒖꽑???섑뻾?덉뒿?덈떎.
        </p>
      </div>
    </div>
  </section>

  <section class="section" id="features">
    <div class="section-head">
      <div>
        <h2>?듭떖 湲곕뒫</h2>
        <p>?⑥씪 task ?쒖뿰???꾨땲?? ??媛吏 湲곕뒫???섎굹???뚯씠?꾨씪?몄쑝濡??듯빀??寃껋씠 ?듭떖?낅땲??</p>
      </div>
    </div>

    <div class="feature-grid">
      <article class="feature">
        <img src="assets/images/feature-navigation.svg" alt="Navigation 湲곕뒫 ?대?吏">
        <div class="body">
          <h3>Navigation</h3>
          <p>?먯뿰??紐낅졊??諛쏆븘 ?섍꼍 ??紐⑺몴 吏?먭퉴吏 ?먯쑉 二쇳뻾?⑸땲?? InternVLA-N1-DualVLN??移대찓???대?吏? 紐낅졊???숈떆???댁꽍??pixel goal??異쒕젰?섎㈃, 濡쒕큸??洹몄뿉 留욎떠 ?대룞?⑸땲??</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-pointing.svg" alt="Pointing 湲곕뒫 ?대?吏">
        <div class="body">
          <h3>Pointing</h3>
          <p>?대?吏 ???뱀젙 媛앹껜瑜?吏?쒗븯硫?濡쒕큸???대떦 媛앹껜濡??ν빀?덈떎. 媛앹껜 吏???뺣낫瑜?pixel goal濡?蹂?섑빐 InternVLA???꾨떖?섎뒗 諛⑹떇?낅땲??</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-following.svg" alt="Following 湲곕뒫 ?대?吏">
        <div class="body">
          <h3>Following</h3>
          <p>?щ엺?대굹 臾쇱껜瑜?吏?띿쟻?쇰줈 異붿쥌?⑸땲?? YOLO 媛앹껜 寃異?寃곌낵瑜?pixel goal ?낅젰?쇰줈 ?ъ슜?섎ŉ, LOVON???쇰? 援ъ“瑜?李⑥슜??紐⑥뀡 釉붾윭? ???異붿쥌 ?섍꼍?먯꽌???덉젙?곸쑝濡??숈옉?섎룄濡?媛쒖꽑?덉뒿?덈떎.</p>
        </div>
      </article>
      <article class="feature">
        <img src="assets/images/feature-backtracking.svg" alt="Backtracking 湲곕뒫 ?대?吏">
        <div class="body">
          <h3>Backtracking</h3>
          <p>LiDAR SLAM 湲곕컲 closed-loop ?쒖뼱濡?怨쇨굅??吏?섏삩 寃쎈줈瑜??먮룞?쇰줈 ?섏쭦???뚯븘?듬땲?? ?ㅻ궡 ?먯쑉二쇳뻾?먯꽌 ?덉젙?깆쓣 ?믪씠???듭떖 湲곕뒫?낅땲??</p>
        </div>
      </article>
    </div>
  </section>

  <section class="section" id="architecture">
    <div class="section-head">
      <div>
        <h2>?쒖뒪???꾪궎?띿쿂</h2>
        <p>?ㅼ젣 ?꾪궎?띿쿂 ?대?吏瑜??섏쨷??援먯껜?????덈룄濡??꾩떆 ?먮━瑜?留덈젴?덉뒿?덈떎. ?ㅻⅨ履??ㅻ챸? 蹂??꾨줈?앺듃??二쇱슂 紐⑤뱢???붿빟???댁슜?낅땲??</p>
      </div>
    </div>

    <div class="architecture-layout">
      <div class="arch-card">
        <img src="assets/images/architecture-placeholder.svg" alt="?쒖뒪???꾪궎?띿쿂 ?꾩떆 ?대?吏">
      </div>
      <div class="arch-notes">
        <div class="note">
          <strong>踰좎씠??紐⑤뜽: InternVLA-N1-DualVLN</strong>
          <span>System1(??섏? ?쒖뼱) + System2(怨좎닔以 ?섏궗寃곗젙)??dual-system 援ъ“瑜?媛吏?VLA foundation model???쒖슜?⑸땲??</span>
        </div>
        <div class="note">
          <strong>LOVON 遺遺?寃고빀</strong>
          <span>LOVON 紐⑤뜽 ?꾩껜瑜?洹몃?濡??곗? ?딄퀬, 援ъ“? 紐⑤뜽 ?쇰?瑜?李⑥슜??InternVLA ?대???寃고빀?덉뒿?덈떎.</span>
        </div>
        <div class="note">
          <strong>蹂댁“ 紐⑤뱢</strong>
          <span>LiDAR SLAM Runner, ROSA Agent + Qwen3.5-4B, YOLO ?낅젰?⑥쓣 ?④퍡 ?곌껐??4媛吏 ?쒖뒪?щ? ?섎굹???먮쫫?쇰줈 留뚮벊?덈떎.</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>?쒖뒪??援ъ꽦 ?붿냼</h2>
        <p>?뚭컻 ?섏씠吏?먯꽌 媛??湲멸퀬 ?깅뵳?댁?湲??ъ슫 遺遺꾩씠?? 移대뱶濡??섎닠???듭떖留?蹂댁씠寃??뺣━?덉뒿?덈떎.</p>
      </div>
    </div>

    <div class="impact-grid">
      <div class="text-panel">
        <h3>踰좎씠??紐⑤뜽</h3>
        <p>InternVLA-N1-DualVLN? System1怨?System2瑜?寃고빀??dual-system VLA foundation model?대ŉ, 蹂??꾨줈?앺듃??二쇰맂 異붾줎 ?붿쭊?낅땲??</p>
      </div>
      <div class="text-panel">
        <h3>?됰룞 遺꾪빐</h3>
        <p>ROSA Agent???먯뿰??紐낅졊??tool ?⑥쐞濡?遺꾪빐??Navigation, Pointing, Following, Backtracking 以??꾩슂??湲곕뒫???몄텧?⑸땲??</p>
      </div>
      <div class="text-panel">
        <h3>?쒓컖 ?낅젰</h3>
        <p>YOLO 寃곌낵瑜?pixel goal ?뺥깭濡?二쇱엯?? VLA瑜??꾩껜 ?ы븰?듯븯吏 ?딆븘???덈줈??task瑜?異붽??????덈룄濡??ㅺ퀎?덉뒿?덈떎.</p>
      </div>
    </div>
  </section>

  <section class="section" id="equipment">
    <div class="section-head">
      <div>
        <h2>?ъ슜 ?λ퉬? 紐⑤뜽</h2>
        <p>?섎뱶?⑥뼱, 紐⑤뜽, ?꾨젅?꾩썙?щ? ???붾㈃??臾띠뼱 蹂댁뿬二쇰㈃ 罹≪뒪???뚭컻 ?섏씠吏???ㅻ뱷?μ씠 ??醫뗭븘吏묐땲??</p>
      </div>
    </div>

    <div class="device-grid">
      <article class="device">
        <img src="image/go2.jpg" alt="Unitree Go2 ?ъ쭊">
        <div class="body">
          <h3>Unitree Go2</h3>
          <p>二쇳뻾 ?뚮옯?쇱쑝濡??ъ슜?섎뒗 4議?蹂댄뻾 濡쒕큸?낅땲?? ?댁옣 Jetson Orin怨??댁옣 LiDAR瑜??쒖슜???ㅽ솚寃??먯쑉 二쇳뻾???섑뻾?⑸땲??</p>
        </div>
      </article>

      <article class="device">
        <img src="assets/images/realsense-d435-placeholder.svg" alt="Intel RealSense D435 ?꾩떆 ?대?吏">
        <div class="body">
          <h3>Intel RealSense D435</h3>
          <p>RGB-D ?낅젰???꾪븳 移대찓?쇱엯?덈떎. 媛앹껜 ?몄떇, 嫄곕━ 異붿젙, ?쒓컖 ?뺣낫 ?섏쭛, ?붾툝?щ쭅 ?뚯씠?꾨씪?몄뿉 ?쒖슜?⑸땲??</p>
        </div>
      </article>

      <article class="device">
        <img src="assets/images/lidar-placeholder.svg" alt="LiDAR ?꾩떆 ?대?吏">
        <div class="body">
          <h3>LiDAR / SLAM</h3>
          <p>?ㅼ떆媛?SLAM 湲곕컲 closed-loop ?쒖뼱瑜??듯빐 怨쇨굅 寃쎈줈瑜?蹂듭썝?섍퀬, ?먯쑉 Backtracking 湲곕뒫???덉젙?곸쑝濡??섑뻾?⑸땲??</p>
        </div>
      </article>
    </div>
  </section>

    <section class="section" id="team">
    <div class="section-head">
      <div>
        <h2>팀 구성과 역할</h2>
        <p>팀원 사진과 GitHub 링크만 먼저 두고, 역할은 일단 비워 둔 상태입니다. 나중에 원하는 역할명으로 바로 채울 수 있습니다.</p>
      </div>
    </div>

    <div class="team-grid">
      <article class="member">
        <img src="assets/images/avatar-1.svg" alt="팀원 1 프로필 사진">
        <div class="body">
          <h3>임민석</h3>
          <span class="role"></span>
          <p>전체 일정 관리, 발표 구성, 시스템 통합, 최종 정리를 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-1" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-2.svg" alt="팀원 2 프로필 사진">
        <div class="body">
          <h3>조원영</h3>
          <span class="role"></span>
          <p>Go2 제어, 주행 로직, 센서 연결 및 실기기 테스트를 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-2" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-3.svg" alt="팀원 3 프로필 사진">
        <div class="body">
          <h3>정유진</h3>
          <span class="role"></span>
          <p>VLA 모델 적용, 프롬프트 설계, 객체 인식 및 행동 생성 파트를 맡습니다.</p>
          <a class="link" href="https://github.com/your-github-id-3" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-4.svg" alt="팀원 4 프로필 사진">
        <div class="body">
          <h3>성재승</h3>
          <span class="role"></span>
          <p>LiDAR SLAM, 경로 복원, 자율 Backtracking 모듈을 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-4" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-1.svg" alt="팀원 5 프로필 사진">
        <div class="body">
          <h3>유리안</h3>
          <span class="role"></span>
          <p>ROSA Agent와 Qwen3.5-4B 연동, tool 분해, 자연어 인터페이스를 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-5" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>

      <article class="member">
        <img src="assets/images/avatar-2.svg" alt="팀원 6 프로필 사진">
        <div class="body">
          <h3>조유빈</h3>
          <span class="role"></span>
          <p>발표 자료, 페이지 디자인, 문서 정리와 자료 아카이빙을 담당합니다.</p>
          <a class="link" href="https://github.com/your-github-id-6" target="_blank" rel="noreferrer">GitHub 연동</a>
        </div>
      </article>
    </div>

    <div class="footer-note">
      팀원이 더 늘어나면 카드만 복제하면 됩니다. 각 카드의 GitHub 링크는 개인 계정에 맞게 바꾸면 바로 연동됩니다.
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>吏꾪뻾 ??꾨씪??/h2>
        <p>?먮낯 ?섏씠吏???덈뜕 ?붾퀎 吏꾪뻾 ?댁뿭??議곌툑 ??蹂닿린 醫뗪쾶 ?뺣━?덉뒿?덈떎.</p>
      </div>
    </div>

    <div class="timeline-grid">
      <div class="text-panel">
        <span class="timeline-month">3??/span>
        <h3>?섍꼍 援ъ텞 諛?踰좎씠?ㅻ씪???먯깋</h3>
        <p class="desc">?꾨줈?앺듃 諛⑺뼢??寃곗젙, ROS2/Zenoh 臾댁꽑 ?듭떊 ?뗭뾽, InternVLA쨌LOVON ?ы쁽, 1李??쒖뿰 諛쒗몴瑜?吏꾪뻾?덉뒿?덈떎.</p>
      </div>
      <div class="text-panel">
        <span class="timeline-month">4??/span>
        <h3>?듭떖 湲곕뒫 援ы쁽</h3>
        <p class="desc">InternVLA??Following??寃고빀?섎뒗 諛⑺뼢?깆쓣 ?뺤젙?섍퀬, LOVON ?쇰? 援ъ“ 李⑥슜, ?붾툝?щ쭅, LiDAR SLAM 湲곕컲 ?먯쑉 Backtracking??援ы쁽?덉뒿?덈떎.</p>
      </div>
      <div class="text-panel">
        <span class="timeline-month">5??/span>
        <h3>?듯빀쨌?됯?쨌?쇰Ц??/h3>
        <p class="desc">Pointing 湲곕뒫 異붽?, ?꾩껜 肄붾뱶 蹂묓빀, ROSA??Qwen3.5-4B ?곌껐, ROS2 ?꾧뎄 媛쒖꽑, Task Planner ?듯빀 ???뺣웾 ?됯?? ?쇰Ц 珥덉븞 ?묒꽦???ㅼ뼱媛붿뒿?덈떎.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="section-head">
      <div>
        <h2>湲곗닠 ?ㅽ깮</h2>
        <p>?댁슜??留롮븘 蹂댁뿬???ㅼ젣濡쒕뒗 ?섎뱶?⑥뼱, 紐⑤뜽, ?뚰봽?몄썾?? 誘몃뱾?⑥뼱, ?쒕??덉씠???뺣룄濡?臾띠뼱??蹂대㈃ ?댄빐媛 ?쎌뒿?덈떎.</p>
      </div>
    </div>

    <div class="stack-grid">
      <div class="text-panel">
        <h3>?섎뱶?⑥뼱</h3>
        <ul>
          <li>Unitree Go2: 4議?蹂댄뻾 濡쒕큸, ?댁옣 Jetson Orin / ?댁옣 LiDAR</li>
          <li>Intel RealSense D435: RGB-D 移대찓??/li>
          <li>RTX 3090: ?숈뒿 諛?異붾줎??GPU</li>
        </ul>
      </div>
      <div class="text-panel">
        <h3>紐⑤뜽쨌AI</h3>
        <ul>
          <li>InternVLA-N1-DualVLN: 硫붿씤 VLA</li>
          <li>LOVON: ?쇰? 援ъ“ 李⑥슜</li>
          <li>Qwen3.5-4B: ROSA agent??LLM</li>
          <li>YOLO: 媛앹껜 寃異?/li>
        </ul>
      </div>
      <div class="text-panel">
        <h3>?뚰봽?몄썾??/h3>
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
        <h2>?꾨줈?앺듃???섏쓽</h2>
        <p>?먮옒 臾몄꽌???ㅼそ???덈뜕 ?쇰Ц???ㅻ챸???뚭컻 ?섏씠吏 ?ㅼ쑝濡??ㅼ떆 ?뺣━?덉뒿?덈떎.</p>
      </div>
    </div>

    <div class="impact-grid">
      <div class="text-panel">
        <h3>1. ?뚰삎 ?ъ” 濡쒕큸 ?섍꼍??????곸쓳</h3>
        <p>?洹쒕え ?쒕??덉씠???곗씠?곕줈 ?숈뒿??VLA 紐⑤뜽? ?泥대줈 ?대㉧?몄씠?쒓툒 ?쒖젏?대굹 怨좏뭹吏?RGB-D ?섍꼍??媛?뺥빀?덈떎. 蹂??꾨줈?앺듃??LOVON???듭떖 紐⑤뱢??InternVLA-N1-DualVLN ?대????좏깮?곸쑝濡??듯빀?? ?뚰삎 ?ъ” 濡쒕큸 蹂몄껜???곸쓳?섎뒗 ?ㅼ슜??寃쎈줈瑜??쒖떆?덉뒿?덈떎.</p>
      </div>
      <div class="text-panel">
        <h3>2. ?⑥씪 task瑜??섏뼱??硫?고깭?ㅽ겕 ?듯빀</h3>
        <p>Navigation, Pointing, Following, Backtracking 4醫?task瑜?ROSA 湲곕컲 LLM ?먯씠?꾪듃 ?꾩뿉 ?섎굹???뚯씠?꾨씪?몄쑝濡?臾띠뿀?듬땲?? ?대? ?듯빐 foundation model???ㅼ젣 task?먯꽌 ?대뼸寃??뺤옣?????덈뒗吏 蹂댁뿬以띾땲??</p>
      </div>
      <div class="text-panel">
        <h3>3. ?먯쑉 濡쒕큸 ?쒖뒪?쒖쓽 ?명꽣?섏씠??/h3>
        <p>Go2 Monitor ?명꽣?섏씠?ㅼ? Zenoh-bridge 湲곕컲 臾댁꽑 ROS2 ?듭떊??寃고빀?? ?꾩옣 ?곌껐留뚯쑝濡?濡쒕큸 ?곹깭瑜??뺤씤?섍퀬 紐낅졊???꾩넚쨌?ㅽ뻾?????덈뒗 援ъ“瑜?留뚮뱾?덉뒿?덈떎. ?대뒗 HRI 愿?먯뿉?쒕룄 以묒슂??湲곕컲???⑸땲??</p>
      </div>
    </div>
  </section>

  <section class="section references">
    <div class="section-head">
      <div>
        <h2>李멸퀬 臾명뿄</h2>
        <p>?듭떖 ?쇰Ц怨?湲곗닠 臾몄꽌???꾨옒泥섎읆 吏㏐쾶 ?뺣━???먮㈃ ?뚭컻 ?섏씠吏媛 ??臾닿굅??蹂댁엯?덈떎.</p>
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


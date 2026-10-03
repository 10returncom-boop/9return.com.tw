# -*- coding: utf-8 -*-
"""欣矩陣 ∞ 欣媒體 — 各頁 spec（供 _gen_site.py 生成）"""
import json
from _gen_cases import CASES_HTML

S = "欣矩陣 ∞ 欣媒體"
D = "沒有做不到，只有想不到"

# ============ 服務頁 ============
SERVICES_BODY = '''
  <section class="hero page-hero">
    <div class="clamp hero-inner">
      <span class="eyebrow">服務項目</span>
      <h1>一站式數位佈局，<span class="grad-text">從內容到流量</span></h1>
      <p class="lead">依你的產業與目標，從內容站點佈局、SEO/AEO/GEO 優化、數位行銷到內容自動更新，一站完成你的數位閉環。</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="pricing.html">查看報價方案<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a class="btn btn-line" href="contact.html">免費諮詢</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="clamp">
      <div class="section-head">
        <span class="eyebrow">六大服務</span>
        <h2>從零到聲量，我們包辦</h2>
      </div>
      <div class="grid cols-2">
        <article class="card glow-card pillar reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3.5 9 12 3.5 20.5 9v11h-17Z"/><path d="M9 20v-6h6v6"/></svg></div>
          <h3>垂直內容站點建置</h3>
          <p>為單一產業打造知識型垂直站點，建立該領域的權威入口，讓訪客一進來就找到他要的內容。</p>
          <ul><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>產業情報＋知識庫＋商品展示整合</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>語意化結構與 SEO 友善架構</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>響應式、日夜主題、豐富 UI 元件</span></li></ul>
        </article>
        <article class="card glow-card pillar reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5 5l2.1 2.1M16.9 16.9 19 19M19 5l-2.1 2.1M7.1 16.9 5 19"/></svg></div>
          <h3>SEO 搜尋引擎優化</h3>
          <p>關鍵字研究、技術 SEO、內容結構與站內優化，讓你的網站與內容在 Google 搜尋中被看見。</p>
          <ul><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>結構化資料 JSON-LD 建置</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>語意化 HTML 與內文優化</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>sitemap、robots、canonical 治理</span></li></ul>
        </article>
        <article class="card glow-card pillar reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 19.5 9.5 14l4 4L20 9"/><path d="M15.5 9H20v4.5"/></svg></div>
          <h3>AEO 答案引擎優化</h3>
          <p>讓語音助理、Google 精選摘要與知識面板直接引用你的回答，搶佔「零點擊」搜尋流量。</p>
          <ul><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>FAQ 結構化與直接回答型內容</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>speakable 語音可讀性</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>知識面板與實體一致性</span></li></ul>
        </article>
        <article class="card glow-card pillar reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 2.5 20 5v6c0 4.5-3.2 8-8 10.5C7.2 19 4 15.5 4 11V5Z"/></svg></div>
          <h3>GEO 生成式引擎優化</h3>
          <p>當 ChatGPT、Perplexity 等生成式 AI 回答問題時，讓你的品牌成為被引用的權威來源。</p>
          <ul><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>權威可信內容與實體資訊</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>可被引用與引用的結構</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>跨平台實體一致性</span></li></ul>
        </article>
        <article class="card glow-card pillar reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3.5 6.5h17M3.5 12h17M3.5 17.5h17"/></svg></div>
          <h3>數位行銷與流量獲取</h3>
          <p>內容行銷、社群導流與全網佈局並進，把優質內容變成持續進站的動能，擴大品牌聲量。</p>
          <ul><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>內容行銷策略規劃</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>社群與平台導流</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>品牌聲量擴散</span></li></ul>
        </article>
        <article class="card glow-card pillar reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 4v6h6M20 20v-6h-6"/><path d="M4 12a8 8 0 0 1 14-4.7M20 12a8 8 0 0 1-14 4.7"/></svg></div>
          <h3>內容自動更新與數據回饋</h3>
          <p>內容持續產出與自動更新，維持搜尋新鮮度；並以流量與行為數據回饋，驅動策略持續升級。</p>
          <ul><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>內容排程與自動更新</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>流量與行為數據儀表</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>以數據優化內容與策略</span></li></ul>
        </article>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="section-head center">
        <span class="eyebrow center">合作流程</span>
        <h2>清楚、透明、一次到位</h2>
      </div>
      <div class="timeline">
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">01 · 諮詢</span><h3>需求盤點</h3><p>了解你的產業、目標與預算，盤點現況與缺口。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">02 · 規劃</span><h3>內容與站點佈局</h3><p>依產業規劃垂直站點架構、內容地圖與關鍵字策略。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">03 · 建置</span><h3>網站開發建置</h3><p>語意化架構、響應式、日夜主題與豐富 UI 元件完成建置。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">04 · 優化</span><h3>SEO / AEO / GEO</h3><p>結構化資料、內文優化與權威內容佈建，全面優化可見度。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">05 · 上線</span><h3>發布與驗證</h3><p>正式上線，sitemap 提交與搜尋引擎驗證，監控初始表現。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">06 · 成長</span><h3>內容更新與數據優化</h3><p>內容自動更新與數據回饋，讓網站持續成長。</p></div></div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="cta-band reveal">
        <svg class="inf breathe" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 16c-2.2 0-4-1.8-4-4s1.8-4 4-4c2.9 0 4.5 4 6.9 4s4-4 6.9-4c2.2 0 4 1.8 4 4s-1.8 4-4 4c-2.9 0-4.5-4-6.9-4S8.9 16 6 16Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <h2>想看完整方案與價格？</h2>
        <p>前往報價方案，或直接與我們聊聊你的需求。</p>
        <div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="pricing.html">查看報價方案</a><a class="btn btn-line" href="contact.html">免費諮詢</a></div>
      </div>
    </div>
  </section>
'''

SERVICES_JSON = {
    "@context": "https://schema.org", "@type": "Service",
    "serviceType": "數位內容站點佈局與 SEO/AEO/GEO 行銷服務",
    "provider": { "@type": "Organization", "name": S, "url": "https://9return.com.tw/" },
    "areaServed": "TW", "availableLanguage": "zh-TW",
    "description": "跨產業垂直內容站點建置、SEO 搜尋引擎優化、AEO 答案引擎優化、GEO 生成式引擎優化、數位行銷與內容自動更新服務。",
}

# ============ 報價頁 ============
PRICING_BODY = '''
  <section class="hero page-hero">
    <div class="clamp hero-inner">
      <span class="eyebrow">報價方案</span>
      <h1>透明報價，<span class="grad-text">依需求估價</span></h1>
      <p class="lead">從單一內容站點到完整數位閉環，都有適合你的方案。以下為參考價，實際以專案估價為準，歡迎免費諮詢。</p>
      <div class="btn-row"><a class="btn btn-primary" href="contact.html">取得正式報價<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div>
    </div>
  </section>

  <section class="section">
    <div class="clamp">
      <div class="pricing-grid">
        <article class="price-card reveal">
          <div class="price-name">基礎方案</div>
          <div class="price-sub">單一垂直內容站點起步</div>
          <div class="price"><span class="from">參考價，專案估價</span>NT$38,000<small> 起</small></div>
          <ul class="price-features">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>單一垂直內容站點建置</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>響應式 + 日夜主題 + 豐富 UI</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>基礎 SEO 結構化資料</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>sitemap / robots / canonical</span></li>
            <li class="off"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5l14 14M19 5 5 19"/></svg><span>內容自動更新系統</span></li>
            <li class="off"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5l14 14M19 5 5 19"/></svg><span>AEO / GEO 深度優化</span></li>
          </ul>
          <a class="btn btn-line" href="contact.html">選擇此方案</a>
        </article>

        <article class="price-card featured reveal">
          <div class="price-name">進階成長方案</div>
          <div class="price-sub">站點 + 三面向優化，最受歡迎</div>
          <div class="price"><span class="from">參考價，專案估價</span>NT$88,000<small> 起</small></div>
          <ul class="price-features">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>內容站點建置（可多站）</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>SEO + AEO + GEO 三合一優化</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>FAQ / 精選摘要 / AI 引用優化</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>內容行銷與流量導入</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>內容自動更新系統</span></li>
            <li class="off"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 5l14 14M19 5 5 19"/></svg><span>多產業全域佈局</span></li>
          </ul>
          <a class="btn btn-primary" href="contact.html">選擇此方案</a>
        </article>

        <article class="price-card reveal">
          <div class="price-name">旗艦全閉環方案</div>
          <div class="price-sub">多產業佈局 + 完整數據閉環</div>
          <div class="price"><span class="from">參考價，專案估價</span>NT$168,000<small> 起</small></div>
          <ul class="price-features">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>多產業垂直站點全域佈局</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>SEO + AEO + GEO 深度整合</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>內容自動更新 + 數據儀表</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>數據回饋閉環與策略優化</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>品牌聲量與全網佈局</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>專屬策略顧問服務</span></li>
          </ul>
          <a class="btn btn-line" href="contact.html">選擇此方案</a>
        </article>
      </div>

      <div class="mt-3 note-box">
        <b>報價說明：</b>以上為參考價區間，實際費用依站點數量、內容規模、優化深度與維護週期估價。另有客製專案，歡迎 <a href="contact.html" style="color:var(--warm);font-weight:600">免費諮詢</a> 取得正式報價。價格含稅與否、付款方式將於正式估價單中載明。
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="section-head center">
        <span class="eyebrow center">方案比較</span>
        <h2>找出最適合你的方案</h2>
      </div>
      <div class="compare-wrap">
        <table class="compare">
          <colgroup><col style="width:24%"><col style="width:19%"><col style="width:19%"><col style="width:19%"><col style="width:19%"></colgroup>
          <thead><tr><th>項目</th><th>基礎</th><th class="hl">進階</th><th>旗艦</th><th>客製</th></tr></thead>
          <tbody>
            <tr><th>內容站點</th><td>單一</td><td>可多站</td><td>多產業全域</td><td>依需求</td></tr>
            <tr><th>SEO 優化</th><td class="yes">基礎</td><td class="yes">完整</td><td class="yes">深度</td><td class="yes">深度</td></tr>
            <tr><th>AEO 優化</th><td class="no">—</td><td class="yes">完整</td><td class="yes">深度</td><td class="yes">深度</td></tr>
            <tr><th>GEO 優化</th><td class="no">—</td><td class="yes">完整</td><td class="yes">深度</td><td class="yes">深度</td></tr>
            <tr><th>內容自動更新</th><td class="no">—</td><td class="yes">標準</td><td class="yes">完整</td><td class="yes">依需求</td></tr>
            <tr><th>數據回饋閉環</th><td class="no">—</td><td class="no">—</td><td class="yes">完整</td><td class="yes">依需求</td></tr>
            <tr><th>數位行銷導入</th><td class="no">—</td><td class="yes">標準</td><td class="yes">完整</td><td class="yes">依需求</td></tr>
            <tr><th>適用對象</th><td>單一品牌起步</td><td>成長型品牌</td><td>多領域集團</td><td>特殊需求</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="section-head center"><span class="eyebrow center">常見問題</span><h2>報價與付款</h2></div>
      <div class="faq">
        <div class="faq-item"><button class="faq-q">價格可以再談嗎？<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button><div class="faq-a"><div class="faq-a-inner">可依實際專案範圍與需求調整。建議先與我們聊聊目標，我們會給出符合需求與預算的建議。</div></div></div>
        <div class="faq-item"><button class="faq-q">多久可以上線？<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button><div class="faq-a"><div class="faq-a-inner">依專案規模而定，單一站點約 2–4 週，多站點與全域佈局則需更長。上線後持續進行優化與內容更新。</div></div></div>
        <div class="faq-item"><button class="faq-q">包含維護嗎？<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button><div class="faq-a"><div class="faq-a-inner">進階與旗艦方案包含內容自動更新與數據回饋優化服務；也可另購維護合約。</div></div></div>
      </div>
    </div>
  </section>
'''

PRICING_JSON = {
    "@context": "https://schema.org", "@type": "OfferCatalog",
    "name": "欣矩陣 ∞ 欣媒體 報價方案",
    "provider": { "@type": "Organization", "name": S, "url": "https://9return.com.tw/" },
    "itemListElement": [
        { "@type": "Offer", "name": "基礎方案", "price": "38000", "priceCurrency": "TWD", "description": "單一垂直內容站點建置，含基礎 SEO 結構化資料。" },
        { "@type": "Offer", "name": "進階成長方案", "price": "88000", "priceCurrency": "TWD", "description": "內容站點加 SEO/AEO/GEO 三合一優化與內容自動更新。" },
        { "@type": "Offer", "name": "旗艦全閉環方案", "price": "168000", "priceCurrency": "TWD", "description": "多產業全域佈局、深度優化與完整數據回饋閉環。" },
    ],
}

# ============ 成功案例頁 ============
CASES_BODY = f'''
  <section class="hero page-hero">
    <div class="clamp hero-inner">
      <span class="eyebrow">成功案例</span>
      <h1>22 個垂直站點，<span class="grad-text">見證佈局實力</span></h1>
      <p class="lead">從文史藝術、寵物生活、房地產到財經與心理療癒，我們已佈局 22 個跨產業垂直內容站點。點擊卡片可直接造訪該站。</p>
    </div>
  </section>

  <section class="section">
    <div class="clamp">
      <div id="caseFilter" class="filter-bar" role="tablist" aria-label="案例分類篩選">
        <button class="filter-btn active" data-filter="全部">全部</button>
        <button class="filter-btn" data-filter="文史藝術">文史藝術</button>
        <button class="filter-btn" data-filter="寵物生活">寵物生活</button>
        <button class="filter-btn" data-filter="房地產">房地產</button>
        <button class="filter-btn" data-filter="財經知識">財經知識</button>
        <button class="filter-btn" data-filter="心理療癒">心理療癒</button>
        <button class="filter-btn" data-filter="時尚娛樂">時尚娛樂</button>
      </div>
      <div class="grid cols-3">
{CASES_HTML}
      </div>
      <div class="empty-hint" id="caseEmpty" style="display:none">沒有符合分類的案例。</div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="cta-band reveal">
        <svg class="inf breathe" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 16c-2.2 0-4-1.8-4-4s1.8-4 4-4c2.9 0 4.5 4 6.9 4s4-4 6.9-4c2.2 0 4 1.8 4 4s-1.8 4-4 4c-2.9 0-4.5-4-6.9-4S8.9 16 6 16Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <h2>下一個成功案例，就是你</h2>
        <p>讓我們為你的品牌佈局一座會自己帶來流量的內容站點群。</p>
        <div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="contact.html">免費諮詢<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a><a class="btn btn-line" href="pricing.html">查看報價</a></div>
      </div>
    </div>
  </section>
'''

# ============ SEO/AEO/GEO 知識頁 ============
SEO_BODY = '''
  <section class="hero page-hero">
    <div class="clamp hero-inner">
      <span class="eyebrow">SEO · AEO · GEO</span>
      <h1>讓品牌，<span class="grad-text">被找到、被引用</span></h1>
      <p class="lead">搜尋引擎、語音助理、生成式 AI——未來的流量來自三個入口。我們幫你把三個入口一次打通。</p>
      <div class="btn-row"><a class="btn btn-primary" href="contact.html">免費諮詢優化方案</a></div>
    </div>
  </section>

  <section class="section">
    <div class="clamp">
      <div class="section-head center">
        <span class="eyebrow center">三個關鍵概念</span>
        <h2>SEO、AEO、GEO 差在哪？</h2>
      </div>
      <div class="def-grid">
        <article class="card def-card reveal">
          <div class="letter">SEO</div>
          <h3>搜尋引擎優化</h3>
          <p>Search Engine Optimization。透過關鍵字、技術與內容優化，讓網站在 Google 等搜尋引擎獲得自然排序，是被動等待被「搜到」的流量入口。</p>
          <ul class="checks"><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>關鍵字與技術優化</span></li><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>結構化資料 JSON-LD</span></li><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>權威內容佈建</span></li></ul>
        </article>
        <article class="card def-card reveal">
          <div class="letter">AEO</div>
          <h3>答案引擎優化</h3>
          <p>Answer Engine Optimization。針對語音助理、Google 精選摘要與知識面板優化，讓搜尋引擎直接把你的回答「唸」給使用者，搶佔零點擊流量。</p>
          <ul class="checks"><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>FAQ 直接回答</span></li><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>精選摘要結構</span></li><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>speakable 語音可讀</span></li></ul>
        </article>
        <article class="card def-card reveal">
          <div class="letter">GEO</div>
          <h3>生成式引擎優化</h3>
          <p>Generative Engine Optimization。當 ChatGPT、Perplexity、Gemini 等 AI 回答問題時，讓你的品牌成為被引用與推薦的權威來源，掌握 AI 時代的曝光。</p>
          <ul class="checks"><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>權威可信內容</span></li><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>實體資訊一致</span></li><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>可被引用結構</span></li></ul>
        </article>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="split">
        <div class="reveal">
          <span class="eyebrow">我們怎麼做</span>
          <h2 style="margin:.7rem 0 .8rem">三面向一次打通，<span class="grad-text">不讓流量從指尖溜走</span></h2>
          <p class="lead">從內容本體、結構化資料到實體一致性，我們同時滿足搜尋引擎、語音助理與生成式 AI 的閱讀邏輯。</p>
          <ul class="checks">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span><b>內容本體</b>——直接回答、結構清晰、權威可信</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span><b>結構化資料</b>——JSON-LD、FAQ、Breadcrumb、Organization</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span><b>實體一致性</b>——名稱、電話、Logo 跨平台一致，強化信賴</span></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span><b>持續更新</b>——內容自動更新，維持新鮮度與引用動能</span></li>
          </ul>
        </div>
        <div class="visual reveal"><img src="assets/card-10-realestate.webp" alt="SEO AEO GEO 數據優化意象" loading="lazy"></div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="section-head center"><span class="eyebrow center">常見問題</span><h2>SEO / AEO / GEO 問答</h2></div>
      <div class="faq">
        <div class="faq-item"><button class="faq-q">為什麼需要 GEO？<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button><div class="faq-a"><div class="faq-a-inner">愈來愈多使用者直接問 AI 獲得答案。若你的品牌沒有被 AI 引用，等於在 AI 時代的搜尋入口消失。GEO 讓生成式引擎在回答時推薦你。</div></div></div>
        <div class="faq-item"><button class="faq-q">AEO 和 SEO 衝突嗎？<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button><div class="faq-a"><div class="faq-a-inner">不衝突。AEO 建立在 SEO 之上，結構清晰、直接回答的內容同時也利於搜尋排名。我們是整合優化，而非互相取捨。</div></div></div>
        <div class="faq-item"><button class="faq-q">多久看得到成效？<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></button><div class="faq-a"><div class="faq-a-inner">SEO/AEO/GEO 屬長期優化，通常 3–6 個月可見明顯改善；結構化資料與技術優化則上線即生效。我們會以數據持續追蹤。</div></div></div>
      </div>
    </div>
  </section>
'''

SEO_FAQ_JSON = {
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [
        { "@type": "Question", "name": "SEO、AEO、GEO 有什麼不同？",
          "acceptedAnswer": { "@type": "Answer", "text": "SEO 是搜尋引擎優化，讓網站在 Google 被搜到；AEO 是答案引擎優化，讓語音助理與精選摘要直接引用你的回答；GEO 是生成式引擎優化，讓 ChatGPT 等 AI 在回答問題時引用你的品牌內容。" } },
        { "@type": "Question", "name": "為什麼需要 GEO 優化？",
          "acceptedAnswer": { "@type": "Answer", "text": "愈來愈多使用者直接詢問生成式 AI 獲得答案，若品牌未被 AI 引用，將在 AI 時代的搜尋入口失去曝光。GEO 讓生成式引擎在回答時推薦你。" } },
        { "@type": "Question", "name": "SEO、AEO、GEO 多久看得到成效？",
          "acceptedAnswer": { "@type": "Answer", "text": "屬長期優化，通常 3 至 6 個月可見明顯改善；結構化資料與技術優化上線即生效，並以數據持續追蹤。" } },
    ],
}

# ============ 關於頁 ============
ABOUT_BODY = '''
  <section class="hero page-hero">
    <div class="clamp hero-inner">
      <span class="eyebrow">關於我們</span>
      <h1>一個想法，<span class="grad-text">一座站點群</span></h1>
      <p class="lead">欣矩陣 ∞ 欣媒體：沒有做不到，只有想不到。我們相信好的內容與好的佈局，能把「想不到」變成做得到的網路聲量。</p>
    </div>
  </section>

  <section class="section">
    <div class="clamp">
      <div class="split">
        <div class="visual reveal"><img src="assets/bg-main.webp" alt="欣矩陣 ∞ 欣媒體 品牌理念意象" loading="lazy"></div>
        <div class="reveal">
          <span class="eyebrow">品牌故事</span>
          <h2 style="margin:.7rem 0 .8rem">結合各種角度，打開眼光與眼界</h2>
          <p class="lead">我們想要看見結合各種角度的知識、產品展示與行銷，一起導入各類產業、家中、職內的新觀點。</p>
          <p style="color:var(--ink-dim);margin-top:1rem">面對波動與轉機，我們把內容放大、把格局打開，對抗無形框架，完成你的價值性創造。從文史藝術、寵物生活到房地產與財經，我們用一座座垂直站點，把每個領域的深度與溫度做出來。</p>
          <div class="badge-row">
            <span class="badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg>跨產業佈局</span>
            <span class="badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg>內容驅動</span>
            <span class="badge"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg>數據閉環</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="section-head center">
        <span class="eyebrow center">設計規劃開發</span>
        <h2>操盤手</h2>
        <p class="lead">每一個站點，都由張書欣親手設計、規劃與開發。</p>
      </div>
      <div style="max-width:420px;margin-inline:auto">
        <div class="card person-card glow-card reveal">
          <div class="person-avatar">張</div>
          <h3>張書欣</h3>
          <div class="role">設計規劃開發</div>
          <p style="color:var(--ink-dim);font-size:.92rem">從內容站點架構、視覺設計到技術建置一手掌握，用「沒有做不到，只有想不到」的精神，為每個品牌打造會成長的數位佈局。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="section-head center">
        <span class="eyebrow center">品牌歷程</span>
        <h2>從一個入口，到一座站點群</h2>
      </div>
      <div class="timeline">
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">起點</span><h3>欣矩陣 ∞ 欣媒體</h3><p>以「沒有做不到，只有想不到」為核心，展開跨產業內容站點佈局。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">佈局</span><h3>文史藝術與寵物生活</h3><p>曾侯乙編鐘、金庸心理、ZooTecture、Petlogic 等站點陸續上線。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">拓展</span><h3>房地產、財經與心理</h3><p>九回房地觀測站、經濟學小遊戲、占星與療癒等領域加入。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">整合</span><h3>SEO / AEO / GEO 優化</h3><p>把搜尋、語音與生成式 AI 三入口整合進每一座站點。</p></div></div>
        <div class="tl-row"><div class="tl-node"><span class="tl-dot"></span></div><div class="tl-axis"></div><div class="tl-body"><span class="tl-time">未來</span><h3>持續成長</h3><p>22 個站點與更多領域持續擴展，完成你的價值性創造。</p></div></div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="clamp">
      <div class="cta-band reveal">
        <svg class="inf breathe" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 16c-2.2 0-4-1.8-4-4s1.8-4 4-4c2.9 0 4.5 4 6.9 4s4-4 6.9-4c2.2 0 4 1.8 4 4s-1.8 4-4 4c-2.9 0-4.5-4-6.9-4S8.9 16 6 16Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <h2>想跟我們一起，完成你的佈局？</h2>
        <div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="contact.html">聯絡我們</a><a class="btn btn-line" href="cases.html">看成功案例</a></div>
      </div>
    </div>
  </section>
'''

# ============ 聯絡頁 ============
CONTACT_BODY = '''
  <section class="hero page-hero">
    <div class="clamp hero-inner">
      <span class="eyebrow">聯絡我們</span>
      <h1>聊聊你的<span class="grad-text">數位佈局</span></h1>
      <p class="lead">無論是內容站點、SEO/AEO/GEO 優化，還是完整的流量閉環，都歡迎與我們聊聊。</p>
    </div>
  </section>

  <section class="section">
    <div class="clamp">
      <div class="grid cols-3">
        <div class="card contact-card reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 5h16v14H4z"/><path d="m4 7 8 6 8-6"/></svg></div>
          <div><h3>Email</h3><p><a href="mailto:zootecture@gmail.com">zootecture@gmail.com</a></p></div>
        </div>
        <div class="card contact-card reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6.5 3.5 9 3l1.6 4.4-2 1.4a13 13 0 0 0 6.6 6.6l1.4-2 4.4 1.6-.5 2.5c-.4 1.6-1.8 2.5-3.4 2.2C11.5 18.6 5.4 12.5 4.3 5.9c-.2-1.6.7-3 2.2-3.4Z"/></svg></div>
          <div><h3>電話</h3><p><a href="tel:0968222201">0968-222201</a></p></div>
        </div>
        <div class="card contact-card reveal">
          <div class="ico"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.5 10.7C21.5 6 16.8 2.2 12 2.2S2.5 6 2.5 10.7c0 4.4 4 8.1 9.5 8.1.5 0 1.2 0 1.8-.1.6.4 1.6 1.1 2.4 1.4.3.1.8-.1.6-.6-.1-.5-.5-1.5-.6-1.9 3-1.3 5.3-3.9 5.3-6.9Z"/></svg></div>
          <div><h3>Line</h3><p><a href="https://line.me/R/ti/p/~331.today" target="_blank" rel="noopener">331.today</a></p></div>
        </div>
      </div>

      <div class="mt-3 split">
        <div class="reveal">
          <span class="eyebrow">留下你的需求</span>
          <h2 style="margin:.7rem 0 .8rem">讓我們為你估價</h2>
          <p class="lead">填寫表單後，我們會盡快與你聯繫。你也可以直接撥打電話或加 Line，即時聊聊。</p>
          <div class="checks">
            <li style="list-style:none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>24 小時內回覆（工作日）</span></li>
            <li style="list-style:none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>免費初步諮詢與估價</span></li>
            <li style="list-style:none"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m4.5 12.5 5 5 10-11"/></svg><span>需求保密，專業回覆</span></li>
          </div>
        </div>
        <form class="card glow-card reveal" style="padding:1.6rem" onsubmit="handleContact(event)">
          <div class="form-grid two">
            <div class="field"><label for="c-name">姓名 <span>*</span></label><input id="c-name" name="name" type="text" required placeholder="你的姓名"></div>
            <div class="field"><label for="c-tel">聯絡電話</label><input id="c-tel" name="tel" type="tel" placeholder="09xx-xxx-xxx"></div>
          </div>
          <div class="form-grid" style="margin-top:1rem">
            <div class="field"><label for="c-email">Email <span>*</span></label><input id="c-email" name="email" type="email" required placeholder="you@email.com"></div>
            <div class="field"><label for="c-subject">需求類型</label>
              <select id="c-subject" name="subject">
                <option>內容站點建置</option>
                <option>SEO / AEO / GEO 優化</option>
                <option>數位行銷與流量</option>
                <option>內容自動更新</option>
                <option>其他</option>
              </select>
            </div>
            <div class="field"><label for="c-msg">需求說明 <span>*</span></label><textarea id="c-msg" name="message" required placeholder="簡單描述你的目標與需求"></textarea></div>
          </div>
          <div class="btn-row">
            <button type="submit" class="btn btn-primary">送出需求<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 11.5 20 4l-6.5 16-3-6.5Z"/><path d="M20 4 10.5 13.5"/></svg></button>
          </div>
          <p class="muted" style="font-size:.8rem;margin-top:.8rem">本頁為前端展示表單，送出後將以 Email 開啟寄件；正式上線可串接後端收件。</p>
        </form>
      </div>
    </div>
  </section>
'''

CONTACT_JS = '''
<script>
function handleContact(e){
  e.preventDefault();
  var name=document.getElementById('c-name').value.trim();
  var email=document.getElementById('c-email').value.trim();
  var msg=document.getElementById('c-msg').value.trim();
  var subj=document.getElementById('c-subject').value;
  var body=encodeURIComponent('姓名：'+name+'\\nEmail：'+email+'\\n需求：'+subj+'\\n說明：'+msg);
  window.location.href='mailto:zootecture@gmail.com?subject='+encodeURIComponent('[欣矩陣諮詢] '+subj)+'&body='+body;
  var btn=e.target.querySelector('button[type=submit]');
  if(btn){ btn.textContent='已開啟寄信視窗'; }
}
</script>
'''

CONTACT_JSON = {
    "@context": "https://schema.org", "@type": "ContactPage",
    "name": "聯絡欣矩陣 ∞ 欣媒體",
    "url": "https://9return.com.tw/contact.html",
    "mainEntity": { "@type": "Organization", "name": S, "telephone": "+886-968-222201", "url": "https://9return.com.tw/" },
}

# 統一彙整（含麵包屑）
PAGES = [
    {
        "file": "services.html", "active": "services.html",
        "title": "服務項目｜欣矩陣 ∞ 欣媒體｜內容站點 × SEO/AEO/GEO × 數位行銷",
        "desc": "欣矩陣 ∞ 欣媒體提供垂直內容站點建置、SEO 搜尋引擎優化、AEO 答案引擎優化、GEO 生成式引擎優化、數位行銷與內容自動更新六大服務，一站完成數位閉環。專線 0968-222201。",
        "keywords": "內容站點建置,SEO優化,AEO,GEO,數位行銷,內容自動更新,流量成長,欣矩陣,欣媒體",
        "canonical": "https://9return.com.tw/services.html",
        "og_title": "服務項目｜欣矩陣 ∞ 欣媒體",
        "og_desc": "垂直內容站點建置、SEO/AEO/GEO 優化、數位行銷與內容自動更新，一站完成數位閉環。",
        "crumbs": [("首頁","index.html"),("服務項目","services.html")],
        "json": SERVICES_JSON,
        "body": SERVICES_BODY, "extra_js": "",
    },
    {
        "file": "pricing.html", "active": "pricing.html",
        "title": "報價方案｜欣矩陣 ∞ 欣媒體｜網站建置與 SEO/AEO/GEO 收費",
        "desc": "欣矩陣 ∞ 欣媒體報價方案：基礎、進階成長與旗艦全閉環三大方案，含內容站點建置、SEO/AEO/GEO 優化、內容自動更新與數據閉環。透明報價，依需求估價，歡迎免費諮詢。",
        "keywords": "網站報價,內容站點建置價格,SEO收費,AEO,GEO,數位行銷報價,欣矩陣,欣媒體",
        "canonical": "https://9return.com.tw/pricing.html",
        "og_title": "報價方案｜欣矩陣 ∞ 欣媒體",
        "og_desc": "基礎、進階、旗艦與客製方案，透明報價，依需求估價。",
        "crumbs": [("首頁","index.html"),("報價方案","pricing.html")],
        "json": PRICING_JSON,
        "body": PRICING_BODY, "extra_js": "",
    },
    {
        "file": "cases.html", "active": "cases.html",
        "title": "成功案例｜欣矩陣 ∞ 欣媒體｜22 個跨產業垂直內容站點",
        "desc": "欣矩陣 ∞ 欣媒體成功案例：22 個跨產業垂直內容站點，涵蓋文史藝術、寵物生活、房地產、財經與心理療癒，點擊即可造訪每座站點。",
        "keywords": "成功案例,內容站點,垂直站點,案例,網站案例,欣矩陣,欣媒體",
        "canonical": "https://9return.com.tw/cases.html",
        "og_title": "成功案例｜欣矩陣 ∞ 欣媒體",
        "og_desc": "22 個跨產業垂直內容站點，見證佈局實力。",
        "crumbs": [("首頁","index.html"),("成功案例","cases.html")],
        "json": None,
        "body": CASES_BODY, "extra_js": "",
    },
    {
        "file": "seo.html", "active": "seo.html",
        "title": "SEO · AEO · GEO 是什麼｜欣矩陣 ∞ 欣媒體｜搜尋、答案與生成式引擎優化",
        "desc": "了解 SEO（搜尋引擎優化）、AEO（答案引擎優化）與 GEO（生成式引擎優化）的差異與整合策略，讓品牌被搜尋引擎、語音助理與生成式 AI 找到並引用。",
        "keywords": "SEO,AEO,GEO,搜尋引擎優化,答案引擎優化,生成式引擎優化,AI搜尋,欣矩陣",
        "canonical": "https://9return.com.tw/seo.html",
        "og_title": "SEO · AEO · GEO 是什麼｜欣矩陣 ∞ 欣媒體",
        "og_desc": "搜尋引擎、語音助理與生成式 AI 三入口一次打通的優化策略。",
        "crumbs": [("首頁","index.html"),("SEO·AEO·GEO","seo.html")],
        "json": SEO_FAQ_JSON,
        "body": SEO_BODY, "extra_js": "",
    },
    {
        "file": "about.html", "active": "about.html",
        "title": "關於我們｜欣矩陣 ∞ 欣媒體｜沒有做不到，只有想不到",
        "desc": "欣矩陣 ∞ 欣媒體：跨產業垂直內容站點佈局與數位行銷整合平台。了解我們的品牌故事、設計規劃開發張書欣與品牌歷程。",
        "keywords": "關於我們,欣矩陣,欣媒體,張書欣,品牌故事,內容站點,數位行銷",
        "canonical": "https://9return.com.tw/about.html",
        "og_title": "關於我們｜欣矩陣 ∞ 欣媒體",
        "og_desc": "一個想法，一座站點群。了解我們的品牌故事與操盤手。",
        "crumbs": [("首頁","index.html"),("關於我們","about.html")],
        "json": None,
        "body": ABOUT_BODY, "extra_js": "",
    },
    {
        "file": "contact.html", "active": "contact.html",
        "title": "聯絡我們｜欣矩陣 ∞ 欣媒體｜免費諮詢與報價",
        "desc": "聯絡欣矩陣 ∞ 欣媒體：電話 0968-222201、Line 331.today、Email zootecture@gmail.com。填寫需求表單，免費諮詢你的內容站點與 SEO/AEO/GEO 數位佈局。",
        "keywords": "聯絡我們,免費諮詢,報價,網站建置,SEO,GEO,欣矩陣,欣媒體,0968-222201",
        "canonical": "https://9return.com.tw/contact.html",
        "og_title": "聯絡我們｜欣矩陣 ∞ 欣媒體",
        "og_desc": "免費諮詢你的內容站點與 SEO/AEO/GEO 數位佈局。",
        "crumbs": [("首頁","index.html"),("聯絡我們","contact.html")],
        "json": CONTACT_JSON,
        "body": CONTACT_BODY, "extra_js": CONTACT_JS,
    },
]

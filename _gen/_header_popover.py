# -*- coding: utf-8 -*-
"""欣矩陣 V1 — 將 header 改為單一 Popover/Dropdown 選單（所有內容整合進選單），移除橫向導覽、免費諮詢與側邊 drawer。"""
import io, os, re

ROOT = r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1"
PAGES = ["index.html","services.html","pricing.html","cases.html","seo.html","about.html","contact.html"]

# 每頁對應的 active 主連結
ACTIVE = {
    "index.html": "index.html", "services.html": "services.html", "pricing.html": "pricing.html",
    "cases.html": "cases.html", "seo.html": "seo.html", "about.html": "about.html", "contact.html": "contact.html",
}

SERVICES_SUBS = [
    ("services.html", "服務項目總覽"),
    ("services.html#sites", "內容站點佈局"),
    ("services.html#seo", "SEO · AEO · GEO"),
    ("services.html#marketing", "數位行銷"),
    ("services.html#update", "內容自動更新"),
]

CASES = [
    ("https://9return.com.tw/zeng-hou-yi-bells/index.html", "曾侯乙編鐘戰國青銅禮樂重器"),
    ("https://9return.com.tw/jinyong-psychology/index.html", "金庸人物與心理學"),
    ("https://331.today/", "331 Gallery 數位藝廊"),
    ("https://zootecture.com/", "ZooTecture 入梯"),
    ("https://petlogic.org/", "Petlogic 毛毛邏輯"),
    ("https://9return.com.tw/dashboard.html", "九回房地觀測站"),
    ("https://9return.com.tw/index.html", "當榮格遇到易經"),
    ("https://9return.com.tw/hongloumeng/index.html", "夢見紅樓夢的家"),
    ("https://9return.com.tw/classic-architecture/index.html", "古代建築還原記"),
    ("https://vocus.cc/salon/zootecture", "順寵毛小孩"),
    ("https://vocus.cc/salon/petlogic", "安寵好好學"),
    ("https://9return.com.tw/index.html", "寵物空間好好裝"),
    ("https://9return.com.tw/index.html", "虛擬試衣間"),
    ("https://9return.com.tw/index.html", "經濟學的小遊戲"),
    ("https://9return.com.tw/index.html", "星象命盤占星"),
    ("https://9return.com.tw/index.html", "三國演義 vs 賽局"),
    ("https://9return.com.tw/index.html", "以物易物好好玩"),
    ("https://9return.com.tw/index.html", "Infucoco 愛幻想"),
    ("https://9return.com.tw/index.html", "音樂家都很怪"),
    ("https://9return.com.tw/index.html", "舒心玫瑰園"),
    ("https://9return.com.tw/index.html", "我看不到但都知道"),
    ("https://9return.com.tw/index.html", "世界名牌這樣唸"),
]

CHEV = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>'

def mplink(href, label, active_href):
    a = " active" if href == active_href else ""
    return '<a class="mp-link%s" href="%s" role="menuitem">%s</a>' % (a, href, label)

def build_header(active_href):
    services_subs = "".join(
        '<a href="%s">%s</a>' % (h, t) for h, t in SERVICES_SUBS)
    cases_subs = "".join(
        '<a href="%s">%s</a>' % (h, t) for h, t in CASES) + \
        '<a class="dd-all" href="cases.html">查看全部案例 →</a>'
    menu = "".join([
        mplink("index.html", "首頁", active_href),
        '<details class="mp-group"><summary class="mp-summary">服務項目' + CHEV + '</summary><div class="mp-subs">' + services_subs + '</div></details>',
        mplink("pricing.html", "報價方案", active_href),
        '<details class="mp-group"><summary class="mp-summary">成功案例' + CHEV + '</summary><div class="mp-subs mp-cases">' + cases_subs + '</div></details>',
        mplink("seo.html", "SEO·AEO·GEO", active_href),
        mplink("about.html", "關於我們", active_href),
        mplink("contact.html", "聯絡我們", active_href),
    ])
    return """<header class="site-header">
  <div class="clamp header-inner">
    <a class="brand" href="index.html" aria-label="欣矩陣 ∞ 欣媒體 首頁">
      <svg class="inf breathe" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 16c-2.2 0-4-1.8-4-4s1.8-4 4-4c2.9 0 4.5 4 6.9 4s4-4 6.9-4c2.2 0 4 1.8 4 4s-1.8 4-4 4c-2.9 0-4.5-4-6.9-4S8.9 16 6 16Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <span>欣矩陣<small>欣媒體</small></span>
    </a>
    <div class="header-actions">
      <button id="themeToggle" class="icon-btn" aria-label="切換主題" title="切換主題" onclick="window.Theme.toggle()">
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5 5l1.7 1.7M17.3 17.3 19 19M19 5l-1.7 1.7M6.7 17.3 5 19"/></svg>
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11Z"/></svg>
      </button>
      <div class="popover-menu" id="popoverMenu">
        <button class="icon-btn menu-btn" id="menuToggle" aria-label="開啟選單" aria-haspopup="menu" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><path d="M3.5 6.5h17M3.5 12h17M3.5 17.5h17"/></svg>
        </button>
        <nav class="menu-popover" aria-label="全站選單" role="menu">""" + menu + """</nav>
      </div>
    </div>
  </div>
</header>"""

def patch(page):
    path = os.path.join(ROOT, page)
    s = io.open(path, encoding="utf-8").read()
    orig = s
    new_head = build_header(ACTIVE[page])
    # 替換 header 區塊
    s = re.sub(r'(?s)<header class="site-header">.*?</header>', new_head, s, count=1)
    # 移除 drawer 區塊（header 之後、<main> 之前的所有內容，含側邊選單註解）
    s = re.sub(r'(?s)</header>.*?<main>', '</header>\n\n<main>', s, count=1)
    io.open(path, "w", encoding="utf-8", newline="").write(s)
    print(page, "changed" if s != orig else "NOCHANGE")

for p in PAGES:
    patch(p)
print("DONE")

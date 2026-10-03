# -*- coding: utf-8 -*-
"""
欣矩陣 ∞ 欣媒體 商業官網 — 多頁生成器
從 index.html 抽取共用 chrome（header/drawer/footer/scripts），
依各頁 spec 生成其餘頁面，確保全站外觀一致。
執行：python _gen_site.py
"""
import os, re, json, sys

BASE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(BASE, "index.html")

with open(INDEX, encoding="utf-8") as f:
    index_html = f.read()

# ---------- 抽取共用區塊 ----------
def between(html, start, end, tag):
    i = html.index(start)
    j = html.index(end, i) + len(end)
    return html[i:j]

HEAD_START = index_html.index("<head>")
HEAD_END = index_html.index("</head>") + len("</head>")
HEAD_CHROME = index_html[HEAD_START:HEAD_END]

HEADER = between(index_html, '<header class="site-header">', "</header>", "header")
DRAWER = between(index_html, '<div class="drawer"', "</aside>\n</div>", "drawer")
FOOTER = between(index_html, '<footer class="site-footer">', "</footer>", "footer")
SCRIPTS = between(index_html, '<button class="to-top"', "</html>", "scripts").replace("</html>", "")
SCRIPTS = SCRIPTS[:SCRIPTS.index('<script src="js/config.js"></script>')] + '<script src="js/config.js"></script>\n<script src="js/utils.js"></script>\n<script src="js/main.js"></script>\n</body>\n</html>\n'

# ---------- 模板 ----------
def make_head(title, desc, keywords, canonical, og_title, og_desc, og_url, extra_json=""):
    h = HEAD_CHROME
    h = h.replace("<title>" + "欣矩陣 ∞ 欣媒體｜跨產業垂直內容站點 × SEO/AEO/GEO 數位行銷整合平台" + "</title>", "<title>" + title + "</title>")
    h = h.replace('<meta name="description" content="欣矩陣 ∞ 欣媒體：沒有做不到，只有想不到。跨產業垂直站點全面佈局，涵蓋產業情報、知識庫、商品展示與數位行銷。一站導入全網流量、SEO 優化、內容自動更新，打通曝光、獲客、數據回饋完整閉環，協助品牌擴大網路聲量。專線 0968-222201。">',
                  '<meta name="description" content="' + desc + '">')
    h = h.replace('<meta name="keywords" content="欣矩陣,欣媒體,內容站點,SEO優化,AEO,GEO,數位行銷,網站建置,流量成長,內容自動更新,品牌聲量,張書欣">',
                  '<meta name="keywords" content="' + keywords + '">')
    h = h.replace('href="https://9return.com.tw/"', 'href="' + canonical + '"')
    h = h.replace('property="og:title" content="欣矩陣 ∞ 欣媒體｜跨產業垂直內容站點 × SEO/AEO/GEO 數位行銷"', 'property="og:title" content="' + og_title + '"')
    h = h.replace('property="og:description" content="涵蓋產業情報、知識庫、商品展示與數位行銷，一站導入全網流量、SEO 優化、內容自動更新，打通曝光、獲客、數據回饋完整閉環。"',
                  'property="og:description" content="' + og_desc + '"')
    h = h.replace('property="og:url" content="https://9return.com.tw/"', 'property="og:url" content="' + og_url + '"')
    h = h.replace('name="twitter:title" content="欣矩陣 ∞ 欣媒體｜跨產業垂直內容站點 × 數位行銷"', 'name="twitter:title" content="' + og_title + '"')
    h = h.replace('name="twitter:description" content="一站式導入全網流量、SEO/AEO/GEO 優化與內容自動更新，完成你的數位佈局。"', 'name="twitter:description" content="' + og_desc + '"')
    if extra_json:
        h = h.rstrip()
        if not h.endswith("</head>"):
            h += "\n"
        h += extra_json + "\n</head>"
    return h

def make_header(active_href):
    def link(href, label):
        cls = ' class="active" aria-current="page"' if href == active_href else ""
        return f'      <a href="{href}"{cls}>{label}</a>'

    sys.path.insert(0, BASE)
    from _gen_cases import CASES

    svc_dd = "\n".join([
        '          <a href="services.html#sites"><span>內容站點佈局</span><em>垂直內容站點與知識庫</em></a>',
        '          <a href="services.html#seo"><span>SEO · AEO · GEO</span><em>三面向優化整合</em></a>',
        '          <a href="services.html#marketing"><span>數位行銷</span><em>內容行銷與流量導入</em></a>',
        '          <a href="services.html#update"><span>內容自動更新</span><em>維持搜尋新鮮度</em></a>',
    ])
    case_items = []
    for c in CASES:
        img, cat, title, desc, href, slug, status = c
        case_items.append(f'          <a href="{href}"><span>{title}</span><em>{slug}</em></a>')
    case_items.append('          <a class="dd-all" href="cases.html">查看全部案例 →</a>')
    cases_dd = "\n".join(case_items)

    svc_cls = ' class="active" aria-current="page"' if active_href == "services.html" else ""
    case_cls = ' class="active" aria-current="page"' if active_href == "cases.html" else ""
    nav = [
        link("index.html", "首頁"),
        f'      <div class="nav-item">\n        <a href="services.html"{svc_cls}>服務項目<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></a>\n        <div class="dropdown">\n{svc_dd}\n        </div>\n      </div>',
        link("pricing.html", "報價方案"),
        f'      <div class="nav-item">\n        <a href="cases.html"{case_cls}>成功案例<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m6 9 6 6 6-6"/></svg></a>\n        <div class="dropdown dropdown-cases">\n{cases_dd}\n        </div>\n      </div>',
        link("seo.html", "SEO·AEO·GEO"),
        link("about.html", "關於我們"),
        link("contact.html", "聯絡我們"),
    ]
    h = HEADER
    h = re.sub(r'<nav class="nav-main" aria-label="主要導覽">.*?</nav>',
               '<nav class="nav-main" aria-label="主要導覽">\n' + "\n".join(nav) + "\n    </nav>", h, flags=re.S)
    return h

def make_drawer(active_href):
    d_links = [
        ("index.html", "首頁", "home"), ("services.html", "服務項目", "grid"), ("pricing.html", "報價方案", "tag"),
        ("cases.html", "成功案例", "star"), ("seo.html", "SEO·AEO·GEO", "chart"),
        ("about.html", "關於我們", "info"), ("contact.html", "聯絡我們", "mail"),
    ]
    icons = {
        "home": '<path d="M3.5 10.5 12 3.5l8.5 7M5.5 9v11h13V9"/>',
        "grid": '<rect x="3.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="3.5" width="7" height="7" rx="1.5"/><rect x="3.5" y="13.5" width="7" height="7" rx="1.5"/><rect x="13.5" y="13.5" width="7" height="7" rx="1.5"/>',
        "tag": '<path d="M12 2.5 20 5v6c0 4.5-3.2 8-8 10.5C7.2 19 4 15.5 4 11V5Z"/><path d="M8.5 11.5 11 14l4.5-4.8"/>',
        "star": '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.9L12 16.9 6.8 19.7l1-5.9L3.5 9.7l5.9-.9Z"/>',
        "chart": '<path d="M4 19.5 9.5 14l4 4L20 9"/><path d="M15.5 9H20v4.5"/>',
        "info": '<circle cx="12" cy="12" r="8.5"/><path d="M12 11.5v4.5M12 7.6v.2"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    }
    items = []
    for href, label, ic in d_links:
        cls = ' class="active"' if href == active_href else ""
        items.append(f'      <a href="{href}"{cls}><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">{icons[ic]}</svg>{label}</a>')
    d = DRAWER
    d = re.sub(r'<nav>\s*.*?\s*</nav>', '<nav>\n' + "\n".join(items) + "\n    </nav>", d, flags=re.S)
    return d

def breadcrumb(crumbs):
    parts = []
    for i, (label, href) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append(f'<span aria-current="page">{label}</span>')
        else:
            parts.append(f'<a href="{href}">{label}</a><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="m9 6 6 6-6 6"/></svg>')
    return ('<nav class="breadcrumb clamp" aria-label="麵包屑導覽">' + "\n".join(parts) + "</nav>")

def write_page(fname, head, header, drawer, crumbs, main_body, footer, scripts):
    html = ("<!DOCTYPE html>\n<html lang=\"zh-Hant\" data-theme=\"dark\">\n" + head +
            "\n<body>\n\n" + header + "\n\n" + drawer + "\n\n<main>\n" + breadcrumb(crumbs) + "\n" + main_body +
            "\n</main>\n\n" + footer + "\n\n" + scripts)
    out = os.path.join(BASE, fname)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print("寫入", fname)

def jsonld_block(obj):
    if not obj:
        return ""
    return '\n<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False) + "\n</script>"

if __name__ == "__main__":
    import sys, importlib
    sys.path.insert(0, BASE)
    pages = importlib.import_module("_gen_pages").PAGES
    for p in pages:
        head = make_head(p["title"], p["desc"], p["keywords"], p["canonical"],
                         p["og_title"], p["og_desc"], p["canonical"],
                         jsonld_block(p.get("json")))
        header = make_header(p["active"])
        drawer = make_drawer(p["active"])
        crumbs = p["crumbs"]
        main_body = p["body"]
        if p.get("extra_js"):
            main_body += "\n" + p["extra_js"]
        write_page(p["file"], head, header, drawer, crumbs, main_body, FOOTER, SCRIPTS)
    print("完成：共產生", len(pages), "個頁面")

# -*- coding: utf-8 -*-
"""欣矩陣 V1 — 為其餘 6 頁補齊 SEO/AEO/GEO meta 與 schema"""
import io, os

ROOT = r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1"

# 每頁：檔案, canonical URL, breadcrumb 項目
PAGES = [
    ("services.html", "https://9return.com.tw/services.html", ["首頁", "服務項目"]),
    ("pricing.html", "https://9return.com.tw/pricing.html", ["首頁", "報價方案"]),
    ("cases.html", "https://9return.com.tw/cases.html", ["首頁", "成功案例"]),
    ("seo.html", "https://9return.com.tw/seo.html", ["首頁", "SEO 知識"]),
    ("about.html", "https://9return.com.tw/about.html", ["首頁", "關於我們"]),
    ("contact.html", "https://9return.com.tw/contact.html", ["首頁", "聯絡我們"]),
]

def patch(page, canon, crumbs):
    path = os.path.join(ROOT, page)
    with io.open(path, "r", encoding="utf-8") as f:
        s = f.read()
    orig = s
    # 1) theme-color + color-scheme
    s = s.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta name="theme-color" content="#14120E">\n<meta name="color-scheme" content="dark light">', 1)
    # 2) apple-touch-icon
    s = s.replace(
        '<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">',
        '<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">\n<link rel="apple-touch-icon" href="assets/favicon.svg">', 1)
    # 3) BreadcrumbList + WebPage schema before </head>
    last_script = s.rfind("</script>")
    head_idx = s.find("</head>")
    crumb_items = "".join(
        ',\n      { "@type": "ListItem", "position": %d, "name": "%s", "item": "%s" }' % (
            i + 1, nm, canon if i == len(crumbs) - 1 else "https://9return.com.tw/")
        for i, nm in enumerate(crumbs))
    schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [''' + crumb_items[2:] + '''
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "url": "''' + canon + '''",
  "inLanguage": "zh-TW",
  "isPartOf": { "@type": "WebSite", "url": "https://9return.com.tw/" }
}
</script>
'''
    s = s[:head_idx] + schema + s[head_idx:]
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print(page, "changed" if s != orig else "NOCHANGE")

for p in PAGES:
    patch(*p)
print("DONE")

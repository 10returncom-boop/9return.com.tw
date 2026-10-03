# -*- coding: utf-8 -*-
"""欣矩陣 V1 — 將 header 品牌改為單行「欣矩陣∞欣媒體」同大小（移除 ∞ 圖示與兩行 small）。"""
import io, os, re

ROOT = r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1"
PAGES = ["index.html","services.html","pricing.html","cases.html","seo.html","about.html","contact.html"]

# 舊 header brand 整段（含 svg .inf）
old_re = re.compile(
    r'<a class="brand" href="index\.html" aria-label="欣矩陣 ∞ 欣媒體 首頁">.*?</a>', re.S)
new_brand = ('<a class="brand" href="index.html" aria-label="欣矩陣 ∞ 欣媒體 首頁">'
             '<span>欣矩陣<span class="amp">∞</span>欣媒體</span></a>')

for p in PAGES:
    path = os.path.join(ROOT, p)
    s = io.open(path, encoding="utf-8").read()
    orig = s
    s2 = old_re.sub(lambda m: new_brand, s, count=1)
    io.open(path, "w", encoding="utf-8", newline="").write(s2)
    print(p, "changed" if s2 != orig else "NOCHANGE")
print("DONE")

# -*- coding: utf-8 -*-
"""修正 footer 品牌：移除前導 ∞ 圖示，改為「欣矩陣∞欣媒體」，∞ 金色文字、字型統一 Noto Sans TC。"""
import io, os, re

ROOT = r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1"
PAGES = ["index.html","services.html","pricing.html","cases.html","seo.html","about.html","contact.html"]

old_re = re.compile(r'<div class="footer-brand">.*?</div>', re.S)
new = ('<div class="footer-brand"><span style="font-family:\'Noto Sans TC\',sans-serif;font-weight:800">'
       '欣矩陣<span style="color:var(--warm)">∞</span>欣媒體</span></div>')

for p in PAGES:
    path = os.path.join(ROOT, p)
    s = io.open(path, encoding="utf-8").read()
    s2, n = old_re.subn(lambda m: new, s, count=1)
    io.open(path, "w", encoding="utf-8", newline="").write(s2)
    print(p, "changed" if s2 != s else "NOCHANGE", "count", n)
print("DONE")

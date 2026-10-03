# -*- coding: utf-8 -*-
"""統一全站字型為 Noto Sans TC（取代 Noto Serif TC）。"""
import io, os

ROOT = r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1"
css_dir = os.path.join(ROOT, "css")
total = 0
for fn in os.listdir(css_dir):
    if not fn.endswith(".css"):
        continue
    path = os.path.join(css_dir, fn)
    s = io.open(path, encoding="utf-8").read()
    if "Noto Serif TC" in s:
        n = s.count("Noto Serif TC")
        s2 = s.replace("Noto Serif TC", "Noto Sans TC")
        io.open(path, "w", encoding="utf-8", newline="").write(s2)
        print(fn, "replaced", n)
        total += n
print("total", total)

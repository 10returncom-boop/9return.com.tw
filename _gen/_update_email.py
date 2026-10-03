# -*- coding: utf-8 -*-
import io, os

ROOT = r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1"
FILES = [os.path.join(ROOT, "contact.html"),
         os.path.join(ROOT, "_gen_pages.py"),
         os.path.join(ROOT, "README.md")]
OLD = "hello@9return.com.tw"
NEW = "zootecture@gmail.com"

for f in FILES:
    s = io.open(f, encoding="utf-8").read()
    n = s.count(OLD)
    if n:
        s = s.replace(OLD, NEW)
        io.open(f, "w", encoding="utf-8", newline="").write(s)
    print(os.path.basename(f), "replaced", n)
print("DONE")

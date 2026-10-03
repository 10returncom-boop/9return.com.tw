# -*- coding: utf-8 -*-
import io, json, glob, os, re
root = r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1"
bad = 0; total = 0
for f in sorted(glob.glob(os.path.join(root, "*.html"))):
    s = io.open(f, encoding="utf-8").read()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    for b in blocks:
        total += 1
        try:
            json.loads(b)
        except Exception as e:
            bad += 1
            print("INVALID", os.path.basename(f), repr(e))
print("total_ldjson_blocks=", total, " bad=", bad)

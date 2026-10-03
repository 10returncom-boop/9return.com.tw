# -*- coding: utf-8 -*-
"""欣矩陣 V1 首頁：將「為何選擇欣矩陣」區段搬移到「四大服務支柱（我們做什麼）」之前。"""
import io, os

ROOT = r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1"
p = os.path.join(ROOT, "index.html")
s = io.open(p, encoding="utf-8").read()

BLOCK_START = "  <!-- ===== 為什麼選擇我們 ===== -->"
FAQ_MARK = "  <!-- ===== FAQ ===== -->"
INSERT_MARK = "  <!-- ===== 四大服務支柱 ===== -->"

bs = s.index(BLOCK_START)
be = s.index(FAQ_MARK)
block = s[bs:be].rstrip()          # 整段含開頭註解，去掉結尾空行
# 移除此區塊（含其後一個空行）
s2 = s[:bs] + s[be:]

# 插入點：四大服務支柱註解之前
ins = s2.index(INSERT_MARK)
# 確保插入點前有空行分隔
s3 = s2[:ins].rstrip() + "\n\n" + block + "\n\n" + s2[ins:]

io.open(p, "w", encoding="utf-8", newline="").write(s3)
print("moved block len=", len(block))
print("ok")

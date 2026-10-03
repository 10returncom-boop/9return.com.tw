# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        logs, fails = [], []
        pg.on("console", lambda m: logs.append("[%s] %s" % (m.type, m.text)) if m.type in ("error","warning") else None)
        pg.on("pageerror", lambda e: logs.append("[PAGEERROR] %s" % e))
        pg.on("requestfailed", lambda r: fails.append("%s %s %s" % (r.method, r.url, r.failure)))
        await pg.goto("https://9return.com.tw/services.html", wait_until="load", timeout=30000)
        await pg.wait_for_timeout(2000)
        # 檢查 footer 品牌
        fb = await pg.evaluate("""() => {
          const el = document.querySelector('.footer-brand');
          return el ? el.innerText.trim() : 'MISSING';
        }""")
        print("footer-brand text:", fb)
        print("--- console err/warn ---")
        for l in logs: print(l)
        print("--- request failed ---")
        for f in fails: print(f)
        if not logs and not fails: print("(none)")
        await b.close()

asyncio.run(main())

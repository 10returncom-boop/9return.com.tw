# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright

URL = "https://9return.com.tw/services.html"

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        logs = []
        pg.on("console", lambda m: logs.append(("[%s]" % m.type) + " " + m.text))
        pg.on("pageerror", lambda e: logs.append("[PAGEERROR] " + str(e)))
        try:
            await pg.goto(URL, wait_until="load", timeout=30000)
            await pg.wait_for_timeout(2500)
            await pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await pg.wait_for_timeout(800)
        except Exception as e:
            logs.append("[NAV-ERR] " + str(e))
        print("URL:", URL)
        print("H1:", await pg.title())
        print("--- console/pageerror ---")
        for l in logs:
            print(l)
        print("--- reveal-hidden-count ---")
        hidden = await pg.evaluate("document.querySelectorAll('.reveal:not(.in)').length")
        print("reveal not-in:", hidden)
        await b.close()

asyncio.run(main())

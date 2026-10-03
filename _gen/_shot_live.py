# -*- coding: utf-8 -*-
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1440,"height":900})
        await pg.goto("https://9return.com.tw/services.html", wait_until="load", timeout=30000)
        await pg.wait_for_timeout(1500)
        await pg.screenshot(path=r"D:\_WWW_325\325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1\_shots\live_services_full.png", full_page=True)
        # 底部版型檢查：footer 是否完整、to-top 是否正常
        info = await pg.evaluate("""() => {
          const footer = document.querySelector('footer');
          const main = document.querySelector('main');
          const hero = document.querySelector('.page-hero');
          return {
            footerBottom: footer ? footer.getBoundingClientRect().bottom + window.scrollY : null,
            pageHeight: document.body.scrollHeight,
            heroH: hero ? hero.getBoundingClientRect().height : null,
            mainChildren: main ? main.children.length : null
          };
        }""")
        print(info)
        await b.close()

asyncio.run(main())

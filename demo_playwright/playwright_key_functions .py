from playwright.async_api import async_playwright

async def playwight_function():
   async with async_playwright() as p:
      browser=await p.chromium.launch(
         headless=False
      )
      pages=await browser.new_page()

      #navigation
      await pages.goto("https://www.google.com/")

      await pages.wait_for_timeout(10000)
      await browser.close()

if __name__=="__main__":   import asyncio
asyncio.run(playwight_function())      

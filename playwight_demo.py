from playwright.sync_api import sync_playwright


def get_latest_news():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=200
        )

        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )

        page = context.new_page()

        # ✅ Direct Google News search (NO CAPTCHA)
        page.goto(
            "https://news.google.com/search?q=India%20vs%20West%20Indies&hl=en-IN&gl=IN&ceid=IN:en"
        )

        page.wait_for_load_state("networkidle")

        # simulate human reading delay
        page.wait_for_timeout(10000)

        print("\nLatest India vs West Indies News:\n")

        articles = page.locator("article")

        count = articles.count()

        for i in range(min(count, 10)):
            article = articles.nth(i)

            title = article.locator("h3").inner_text()
            link = article.locator("a").first.get_attribute("href")

            # Fix relative links
            if link.startswith("./"):
                link = "https://news.google.com" + link[1:]

            print(f"{i+1}. {title}")
            print(link)
            print()

        browser.close()


if __name__ == "__main__":
    get_latest_news()
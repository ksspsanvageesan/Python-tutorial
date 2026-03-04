from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)


def get_latest_news():
    news_list = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,      # Use True for API servers
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

        page.goto(
            "https://news.google.com/search?q=India%20vs%20West%20Indies&hl=en-IN&gl=IN&ceid=IN:en"
        )

        page.wait_for_load_state("networkidle")

        # simulate reading delay
        page.wait_for_timeout(5000)

        articles = page.locator("article")
        count = articles.count()

        for i in range(min(count, 10)):
            article = articles.nth(i)

            title = article.locator("h3").inner_text()
            link = article.locator("a").first.get_attribute("href")

            # Fix relative link
            if link and link.startswith("./"):
                link = "https://news.google.com" + link[1:]

            news_list.append({
                "title": title,
                "link": link
            })

        browser.close()

    return news_list


# ✅ API Endpoint
@app.route("/news", methods=["GET"])
def news_api():
    data = get_latest_news()
    return jsonify({
        "status": "success",
        "count": len(data),
        "news": data
    })


if __name__ == "__main__":
    app.run(debug=True)
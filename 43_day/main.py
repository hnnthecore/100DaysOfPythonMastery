import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
import csv


BASE_URL = "https://quotes.toscrape.com/page/{}/"
PAGES = 10  # scrape first 10 pages automatically
OUTPUT_JSON = "async_quotes.json"
OUTPUT_CSV = "async_quotes.csv"


async def fetch_page(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.text()


def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    for q in soup.select(".quote"):
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in q.select(".tags .tag")]

        quotes.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    return quotes


async def scrape_all():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range(1, PAGES + 1):
            url = BASE_URL.format(i)
            tasks.append(fetch_page(session, url))

        html_pages = await asyncio.gather(*tasks)

        all_quotes = []
        for html in html_pages:
            all_quotes.extend(parse_quotes(html))

        return all_quotes


def save_json(data):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_csv(data):
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        for row in data:
            writer.writerow({
                "quote": row["quote"],
                "author": row["author"],
                "tags": ", ".join(row["tags"])
            })


def main():
    print("Starting async crawl...")
    result = asyncio.run(scrape_all())

    print(f"Scraped {len(result)} quotes using async tasks.")
    save_json(result)
    save_csv(result)

    print("\nPreview:")
    for item in result[:5]:
        print(f"{item['quote']} - {item['author']}")

    print("\nDone.")


if __name__ == "__main__":
    main()

import requests
import time
import random
import json
import csv
from bs4 import BeautifulSoup


URL = "https://quotes.toscrape.com/page/{}/"

OUTPUT_JSON = "stealth_quotes.json"
OUTPUT_CSV = "stealth_quotes.csv"

PAGES = 10
RETRIES = 3


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:110.0) Gecko/20100101 Firefox/110.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
]


def fetch_page(url):
    for attempt in range(RETRIES):
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.google.com/",
            "Connection": "keep-alive"
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text

            time.sleep(1 + random.random())

        except requests.RequestException:
            time.sleep(1.5 + random.random())

    return None


def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    data = []

    quotes = soup.select(".quote")
    for q in quotes:
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in q.select(".tags .tag")]

        data.append({"quote": text, "author": author, "tags": tags})

    return data


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
    all_results = []

    for page in range(1, PAGES + 1):
        url = URL.format(page)
        print(f"Scraping page: {url}")

        html = fetch_page(url)
        if not html:
            print(f"Failed to scrape page {page}, skipping.")
            continue

        scraped = parse_page(html)
        all_results.extend(scraped)

        delay = random.uniform(1.5, 4.0)
        print(f"Sleeping {delay:.2f} seconds to avoid detection.")
        time.sleep(delay)

    save_json(all_results)
    save_csv(all_results)

    print(f"Scraped {len(all_results)} quotes total.")
    print("Export complete.")


if __name__ == "__main__":
    main()

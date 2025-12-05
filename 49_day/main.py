import requests
from bs4 import BeautifulSoup
import csv
import json

BASE_URL = "https://quotes.toscrape.com/tag/{tag}/page/{page}/"
OUTPUT_JSON = "day49_quotes.json"
OUTPUT_CSV = "day49_quotes.csv"


def fetch_tag_page(tag: str, page: int):
    url = BASE_URL.format(tag=tag, page=page)
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.text


def parse_quotes(html: str):
    soup = BeautifulSoup(html, "html.parser")
    quote_blocks = soup.select("div.quote")
    results = []

    for block in quote_blocks:
        text = block.find("span", class_="text").get_text(strip=True)
        author = block.find("small", class_="author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in block.select("div.tags a.tag")]

        results.append(
            {
                "quote": text,
                "author": author,
                "tags": tags,
            }
        )
    return results


def scrape_tag(tag: str):
    all_quotes = []
    page = 1

    while True:
        html = fetch_tag_page(tag, page)
        if not html:
            break

        quotes = parse_quotes(html)
        if not quotes:
            break

        all_quotes.extend(quotes)
        page += 1

    return all_quotes


def save_json(data):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def save_csv(data):
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        for row in data:
            writer.writerow(
                {
                    "quote": row["quote"],
                    "author": row["author"],
                    "tags": ", ".join(row["tags"]),
                }
            )


def main():
    tag = input("Enter a tag (like a hashtag, e.g. love, life, humor): ").strip().lower()
    if not tag:
        print("Tag cannot be empty.")
        return

    print(f"Scraping quotes for tag: {tag}")
    quotes = scrape_tag(tag)

    if not quotes:
        print(f"No quotes found for tag: {tag}")
        return

    save_json(quotes)
    save_csv(quotes)

    print(f"Scraped {len(quotes)} quotes for tag '{tag}'.")
    print(f"Saved to {OUTPUT_JSON} and {OUTPUT_CSV}.")


if __name__ == "__main__":
    main()

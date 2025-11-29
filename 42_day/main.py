import requests
from bs4 import BeautifulSoup
import json
import csv
from urllib.parse import urljoin


BASE_URL = "https://quotes.toscrape.com"
OUTPUT_JSON = "quotes_data.json"
OUTPUT_CSV = "quotes_data.csv"


def fetch_soup(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def extract_author_details(author_url):
    soup = fetch_soup(author_url)

    name = soup.find("h3", class_="author-title").get_text(strip=True)
    birth_date = soup.find("span", class_="author-born-date").get_text(strip=True)
    birth_place = soup.find("span", class_="author-born-location").get_text(strip=True)
    description = soup.find("div", class_="author-description").get_text(strip=True)

    return {
        "name": name,
        "birth_date": birth_date,
        "birth_place": birth_place,
        "bio": description
    }


def scrape_quotes():
    all_data = []
    authors_scraped = {}

    url = BASE_URL

    while url:
        print(f"Scraping page: {url}")
        soup = fetch_soup(url)

        for box in soup.find_all("div", class_="quote"):
            text = box.find("span", class_="text").get_text(strip=True)
            author = box.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in box.find_all("a", class_="tag")]

            author_link = urljoin(BASE_URL, box.find("a")["href"])

            if author not in authors_scraped:
                authors_scraped[author] = extract_author_details(author_link)

            entry = {
                "quote": text,
                "author": author,
                "tags": tags,
                "author_details": authors_scraped[author]
            }

            all_data.append(entry)

        next_button = soup.find("li", class_="next")
        url = urljoin(BASE_URL, next_button.a["href"]) if next_button else None

    return all_data


def save_json(data):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_csv(data):
    rows = []
    for item in data:
        rows.append({
            "quote": item["quote"],
            "author": item["author"],
            "tags": ", ".join(item["tags"]),
            "birth_date": item["author_details"]["birth_date"],
            "birth_place": item["author_details"]["birth_place"]
        })

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    print("Starting crawl...")
    data = scrape_quotes()

    print(f"Scraped {len(data)} quotes.")
    print("Saving output files...")

    save_json(data)
    save_csv(data)

    print("\nSample:")
    for item in data[:3]:
        print(f"{item['quote']} - {item['author']}")

    print("\nDone.")


if __name__ == "__main__":
    main()

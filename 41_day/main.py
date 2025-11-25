import requests
from bs4 import BeautifulSoup
import json
import csv


URL = "https://www.w3schools.com/html/html_tables.asp"
OUTPUT_JSON = "table_data.json"
OUTPUT_CSV = "table_data.csv"


def fetch_html(url):
    """Fetch webpage and return BeautifulSoup object."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def parse_table(soup):
    """Parse HTML table and return list of dicts."""
    table = soup.find("table", id="customers")
    rows = table.find_all("tr")

    headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]

    data = []
    for row in rows[1:]:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]

        # Skip incomplete rows
        if len(cols) != len(headers):
            continue

        entry = dict(zip(headers, cols))
        data.append(entry)

    return data


def save_json(data, filename):
    """Save list of dicts to JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_csv(data, filename):
    """Save list of dicts to CSV."""
    if not data:
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main():
    print("Fetching HTML...")
    soup = fetch_html(URL)

    print("Parsing table data...")
    table_data = parse_table(soup)

    print(f"Extracted {len(table_data)} rows.")

    print("Saving JSON and CSV files...")
    save_json(table_data, OUTPUT_JSON)
    save_csv(table_data, OUTPUT_CSV)

    print("\nSample preview:")
    for item in table_data[:3]:
        print(item)

    print("\nDone.")


if __name__ == "__main__":
    main()

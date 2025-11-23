import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

BASE_URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "jobs.csv"


def fetch_page(url):
    """Fetch a single page and return BeautifulSoup object."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def extract_jobs_from_page(soup):
    """Extract job postings from a soup page."""
    jobs = []

    cards = soup.find_all("div", class_="card-content")
    for card in cards:
        title_elem = card.find("h2", class_="title")
        company_elem = card.find("h3", class_="subtitle")
        location_elem = card.find("p", class_="location")

        link_elem = card.find("a", string="Apply")
        link = urljoin(BASE_URL, link_elem["href"]) if link_elem else ""

        title = title_elem.get_text(strip=True) if title_elem else "N/A"
        company = company_elem.get_text(strip=True) if company_elem else "N/A"
        location = location_elem.get_text(strip=True) if location_elem else "N/A"

        jobs.append(
            {
                "title": title,
                "company": company,
                "location": location,
                "apply_link": link,
            }
        )

    return jobs


def find_next_page(soup):
    """Return the URL for the next page if it exists, otherwise None."""
    next_button = soup.find("a", string="Next")
    if next_button and "href" in next_button.attrs:
        return urljoin(BASE_URL, next_button["href"])
    return None


def scrape_all_jobs():
    """Scrape all jobs across all pages."""
    all_jobs = []
    current_url = BASE_URL

    print("Starting job scrape...")

    while current_url:
        print(f"Fetching: {current_url}")
        soup = fetch_page(current_url)
        jobs = extract_jobs_from_page(soup)
        print(f"Found {len(jobs)} jobs on this page.")
        all_jobs.extend(jobs)
        current_url = find_next_page(soup)

    print(f"Total jobs collected: {len(all_jobs)}")
    return all_jobs


def save_to_csv(jobs, filename):
    """Save jobs list to CSV file."""
    fieldnames = ["title", "company", "location", "apply_link"]
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)


def main():
    jobs = scrape_all_jobs()
    if not jobs:
        print("No jobs found. Exiting.")
        return

    save_to_csv(jobs, OUTPUT_FILE)
    print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}.")

    print("\nSample results:")
    for job in jobs[:5]:
        print(f"- {job['title']} at {job['company']} ({job['location']})")


if __name__ == "__main__":
    main()

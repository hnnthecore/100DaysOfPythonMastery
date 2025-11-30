import time
import json
import csv
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://books.toscrape.com/"
PAGES_TO_SCRAPE = 3  # scrape first 3 pages

OUTPUT_JSON = "books_day45.json"
OUTPUT_CSV = "books_day45.csv"


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


def open_site(driver):
    driver.get(BASE_URL)
    time.sleep(2)


def scrape_page(driver):
    books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    results = []

    for book in books:
        # Title
        try:
            title_el = book.find_element(By.CSS_SELECTOR, "h3 a")
            title = title_el.get_attribute("title").strip()
        except Exception:
            continue

        # Price
        try:
            price = book.find_element(By.CSS_SELECTOR, "p.price_color").text.strip()
        except Exception:
            price = "N/A"

        # Rating
        try:
            rating_el = book.find_element(By.CSS_SELECTOR, "p.star-rating")
            classes = rating_el.get_attribute("class").split()
            rating = [c for c in classes if c != "star-rating"][0] if len(classes) > 1 else "N/A"
        except Exception:
            rating = "N/A"

        # Link
        try:
            rel_link = title_el.get_attribute("href")
            link = rel_link
        except Exception:
            link = "N/A"

        results.append(
            {
                "title": title,
                "price": price,
                "rating": rating,
                "link": link,
            }
        )

    return results


def go_to_next_page(driver):
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        next_url = urljoin(driver.current_url, next_button.get_attribute("href"))
        driver.get(next_url)
        time.sleep(2)
        return True
    except Exception:
        return False


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_csv(data, filename):
    if not data:
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["title", "price", "rating", "link"]
        )
        writer.writeheader()
        writer.writerows(data)


def main():
    driver = setup_driver()
    all_books = []

    try:
        open_site(driver)

        current_page = 1
        while current_page <= PAGES_TO_SCRAPE:
            print(f"Scraping page {current_page}...")
            page_data = scrape_page(driver)
            print(f"Found {len(page_data)} books on this page.")
            all_books.extend(page_data)

            if current_page == PAGES_TO_SCRAPE:
                break

            if not go_to_next_page(driver):
                break

            current_page += 1

        print(f"Total books scraped: {len(all_books)}")

        save_json(all_books, OUTPUT_JSON)
        save_csv(all_books, OUTPUT_CSV)

        driver.save_screenshot("day45_books.png")
        print("Screenshot saved as day45_books.png")

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()

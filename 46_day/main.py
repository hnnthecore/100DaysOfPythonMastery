import time
import json
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.bbc.com/news"
SCROLL_STEPS = 7     # how many scroll-down screenshots to capture
SCROLL_PAUSE = 2     # seconds between scrolls

OUTPUT_JSON = "day46_news.json"
OUTPUT_CSV = "day46_news.csv"


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def scroll_and_capture(driver):
    screenshots = []
    for i in range(1, SCROLL_STEPS + 1):
        filename = f"day46_frame_{i}.png"
        driver.save_screenshot(filename)
        screenshots.append(filename)

        driver.execute_script("window.scrollBy(0, document.body.scrollHeight/3);")
        time.sleep(SCROLL_PAUSE)

    return screenshots


def scrape_news(driver):
    articles = driver.find_elements(By.CSS_SELECTOR, "article")
    results = []

    for art in articles:
        try:
            headline = art.find_element(By.CSS_SELECTOR, "h2").text.strip()
        except:
            continue

        try:
            link = art.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        except:
            link = "N/A"

        try:
            category = art.find_element(By.CSS_SELECTOR, "[data-testid=card-metadata-tag]").text.strip()
        except:
            category = "Uncategorized"

        results.append({
            "headline": headline,
            "category": category,
            "link": link
        })

    return results


def save_json(data):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def save_csv(data):
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["headline", "category", "link"])
        writer.writeheader()
        writer.writerows(data)


def main():
    driver = setup_driver()

    try:
        driver.get(URL)
        time.sleep(3)

        frames = scroll_and_capture(driver)
        scraped = scrape_news(driver)

        save_json(scraped)
        save_csv(scraped)

        print(f"Captured {len(frames)} screenshots.")
        print(f"Extracted {len(scraped)} news articles.")

    except Exception as e:
        print("Error:", e)

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    main()

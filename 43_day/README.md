# ⚡ Day 43 – AsyncCrawler: Parallel Web Scraper

Speed isn't magic — it's concurrency executed with intent.

---------------------------------------------------------

## 🧠 Concepts Practised
- Asynchronous scraping using aiohttp
- Parallel fetching using asyncio
- Fast multi-page extraction
- Parsing HTML with BeautifulSoup
- Exporting data to JSON & CSV
- Scaling scrapers for automation

---------------------------------------------------------

## 💡 Project Overview

AsyncCrawler scrapes multiple pages at once instead of sequentially.  
Target: https://quotes.toscrape.com/page/1/

You set page count inside main.py:
    PAGES = 10

The scraper:
- Builds URLs automatically
- Fetches all pages in parallel
- Extracts quote + author + tags
- Saves output to:
    async_quotes.json
    async_quotes.csv

---------------------------------------------------------

## ⚙ Features
• Scrapes many pages simultaneously  
• Much faster than requests-based scraping  
• Clean structured JSON output  
• CSV export for Excel/Sheets  
• Scales to 20/50/100+ pages easily  
• No Selenium needed

---------------------------------------------------------

## 📸 Sample output

![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day43_output.png)

---------------------------------------------------------

## 🚀 How to Run

Install dependencies:
    pip install aiohttp beautifulsoup4

Run script:
    python main.py

Generated files:
    async_quotes.json
    async_quotes.csv

---------------------------------------------------------

## 📝 Notes
• Async crawler = massive speed improvement  
• Ideal for pagination scraping  
• Next step before anti-blocking + rotation

---------------------------------------------------------

## 🎯 Takeaways
You now know how to:
• Run async scrapers  
• Fetch data in parallel  
• Export datasets cleanly  
• Scale scrapers beyond Day 42


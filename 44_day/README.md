# 🥷 Day 44 – StealthCrawler: Anti-Scraping + Header Rotation Engine

## Concepts Practised
• Fake browser identity with rotated User-Agents  
• Spoof headers: Accept-Language, Referer, Encoding  
• Random request delay to mimic human behaviour  
• Retry system to survive blocked responses  
• Error-tolerant scraping workflow  
• JSON & CSV export like production bots

---------------------------------------------------------------------

## Project Overview

StealthCrawler scrapes quotes.toscrape.com while avoiding basic bot detection.

Instead of sending repeated identical requests (risky), the bot:
    • randomizes user-agent each request
    • sleeps between 1.5-4s randomly
    • retries failed requests up to 3 times
    • uses browser-like request headers

This simulates real human browsing patterns.

Output files:
    stealth_quotes.json
    stealth_quotes.csv

---------------------------------------------------------------------

## Features
• Anti-scraping safe behaviour  
• Random headers + UA impersonation  
• Retries if site blocks or throttles  
• Graceful fail recovery  
• JSON + CSV export  
• Fully production-style design  

---------------------------------------------------------------------

## How to Run

Install dependencies:
    pip install requests beautifulsoup4 fake-useragent

Run script:
    python main.py

Output generated:
    stealth_quotes.json
    stealth_quotes.csv

---------------------------------------------------------------------

## Output Screenshot 

![ouput](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day44_output.png)

---------------------------------------------------------------------

## Takeaways
Today you learned:
• How to hide your scraper signature  
• How to rotate headers + UA randomly  
• How to retry requests without breaking  
• How to scrape like a real user  


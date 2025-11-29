# 🕸 Day 42 – MiniCrawler: Multi-Page Quote & Author Spider

> *"Scrapers don’t collect data — they extract truth buried in markup."*

---

## 🧠 Concepts Practised
- Multi-page web crawling using `requests`
- HTML parsing with `BeautifulSoup`
- Following links recursively through pagination
- Extracting nested content (quotes → author page → biography)
- Avoiding duplicate requests with caching
- Normalizing structured data
- Exporting JSON + CSV datasets
- Building scalable scraper architecture

---

## 💡 Project Overview
**MiniCrawler** is a multi-layer web scraping engine that crawls through an entire website, page by page, extracting every quote and its author details.

It targets:


Unlike single-page scrapers, this bot automatically:

1. Loads initial quote page  
2. Extracts quotes, tags, and author names  
3. Follows the **Next** page links  
4. Enters each author profile  
5. Scrapes biography, birthdate, birthplace  
6. Saves everything into clean JSON + CSV outputs  

This introduces you to **real crawler-level scraping**, where data is spread across multiple pages.

---

## ⚙ Features
- Complete site traversal  
- Detailed author metadata extraction  
- Caches authors to prevent repeated scraping  
- Saves structured JSON  
- Saves flattened CSV view  
- Terminal preview of collected samples  
- Handles pagination intelligently  

---

## 📸 Screenshots & Output

![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day42_output.png)

---

## 🚀 How to Run

1. Install required modules:
```bash
pip install requests beautifulsoup4

# 🛒 Day 45 – BookStoreBot: Selenium Browser Automation Scraper

> *"When requests fail — automation steps in."*

---

### 🧠 Concepts Practised
- Browser automation using Selenium  
- Dynamic webpage scraping with live DOM control  
- CSS selectors for real-element extraction  
- Pagination navigation using next-page detection  
- Automated dataset export to JSON + CSV  
- Screenshot capturing for visual output reference  
- Scalable web-scraping architecture with retries & waits  

---

### 💡 Project Overview
**BookStoreBot** is a Selenium-powered automation agent that scrapes book listings directly from a live website:
[link](https://books.toscrape.com/)

Unlike traditional HTTP scraping, this system loads a real browser instance — allowing you to handle dynamic pages, scripts, real-time elements, and interactive navigation.

The bot scrolls through multiple pages, extracts book info, captures a screenshot, and saves structured datasets for future analysis or ML/NLP training.

---

### ⚙️ Features
✅ Fully automated browser-based scraping  
✅ Extracts Title, Price, Rating & Source URL  
✅ Multi-page crawler (configurable depth)  
✅ Exports JSON + CSV datasets  
✅ Saves browser screenshot for verification  
✅ Zero API usage — works fully offline after code execution  
✅ Perfect first step before advanced Selenium automation  

---

### 🔍 Data Captured Per Book
| Field | Description |
|-------|-------------|
| Title | Book/Product name |
| Price | Displayed retail price |
| Rating | Star rating value extracted from CSS |
| Link | Direct product detail page URL |

---

### 🧩 Screenshots & Output
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day45_books.png)

### 🚀 How to Run

1) Install required packages:
2) Execute the bot:
3) After completion, the following files are generated:
books_day45.json
books_day45.csv
day45_books.png


Open them to explore extracted book data visually and programmatically.

---

### 📝 Notes
- This marks your transition from request-based scraping to full browser automation  
- Selenium enables interaction with dynamic content, JS rendering, and live UI workflows  
- From here, login automation, form filling, infinite scrolling & web-autonomous tasks become possible  

---

### 🎯 Takeaways
By completing this project, you now understand:
- How to launch and automate Chrome using Selenium  
- How to detect & extract live DOM elements  
- How to paginate, scrape, format, and export real data  
- How automation can bypass static scraping limitations  

Day 45 unlocks a new tier — **you now control the browser itself.**


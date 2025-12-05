# 🔖 Day 49 – HashScope: Tag-Based Quote Scraper

> *"If Instagram hashtags were legal to scrape — this is how they would feel."*

---

### 🧠 Concepts Practised
- Web scraping with BeautifulSoup  
- Paginated scraping (page 1 → page N)  
- Dynamic URL construction  
- Handling missing pages and graceful exits  
- JSON and CSV structured export  
- CLI-based tag input simulation (like hashtag search)  
- Text extraction from HTML blocks  

---

### 💡 Project Overview
**HashScope** is a safe, legal “hashtag-style” scraper inspired by Instagram's tag explorer — but built on a website designed for scraping practice.

You give it a **tag** (e.g. `love`, `life`, `humor`, `inspirational`)  
and it automatically:

- Visits all pages matching that tag  
- Extracts quotes, authors, and tag lists  
- Saves everything into JSON + CSV formats  

This project teaches you how to simulate hashtag exploration *without* violating any website’s terms of service.  
It mirrors the logic of “scroll through posts by hashtag,” but in a safe environment.

---

### ⚙️ Features
✔ Tag-based scraping (like hashtags)  
✔ Scrapes all pages automatically  
✔ Extracts quote, author, and tags  
✔ Saves clean JSON & CSV datasets  
✔ No login, no authentication, no API keys  
✔ Fully legal and supported test site  

---

### 🖼 Output Preview

![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day49_output.png)


---

### 🚀 How to Run

Install required libraries:
```bash
pip install requests beautifulsoup4

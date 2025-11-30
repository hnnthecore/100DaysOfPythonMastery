# 📰 Day 46 – AutoScroll NewsBot: Selenium Visual Scraper

> *"If the data won't come to you — scroll until it does."*

---

### 🧠 Concepts Practised
- Selenium browser automation  
- Live webpage scraping with dynamic DOM interaction  
- Automated scrolling simulation (human-like behaviour)  
- Multi-frame screenshot capture  
- News headline extraction with category & links  
- JSON & CSV structured dataset export  
- Handling multiple page states without API access  

---

### 💡 Project Overview
**AutoScroll NewsBot** is a visual automation agent that browses BBC News like a human — scrolls gradually, captures multiple screenshots, and extracts article data directly from the rendered webpage.

Instead of relying on static requests, this bot controls an actual browser, enabling it to collect live, JavaScript-loaded headlines reliably. The result is both visual (screenshots) and analytical (JSON/CSV export).

This marks your entry into real automation workflows.

---

### ⚙️ Features
✅ Human-like scrolling behaviour  
✅ Multi-frame screenshot timeline  
✅ Extracts headline + category + article link  
✅ Exports to JSON + CSV datasets  
✅ Works without API keys or login  
✅ Fully Selenium-driven real browser automation  
✅ No fragile form sites, no dead links  

---

### 🧩 Screenshots & Output

#### 📸 Scroll Frame Captures
![ss](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/46_day/day46_frame_1.png)
![ss](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/46_day/day46_frame_2.png)
![ss](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/46_day/day46_frame_3.png)



---

### 🚀 How to Run

Install requirements:
    pip install selenium webdriver-manager

Run script:
    python main.py

Generated files:
    day46_news.json
    day46_news.csv
    day46_frame_1.png → day46_frame_n.png

The number of frames depends on scroll depth configured in SCROLL_STEPS.

---

### 📝 Notes
- Uses Selenium to simulate real browsing instead of raw HTTP requests  
- Works reliably with dynamic content and news feeds  
- Screenshots create a visual audit trail of runtime behaviour  
- Code can scale into full-page screenshot stitching or continuous monitoring  

---

### 🎯 Takeaways
You learned how to:
• Control Chrome with Selenium  
• Scroll & visually document webpage state  
• Extract headlines dynamically  
• Produce structured data exports at scale  

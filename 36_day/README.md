# 📰 Day 36 – NewsFlash: Live News Headlines Reader

> "A Tkinter-powered desktop app that fetches and displays live news headlines from free, public RSS feeds."

---
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/news.gif)
## 🧠 Concepts Practised
- Tkinter GUI layout & scrollable content  
- RSS feed parsing (XML parsing with `ElementTree`)  
- Threading for non-freezing UI  
- HTTP requests with user-agent headers  
- Webbrowser integration for opening articles  
- Clean UI card-style layout  
- Error handling and network-failure fallback  

---

## 💡 Project Overview
**NewsFlash** is a live news reader built with Tkinter.  
It fetches headlines from public, completely free RSS feeds (no API keys or login required).

The user selects a news source, and the app displays:
- Top 10 headlines  
- Article titles  
- Clickable links that open in the browser  

Everything loads on a background thread, keeping the UI smooth even during fetching.

---

## ⚙️ Features

### ✔ Multiple News Sources  
Supports free RSS feeds such as:
- BBC News  
- Reuters World  
- ABC Top Stories  

### ✔ Live Headline Fetching  
Retrieves fresh headlines each time you click **Load Headlines**.

### ✔ Clickable Cards  
Each headline includes a button to open the full article in your web browser.

### ✔ Threaded API Calls  
Prevents GUI freezing while fetching or parsing RSS.

### ✔ Clean User Interface  
Simple two-column layout with white news cards and padded spacing.

### ✔ Error Handling  
Shows messages when:
- No internet  
- RSS feed fails  
- Bad or empty data  

---

## 🖼️ Screenshot / Output  
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day36_output.png)


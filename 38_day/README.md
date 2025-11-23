# 📚 Day 38 – BookFinder: Book Search & Details Explorer

> *"A room without books is like a body without a soul." — Cicero*

---

## 🧠 Concepts Practised
- Fetching data from a public API using `requests`
- Passing parameters using `params`
- JSON parsing and safe data extraction
- Tkinter GUI development (frames, listbox, panels, text widgets)
- Image loading & resizing using Pillow
- Background threading to avoid UI freezing
- Clean UI/UX layout structure
- Error handling for missing fields or network errors

---

## 💡 Project Overview
**BookFinder** is a Tkinter-powered desktop application that lets you search books instantly using the **Google Books API** (no API key required).

Type a book title, author name, or keyword, and the app fetches:

- Book cover  
- Title & subtitle  
- Authors  
- Publisher  
- Genres / categories  
- Published date  
- Page count  
- Language  
- Rating & rating count  
- Full book description  

The UI has two main panels:

- **Left panel**: Search results list  
- **Right panel**: Book details + cover image

---

## ⚙️ Features
- Live search using Google Books API  
- Auto-loaded book covers  
- Clean and readable details panel  
- Sidebar results list  
- Threaded API fetch (no UI freezing)  
- Graceful fallback for missing data  
- Fully responsive Tkinter GUI  

---

## 📸 Screenshots & Output
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day38_output.png)


---

## 🚀 How to Run

1. Install required libraries:
```bash
pip install requests pillow


Example:

# 📊 Day 41 – HTMLParser Pro: Advanced HTML Structure Extractor

> *"The web hides structure in plain sight — your job is to reveal it."*

---

## 🧠 Concepts Practised
- Fetching raw HTML using `requests`
- Parsing structured tables with `BeautifulSoup`
- Understanding DOM hierarchy (rows, headers, cells)
- Handling missing or malformed HTML safely
- Normalizing unstructured data into consistent formats
- Exporting parsed data to **JSON** and **CSV**
- Clean CLI-based data extraction workflow

---

## 💡 Project Overview
**HTMLParser Pro** is a web-scraping utility that extracts structured table data from HTML pages and converts it into clean, machine-readable formats.

It uses the public W3Schools HTML Tables demo page:
[link](https://www.w3schools.com/html/html_tables.asp)


Your script loads the page, parses the `#customers` table, and extracts:

- Company  
- Contact  
- Country  

Then saves the results into:

- `table_data.json`
- `table_data.csv`

This project is a crucial stepping stone before learning Selenium because it forces you to understand **real HTML table structure**, which is essential for automating browser interactions later.

---

## ⚙️ Features
- Automatic table detection  
- Header extraction  
- Row normalization  
- Clean JSON export  
- Clean CSV export  
- Terminal preview of extracted data  
- Works on any static HTML table with minimal modifications  

---

## 📸 Screenshots & Output

### 1. Program Output (Terminal Preview)
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day41_output.png)

---

### 2. Extracted JSON File  
![output json](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day41_tablejson.png)

---

### 3. Extracted CSV File  
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day41_csv.png) 

---

## 🚀 How to Run

1. Install dependencies:
```bash
pip install requests beautifulsoup4

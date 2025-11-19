# 💱 Day 35 – FXDesk: Real-Time Currency Converter

> "A clean Tkinter GUI app that converts currency using a completely free, no-key required exchange rate API."

---

## 🧠 Concepts Practised
- Tkinter GUI layout & widget design  
- Combobox usage for dropdown currency selection  
- Real-time API data fetching  
- Threading for smooth, non-blocking GUI  
- Exception handling  
- Calculating conversions via base currency  
- Updating UI dynamically  

---

## 💡 Project Overview
**FXDesk** is a real-time currency converter built with Tkinter.  
It uses the **ER-API** (open, free, no login required) to fetch live exchange rates and convert between 160+ currencies instantly.

The interface allows you to:
- Select a source currency  
- Enter an amount  
- Select a target currency  
- Convert using accurate, real-time rates  

Threading ensures the GUI remains smooth during API requests.

---

## ⚙️ Features

### ✔ Live Exchange Rates  
Fetched from **https://open.er-api.com** – free and requires no API key.

### ✔ Currency Selection  
Dropdowns for selecting source and target currencies.

### ✔ Multi-Threaded API Calls  
Prevents UI freezing during network operations.

### ✔ Clean UI  
Soft palette, centered layout, and clear typography.

### ✔ Error Handling  
Gracefully handles invalid inputs or connection issues.

---

## 🖼️ Screenshot / Output
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day35_output.png)


---

## ▶️ How to Run

1. Install required dependencies:
```bash
pip install requests

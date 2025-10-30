# 💹 Day 15 – CryptoPulse: Real-Time Cryptocurrency Tracker

> *“Because markets never sleep — and neither does Python.”*

---
![gif](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/crypto.gif)
### 🧠 Concepts Practised
- Using **public REST APIs** for real-time financial data  
- Parsing structured **JSON** responses  
- Building clean, dynamic **console dashboards**  
- Handling **multi-currency conversions** and **percentage change calculations**  
- Logging market snapshots persistently with **timestamps**  
- Displaying formatted tabular data with Unicode icons and visuals  

---

### 💡 Project Overview
**CryptoPulse** is a **real-time cryptocurrency dashboard** that fetches live data from the free **CoinGecko API** and displays key market metrics such as:

- 💰 Current Price (USD, CHF, EUR, INR)  
- 📈 24-hour Percentage Change  
- 💹 Market Capitalization  
- 🕒 Timestamp of data retrieval  

It also **saves each data snapshot** to a JSON file, allowing you to track your watchlist trends over time and review your recent sessions.

---

### 📈 Features
- 🔄 Fetches **live crypto prices** for any combination of coins (e.g., Bitcoin, Ethereum, Solana)  
- 💵 Displays prices in **multiple currencies** — USD, CHF, EUR, and INR  
- 📊 Shows **24-hour change percentage** with up/down arrows (📈 / 📉)  
- 💾 Automatically logs results in `crypto_log.json`  
- 🕰 Displays **last 3 session timestamps** for quick glance at recent activity  
- ⚙️ Built entirely using **Python + CoinGecko API (no key required)**  

---

### 🧩 Screenshots

#### 💻 Console Dashboard Output
 
![CryptoPulse Dashboard](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day15_output.png)

#### 💾 JSON Log File
![CryptoPulse Log File](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day15_file.png)

---

### 🚀 Run the Program
```bash
python main.py

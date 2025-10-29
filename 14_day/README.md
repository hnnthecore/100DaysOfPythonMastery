# 🌍 Day 14 – DataPulse: Live Weather & Stats Dashboard

> *“Because data isn’t just numbers — it’s the pulse of the planet.”*

---
![meme](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/forget-check-weather-forecast.png)
### 🧠 Concepts Practised
- Working with **APIs** and handling **HTTP requests**
- Parsing and processing **JSON data**
- Building real-time console interfaces
- Logging live data with timestamps
- Handling errors and edge cases in real-world data
- Formatting dynamic output for better readability

---

### 💡 Project Overview
**DataPulse** is a live weather dashboard powered by the **Open-Meteo API** — a free, real-time weather data source.  
It fetches the latest temperature, wind speed, and conditions for cities like **Zurich**, **Geneva**, **Tokyo**, and more.  

The dashboard not only displays this data beautifully in the terminal (with weather emojis and clean formatting)  
but also **saves every lookup** into a `weather_log.json` file — allowing you to view your recent trends anytime.

---

### 📈 Features
- 🌦️ **Live Weather Data** fetched directly from Open-Meteo API  
- 🧾 **JSON Log Storage** for all previous sessions  
- 🕒 **Timestamped Records** for each weather check  
- 🌍 **City Database** (Zurich, Geneva, Bern, Basel, Lausanne, London, etc.)  
- 💾 **Auto Logging System** — maintains last 5 entries in `weather_log.json`  
- ⚙️ **Graceful Error Handling** for network issues and unknown cities  

---

### 🧩 Screenshots

#### 💻 Console Weather Dashboard
![DataPulse Weather Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day14_output.png)

#### 💾 JSON Log History
![DataPulse JSON Log](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day14_json.png)

---

### 🚀 Run the Program
```bash
python main.py

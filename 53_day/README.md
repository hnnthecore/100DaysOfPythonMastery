# 🌤️ Day 53 – WeatherSphere: Interactive Weather Dashboard

> *"Forecasts are clearer when you can see the whole picture."*

---

### 🧠 Concepts Practised
- Consuming public APIs (wttr.in – no key required)  
- Parsing JSON weather data  
- GUI dashboard design using Tkinter  
- Embedding Matplotlib charts inside a Tkinter window  
- Bar-chart visualization of temperature forecasts  
- Implementing local JSON caching for offline support  
- Error handling for network failures  
- Clean UI layout structuring  

---

### 💡 Project Overview
**WeatherSphere** is a desktop weather dashboard that retrieves live weather data for any city and displays it in a clean, visual format.

It shows:
- Current temperature  
- Humidity  
- Wind speed  
- A 3-day temperature forecast chart  
- Cached weather results when offline  

The app uses the **wttr.in weather API**, which requires **no API key**, making it perfect for beginner-friendly and stable projects.

---

### ⚙️ Features
✔ Live weather data for any city  
✔ Beautiful 3-day forecast bar chart  
✔ No API keys or login required  
✔ Cached data for offline viewing  
✔ Temperature, humidity, wind, conditions  
✔ Clean Tkinter GUI  
✔ Safe and reliable API source  
✔ Fully offline after the first load  

---

### 🖼️ Screenshot Preview

![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day53_output.png)

---

### 🚀 How to Run

Install required libraries:
```bash
pip install requests matplotlib

# 🧭 Day 92 – Focus Timer (GUI with Tkinter)

> *“Focus isn’t about doing more — it’s about doing one thing well.”*

---


### 🧠 Concepts Practised
- GUI development using Tkinter  
- Event-driven programming  
- Using `after()` for non-blocking timers  
- Handling user input in GUI applications  
- Basic state management in UI apps  
- Writing efficient, lightweight desktop tools  

---

### 💡 Project Overview
The **Focus Timer** is a minimal, GUI-based productivity tool inspired by the Pomodoro technique.

The application allows users to:
- Set a focus duration  
- Set a break duration  
- Start a single focus session  
- View a live countdown timer  
- Automatically switch from focus time to break time  

Unlike CLI timers, this version provides a **clean visual interface** while remaining lightweight and CPU-safe.

---

### 🧩 Sample Output
![Focus Timer Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day92_output.png)

- Clean and minimal GUI  
- Live countdown updates every second  
- Popup alerts for focus completion and breaks  
- Smooth transition between focus and break sessions  

This demonstrates proper **event-based GUI timing** without blocking the application.

---

### 🧠 Key Learning
You learned how to:
- Build GUI applications using Tkinter  
- Manage time-based events without `while` loops  
- Use `after()` for safe, scheduled updates  
- Design responsive desktop applications  
- Structure GUI logic cleanly and readably  

These are essential skills for building **desktop tools and lightweight applications** in Python.

---

### 🚀 Run the Program
1. Ensure Python is installed  
2. Run the application:
   ```bash
   python main.py

# 🧭 Day 77 – URL Shortener with Real-Time Analytics (Flask & SQLite)

> *"Backends become powerful when they measure behavior, not just store data."*

---


### 🧠 Concepts Practised
- Designing backend services instead of simple CRUD apps  
- URL shortening and redirection logic  
- Generating unique short identifiers  
- Event-based analytics tracking  
- Logging user behavior (click events)  
- Storing timestamps and IP addresses  
- Database relationships between entities  
- Building analytics and reporting views  

---

### 💡 Project Overview
This project upgrades the URL Shortener into a **real analytics-enabled backend service**.

The application allows users to:
- Convert long URLs into short links  
- Redirect users using short URLs  
- Track every click as an analytics event  
- Store click metadata such as:
  - IP address  
  - Timestamp  
- View analytics reports for each short URL  

Instead of focusing on authentication or UI-heavy features, this project emphasizes **backend intelligence and data tracking**, similar to real-world SaaS systems.

---

### 🧩 Sample Output
![URL Analytics Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day77_output_1.png)
![URL Analytics Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day77_output_2.png)
- Short URLs redirect correctly to original links  
- Every redirect logs a click event  
- Analytics page displays:
  - Total clicks  
  - Click timestamps  
  - Visitor IP addresses  

This demonstrates a complete **generate → track → analyze** backend workflow.

---

### 🧠 Key Learning
You learned how to:
- Build backend services that track user behavior  
- Design database schemas for analytics data  
- Log events during request handling  
- Work with timestamps and request metadata  
- Separate service logic from presentation  
- Think beyond CRUD and focus on backend systems  

This project introduces **analytics-driven backend thinking**, a key skill for scalable applications.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

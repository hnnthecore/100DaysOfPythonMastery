# 🧭 Day 78 – System Status Monitor Dashboard (Flask & SQLite)

> *"Reliable systems are built by observing failures, not ignoring them."*

---

### 🧠 Concepts Practised
- Backend observability fundamentals  
- Designing monitoring-style dashboards  
- Status-based state management  
- Logging historical events with timestamps  
- Using SQLite for time-series–like data  
- Building admin-style interfaces  
- Separating current state from historical logs  

---

### 💡 Project Overview
This project introduces a **System Status Monitor Dashboard**, inspired by real-world DevOps and admin tools.

The application allows users to:
- Add services (API, Website, Database, etc.)  
- Assign a current status:
  - 🟢 Online  
  - 🟡 Degraded  
  - 🔴 Down  
- Update service status at any time  
- Automatically log every status change with a timestamp  
- View both **current system state** and **historical status logs**

Instead of focusing on users or analytics, this project emphasizes **observability and system health tracking**, a critical backend concept.

---

### 🧩 Sample Output
![System Monitor Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day78_output_1.png)
![System Monitor Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day78_output_2.png)

- Card-based dashboard displaying service status  
- Visual status indicators for quick scanning  
- Buttons to update service state instantly  
- Historical logs recording every status change  

This demonstrates a complete **monitor → update → log → observe** workflow.

---

### 🧠 Key Learning
You learned how to:
- Think in terms of system monitoring and observability  
- Model current state vs historical data  
- Log backend events with timestamps  
- Build dashboard-style UIs for admin tools  
- Use SQLite beyond simple CRUD apps  
- Design backend systems that track behavior over time  

These skills are foundational for building **admin panels, DevOps tools, and SaaS dashboards**.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

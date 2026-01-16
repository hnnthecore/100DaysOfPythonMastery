# 🧭 Day 90 – API Rate Limiter & Abuse Detection Engine

> *“Most systems don’t fail from bugs — they fail from abuse.”*

---


### 🧠 Concepts Practised
- Rate limiting fundamentals  
- Token Bucket algorithm  
- Time-based request control  
- Burst traffic handling  
- Abuse and misuse prevention  
- Infrastructure-level backend thinking  
- Defensive system design  

---

### 💡 Project Overview
This project implements an **API Rate Limiter & Abuse Detection Engine**, a core building block of real-world backend infrastructure.

Instead of building features or interfaces, this system focuses on **protecting backend services** by controlling how frequently clients can make requests.

The engine:
- Allows a limited number of requests  
- Supports short traffic bursts  
- Refills capacity gradually over time  
- Blocks requests when limits are exceeded  

This is the same foundational logic used in **API gateways, cloud platforms, and security layers**.

---

### 🧩 Sample Output
![API Rate Limiter Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day90_output.png)

- Requests allowed until token capacity is reached  
- Excess requests are rate-limited  
- Requests resume as tokens refill over time  
- Clear visibility into traffic control behavior  

This visually demonstrates how **burst traffic is handled safely** without crashing the system.

---

### 🧠 Key Learning
You learned how to:
- Implement rate limiting using time-based algorithms  
- Control access to backend resources fairly  
- Handle burst traffic without rejecting all users  
- Prevent abuse without complex authentication  
- Think like an infrastructure engineer  
- Understand how real API gateways work internally  

These concepts are essential for **scalable, secure backend systems**.

---

### 🚀 Run the Program
1. Ensure Python is installed  
2. Run the simulation:
   ```bash
   python main.py

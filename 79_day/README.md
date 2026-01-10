# 🧭 Day 79 – Feature Flags & A/B Testing System (Flask & SQLite)

> *"Great products don’t ship one version — they test many."*

---


### 🧠 Concepts Practised
- Feature flags and rollout strategies  
- A/B testing fundamentals  
- Backend-driven UI decisions  
- Deterministic user bucketing using hashing  
- Percentage-based feature rollout  
- SQLite-backed configuration storage  
- Product experimentation logic  

---

### 💡 Project Overview
This project implements a **Feature Flag and A/B Testing system**, a technique widely used in modern SaaS products.

The backend dynamically decides whether a user should see a new feature based on:
- A predefined rollout percentage  
- A deterministic hashing strategy applied to user IDs  

This allows teams to:
- Gradually roll out features  
- Test new functionality safely  
- Enable or disable features without redeploying the app  

The decision logic lives entirely on the backend, making it scalable and consistent across platforms.

---

### 🧩 Sample Output
![Feature Flag Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day79_output.png)

- Different users see different experiences  
- Feature visibility remains consistent for the same user  
- Rollout percentage controls exposure  
- Backend decides feature availability in real time  

This demonstrates a complete **backend-controlled experimentation flow**.

---

### 🧠 Key Learning
You learned how to:
- Implement feature flags in a backend system  
- Use hashing to create stable user buckets  
- Control feature rollouts using percentages  
- Separate feature configuration from application logic  
- Build systems that support experimentation and safe releases  
- Think like a product and platform engineer  

This project introduces **SaaS-grade backend decision-making**.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

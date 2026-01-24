# 🧭 Day 99 – Event Processing Pipeline (System Design Project)

> *“Software is not about features — it’s about flow.”*

---

### 🧠 Concepts Practised
- Event-driven system design  
- Pipeline-based processing architecture  
- Validation and routing logic  
- Separation of concerns (generator, router, handler, logger)  
- Backend-style workflow modeling  
- Logging and observability concepts  
- Designing systems instead of scripts  

---

### 💡 Project Overview
The **Event Processing Pipeline** is a system-level Python project that simulates how backend services handle events internally.

Instead of focusing on user interfaces or APIs, this project models the **flow of data through a system**, including:
- Event generation  
- Validation  
- Routing based on event type  
- Specialized handling  
- Logging for traceability  
- Final system reporting  

This mirrors the internal architecture of **backend services, message queues, logging pipelines, and data processors**, without requiring a running server.

---

### 🧩 Sample Output
![Event Pipeline Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day99_output.png)

- Events are generated dynamically  
- Each event passes through validation and routing  
- Different handlers process different event types  
- Results are logged for observability  
- A final system summary is produced  

This demonstrates how **complex systems can be modeled through clear stages and responsibilities**.

---

### 🧠 Key Learning
You learned how to:
- Design event-driven systems in Python  
- Model backend pipelines without frameworks  
- Separate validation, routing, and processing logic  
- Implement logging for system traceability  
- Think in terms of workflows instead of single scripts  

These concepts are foundational to **backend engineering, distributed systems, and data pipelines**.

---

### 🚀 Run the Program
1. Ensure Python is installed  
2. Create an empty `events.log` file in the project folder  
3. Run the pipeline:
   ```bash
   python main.py

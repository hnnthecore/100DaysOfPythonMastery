# 🧭 Day 83 – IFTTT-Style Rule Engine (Flask & SQLite)

> *“Automation is just decision-making written down.”*

---


### 🧠 Concepts Practised
- Rule-based system design  
- IF-THIS-THEN-THAT (IFTTT) logic  
- Condition → action mapping  
- Backend decision engines  
- Decoupling inputs from outcomes  
- Evaluating dynamic rules at runtime  
- Using SQLite for logic storage  

---

### 💡 Project Overview
This project implements a **rule engine** similar to platforms like **IFTTT** or **Zapier**, but in a simplified, logic-focused way.

Users can define rules such as:
- IF mood = sad → THEN play music  
- IF weather = rainy → THEN suggest indoor activity  
- IF energy = low → THEN recommend rest  

The backend evaluates user input against stored rules and dynamically determines which actions should be triggered.

This project shifts focus from traditional CRUD apps to **automation and decision systems**.

---

### 🧩 Sample Output
![Rule Engine Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day83_output.png)

- Rules created dynamically by users  
- Inputs tested against multiple conditions  
- Matching rules trigger corresponding actions  
- Multiple actions can fire from a single input  

This demonstrates a complete **define → evaluate → trigger** automation workflow.

---

### 🧠 Key Learning
You learned how to:
- Build rule-based automation systems  
- Separate decision logic from application flow  
- Evaluate conditions dynamically  
- Design backend logic engines  
- Think in terms of systems, not screens  
- Understand how real automation platforms work internally  

This project introduces **backend intelligence**, a critical skill for scalable systems.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

# 🧭 Day 81 – Digital Time Capsule (Flask & SQLite)

> *"Some messages aren’t meant for now."*

---

### 🧠 Concepts Practised
- Time-based access control  
- Working with dates and timestamps in Python  
- Conditional content rendering based on time  
- Backend-driven visibility logic  
- Using SQLite for persistent storage  
- Designing applications around future state  
- Separating creation logic from viewing logic  

---

### 💡 Project Overview
The **Digital Time Capsule** is a creative, emotion-driven web application where users can write messages intended for the future.

Users can:
- Write a message to their future self  
- Select a future date when the message should unlock  
- Seal the message in a “time capsule”  
- View capsules that automatically unlock when the chosen date arrives  

Until the unlock date, messages remain **completely hidden**, making time itself a core feature of the application.

---

### 🧩 Sample Output
![Digital Time Capsule Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day81_output_1.png)

- Capsule creation form with future date selection  
- Locked messages displayed with a 🔒 indicator  
- Messages automatically revealed after unlock date  
- Clean, minimal UI focused on content and timing  

This demonstrates a full **create → wait → reveal** workflow driven entirely by backend logic.

---

### 🧠 Key Learning
You learned how to:
- Use time as a condition in application logic  
- Control data visibility based on dates  
- Compare current time with stored timestamps  
- Build applications that behave differently over time  
- Think beyond instant feedback and CRUD patterns  
- Design features around real-world concepts  

This project introduces **temporal logic**, a powerful and often overlooked backend skill.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

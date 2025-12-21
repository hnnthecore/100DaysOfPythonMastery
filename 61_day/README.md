# 🧭 Day 61 – Introduction to Web Development with Flask

> *"Before building web apps, understand how the web really works."*

---

![Flask Intro GIF](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/flask.gif)

### 🧠 Concepts Practised
- Creating a web server using Flask  
- Running Python applications from the command line  
- Understanding `__name__` and `__main__` in Python  
- How URLs map to Python functions  
- Python functions as first-class objects  
- Understanding decorator functions and the `@` syntax  
- How Flask routing works internally  

---

### 💡 Project Overview
This project is a **foundational introduction to Flask and web development**.

Instead of building a complex application, the focus is on understanding **how Flask actually works**:
- How a Flask server starts  
- How browser requests reach Python functions  
- Why Flask uses decorators for routing  
- How core Python concepts power web frameworks  

This day removes the “magic” from Flask and prepares you for real-world web apps in the upcoming days.

---

### 🧩 Sample Output
![Flask Routes Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day61_output.png)

Visiting different URLs triggers different Python functions:
- `/` → Home route  
- `/about` → About page  
- `/contact` → Contact page  

This clearly demonstrates the **request → function → response** lifecycle.

---

### 🧠 Key Learning
You learned how to:
- Start and run a Flask web server  
- Use `__name__ == "__main__"` correctly  
- Understand Flask decorators at a conceptual level  
- Map URLs to Python functions  
- See how web frameworks rely on Python fundamentals  

This foundation makes future Flask topics feel logical instead of confusing.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

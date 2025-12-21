# 🧭 Day 63 – Passing Data from Python to HTML (Jinja Basics)

> *"Web pages become powerful when they are dynamic."*

---

![Flask Jinja Intro](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/crazyyyy.gif)

### 🧠 Concepts Practised
- Passing data from Python to HTML using Flask  
- Understanding Jinja templating engine  
- Using `{{ }}` to display dynamic values  
- Using `{% for %}` loops inside templates  
- Rendering lists and dictionaries in HTML  
- Backend → frontend data flow in web apps  

---

### 💡 Project Overview
This project introduces **dynamic HTML rendering** using Flask and Jinja templates.

Instead of serving static pages, Python now sends **real data** to HTML files, allowing pages to update dynamically based on backend logic.

You learn how Flask:
- Injects Python variables into templates  
- Uses Jinja syntax to render dynamic content  
- Keeps logic in Python and presentation in HTML  

This is a crucial step toward building real-world web applications.

---

### 🧩 Sample Output
![Flask Dynamic Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day63_output_1.png)
![Flask Dynamic Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day63_output_2.png)

- Home page dynamically displays username, role, and skills  
- Profile page renders user data using dictionaries  
- HTML content updates based on Python values  

This demonstrates **live data flowing from backend to frontend**.

---

### 🧠 Key Learning
You learned how to:
- Pass variables from Flask routes to templates  
- Use Jinja placeholders (`{{ }}`) correctly  
- Loop through lists using `{% for %}`  
- Render dictionaries inside HTML  
- Build dynamic pages using Flask  

These skills are essential for dashboards, profiles, and interactive web apps.

---

### 🚀 Run the Program
1. Install Flask (if not already installed):
   ```bash
   pip install flask

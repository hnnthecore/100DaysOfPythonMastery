# 🧭 Day 62 – Rendering HTML with Flask (Templates & Jinja Basics)

> *"Python handles logic, HTML handles presentation."*

---



### 🧠 Concepts Practised
- Rendering HTML pages using Flask  
- Understanding the `templates/` folder convention  
- Using `render_template()` to serve HTML  
- Separating backend logic from frontend presentation  
- Mapping URLs to HTML pages via Python functions  
- Building multi-page Flask applications  

---

### 💡 Project Overview
This project introduces **HTML rendering in Flask** using templates.

Instead of returning plain text, Flask now serves full HTML pages stored inside a dedicated `templates/` folder.  
This separation ensures:
- Python handles **logic and routing**
- HTML handles **structure and content**

The project demonstrates how Flask connects URLs to HTML pages in a clean and scalable way.

---

### 🧩 Sample Output
![Flask Template Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day62_output_1.png)
![Flask Templates Intro](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day62_output_2.png)

- `/` → Renders the home page (`index.html`)  
- `/about` → Renders the about page (`about.html`)  

Each page is served dynamically by Flask using Python functions.

---

### 🧠 Key Learning
You learned how to:
- Use `render_template()` to return HTML responses  
- Understand why Flask requires a `templates/` folder  
- Build multi-page web applications  
- Separate backend logic from frontend UI  
- Structure Flask projects properly from the beginning  

This knowledge is essential for all real-world Flask applications.

---

### 🚀 Run the Program
1. Install Flask (if not already installed):
   ```bash
   pip install flask

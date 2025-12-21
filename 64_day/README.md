# 🧭 Day 64 – Template Inheritance in Flask (DRY Principle)

> *"Write common layout once. Reuse it everywhere."*

---

![Flask Template Inheritance](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/badlands-chugs-estus-flask.gif)

### 🧠 Concepts Practised
- Template inheritance in Flask  
- Using `base.html` for shared layouts  
- Understanding `{% extends %}` in Jinja  
- Understanding `{% block %}` and block replacement  
- Applying the DRY (Don’t Repeat Yourself) principle  
- Structuring scalable Flask templates  

---

### 💡 Project Overview
This project introduces **template inheritance**, a core concept in real-world Flask applications.

Instead of repeating the same HTML structure (head, navigation, footer) on every page, Flask allows you to define a **base template** and extend it across multiple pages.

Each page:
- Inherits the same layout  
- Replaces only the content it needs  
- Stays clean, readable, and maintainable  

This approach is essential for building scalable web applications.

---

### 🧩 Sample Output

![Flask Base Template Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day64_output_1.png)
![Flask Base Template Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day64_output_2.png)

- Home and About pages share the same navigation and footer  
- Only the main content changes between pages  
- Layout consistency is maintained across the app  

This demonstrates how Flask avoids code duplication using templates.

---

### 🧠 Key Learning
You learned how to:
- Create a reusable `base.html` layout  
- Extend templates using `{% extends %}`  
- Define and override content using `{% block %}`  
- Apply the DRY principle in Flask projects  
- Structure templates the way real applications do  

This knowledge is critical for professional Flask development.

---

### 🚀 Run the Program
1. Install Flask (if not already installed):
   ```bash
   pip install flask

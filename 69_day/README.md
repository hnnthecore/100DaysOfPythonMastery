# 🧭 Day 69 – Introduction to Flask-WTForms

> *"Abstractions exist to remove repetition, not understanding."*

---

### 🧠 Concepts Practised
- Understanding why Flask-WTForms exists  
- Replacing manual validation with WTForms  
- Creating form classes using `FlaskForm`  
- Using built-in WTForms validators  
- CSRF protection and the role of `SECRET_KEY`  
- Cleaner separation of routes and validation logic  
- Integrating WTForms with Flask templates  

---

### 💡 Project Overview
This project introduces **Flask-WTForms**, a powerful extension that simplifies form handling and validation in Flask applications.

After manually validating forms in previous days, this project demonstrates how WTForms:
- Moves validation logic out of routes  
- Reduces repetitive code  
- Provides structured, reusable form definitions  
- Automatically handles security features like CSRF protection  

The goal is to understand **why WTForms exists**, not just how to use it.

---

### 🧩 Sample Output
![Flask WTForms Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day69_output.png)

- User submits a name using a WTForms-powered form  
- Validation errors are displayed automatically  
- Valid input triggers a success message  
- Form handling feels cleaner and more structured  

This shows how WTForms simplifies real-world form workflows.

---

### 🧠 Key Learning
You learned how to:
- Define forms using `FlaskForm`  
- Apply built-in validators instead of manual checks  
- Use `validate_on_submit()` correctly  
- Understand CSRF protection in Flask forms  
- Separate validation logic from route logic  
- Build scalable and maintainable form systems  

These concepts are essential for professional Flask development.

---

### 🚀 Run the Program
1. Install required packages:
   ```bash
   pip install flask flask-wtf

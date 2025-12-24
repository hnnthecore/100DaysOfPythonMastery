# 🧭 Day 67 – Form Validation & Error Handling in Flask (Bootstrap)

> *"Good apps don’t just accept input — they guide it."*

---

### 🧠 Concepts Practised
- Backend form validation in Flask  
- Handling invalid and empty user input  
- Sending error and success states to templates  
- Conditional rendering using Jinja  
- Using Bootstrap alerts for user feedback  
- Improving user experience with clear validation messages  

---

### 💡 Project Overview
This project focuses on **validating user input and handling errors gracefully** in a Flask application.

Instead of blindly accepting form submissions, the backend now:
- Checks whether input is empty  
- Enforces basic validation rules  
- Displays meaningful error messages when validation fails  
- Shows success feedback only when input is valid  

Bootstrap alerts are used to clearly communicate success and failure states to the user, making the application feel more professional and user-friendly.

---

### 🧩 Sample Output
![Flask Validation Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day67_output.png)

- Invalid input triggers a red error alert  
- Valid input shows a green success message  
- User input is preserved after submission  
- Feedback is clear and immediate  

This demonstrates proper **backend-controlled validation with frontend feedback**.

---

### 🧠 Key Learning
You learned how to:
- Validate user input on the backend (not just frontend)  
- Prevent invalid data from being accepted  
- Display contextual error and success messages  
- Use Jinja conditionals to control UI feedback  
- Combine Flask logic with Bootstrap for better UX  

These concepts are essential for building secure and reliable web applications.

---

### 🚀 Run the Program
1. Install Flask (if not already installed):
   ```bash
   pip install flask

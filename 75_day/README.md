# 🧭 Day 75 – User Authentication System with Flask & SQLite

> *"Security begins the moment you stop trusting plain text."*

---


### 🧠 Concepts Practised
- User authentication fundamentals  
- Secure password hashing using Werkzeug  
- User registration and login flow  
- Session management in Flask  
- Protecting routes using login checks  
- Logout functionality  
- Using SQLite for storing user credentials securely  

---

### 💡 Project Overview
This project introduces a **complete authentication system** built with **Flask and SQLite**.

Users can:
- Register with a username and password  
- Log in using secure, hashed credentials  
- Access a protected dashboard only after authentication  
- Log out safely, clearing the session  

Passwords are **never stored in plain text**, following real-world security best practices.

This project represents a major step toward building **secure, production-ready applications**.

---

### 🧩 Sample Output
![Flask Auth Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day75_output_1.png)
![Flask Auth Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day75_output_2.png)
![Flask Auth Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day75_output_3.png)

- User registration form  
- Login screen with credential validation  
- Protected dashboard accessible only to logged-in users  
- Session-based authentication flow  

This demonstrates a full **register → login → protected access → logout** lifecycle.

---

### 🧠 Key Learning
You learned how to:
- Implement user authentication from scratch  
- Hash and verify passwords securely  
- Use Flask sessions to track logged-in users  
- Protect routes from unauthorized access  
- Build login and registration systems safely  
- Understand core security principles in backend development  

These skills are essential for building real-world web applications.

---

### 🚀 Run the Program
1. Install required packages:
   ```bash
   pip install flask werkzeug

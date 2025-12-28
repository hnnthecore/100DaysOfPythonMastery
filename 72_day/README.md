# 🧭 Day 72 – Notes App with Flask & SQLite

> *"What you save today is what you can build on tomorrow."*

---


### 🧠 Concepts Practised
- Introduction to SQLite databases  
- Connecting Flask applications to SQLite  
- Creating database tables programmatically  
- Inserting records into a database  
- Fetching and displaying stored data  
- Using WTForms with database-backed applications  
- Separating form logic, database logic, and templates  

---

### 💡 Project Overview
This project introduces **real data persistence** using **SQLite**, marking a major milestone in backend development.

A simple **Notes App** is built where users can:
- Create notes with a title and content  
- Save notes permanently using SQLite  
- View all previously saved notes, even after restarting the server  

Unlike in-memory storage, SQLite ensures that data is **structured, reliable, and persistent**, making this the foundation for real-world applications.

---

### 🧩 Sample Output
![Notes App Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day72_output_1.png)
![Notes App Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day72_output_2.png)

- Notes are added through a validated WTForms form  
- Saved notes persist across server restarts  
- Notes are displayed dynamically using Bootstrap cards  
- Clean navigation separates adding and viewing notes  

This demonstrates a complete **create → store → retrieve** workflow.

---

### 🧠 Key Learning
You learned how to:
- Work with SQLite as a lightweight database  
- Create and manage database tables  
- Insert and retrieve records using SQL  
- Connect Flask routes to persistent storage  
- Build database-backed web applications  
- Lay the groundwork for full CRUD systems  

This project is the stepping stone toward advanced database-driven apps.

---

### 🚀 Run the Program
1. Install required packages:
   ```bash
   pip install flask flask-wtf

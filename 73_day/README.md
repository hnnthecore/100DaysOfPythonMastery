# 🧭 Day 73 – Full CRUD Notes App with Flask & SQLite

> *"Data is easy to create. Managing it correctly is engineering."*

---

### 🧠 Concepts Practised
- Full CRUD operations (Create, Read, Update, Delete)  
- Using SQLite as a persistent database  
- Creating and managing database tables  
- Updating and deleting records using SQL  
- Working with URL parameters in Flask routes  
- Reusing WTForms for create and edit flows  
- Structuring a real database-backed Flask app  

---

### 💡 Project Overview
This project upgrades the previous Notes App into a **full CRUD web application** using **Flask and SQLite**.

Users can now:
- Create new notes  
- View all saved notes  
- Edit existing notes  
- Delete notes permanently  

Each action directly interacts with the SQLite database, making the application fully persistent and stateful — just like real-world backend systems.

---

### 🧩 Sample Output
![Notes CRUD Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day73_output.png)
![Notes CRUD Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day73_output_1.png)

- Notes are displayed dynamically from the database  
- Each note includes **Edit** and **Delete** actions  
- Edited notes update instantly in SQLite  
- Deleted notes are permanently removed  

This demonstrates a complete **CRUD lifecycle** in a Flask application.

---

### 🧠 Key Learning
You learned how to:
- Implement full CRUD functionality in Flask  
- Safely update and delete database records  
- Use route parameters (`/<int:id>`) effectively  
- Reuse forms for both creation and editing  
- Build scalable, database-driven applications  
- Think like a backend engineer, not just a coder  

This is a **major backend milestone**.

---

### 🚀 Run the Program
1. Install required packages:
   ```bash
   pip install flask flask-wtf

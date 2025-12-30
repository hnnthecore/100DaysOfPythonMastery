# 🧭 Day 74 – REST API with Flask & SQLite (Notes App)

> *"If your application can speak JSON, it can speak to the world."*


### 🧠 Concepts Practised
- Understanding RESTful APIs  
- Returning JSON responses using Flask  
- Using HTTP methods (GET, POST, PUT, DELETE)  
- Handling request data with `request.get_json()`  
- Working with HTTP status codes  
- Exposing database-backed data as an API  
- Running HTML views and API endpoints side-by-side  

---

### 💡 Project Overview
This project extends the **Notes App** into a **RESTful API**, allowing data to be accessed programmatically using JSON.

The same SQLite database now supports:
- Traditional HTML-based views for users  
- API endpoints for external clients  

The backend exposes endpoints to:
- Fetch all notes  
- Fetch a single note  
- Create new notes via JSON  
- Update existing notes  
- Delete notes  

This demonstrates how **one backend can serve both UI and API consumers**.

---

### 🧩 Sample Output
![Notes API Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day74_output.png)

- Notes returned as structured JSON  
- API tested via browser or API clients  
- Correct HTTP status codes for each action  
- Database updates reflected instantly  

This shows a complete **API-driven CRUD workflow**.

---

### 🧠 Key Learning
You learned how to:
- Design REST-style API endpoints  
- Return JSON responses from Flask  
- Use proper HTTP methods and status codes  
- Share one database between UI and API layers  
- Build backend services usable by web & mobile apps  
- Think in terms of scalable backend architecture  

This is a **major backend engineering milestone**.

---

### 🚀 Run the Program
1. Install required packages:
   ```bash
   pip install flask flask-wtf

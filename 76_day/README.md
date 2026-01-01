# 🧭 Day 76 – URL Shortener with Flask & SQLite

> *"Great backend systems don’t just store data — they transform it."*

---

![URL Shortener Intro](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/dance-vibing.gif)

### 🧠 Concepts Practised
- Backend service design using Flask  
- Mapping long data to short unique identifiers  
- Generating random, collision-resistant keys  
- Using SQLite as a lookup table  
- Handling dynamic URL routes  
- HTTP redirection (`302`)  
- Separating business logic from presentation  

---

### 💡 Project Overview
This project implements a **URL Shortener service**, similar in concept to Bitly or TinyURL.

The application allows users to:
- Submit a long URL  
- Generate a short, unique URL  
- Store the mapping in a SQLite database  
- Redirect users back to the original URL when the short link is accessed  

Instead of focusing on users or authentication, this project emphasizes **pure backend logic and data transformation**, introducing a new way of thinking about web services.

---

### 🧩 Sample Output
![URL Shortener Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day76_output.png)

- User submits a long URL  
- Backend generates a unique short code  
- Short URL is displayed instantly  
- Visiting the short URL redirects to the original site  

This demonstrates a complete **input → transform → persist → redirect** workflow.

---

### 🧠 Key Learning
You learned how to:
- Design a backend service that transforms data  
- Generate and manage unique identifiers  
- Store and retrieve mappings efficiently using SQLite  
- Implement dynamic URL routing in Flask  
- Use HTTP redirects correctly  
- Think beyond CRUD and focus on backend problem-solving  

This project introduces **service-oriented backend thinking**, which is essential for real-world systems.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

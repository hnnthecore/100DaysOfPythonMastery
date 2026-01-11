# 🧭 Day 82 – Choose Your Own Adventure Engine (Flask & SQLite)

> *“Every choice creates a different reality.”*

---


### 🧠 Concepts Practised
- State-based application design  
- Graph-like data structures (scenes and choices)  
- Backend-driven UI flow  
- Branching logic and multiple outcomes  
- Using SQLite to model relationships  
- Dynamic routing based on user choices  
- Designing interactive systems  

---

### 💡 Project Overview
This project implements a **Choose Your Own Adventure Engine**, inspired by interactive fiction and story-driven games.

The application is built around the idea of **scenes** and **choices**:
- Each scene presents a part of the story  
- Each choice leads to a different scene  
- Some scenes are endings, while others continue the story  

User decisions directly influence the narrative, creating multiple paths and outcomes from the same starting point.

This project focuses on **logic, state transitions, and storytelling**, rather than traditional CRUD workflows.

---

### 🧩 Sample Output
![Adventure Engine Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day82_output.gif)

- Story scenes rendered dynamically  
- Multiple choices presented per scene  
- Different paths lead to different endings  
- Option to restart and explore new outcomes  

This demonstrates a complete **choice → consequence → outcome** system.

---

### 🧠 Key Learning
You learned how to:
- Model applications as state machines  
- Represent branching logic using database relationships  
- Build backend-driven interactive experiences  
- Control application flow using routing and state  
- Combine creativity with backend logic  
- Think beyond forms and dashboards  

This project introduces **game-engine-style thinking**, which is widely applicable in workflows, automation tools, and interactive systems.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

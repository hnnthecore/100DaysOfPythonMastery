# 🧭 Day 80 – Feature Flag Admin Panel (Flask & SQLite)

> *"Real power is not building features — it’s controlling them."*

---

### 🧠 Concepts Practised
- Feature flag management systems  
- Runtime configuration control  
- Admin dashboard design  
- Percentage-based rollout strategies  
- Updating backend behavior without redeploying  
- SQLite UPDATE queries  
- Backend-driven product control  

---

### 💡 Project Overview
This project extends the **Feature Flags & A/B Testing system** by adding a **live Admin Panel** to control feature rollouts.

Instead of hardcoding feature exposure, the admin can now:
- Change rollout percentages in real time  
- Enable or disable features instantly  
- Control user experience without restarting the server  

This mirrors how modern SaaS products safely release features to users.

---

### 🧩 Sample Output
![Feature Flag Admin Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day80_output.png)

- Admin dashboard showing current rollout percentage  
- Live updates to feature exposure  
- User-facing view changes immediately  
- Consistent feature behavior per user  

This demonstrates **runtime control over backend decision logic**.

---

### 🧠 Key Learning
You learned how to:
- Build admin panels for backend systems  
- Control application behavior dynamically  
- Implement safe rollout strategies  
- Update configuration data at runtime  
- Separate feature logic from application code  
- Design systems used by real product teams  

This project introduces **production-level backend control patterns**.

---

### 🚀 Run the Program
1. Install Flask:
   ```bash
   pip install flask

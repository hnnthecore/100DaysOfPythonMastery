# 🧭 Day 71 – Coffee & Wifi Rating App (Flask + WTForms + Bootstrap)

> *"Good projects combine multiple ideas into one clear purpose."*

---

![Coffee & Wifi Intro](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/coffeecat.gif)

### 🧠 Concepts Practised
- Building a complete Flask mini-application  
- Using Flask-WTForms for structured form handling  
- Validating multiple inputs using WTForms validators  
- Using Bootstrap for clean and responsive UI  
- Redirecting after successful form submission  
- Displaying submitted data dynamically  
- Managing temporary in-memory data  

---

### 💡 Project Overview
This project is a **purpose-driven mini web application** where users can submit and view cafes based on **WiFi strength and coffee quality**.

The application allows users to:
- Add cafe details using a validated WTForms form  
- Rate WiFi strength and coffee quality  
- View a list of submitted cafes in a clean layout  

This project combines routing, forms, validation, redirects, and UI styling into a **single cohesive Flask app**, making it feel closer to a real-world product.

---

### 🧩 Sample Output
![Coffee & Wifi Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day71_output_1.png)
![Coffee & Wifi Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day71_output_2.png)

- Users submit cafe information via a form  
- Valid submissions redirect to the cafe list page  
- Cafes are displayed using Bootstrap cards  
- Ratings are shown using visual star indicators  

This demonstrates a complete **add → validate → display** workflow.

---

### 🧠 Key Learning
You learned how to:
- Combine Flask routes into a multi-page application  
- Use WTForms in a real mini-project context  
- Validate and process structured form data  
- Redirect users after successful submissions  
- Dynamically render submitted data  
- Build applications that feel product-oriented  

This project marks the transition from **concept demos** to **real, usable Flask applications**.

---

### 🚀 Run the Program
1. Install required packages:
   ```bash
   pip install flask flask-wtf

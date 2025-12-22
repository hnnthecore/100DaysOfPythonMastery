# 🧭 Day 65 – Static Files in Flask (CSS & Assets)

> *"Logic lives in Python. Design lives in CSS."*

---

### 🧠 Concepts Practised
- Understanding the `static/` folder in Flask  
- Serving CSS files in a Flask application  
- Linking static assets using `url_for()`  
- Separating frontend styling from backend logic  
- Applying basic styling to Flask templates  
- Organizing assets in real-world Flask projects  

---

### 💡 Project Overview
This project introduces **static files in Flask**, focusing on how CSS is served and linked properly.

Instead of embedding styles directly in HTML or Python, Flask follows a clean structure where:
- HTML files live inside the `templates/` folder  
- CSS, images, and JavaScript live inside the `static/` folder  

Using `url_for()`, Flask safely links these assets, ensuring paths work correctly across environments.

This separation keeps applications clean, scalable, and professional.

---

### 🧩 Sample Output
![Flask Static CSS Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day65_output_1.png)
![Flask Static CSS Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day65_output_2.png)

- Pages share a common layout and styling  
- Navigation and content are styled using external CSS  
- The same CSS file applies to multiple pages  

This demonstrates how Flask connects backend routes with frontend assets.

---

### 🧠 Key Learning
You learned how to:
- Use the `static/` folder to store CSS files  
- Link static assets using `url_for()`  
- Keep styling separate from Python logic  
- Apply consistent design across multiple pages  
- Structure Flask projects like real applications  

This knowledge is essential for building maintainable web apps.

---

### 🚀 Run the Program
1. Install Flask (if not already installed):
   ```bash
   pip install flask

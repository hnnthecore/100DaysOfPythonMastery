# 🔐 Day 40 – FormBot: Automated Login & Session-Based Scraper

> *"Automation isn’t magic — it’s mastery over repetition."*

---

## 🧠 Concepts Practised
- Handling website logins using `requests.Session`
- Extracting CSRF tokens from HTML forms
- Sending authenticated POST requests
- Maintaining cookies and session state
- Scraping data available only after login
- Parsing HTML with `BeautifulSoup`
- Clean CLI workflow and error handling

---

## 💡 Project Overview
**FormBot** is a command-line web automation tool that demonstrates how to log into a website using Python — without Selenium.

The project connects to the public demo site:
[https://quotes.toscrape.com/login](https://quotes.toscrape.com/login)


This site is intentionally designed for testing scraping and login automation.

FormBot:
- Loads the login page  
- Extracts the hidden CSRF token  
- Logs in using a username and password  
- Maintains a session with cookies  
- Scrapes quotes that are only available after authentication  

This is the exact foundational skill needed before moving into browser automation (Selenium).

---

## ⚙️ Features
- Automated login using HTTP POST  
- CSRF token extraction  
- Session-based authentication  
- Scrapes private/authenticated content  
- Fully legal and demo-friendly  
- No external dependencies beyond Requests + BeautifulSoup  
- Clean CLI execution  

---

## 📸 Screenshots & Output
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day40_output.png)


---

## 🚀 How to Run

1. Install dependencies:
```bash
pip install requests beautifulsoup4


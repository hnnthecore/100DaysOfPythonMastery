# 🧠 Day 48 – AutoSummarizer Pro: Offline AI Text Summarizer

> *"When words feel heavy, let the machine lighten the load."*

---

### 🧠 Concepts Practised
- Offline natural language processing (NLP)
- Text tokenization and sentence ranking
- Keyword-frequency scoring algorithm
- Tkinter GUI for dual-pane text editing
- Adjustable summary compression
- Clipboard + file export tools
- Dark/Light UI theme switching

---

### 💡 Project Overview
**AutoSummarizer Pro** is a fully offline AI summarizer built using classical NLP techniques.  
Instead of relying on APIs or cloud models, it uses NLTK tokenization and a TextRank-style scoring engine to identify the most important sentences in any large text.

You paste long text in the left pane, select how short you want the summary to be, and the summarizer produces a concise version in the right pane — perfect for articles, book excerpts, research notes, and reports.

This app works completely offline after downloading NLTK data once.

---

### ⚙️ Features
✔ Offline summarization — no internet required  
✔ Dual-pane editor (Input → Summary)  
✔ Adjustable summary length slider  
✔ Robust sentence scoring using word frequencies  
✔ Remove stopwords + punctuation handling  
✔ Copy-to-clipboard support  
✔ Save summary to file  
✔ Dark mode for night reading  


### 🖼 GUI Screenshot

![gui](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day48_output.png)

---


### 📝 Notes
- Summarizer uses classical NLP, not neural networks, making it fast and offline-friendly  
- Works best on long text (3+ sentences)  
- Summary length slider determines compression %  
- The GUI is designed for readability and large text blocks  

---

### 🎯 Takeaways
With this project, you learned:
- How to apply NLP pipelines in Python  
- How to build practical GUI tools  
- How automatic summarization algorithms work  
- How to combine text processing + user interfaces  



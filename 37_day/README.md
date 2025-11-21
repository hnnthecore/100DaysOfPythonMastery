# 🎬 Day 37 – MovieQuest: Movie Search & Info Explorer

> *"Cinema is the most beautiful fraud in the world." — Jean-Luc Godard*

---

## 🧠 Concepts Practised
- API requests using `requests`
- Passing URL parameters using `params`
- Handling HTTP response codes & errors
- Parsing and extracting JSON data
- Tkinter GUI design (frames, labels, text widgets)
- Loading, resizing, and displaying images with Pillow
- Using threads to keep the GUI responsive
- Structuring a clean and user-friendly desktop interface

---

## 💡 Project Overview
**MovieQuest** is a Tkinter-based desktop application that lets you search for any movie and instantly view detailed information fetched from the OMDb API.

When you enter a movie title, the app displays:

- Movie poster  
- Release year  
- Genre  
- Director  
- Cast  
- Language & country  
- IMDb rating  
- Plot summary  

The GUI is designed to be simple, responsive, and visually clean. Poster loading and API fetching happen in the background to prevent UI freezing.

---

## ⚙️ Features
- Movie search by title  
- Live data retrieval from the OMDb API  
- High-quality poster display (auto-resized)  
- Organized info panel (plot, actors, rating, etc.)  
- Multithreaded API calls  
- Graceful error handling  
- Minimal, polished Tkinter layout  

---

## 📸 Screenshots & Output
![output](https://github.com/hnnthecore/100DaysOfPythonMastery/blob/main/assets/day37_output.png)


---

## 📝 Notes
- Free OMDb API keys take a few minutes to activate.
- The app automatically falls back to text-based output if the poster fails to load.
- Designed for compatibility across all operating systems using Tkinter.

---

## 🎯 Takeaways
This project combines GUI development, real-time API consumption, JSON parsing, image processing, and threading — a strong and practical addition to your 100 Days of Python Mastery series.

# 🔥 Day 34 – PocketDex: Pokémon Search & Viewer

> "A clean Tkinter-powered Pokémon lookup tool using the free PokeAPI."

---
![gif](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/venonat-pokemon.gif)
## 🧠 Concepts Practised
- Tkinter GUI design  
- Image fetching & rendering (`PIL`, `ImageTk`)  
- Public API requests (no key required)  
- Threading for non-blocking UI  
- Error handling  
- JSON parsing  
- Clean layout structuring  

---

## 💡 Project Overview
**PocketDex** is a modern Pokémon search application built with Tkinter.  
Users can enter a Pokémon name or ID, and the app will fetch:

- Official artwork  
- Name  
- ID  
- Types  
- Abilities  
- Base stats  

It uses the **PokeAPI**, a completely free and keyless API, ensuring easy setup with no sign-ups.

The UI is divided into a search bar, Pokémon artwork display, and detailed info panel.

---

## ⚙️ Features
### ✔ Pokémon Search Engine  
Enter a Pokémon’s name or ID and fetch live data instantly.

### ✔ High-Quality Artwork Display  
Fetches and renders official artwork from PokeAPI.

### ✔ Clean Stats & Ability Breakdown  
Stats are shown in a structured, readable way.

### ✔ Non-Freezing UI  
Threading ensures the interface remains responsive during API calls.

### ✔ Error Handling  
Gracefully handles invalid names or network issues.

---

## 🖼️ Screenshot / Output  
![output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day34_output.png)


---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install requests pillow



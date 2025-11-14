# 🎹 Day 30 – PianoPy: Keyboard Piano Simulator

> *"Turn your keyboard into a musical instrument."*

---

### 🧠 Concepts Practised
- Real-time keyboard event handling  
- Audio synthesis using sine waves  
- Frequency-to-sound conversion  
- Tone generation with numpy  
- Live sound playback through pygame  
- User interaction inside custom window  

---

### 💡 Project Overview
**PianoPy** transforms your computer keyboard into a simple digital piano.  
Each key press generates a musical note using pure sine-wave synthesis, without relying on pre-recorded audio files.

The result is a responsive, lightweight musical tool that demonstrates:
- waveform generation  
- frequency mapping  
- real-time audio playback  

This project blends programming with music theory in an interactive and enjoyable way.

---

### ⚙️ Features
✅ Play notes from C4 to C5 using keyboard keys  
✅ Real-time audio playback using pygame  
✅ Synthesized tones (no audio files)  
✅ Clean, responsive interface  
✅ Works fully offline  

---

### 🎼 Key → Note Mapping
| Key | Note | Frequency (Hz) |
|-----|------|----------------|
| A   | C4   | 261.63         |
| S   | D4   | 293.66         |
| D   | E4   | 329.63         |
| F   | F4   | 349.23         |
| G   | G4   | 392.00         |
| H   | A4   | 440.00         |
| J   | B4   | 493.88         |
| K   | C5   | 523.25         |

---

### 🧩 Screenshots & Output

![PianoPy Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day30_output.png)

---

### 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install pygame numpy

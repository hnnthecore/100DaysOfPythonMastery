import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time


class AudioDesk:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 52 - AudioDesk: Recorder & Waveform Visualizer")
        self.root.geometry("800x500")
        self.root.configure(bg="#f2f2f2")

        self.fs = 44100
        self.recording = False
        self.audio_data = []

        self.build_ui()
        self.build_graph()

    def build_ui(self):
        title = tk.Label(self.root, text="AudioDesk – Voice Recorder",
                         font=("Arial", 20, "bold"), bg="#f2f2f2")
        title.pack(pady=15)

        frame = tk.Frame(self.root, bg="#f2f2f2")
        frame.pack()

        tk.Button(frame, text="Start Recording", font=("Arial", 14),
                  command=self.start_recording).grid(row=0, column=0, padx=10)

        tk.Button(frame, text="Stop Recording", font=("Arial", 14),
                  command=self.stop_recording).grid(row=0, column=1, padx=10)

        tk.Button(frame, text="Play Recording", font=("Arial", 14),
                  command=self.play_audio).grid(row=0, column=2, padx=10)

        tk.Button(frame, text="Save as WAV", font=("Arial", 14),
                  command=self.save_audio).grid(row=0, column=3, padx=10)

    def build_graph(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 3))
        self.ax.set_ylim(-1, 1)
        self.ax.set_xlim(0, 2000)
        self.ax.axis("off")

        self.line, = self.ax.plot([], [], lw=2)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(pady=20)

    def update_waveform(self):
        while self.recording:
            if len(self.audio_data) > 2000:
                segment = self.audio_data[-2000:]
            else:
                segment = self.audio_data

            self.line.set_data(range(len(segment)), segment)
            self.ax.set_xlim(0, max(2000, len(segment)))

            self.canvas.draw()
            time.sleep(0.05)

    def start_recording(self):
        if self.recording:
            return

        self.audio_data = []
        self.recording = True

        threading.Thread(target=self.capture_audio, daemon=True).start()
        threading.Thread(target=self.update_waveform, daemon=True).start()

    def capture_audio(self):
        def callback(indata, frames, time, status):
            if self.recording:
                self.audio_data.extend(indata[:, 0].tolist())

        with sd.InputStream(callback=callback, channels=1, samplerate=self.fs):
            while self.recording:
                sd.sleep(100)

    def stop_recording(self):
        self.recording = False

    def play_audio(self):
        if not self.audio_data:
            messagebox.showerror("Error", "No audio recorded.")
            return
        sd.play(np.array(self.audio_data), self.fs)

    def save_audio(self):
        if not self.audio_data:
            messagebox.showerror("Error", "No audio to save.")
            return

        path = filedialog.asksaveasfilename(defaultextension=".wav",
                                            filetypes=[("WAV files", "*.wav")])
        if not path:
            return

        normalized = np.int16(np.array(self.audio_data) / np.max(np.abs(self.audio_data)) * 32767)
        write(path, self.fs, normalized)

        messagebox.showinfo("Saved", "Audio saved successfully!")


if __name__ == "__main__":
    root = tk.Tk()
    AudioDesk(root)
    root.mainloop()

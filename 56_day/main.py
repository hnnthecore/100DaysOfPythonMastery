import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os

pygame.mixer.init()


class SoundWaveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SoundWave - Audio Player")
        self.root.geometry("600x450")

        self.playlist = []
        self.current_index = None
        self.paused = False

        self.build_ui()

    def build_ui(self):
        title = tk.Label(self.root, text="SoundWave", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        self.song_label = tk.Label(self.root, text="No song playing", font=("Arial", 12))
        self.song_label.pack(pady=5)

        self.listbox = tk.Listbox(self.root, width=60, height=10)
        self.listbox.pack(pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.select_song)

        controls = tk.Frame(self.root)
        controls.pack(pady=10)

        tk.Button(controls, text="Load Songs", width=12, command=self.load_songs).grid(row=0, column=0, padx=5)
        tk.Button(controls, text="Play", width=10, command=self.play_song).grid(row=0, column=1, padx=5)
        tk.Button(controls, text="Pause", width=10, command=self.pause_song).grid(row=0, column=2, padx=5)
        tk.Button(controls, text="Stop", width=10, command=self.stop_song).grid(row=0, column=3, padx=5)

    def load_songs(self):
        files = filedialog.askopenfilenames(
            title="Select Audio Files",
            filetypes=[("Audio Files", "*.mp3 *.wav")]
        )

        if not files:
            return

        for file in files:
            if file not in self.playlist:
                self.playlist.append(file)
                self.listbox.insert(tk.END, os.path.basename(file))

    def select_song(self, event):
        if not self.listbox.curselection():
            return
        self.current_index = self.listbox.curselection()[0]
        self.play_song()

    def play_song(self):
        if self.current_index is None:
            if not self.playlist:
                messagebox.showwarning("No Songs", "Load songs first.")
                return
            self.current_index = 0

        try:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.paused = False
            song_name = os.path.basename(self.playlist[self.current_index])
            self.song_label.config(text=f"Playing: {song_name}")
        except Exception as e:
            messagebox.showerror("Playback Error", str(e))

    def pause_song(self):
        if pygame.mixer.music.get_busy():
            if not self.paused:
                pygame.mixer.music.pause()
                self.paused = True
                self.song_label.config(text="Paused")
            else:
                pygame.mixer.music.unpause()
                self.paused = False
                song_name = os.path.basename(self.playlist[self.current_index])
                self.song_label.config(text=f"Playing: {song_name}")

    def stop_song(self):
        pygame.mixer.music.stop()
        self.song_label.config(text="Stopped")


if __name__ == "__main__":
    root = tk.Tk()
    app = SoundWaveApp(root)
    root.mainloop()

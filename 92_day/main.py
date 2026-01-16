import tkinter as tk
from tkinter import messagebox

class FocusTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Timer")
        self.root.geometry("300x260")
        self.root.resizable(False, False)

        self.is_focus = True
        self.remaining_seconds = 0

        # Title
        self.title_label = tk.Label(
            root, text="🎯 Focus Timer", font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        # Time inputs
        self.focus_entry = self.create_entry("Focus Minutes")
        self.break_entry = self.create_entry("Break Minutes")

        # Timer display
        self.timer_label = tk.Label(
            root, text="00:00", font=("Arial", 28, "bold")
        )
        self.timer_label.pack(pady=10)

        # Start button
        self.start_btn = tk.Button(
            root, text="Start Session", command=self.start_timer
        )
        self.start_btn.pack(pady=10)

    def create_entry(self, label_text):
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        label = tk.Label(frame, text=label_text)
        label.pack(side="left", padx=5)

        entry = tk.Entry(frame, width=5)
        entry.pack(side="right")
        return entry

    def start_timer(self):
        try:
            focus_minutes = int(self.focus_entry.get())
            break_minutes = int(self.break_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
            return

        if focus_minutes <= 0 or break_minutes <= 0:
            messagebox.showerror("Error", "Time must be greater than zero")
            return

        self.focus_seconds = focus_minutes * 60
        self.break_seconds = break_minutes * 60

        self.is_focus = True
        self.remaining_seconds = self.focus_seconds
        self.update_timer()

    def update_timer(self):
        mins, secs = divmod(self.remaining_seconds, 60)
        self.timer_label.config(text=f"{mins:02d}:{secs:02d}")

        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self.root.after(1000, self.update_timer)
        else:
            if self.is_focus:
                messagebox.showinfo("Break Time", "Focus complete! Time for a break ☕")
                self.is_focus = False
                self.remaining_seconds = self.break_seconds
                self.update_timer()
            else:
                messagebox.showinfo("Done", "Session complete! 🎉")

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusTimer(root)
    root.mainloop()

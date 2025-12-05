import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

SAVE_FILE = "day51_taskboard.json"


PASTEL_COLORS = [
    "#F9D5E5",  # Pink
    "#FCE1A8",  # Soft Yellow
    "#D5E8D4",  # Green
    "#D6EAF8",  # Blue
    "#E8DAEF",  # Lavender
]


class StickyNote:
    def __init__(self, canvas, x, y, text="", color="#F9D5E5"):
        self.canvas = canvas
        self.color = color

        self.frame = tk.Frame(canvas, bg=color, width=180, height=120, highlightbackground="#999", highlightthickness=1)
        self.label = tk.Label(self.frame, text=text, bg=color, wraplength=150, justify="left")
        self.label.pack(padx=5, pady=5)

        self.window = canvas.create_window(x, y, window=self.frame, anchor="nw")

        self.frame.bind("<Button-1>", self.start_drag)
        self.frame.bind("<B1-Motion>", self.on_drag)
        self.frame.bind("<Button-3>", self.open_menu)

        self.start_x = 0
        self.start_y = 0

    def start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.canvas.move(self.window, dx, dy)

    def open_menu(self, event):
        menu = tk.Menu(self.frame, tearoff=0)
        menu.add_command(label="Edit", command=self.edit_text)
        menu.add_command(label="Delete", command=self.delete)
        menu.tk_popup(event.x_root, event.y_root)

    def edit_text(self):
        new_text = simpledialog.askstring("Edit Note", "Enter new text:", initialvalue=self.label.cget("text"))
        if new_text is not None:
            self.label.config(text=new_text)

    def delete(self):
        self.canvas.delete(self.window)

    def get_data(self):
        x, y = self.canvas.coords(self.window)
        return {
            "x": x,
            "y": y,
            "text": self.label.cget("text"),
            "color": self.color
        }


class TaskBoardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 51 - TaskBoard: Sticky Notes Manager")
        self.root.geometry("1200x700")
        self.root.config(bg="#f7f7f7")

        self.notes = []

        self.build_ui()
        self.load_notes()

    def build_ui(self):
        top = tk.Frame(self.root, bg="#f7f7f7")
        top.pack(fill="x", pady=10)

        tk.Button(top, text="Add Note", font=("Arial", 12), command=self.add_note).pack(side="left", padx=10)
        tk.Button(top, text="Save Board", font=("Arial", 12), command=self.save_notes).pack(side="left")

        self.canvas = tk.Canvas(self.root, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

    def add_note(self):
        text = simpledialog.askstring("New Note", "Enter note text:")
        if not text:
            return

        color = PASTEL_COLORS[len(self.notes) % len(PASTEL_COLORS)]
        note = StickyNote(self.canvas, 50, 50, text, color)
        self.notes.append(note)

    def save_notes(self):
        data = [note.get_data() for note in self.notes]

        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Saved", "Board saved successfully!")

    def load_notes(self):
        if not os.path.exists(SAVE_FILE):
            return

        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        for n in data:
            note = StickyNote(
                self.canvas,
                x=n["x"],
                y=n["y"],
                text=n["text"],
                color=n["color"]
            )
            self.notes.append(note)


if __name__ == "__main__":
    root = tk.Tk()
    TaskBoardApp(root)
    root.mainloop()

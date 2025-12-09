import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

SAVE_FILE = "day55_timeblocks.json"

BLOCK_COLORS = [
    "#FFCDD2",  # Red
    "#C5E1A5",  # Green
    "#BBDEFB",  # Blue
    "#FFF9C4",  # Yellow
    "#D1C4E9",  # Purple
]


class TimeBlock:
    def __init__(self, canvas, y, text, color):
        self.canvas = canvas
        self.text = text
        self.color = color

        self.height = 80

        self.rect = canvas.create_rectangle(100, y, 500, y + self.height, fill=color, outline="#444")
        self.label = canvas.create_text(300, y + 40, text=text, font=("Arial", 14, "bold"))

        self.dragging = False

        # Bind drag events
        canvas.tag_bind(self.rect, "<Button-1>", self.start_drag)
        canvas.tag_bind(self.label, "<Button-1>", self.start_drag)

        canvas.tag_bind(self.rect, "<B1-Motion>", self.on_drag)
        canvas.tag_bind(self.label, "<B1-Motion>", self.on_drag)

        # Right-click menu
        canvas.tag_bind(self.rect, "<Button-3>", self.menu)
        canvas.tag_bind(self.label, "<Button-3>", self.menu)

    def start_drag(self, event):
        self.dragging = True
        self.start_y = event.y

    def on_drag(self, event):
        if not self.dragging:
            return

        dy = event.y - self.start_y
        self.canvas.move(self.rect, 0, dy)
        self.canvas.move(self.label, 0, dy)

        self.start_y = event.y

    def menu(self, event):
        menu = tk.Menu(self.canvas, tearoff=0)
        menu.add_command(label="Edit", command=self.edit)
        menu.add_command(label="Delete", command=self.delete)
        menu.post(event.x_root, event.y_root)

    def edit(self):
        new_text = simpledialog.askstring("Edit Block", "Enter new text:", initialvalue=self.text)
        if new_text:
            self.text = new_text
            self.canvas.itemconfig(self.label, text=new_text)

    def delete(self):
        self.canvas.delete(self.rect)
        self.canvas.delete(self.label)

    def get_data(self):
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        return {
            "text": self.text,
            "color": self.color,
            "y": y1,
            "height": self.height
        }


class TimeBlockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 55 - TimeBlock: Daily Planner")
        self.root.geometry("800x700")

        self.blocks = []

        self.build_ui()
        self.load_blocks()

    def build_ui(self):
        top = tk.Frame(self.root)
        top.pack(fill="x", pady=10)

        tk.Button(top, text="Add Block", font=("Arial", 12),
                  command=self.add_block).pack(side="left", padx=10)

        tk.Button(top, text="Save", font=("Arial", 12),
                  command=self.save_blocks).pack(side="left", padx=10)

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Timeline hour markers
        for i in range(8, 21):
            y = (i - 8) * 60 + 20
            self.canvas.create_text(70, y, text=f"{i}:00", font=("Arial", 12))

    def add_block(self):
        text = simpledialog.askstring("New Block", "Enter task:")
        if not text:
            return

        color = BLOCK_COLORS[len(self.blocks) % len(BLOCK_COLORS)]
        y = 100 + len(self.blocks) * 90

        block = TimeBlock(self.canvas, y, text, color)
        self.blocks.append(block)

    def save_blocks(self):
        data = [b.get_data() for b in self.blocks]

        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Saved", "Schedule saved successfully!")

    def load_blocks(self):
        if not os.path.exists(SAVE_FILE):
            return

        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

        for item in data:
            block = TimeBlock(self.canvas, item["y"], item["text"], item["color"])
            self.blocks.append(block)


if __name__ == "__main__":
    root = tk.Tk()
    TimeBlockApp(root)
    root.mainloop()

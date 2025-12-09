import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from PIL import ImageGrab


class Node:
    def __init__(self, canvas, x, y, text):
        self.canvas = canvas
        self.text = text

        self.rect = canvas.create_rectangle(x, y, x + 130, y + 50, fill="#FFECB3", outline="#333")
        self.label = canvas.create_text(x + 65, y + 25, text=text, font=("Arial", 12, "bold"))

        self.dragging = False
        self.connections = []

        canvas.tag_bind(self.rect, "<Button-1>", self.start_drag)
        canvas.tag_bind(self.label, "<Button-1>", self.start_drag)

        canvas.tag_bind(self.rect, "<B1-Motion>", self.on_drag)
        canvas.tag_bind(self.label, "<B1-Motion>", self.on_drag)

        canvas.tag_bind(self.rect, "<Button-3>", self.open_menu)
        canvas.tag_bind(self.label, "<Button-3>", self.open_menu)

    def get_center(self):
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        return (x1 + x2) / 2, (y1 + y2) / 2

    def start_drag(self, event):
        self.dragging = True
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        if not self.dragging:
            return
        dx = event.x - self.start_x
        dy = event.y - self.start_y

        self.canvas.move(self.rect, dx, dy)
        self.canvas.move(self.label, dx, dy)

        self.start_x = event.x
        self.start_y = event.y

        for line in self.connections:
            line.update_position()

    def stop_drag(self, event):
        self.dragging = False

    def open_menu(self, event):
        menu = tk.Menu(self.canvas, tearoff=0)
        menu.add_command(label="Edit Text", command=self.edit_text)
        menu.add_command(label="Delete Node", command=self.delete)
        menu.post(event.x_root, event.y_root)

    def edit_text(self):
        new = simpledialog.askstring("Edit Node", "Enter new text:", initialvalue=self.text)
        if new:
            self.text = new
            self.canvas.itemconfig(self.label, text=new)

    def delete(self):
        for c in list(self.connections):
            c.delete()
        self.canvas.delete(self.rect)
        self.canvas.delete(self.label)


class Connection:
    def __init__(self, canvas, node1, node2):
        self.canvas = canvas
        self.node1 = node1
        self.node2 = node2

        x1, y1 = node1.get_center()
        x2, y2 = node2.get_center()

        self.line = canvas.create_line(x1, y1, x2, y2, width=2, arrow=tk.LAST)
        node1.connections.append(self)
        node2.connections.append(self)

    def update_position(self):
        x1, y1 = self.node1.get_center()
        x2, y2 = self.node2.get_center()
        self.canvas.coords(self.line, x1, y1, x2, y2)

    def delete(self):
        self.node1.connections.remove(self)
        self.node2.connections.remove(self)
        self.canvas.delete(self.line)


class MindSketchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 54 - MindSketch: Concept Map Builder")
        self.root.geometry("1200x700")

        self.nodes = []
        self.selected_node = None

        self.build_ui()

    def build_ui(self):
        top = tk.Frame(self.root)
        top.pack(fill="x", pady=10)

        tk.Button(top, text="Add Node", font=("Arial", 12),
                  command=self.add_node).pack(side="left", padx=10)

        tk.Button(top, text="Connect Nodes", font=("Arial", 12),
                  command=self.prepare_connection).pack(side="left", padx=10)

        tk.Button(top, text="Export as PNG", font=("Arial", 12),
                  command=self.export_png).pack(side="left", padx=10)

        self.info = tk.Label(top, text="", font=("Arial", 12))
        self.info.pack(side="left", padx=20)

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

    def add_node(self):
        text = simpledialog.askstring("New Node", "Enter concept text:")
        if not text:
            return
        node = Node(self.canvas, 100, 100, text)
        self.nodes.append(node)

    def prepare_connection(self):
        self.info.config(text="Select FIRST node...")
        self.canvas.bind("<Button-1>", self.select_first)

    def select_first(self, event):
        node = self.find_node(event.x, event.y)
        if node:
            self.first = node
            self.info.config(text="Select SECOND node...")
            self.canvas.bind("<Button-1>", self.select_second)

    def select_second(self, event):
        node = self.find_node(event.x, event.y)
        if node:
            Connection(self.canvas, self.first, node)
            self.info.config(text="")
        self.canvas.unbind("<Button-1>")

    def find_node(self, x, y):
        items = self.canvas.find_overlapping(x, y, x, y)
        for n in self.nodes:
            if n.rect in items or n.label in items:
                return n
        return None

    def export_png(self):
        file = filedialog.asksaveasfilename(defaultextension=".png")
        if not file:
            return

        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        w = x + self.canvas.winfo_width()
        h = y + self.canvas.winfo_height()

        img = ImageGrab.grab().crop((x, y, w, h))
        img.save(file)
        messagebox.showinfo("Saved", "Canvas exported as PNG!")


if __name__ == "__main__":
    root = tk.Tk()
    MindSketchApp(root)
    root.mainloop()

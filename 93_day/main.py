import tkinter as tk
from tkinter import messagebox

class BarChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Data Visualizer")
        self.root.geometry("500x400")

        # Input section
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter numbers (comma separated):").pack(side="left")
        self.entry = tk.Entry(input_frame, width=30)
        self.entry.pack(side="left", padx=5)

        tk.Button(
            input_frame, text="Visualize", command=self.visualize
        ).pack(side="left")

        # Canvas for drawing
        self.canvas = tk.Canvas(root, width=460, height=300, bg="white")
        self.canvas.pack(pady=15)

    def visualize(self):
        raw = self.entry.get()

        try:
            values = [int(v.strip()) for v in raw.split(",") if v.strip()]
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter only numbers")
            return

        if not values:
            messagebox.showerror("Invalid Input", "Enter at least one number")
            return

        self.draw_bars(values)

    def draw_bars(self, values):
        self.canvas.delete("all")

        max_value = max(values)
        bar_width = 40
        spacing = 15
        start_x = 20
        canvas_height = 280

        for i, value in enumerate(values):
            # Normalize height based on max value
            bar_height = (value / max_value) * 200

            x1 = start_x + i * (bar_width + spacing)
            y1 = canvas_height - bar_height
            x2 = x1 + bar_width
            y2 = canvas_height

            self.canvas.create_rectangle(
                x1, y1, x2, y2, fill="#4CAF50", outline=""
            )

            self.canvas.create_text(
                x1 + bar_width / 2, y1 - 10, text=str(value)
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = BarChartApp(root)
    root.mainloop()

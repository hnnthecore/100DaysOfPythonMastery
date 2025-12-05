import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps

class PixelCrafter:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 50 - PixelCrafter: Image Editor")
        self.root.geometry("1200x700")
        self.root.config(bg="#f7f7f7")

        self.original_image = None
        self.display_image = None

        self.build_ui()

    def build_ui(self):
        title = tk.Label(self.root, text="PixelCrafter – Image Editor Studio",
                         font=("Segoe UI", 20, "bold"), bg="#f7f7f7")
        title.pack(pady=10)

        container = tk.Frame(self.root, bg="#f7f7f7")
        container.pack(fill="both", expand=True)

        # Left preview
        self.preview = tk.Label(container, bg="#ddd")
        self.preview.pack(side="left", expand=True, padx=20, pady=20)

        # Right controls
        controls = tk.Frame(container, bg="#f7f7f7")
        controls.pack(side="right", fill="y", padx=20)

        tk.Button(controls, text="Open Image", font=("Arial", 12),
                  command=self.open_image).pack(pady=10, fill="x")

        tk.Button(controls, text="Save Image", font=("Arial", 12),
                  command=self.save_image).pack(pady=10, fill="x")

        ttk.Separator(controls).pack(fill="x", pady=10)

        # Filters
        tk.Label(controls, text="Filters:", font=("Arial", 14, "bold"), bg="#f7f7f7").pack(pady=5)

        tk.Button(controls, text="Grayscale", command=lambda: self.apply_filter("gray")).pack(pady=5, fill="x")
        tk.Button(controls, text="Sepia", command=lambda: self.apply_filter("sepia")).pack(pady=5, fill="x")
        tk.Button(controls, text="Invert", command=lambda: self.apply_filter("invert")).pack(pady=5, fill="x")
        tk.Button(controls, text="Blur", command=lambda: self.apply_filter("blur")).pack(pady=5, fill="x")
        tk.Button(controls, text="Sharpen", command=lambda: self.apply_filter("sharpen")).pack(pady=5, fill="x")

        ttk.Separator(controls).pack(fill="x", pady=10)

        # Brightness
        tk.Label(controls, text="Brightness", bg="#f7f7f7").pack()
        self.brightness_slider = tk.Scale(controls, from_=0.5, to=2, resolution=0.1, orient="horizontal",
                                          command=self.adjust_brightness, length=200)
        self.brightness_slider.set(1)
        self.brightness_slider.pack(pady=5)

        # Contrast
        tk.Label(controls, text="Contrast", bg="#f7f7f7").pack()
        self.contrast_slider = tk.Scale(controls, from_=0.5, to=2, resolution=0.1, orient="horizontal",
                                        command=self.adjust_contrast, length=200)
        self.contrast_slider.set(1)
        self.contrast_slider.pack(pady=5)

        ttk.Separator(controls).pack(fill="x", pady=10)

        tk.Button(controls, text="Rotate 90°", command=self.rotate).pack(pady=10, fill="x")

    def show_image(self, img):
        img_resized = img.copy()
        img_resized.thumbnail((700, 600))
        self.display_image = ImageTk.PhotoImage(img_resized)
        self.preview.config(image=self.display_image)

    def open_image(self):
        path = filedialog.askopenfilename()
        if not path:
            return
        self.original_image = Image.open(path)
        self.working_image = self.original_image.copy()
        self.show_image(self.working_image)

    def save_image(self):
        if self.working_image is None:
            messagebox.showerror("Error", "No image to save.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            self.working_image.save(path)
            messagebox.showinfo("Saved", "Image saved successfully.")

    def apply_filter(self, mode):
        if self.working_image is None:
            return
        img = self.working_image

        if mode == "gray":
            img = ImageOps.grayscale(img)
        elif mode == "sepia":
            sepia = ImageOps.colorize(ImageOps.grayscale(img), "#704214", "#FFF4D8")
            img = sepia
        elif mode == "invert":
            img = ImageOps.invert(img)
        elif mode == "blur":
            img = img.filter(ImageFilter.BLUR)
        elif mode == "sharpen":
            img = img.filter(ImageFilter.SHARPEN)

        self.working_image = img
        self.show_image(img)

    def adjust_brightness(self, value):
        if self.working_image is None:
            return
        enhancer = ImageEnhance.Brightness(self.working_image)
        img = enhancer.enhance(float(value))
        self.show_image(img)

    def adjust_contrast(self, value):
        if self.working_image is None:
            return
        enhancer = ImageEnhance.Contrast(self.working_image)
        img = enhancer.enhance(float(value))
        self.show_image(img)

    def rotate(self):
        if self.working_image is None:
            return
        self.working_image = self.working_image.rotate(90, expand=True)
        self.show_image(self.working_image)


if __name__ == "__main__":
    root = tk.Tk()
    PixelCrafter(root)
    root.mainloop()

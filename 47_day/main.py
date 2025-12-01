import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests

API_URL = "https://api.mymemory.translated.net/get"

LANGUAGES = {
    "Swiss German (Schwiizerdütsch)": "de-CH",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Norwegian": "no",
    "Swedish": "sv",
    "Danish": "da",
    "Finnish": "fi",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Simplified)": "zh-CN"
}


class AutoTranslateMail:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 47 - AutoTranslateMail (International Edition)")
        self.root.geometry("1200x650")
        self.root.configure(bg="#f5f5f5")
        self.dark_mode = False
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="AutoTranslate Mail — International Edition", 
                 font=("Segoe UI", 20, "bold"), bg="#f5f5f5").pack(pady=10)

        frame = tk.Frame(self.root, bg="#f5f5f5")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        left = tk.Frame(frame, bg="#f5f5f5")
        left.pack(side="left", fill="both", expand=True, padx=10)

        tk.Label(left, text="Original Draft", font=("Segoe UI", 14, "bold"), bg="#f5f5f5").pack()
        self.input_box = tk.Text(left, font=("Segoe UI", 12), wrap="word", height=22)
        self.input_box.pack(fill="both", expand=True, pady=10)

        right = tk.Frame(frame, bg="#f5f5f5")
        right.pack(side="right", fill="both", expand=True, padx=10)

        tk.Label(right, text="Translated Email", font=("Segoe UI", 14, "bold"), bg="#f5f5f5").pack()
        self.output_box = tk.Text(right, font=("Segoe UI", 12), wrap="word", height=22)
        self.output_box.pack(fill="both", expand=True, pady=10)

        bottom = tk.Frame(self.root, bg="#f5f5f5")
        bottom.pack(fill="x", pady=10)

        tk.Label(bottom, text="Translate To:", font=("Segoe UI", 12), bg="#f5f5f5").pack(side="left", padx=10)

        self.language = ttk.Combobox(bottom, values=list(LANGUAGES.keys()), width=25, font=("Segoe UI", 11))
        self.language.set("Swiss German (Schwiizerdütsch)")
        self.language.pack(side="left", padx=10)

        tk.Button(bottom, text="TRANSLATE", font=("Segoe UI", 12, "bold"), command=self.translate).pack(side="left", padx=10)
        tk.Button(bottom, text="COPY", font=("Segoe UI", 11), command=self.copy_text).pack(side="left", padx=10)
        tk.Button(bottom, text="SAVE", font=("Segoe UI", 11), command=self.save_file).pack(side="left", padx=10)
        tk.Button(bottom, text="CLEAR", font=("Segoe UI", 11), command=self.clear_boxes).pack(side="left", padx=10)
        tk.Button(bottom, text="DARK MODE", font=("Segoe UI", 11), command=self.toggle_dark).pack(side="right", padx=10)

    def translate(self):
        text = self.input_box.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Empty Field", "Enter text first.")
            return

        lang = LANGUAGES[self.language.get()]
        params = {"q": text, "langpair": f"en|{lang}"}

        try:
            response = requests.get(API_URL, params=params)
            result = response.json()["responseData"]["translatedText"]
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", result)
        except:
            messagebox.showerror("Error", "Translation failed. Try later.")

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output_box.get("1.0", "end"))

    def save_file(self):
        content = self.output_box.get("1.0", "end").strip()
        if not content:
            messagebox.showerror("Error", "Nothing to save.")
            return

        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Saved", "Email saved successfully.")

    def clear_boxes(self):
        self.input_box.delete("1.0", "end")
        self.output_box.delete("1.0", "end")

    def toggle_dark(self):
        self.dark_mode = not self.dark_mode
        bg = "#1a1a1a" if self.dark_mode else "#f5f5f5"
        fg = "white" if self.dark_mode else "black"

        self.root.configure(bg=bg)
        for widget in self.root.winfo_children():
            try: widget.configure(bg=bg, fg=fg)
            except: pass


if __name__ == "__main__":
    root = tk.Tk()
    AutoTranslateMail(root)
    root.mainloop()

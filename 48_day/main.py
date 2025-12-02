import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Download resources if missing
try:
    nltk.data.find("tokenizers/punkt")
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("punkt")
    nltk.download("stopwords")


class AutoSummarizerPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Day 48 - AutoSummarizer Pro (Offline AI)")
        self.root.geometry("1200x650")
        self.root.configure(bg="#f7f7f7")
        self.dark_mode = False

        self.build_ui()

    def build_ui(self):
        title = tk.Label(self.root, text="AutoSummarizer Pro — Offline AI Summarizer",
                         font=("Segoe UI", 20, "bold"), bg="#f7f7f7")
        title.pack(pady=10)

        frame = tk.Frame(self.root, bg="#f7f7f7")
        frame.pack(fill="both", expand=True, padx=20, pady=10)

        # INPUT TEXT
        left = tk.Frame(frame, bg="#f7f7f7")
        left.pack(side="left", fill="both", expand=True, padx=10)

        tk.Label(left, text="Original Text", font=("Segoe UI", 14, "bold"), bg="#f7f7f7").pack()
        self.input_text = tk.Text(left, font=("Segoe UI", 12), wrap="word", height=22)
        self.input_text.pack(fill="both", expand=True, pady=10)

        # OUTPUT TEXT
        right = tk.Frame(frame, bg="#f7f7f7")
        right.pack(side="right", fill="both", expand=True, padx=10)

        tk.Label(right, text="AI Summary", font=("Segoe UI", 14, "bold"), bg="#f7f7f7").pack()
        self.output_text = tk.Text(right, font=("Segoe UI", 12), wrap="word", height=22)
        self.output_text.pack(fill="both", expand=True, pady=10)

        # SUMMARY LENGTH SLIDER
        controls = tk.Frame(self.root, bg="#f7f7f7")
        controls.pack(fill="x", pady=10)

        tk.Label(controls, text="Summary Length:", font=("Segoe UI", 12), bg="#f7f7f7").pack(side="left", padx=10)

        self.length_var = tk.IntVar(value=30)
        tk.Scale(controls, from_=10, to=60, orient="horizontal", variable=self.length_var,
                 length=200).pack(side="left", padx=10)

        # BUTTONS
        tk.Button(controls, text="SUMMARIZE", font=("Segoe UI", 12, "bold"),
                  command=self.summarize).pack(side="left", padx=10)

        tk.Button(controls, text="COPY", font=("Segoe UI", 11),
                  command=self.copy_text).pack(side="left", padx=10)

        tk.Button(controls, text="SAVE", font=("Segoe UI", 11),
                  command=self.save_file).pack(side="left", padx=10)

        tk.Button(controls, text="CLEAR", font=("Segoe UI", 11),
                  command=self.clear_boxes).pack(side="left", padx=10)

        tk.Button(controls, text="DARK MODE", font=("Segoe UI", 11),
                  command=self.toggle_dark).pack(side="right", padx=10)

    # -------------------
    # SUMMARIZER ENGINE
    # -------------------
    def summarize(self):
        text = self.input_text.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("No Input", "Enter some text to summarize.")
            return

        # Tokenization
        sentences = sent_tokenize(text)
        if len(sentences) < 3:
            messagebox.showwarning("Too Short", "Text should be at least 3 sentences.")
            return

        stop_words = set(stopwords.words("english"))
        word_freq = {}

        # Word Frequency Table
        for word in word_tokenize(text.lower()):
            if word not in stop_words and word not in string.punctuation:
                word_freq[word] = word_freq.get(word, 0) + 1

        # Normalize frequencies
        max_freq = max(word_freq.values())
        for w in word_freq:
            word_freq[w] = word_freq[w] / max_freq

        # Sentence Scoring
        sentence_scores = {}
        for sent in sentences:
            for w in word_tokenize(sent.lower()):
                if w in word_freq:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[w]

        # Select top sentences
        summary_len = max(1, len(sentences) * self.length_var.get() // 100)
        ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
        summary = " ".join(ranked[:summary_len])

        # Show in output box
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", summary)

    # -------------------
    # UTILITY FUNCTIONS
    # -------------------
    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output_text.get("1.0", "end"))

    def save_file(self):
        content = self.output_text.get("1.0", "end").strip()
        if not content:
            messagebox.showerror("Error", "Nothing to save.")
            return

        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Saved", "Summary saved successfully.")

    def clear_boxes(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")

    def toggle_dark(self):
        self.dark_mode = not self.dark_mode
        bg = "#1b1b1b" if self.dark_mode else "#f7f7f7"
        fg = "white" if self.dark_mode else "black"
        self.root.configure(bg=bg)

        for w in self.root.winfo_children():
            try:
                w.configure(bg=bg, fg=fg)
            except:
                pass


if __name__ == "__main__":
    root = tk.Tk()
    AutoSummarizerPro(root)
    root.mainloop()

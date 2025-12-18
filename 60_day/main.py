import tkinter as tk
from tkinter import ttk, messagebox
import random

# ---------------- CONFIG ---------------- #
SEQUENCE_LENGTH = 20
CHOICES = ["A", "B"]
# ---------------------------------------- #

sequence = []


def add_choice(choice):
    if len(sequence) >= SEQUENCE_LENGTH:
        return

    sequence.append(choice)
    update_display()

    if len(sequence) == SEQUENCE_LENGTH:
        analyze_sequence()


def update_display():
    seq_label.config(text=" ".join(sequence))
    count_label.config(text=f"Length: {len(sequence)} / {SEQUENCE_LENGTH}")


def analyze_sequence():
    human_score = 0

    # 1. Repetition avoidance (humans avoid repeats)
    repeats = sum(1 for i in range(1, len(sequence)) if sequence[i] == sequence[i - 1])
    if repeats < 3:
        human_score += 2

    # 2. Alternation bias (humans alternate too much)
    alternations = sum(1 for i in range(1, len(sequence)) if sequence[i] != sequence[i - 1])
    if alternations > len(sequence) * 0.7:
        human_score += 2

    # 3. Distribution imbalance
    count_a = sequence.count("A")
    count_b = sequence.count("B")
    if abs(count_a - count_b) <= 2:
        human_score += 1

    # 4. Long streaks (machines tolerate streaks more)
    max_streak = get_max_streak()
    if max_streak <= 3:
        human_score += 2

    # Verdict
    if human_score >= 5:
        verdict = "🧠 Likely Human-Generated"
    else:
        verdict = "🤖 Likely Machine-Generated"

    messagebox.showinfo(
        "Analysis Result",
        f"Sequence: {' '.join(sequence)}\n\n"
        f"Repeats: {repeats}\n"
        f"Alternations: {alternations}\n"
        f"A Count: {count_a} | B Count: {count_b}\n"
        f"Max Streak: {max_streak}\n\n"
        f"Final Verdict:\n{verdict}"
    )


def get_max_streak():
    max_streak = 1
    current_streak = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 1

    return max_streak


def reset():
    sequence.clear()
    seq_label.config(text="")
    count_label.config(text=f"Length: 0 / {SEQUENCE_LENGTH}")


# ---------------- UI ---------------- #
root = tk.Tk()
root.title("Human Randomness Detector")
root.geometry("520x340")
root.resizable(False, False)

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

title = ttk.Label(
    frame,
    text="🧠 Human Randomness Detector",
    font=("Segoe UI", 16, "bold")
)
title.pack(pady=(0, 5))

subtitle = ttk.Label(
    frame,
    text="Generate a random sequence. We’ll judge it.",
    foreground="gray"
)
subtitle.pack(pady=(0, 15))

seq_label = ttk.Label(
    frame,
    text="",
    wraplength=480,
    font=("Segoe UI", 12)
)
seq_label.pack(pady=10)

count_label = ttk.Label(frame, text="Length: 0 / 20")
count_label.pack(pady=5)

btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=10)

btn_a = ttk.Button(btn_frame, text="A", command=lambda: add_choice("A"))
btn_a.grid(row=0, column=0, padx=10)

btn_b = ttk.Button(btn_frame, text="B", command=lambda: add_choice("B"))
btn_b.grid(row=0, column=1, padx=10)

reset_btn = ttk.Button(frame, text="Reset", command=reset)
reset_btn.pack(pady=10)

root.mainloop()

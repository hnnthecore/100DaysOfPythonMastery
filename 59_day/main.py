import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

# ---------------- CONFIG ---------------- #
ROUNDS = 8
TIME_LIMIT = 4.0  # seconds per round

COLORS = {
    "RED": "red",
    "BLUE": "blue",
    "GREEN": "green",
    "YELLOW": "gold"
}
# ---------------------------------------- #

current_round = 0
start_time = 0
score = 0
reaction_times = []

current_correct_color = ""


def start_game():
    global current_round, score, reaction_times
    current_round = 0
    score = 0
    reaction_times = []
    start_btn.config(state="disabled")
    next_round()


def next_round():
    global current_round, start_time, current_correct_color

    if current_round >= ROUNDS:
        end_game()
        return

    word = random.choice(list(COLORS.keys()))
    color = random.choice(list(COLORS.values()))

    current_correct_color = color

    stimulus_label.config(text=word, foreground=color)
    round_label.config(text=f"Round {current_round + 1} / {ROUNDS}")

    start_time = time.perf_counter()
    root.after(int(TIME_LIMIT * 1000), timeout)

    current_round += 1


def timeout():
    messagebox.showwarning("Too Slow!", "You didn’t respond in time!")
    reaction_times.append(TIME_LIMIT)
    next_round()


def submit_choice(choice):
    global score

    end_time = time.perf_counter()
    reaction_time = end_time - start_time
    reaction_times.append(round(reaction_time, 2))

    if choice == current_correct_color:
        score += 1

    next_round()


def end_game():
    start_btn.config(state="normal")

    avg_time = round(sum(reaction_times) / len(reaction_times), 2)

    if score >= 6:
        verdict = "🧠 Sharp Focus"
    elif score >= 4:
        verdict = "😐 Moderate Load"
    else:
        verdict = "🥵 Cognitive Overload"

    messagebox.showinfo(
        "Results",
        f"Score: {score}/{ROUNDS}\n"
        f"Average Reaction Time: {avg_time}s\n\n"
        f"Final Verdict: {verdict}"
    )


# ---------------- UI ---------------- #
root = tk.Tk()
root.title("Cognitive Load Reaction Test")
root.geometry("420x380")
root.resizable(False, False)

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

title = ttk.Label(
    frame,
    text="🎯 Cognitive Load Test",
    font=("Segoe UI", 16, "bold")
)
title.pack(pady=(0, 5))

subtitle = ttk.Label(
    frame,
    text="Choose the COLOR — not the word",
    foreground="gray"
)
subtitle.pack(pady=(0, 15))

round_label = ttk.Label(frame, text="Click Start", font=("Segoe UI", 11))
round_label.pack(pady=5)

stimulus_label = ttk.Label(
    frame,
    text="READY",
    font=("Segoe UI", 28, "bold")
)
stimulus_label.pack(pady=20)

btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=10)

for name, color in COLORS.items():
    btn = ttk.Button(
        btn_frame,
        text=name,
        command=lambda c=color: submit_choice(c)
    )
    btn.pack(side="left", padx=5)

start_btn = ttk.Button(frame, text="Start Test", command=start_game)
start_btn.pack(pady=15)

root.mainloop()

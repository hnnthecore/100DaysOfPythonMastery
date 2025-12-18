import tkinter as tk
from tkinter import ttk, messagebox
import time

# ---------------- CONFIG ---------------- #
QUESTIONS = [
    "What is your full name?",
    "What city were you born in?",
    "Did you lie today?",
    "What was your last meal?",
    "Have you ever broken a rule on purpose?"
]

HESITATION_THRESHOLD = 2.5  # seconds
BACKSPACE_WEIGHT = 0.7
TIME_WEIGHT = 1.3
# ---------------------------------------- #

current_question_index = 0
start_time = 0
backspace_count = 0
results = []


def start_test():
    global current_question_index, results
    current_question_index = 0
    results = []
    start_btn.config(state="disabled")
    show_question()


def show_question():
    global start_time, backspace_count

    backspace_count = 0
    answer_entry.delete(0, tk.END)
    answer_entry.focus()

    question_label.config(
        text=f"Q{current_question_index + 1}: {QUESTIONS[current_question_index]}"
    )

    start_time = time.perf_counter()


def track_backspace(event):
    global backspace_count
    if event.keysym == "BackSpace":
        backspace_count += 1


def submit_answer():
    global current_question_index

    end_time = time.perf_counter()
    response_time = end_time - start_time

    score = (response_time * TIME_WEIGHT) + (backspace_count * BACKSPACE_WEIGHT)

    if response_time > HESITATION_THRESHOLD or backspace_count > 2:
        verdict = "🤔 Hesitant"
    else:
        verdict = "😎 Confident"

    results.append({
        "question": QUESTIONS[current_question_index],
        "time": round(response_time, 2),
        "backspaces": backspace_count,
        "verdict": verdict
    })

    current_question_index += 1

    if current_question_index < len(QUESTIONS):
        show_question()
    else:
        end_test()


def end_test():
    start_btn.config(state="normal")
    summary = ""

    hesitant_count = 0
    for r in results:
        summary += (
            f"{r['question']}\n"
            f"Time: {r['time']}s | Backspaces: {r['backspaces']}\n"
            f"Verdict: {r['verdict']}\n\n"
        )
        if "Hesitant" in r["verdict"]:
            hesitant_count += 1

    if hesitant_count >= 3:
        final_result = "🚨 High Hesitation Detected"
    elif hesitant_count == 2:
        final_result = "⚠️ Mixed Confidence"
    else:
        final_result = "✅ High Confidence"

    messagebox.showinfo(
        "Lie Detector Result",
        summary + f"\nFinal Analysis: {final_result}"
    )


# ---------------- UI ---------------- #
root = tk.Tk()
root.title("Digital Lie Detector")
root.geometry("500x320")
root.resizable(False, False)

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

title_label = ttk.Label(
    frame,
    text="🧬 Digital Lie Detector",
    font=("Segoe UI", 16, "bold")
)
title_label.pack(pady=(0, 10))

subtitle_label = ttk.Label(
    frame,
    text="We analyze hesitation — not truth.",
    foreground="gray"
)
subtitle_label.pack(pady=(0, 15))

question_label = ttk.Label(
    frame,
    text="Click Start to Begin",
    wraplength=460,
    font=("Segoe UI", 11)
)
question_label.pack(pady=10)

answer_entry = ttk.Entry(frame, font=("Segoe UI", 11))
answer_entry.pack(fill="x", pady=10)
answer_entry.bind("<KeyPress>", track_backspace)

btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=10)

submit_btn = ttk.Button(btn_frame, text="Submit Answer", command=submit_answer)
submit_btn.grid(row=0, column=0, padx=5)

start_btn = ttk.Button(btn_frame, text="Start Test", command=start_test)
start_btn.grid(row=0, column=1, padx=5)

root.mainloop()

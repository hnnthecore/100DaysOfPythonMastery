"""
PyOS - Python Operating System
------------------------------
A symbolic operating system built in Python that
demonstrates system thinking, modular design,
event processing, decision logic, and AI-style reasoning.

This project summarizes the entire 100-day journey.
"""

import time
import random
from collections import Counter


# -----------------------------
# SYSTEM STATE
# -----------------------------
system_memory = []
event_log = []
knowledge_base = {
    "python": "Python is a versatile language for automation, data, and systems.",
    "automation": "Automation reduces repetitive tasks using scripts.",
    "data": "Data analysis extracts insight from structured information.",
    "career": "Strong fundamentals lead to long-term growth."
}


# -----------------------------
# CORE SERVICES
# -----------------------------
def log_event(message):
    timestamp = time.strftime("%H:%M:%S")
    event_log.append(f"[{timestamp}] {message}")


def system_status():
    print("\nSYSTEM STATUS")
    print("-" * 30)
    print(f"Memory entries: {len(system_memory)}")
    print(f"Events logged: {len(event_log)}")


# -----------------------------
# AI REASONING MODULE
# -----------------------------
def ai_query(question):
    words = question.lower().split()
    scores = Counter()

    for key, value in knowledge_base.items():
        for word in words:
            if word in value.lower():
                scores[key] += 1

    if not scores:
        return "No relevant knowledge found."

    best = scores.most_common(1)[0][0]
    return knowledge_base[best]


# -----------------------------
# DECISION ENGINE
# -----------------------------
def decision_engine():
    print("\nDecision Engine")
    focus = int(input("Focus level (1-5): "))
    time_available = int(input("Time available (1-5): "))

    score = focus + time_available

    if score >= 8:
        return "Work on a complex system-level project."
    elif score >= 5:
        return "Improve an existing project."
    else:
        return "Revise fundamentals and rest."


# -----------------------------
# EVENT SIMULATION
# -----------------------------
def generate_event():
    event = random.choice([
        "USER_LOGIN",
        "DATA_PROCESSED",
        "ERROR_DETECTED",
        "TASK_COMPLETED"
    ])
    log_event(event)
    print("Event:", event)


# -----------------------------
# PYOS SHELL
# -----------------------------
def pyos_shell():
    print("\nWelcome to PyOS")
    print("Type 'help' to see available commands.")

    while True:
        command = input("\nPyOS > ").strip().lower()

        if command == "help":
            print("""
commands:
  status     - system status
  event      - generate system event
  remember   - store a memory
  recall     - view memories
  ask        - ask the AI engine
  decide     - run decision engine
  logs       - view system logs
  exit       - shutdown PyOS
            """)

        elif command == "status":
            system_status()

        elif command == "event":
            generate_event()

        elif command == "remember":
            memory = input("Enter memory: ")
            system_memory.append(memory)
            log_event("Memory stored")

        elif command == "recall":
            print("\nMEMORY")
            for m in system_memory:
                print("-", m)

        elif command == "ask":
            q = input("Ask a question: ")
            answer = ai_query(q)
            print("AI:", answer)

        elif command == "decide":
            decision = decision_engine()
            print("Decision:", decision)

        elif command == "logs":
            print("\nSYSTEM LOGS")
            for e in event_log[-10:]:
                print(e)

        elif command == "exit":
            print("Shutting down PyOS...")
            break

        else:
            print("Unknown command")


# -----------------------------
# BOOT SEQUENCE
# -----------------------------
def main():
    print("Booting PyOS...")
    time.sleep(1)
    pyos_shell()


if __name__ == "__main__":
    main()

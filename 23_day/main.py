# Day 23 - PuzzlePy: Logic Puzzle Generator
# An interactive puzzle generator and solver for math, words, and logic-based challenges.

import random
import time
import json
import os
from datetime import datetime

SCORE_FILE = "puzzlepy_scores.json"

# --------------------------------------------------
# Utility Functions
# --------------------------------------------------
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"games_played": 0, "correct": 0, "incorrect": 0}


def save_scores(scores):
    with open(SCORE_FILE, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=4)


def update_score(is_correct):
    scores = load_scores()
    scores["games_played"] += 1
    if is_correct:
        scores["correct"] += 1
    else:
        scores["incorrect"] += 1
    save_scores(scores)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# --------------------------------------------------
# Puzzle Generators
# --------------------------------------------------
def math_puzzle():
    operations = ["+", "-", "*"]
    a, b = random.randint(2, 12), random.randint(2, 12)
    op = random.choice(operations)
    expression = f"{a} {op} {b}"
    correct = eval(expression)
    print(f"Solve this: {expression}")
    answer = input("Your answer: ").strip()

    try:
        if int(answer) == correct:
            print("Correct!")
            update_score(True)
        else:
            print(f"Incorrect. The answer was {correct}.")
            update_score(False)
    except ValueError:
        print(f"Invalid input. The correct answer was {correct}.")
        update_score(False)


def word_puzzle():
    words = ["python", "algorithm", "variable", "developer", "terminal"]
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    print(f"Unscramble this word: {scrambled}")
    answer = input("Your guess: ").strip().lower()

    if answer == word:
        print("Correct!")
        update_score(True)
    else:
        print(f"Incorrect. The word was '{word}'.")
        update_score(False)


def logic_puzzle():
    puzzles = [
        {
            "question": "A farmer has 17 sheep, and all but 9 run away. How many are left?",
            "answer": "9"
        },
        {
            "question": "You’re running a race and pass the person in 2nd place. What place are you in?",
            "answer": "2"
        },
        {
            "question": "What five-letter word becomes shorter when you add two letters to it?",
            "answer": "short"
        },
    ]
    puzzle = random.choice(puzzles)
    print(puzzle["question"])
    answer = input("Your answer: ").strip().lower()

    if answer == puzzle["answer"]:
        print("Correct!")
        update_score(True)
    else:
        print(f"Incorrect. The answer was '{puzzle['answer']}'.")
        update_score(False)


# --------------------------------------------------
# Main Game Loop
# --------------------------------------------------
def show_scoreboard():
    scores = load_scores()
    print("\n--- Scoreboard ---")
    print(f"Games Played: {scores['games_played']}")
    print(f"Correct: {scores['correct']}")
    print(f"Incorrect: {scores['incorrect']}")
    print("------------------\n")


def main():
    while True:
        clear_screen()
        print("=" * 60)
        print(" PUZZLEPY – LOGIC PUZZLE GENERATOR ".center(60))
        print("=" * 60)
        print("Select a puzzle type:")
        print("1. Math Puzzle")
        print("2. Word Puzzle")
        print("3. Logic Puzzle")
        print("4. View Scoreboard")
        print("5. Exit")
        print("-" * 60)

        choice = input("Enter your choice: ").strip()

        clear_screen()
        if choice == "1":
            math_puzzle()
        elif choice == "2":
            word_puzzle()
        elif choice == "3":
            logic_puzzle()
        elif choice == "4":
            show_scoreboard()
        elif choice == "5":
            print("Thanks for playing PuzzlePy!")
            break
        else:
            print("Invalid choice. Try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

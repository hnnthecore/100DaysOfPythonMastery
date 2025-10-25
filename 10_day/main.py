# Day 10 - Advanced Dice Roll Game 🎲
# Project: Multi-dice simulator with animation, score tracking, and session logging

import random
import time
import os
import sys
import itertools
from datetime import datetime

# Dice faces using ASCII art
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘",
    ),
}


def clear_screen():
    """Clears terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def rolling_animation():
    """Displays a spinning animation for realism."""
    spinner = itertools.cycle(["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"])
    print("Rolling the dice ", end="")
    for _ in range(15):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
    print("\n")


def show_dice(value):
    """Displays the ASCII art for the rolled dice."""
    for line in DICE_ART[value]:
        print(line)


def log_result(results, total):
    """Logs dice results to a file with timestamp."""
    with open("dice_log.txt", "a", encoding="utf-8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} | Rolled: {results} | Total: {total}\n")


def main():
    """Main interactive loop."""
    print("🎲 Welcome to the Advanced Dice Roll Game! 🎲\n")

    roll_count = 0
    total_score = 0
    highest_roll = 0

    while True:
        # Choose how many dice to roll
        while True:
            num_dice = input("How many dice do you want to roll? (1–5): ")
            if not num_dice.isdigit() or not 1 <= int(num_dice) <= 5:
                print("Please enter a number between 1 and 5.\n")
                continue
            num_dice = int(num_dice)
            break

        clear_screen()
        rolling_animation()

        # Generate dice values
        results = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(results)

        print(f"You rolled {num_dice} dice!\n")
        for val in results:
            show_dice(val)
            time.sleep(0.3)

        print(f"\n🎯 Total value: {total}\n")

        # Update stats
        roll_count += num_dice
        total_score += total
        if total > highest_roll:
            highest_roll = total

        # Log the result
        log_result(results, total)

        # Ask user for next step
        choice = input("Roll again? (y/n): ").lower().strip()
        if choice != "y":
            break

        clear_screen()

    # Show session summary
    if roll_count > 0:
        print("\n--- Game Summary ---")
        print(f"Total dice rolled: {roll_count}")
        print(f"Average roll value: {total_score / roll_count:.2f}")
        print(f"Highest total rolled: {highest_roll}")
    print("\nThanks for playing! Goodbye 👋\n")


if __name__ == "__main__":
    main()

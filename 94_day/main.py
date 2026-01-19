import random
import string
from collections import Counter
import re

# -----------------------------
# TOOL 1: Text Analyzer
# -----------------------------
def text_analyzer():
    text = input("\nEnter text to analyze:\n> ")

    words = re.findall(r"\b\w+\b", text.lower())
    sentences = re.split(r"[.!?]", text)

    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()])
    common_words = Counter(words).most_common(5)

    print("\n📊 Text Analysis Result")
    print("-" * 30)
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")

    print("\nMost Common Words:")
    for word, count in common_words:
        print(f"- {word}: {count}")


# -----------------------------
# TOOL 2: Password Strength Checker
# -----------------------------
def password_checker():
    password = input("\nEnter password:\n> ")

    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    print("\n🔐 Password Strength")
    print("-" * 30)

    if score <= 1:
        print("Weak ❌")
    elif score == 2:
        print("Moderate ⚠️")
    elif score == 3:
        print("Strong ✅")
    else:
        print("Very Strong 💪")


# -----------------------------
# TOOL 3: Number Analyzer
# -----------------------------
def number_analyzer():
    raw = input("\nEnter numbers (comma separated):\n> ")

    try:
        numbers = [int(n.strip()) for n in raw.split(",")]
    except ValueError:
        print("❌ Invalid numbers")
        return

    print("\n🔢 Number Analysis")
    print("-" * 30)
    print(f"Count: {len(numbers)}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")


# -----------------------------
# TOOL 4: Random Generator
# -----------------------------
def random_generator():
    print("\n🎲 Random Generator")
    print("1. Random Number")
    print("2. Random Password")

    choice = input("> ")

    if choice == "1":
        print("Random Number:", random.randint(1, 100))
    elif choice == "2":
        pwd = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        print("Random Password:", pwd)
    else:
        print("Invalid choice")


# -----------------------------
# MAIN MENU
# -----------------------------
def main_menu():
    while True:
        print("\n🧠 PYTHON PLAYGROUND")
        print("=" * 30)
        print("1. Text Analyzer")
        print("2. Password Strength Checker")
        print("3. Number Analyzer")
        print("4. Random Generator")
        print("5. Exit")

        choice = input("> ")

        if choice == "1":
            text_analyzer()
        elif choice == "2":
            password_checker()
        elif choice == "3":
            number_analyzer()
        elif choice == "4":
            random_generator()
        elif choice == "5":
            print("👋 Exiting Playground")
            break
        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main_menu()

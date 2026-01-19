import datetime
import time
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_FILE = os.path.join(BASE_DIR, "notes.txt")


# -----------------------------
# UTILITY FUNCTIONS
# -----------------------------
def show_datetime():
    now = datetime.datetime.now()
    print("\n📅 Current Date & Time")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def add_note():
    note = input("\n📝 Enter your note:\n> ").strip()
    if not note:
        print("❌ Empty note not saved")
        return

    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(note + "\n")

    print("✅ Note saved")


def view_notes():
    print("\n📒 Your Notes")
    print("-" * 30)

    if not os.path.exists(NOTES_FILE):
        print("No notes found")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        notes = f.readlines()

    if not notes:
        print("No notes yet")
        return

    for i, note in enumerate(notes, 1):
        print(f"{i}. {note.strip()}")


def search_notes():
    keyword = input("\n🔍 Search keyword:\n> ").lower()

    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        notes = f.readlines()

    results = [n for n in notes if keyword in n.lower()]

    print("\n🔎 Search Results")
    print("-" * 30)

    if not results:
        print("No matching notes")
        return

    for note in results:
        print("-", note.strip())


def set_reminder():
    try:
        minutes = int(input("\n⏰ Reminder in how many minutes?\n> "))
    except ValueError:
        print("❌ Invalid time")
        return

    print(f"⏳ Reminder set for {minutes} minutes...")
    time.sleep(minutes * 60)
    print("\n🔔 REMINDER: Time's up!")


def random_helper():
    options = input("\n🎲 Enter options (comma separated):\n> ")
    choices = [o.strip() for o in options.split(",") if o.strip()]

    if not choices:
        print("❌ No options provided")
        return

    print("✅ Random choice:", random.choice(choices))


# -----------------------------
# MAIN MENU
# -----------------------------
def main():
    while True:
        print("\n🤖 SMART CLI ASSISTANT")
        print("=" * 30)
        print("1. Show date & time")
        print("2. Add a note")
        print("3. View notes")
        print("4. Search notes")
        print("5. Set a reminder")
        print("6. Random helper")
        print("7. Exit")

        choice = input("> ")

        if choice == "1":
            show_datetime()
        elif choice == "2":
            add_note()
        elif choice == "3":
            view_notes()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            set_reminder()
        elif choice == "6":
            random_helper()
        elif choice == "7":
            print("👋 Goodbye")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()

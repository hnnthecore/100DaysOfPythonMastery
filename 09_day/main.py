# Day 9 - Expense Tracker
# Project: Track and manage daily expenses using file handling and simple data storage

from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    """Add a new expense entry."""
    description = input("Enter expense description: ").strip()
    category = input("Enter category (food, travel, bills, etc.): ").capitalize()

    # Validate amount input
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{date},{description},{category},{amount:.2f}\n"

    # Append new entry to CSV file
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(entry)

    print(f"Expense added: {description} - {category} - {amount:.2f}\n")


def view_expenses():
    """Display all recorded expenses."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = file.readlines()
            if not data:
                print("No expenses recorded yet.\n")
                return

            print("\n--- Expense History ---")
            print(f"{'Date':<20} {'Description':<20} {'Category':<15} {'Amount':>10}")
            print("-" * 70)

            for line in data:
                date, desc, cat, amount = line.strip().split(",")
                print(f"{date:<20} {desc:<20} {cat:<15} {amount:>10}")
            print()
    except FileNotFoundError:
        print("No expense file found. Add an expense first.\n")


def show_total():
    """Calculate and display total spending."""
    total = 0
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    try:
                        total += float(parts[3])
                    except ValueError:
                        pass
        print(f"\nTotal recorded expenses: {total:.2f}\n")
    except FileNotFoundError:
        print("No expense file found. Add an expense first.\n")


def view_by_category():
    """Show total spending by category."""
    category_totals = {}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    category = parts[2]
                    try:
                        amount = float(parts[3])
                        category_totals[category] = category_totals.get(category, 0) + amount
                    except ValueError:
                        pass

        if category_totals:
            print("\n--- Spending by Category ---")
            for cat, total in category_totals.items():
                print(f"{cat:<15}: {total:.2f}")
            print()
        else:
            print("No categorized expenses yet.\n")
    except FileNotFoundError:
        print("No expense file found.\n")


def main():
    """Main menu for Expense Tracker."""
    print("Welcome to the Expense Tracker!\n")

    while True:
        print("Options: add / view / total / category / exit")
        choice = input("Enter your choice: ").lower().strip()

        if choice == "add":
            add_expense()
        elif choice == "view":
            view_expenses()
        elif choice == "total":
            show_total()
        elif choice == "category":
            view_by_category()
        elif choice == "exit":
            print("Goodbye! Your expenses are safely saved.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()

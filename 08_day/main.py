# Day 8 - Coffee Machine Simulator
# Project: Real-world coffee vending simulation using functions, loops, and dictionaries

# Menu data containing required ingredients and cost for each drink
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

# Machine resources
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}


def print_report():
    """Print the current status of resources."""
    print("\nMachine Report:")
    for item, value in resources.items():
        if item == "water" or item == "milk":
            print(f"{item.capitalize()}: {value}ml")
        elif item == "coffee":
            print(f"{item.capitalize()}: {value}g")
        elif item == "money":
            print(f"{item.capitalize()}: CHF {value:.2f}")
    print()


def check_resources(drink):
    """Check if there are enough resources to make the drink."""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.\n")
            return False
    return True


def process_coins():
    """Calculate the total money inserted."""
    print("Please insert coins.")
    total = 0
    try:
        total += int(input("How many 1 CHF coins?: ")) * 1
        total += int(input("How many 0.5 CHF coins?: ")) * 0.5
        total += int(input("How many 0.2 CHF coins?: ")) * 0.2
    except ValueError:
        print("Invalid input. Coins not recognized.\n")
    return round(total, 2)


def transaction_successful(payment, drink_cost):
    """Return True when the payment is accepted, or False if insufficient."""
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        if change > 0:
            print(f"Transaction successful! Here is CHF {change:.2f} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.\n")
        return False


def make_coffee(drink):
    """Deduct ingredients from resources and serve the coffee."""
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!\n")


# Main control loop
print("Welcome to the Coffee Machine ")

while True:
    choice = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()

    if choice == "exit":
        print("Turning off the coffee machine. Goodbye!")
        break

    elif choice == "report":
        print_report()

    elif choice in MENU:
        if check_resources(choice):
            payment = process_coins()
            if transaction_successful(payment, MENU[choice]["cost"]):
                make_coffee(choice)
    else:
        print("Invalid choice. Please try again.\n")

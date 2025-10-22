# Day 7 - Tip Calculator
# Project: Calculate per-person restaurant bill including tip 

def calculate_tip(total_bill, tip_percent, people_count):
    """Calculate the amount each person should pay."""
    tip_amount = total_bill * (tip_percent / 100)
    total_with_tip = total_bill + tip_amount
    amount_per_person = total_with_tip / people_count
    return round(amount_per_person, 2)

print("Welcome to the Tip Calculator!")

# Input validation
while True:
    try:
        total_bill = float(input("Enter the total bill amount (CHF): "))
        tip_percent = float(input("Enter the tip percentage you'd like to give (e.g. 10, 12, 15): "))
        people_count = int(input("How many people to split the bill? "))

        if total_bill <= 0 or people_count <= 0:
            print("Please enter positive values.\n")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

# Calculation
each_pay = calculate_tip(total_bill, tip_percent, people_count)

# Output
print(f"\nEach person should pay: CHF {each_pay:.2f}")
print("Danke! Enjoy your meal 🇨🇭")

# Day 2 - Python Variables, Data Types & Simple Calculator
# Project: Simple Calculator


# Intro message with flair
print("Jarvis Offline... Activating Tony Stark's Backup Calculator System")

# Ask user for two numbers
num1 = float(input("Enter the first number, Boss: "))
num2 = float(input("Enter the second number: "))

# Display operation options
print("\nAvailable operations:")
print(" + for Addition")
print(" - for Subtraction")
print(" * for Multiplication")
print(" / for Division")

# Ask for operation
operation = input("\nWhich operation do you want to perform? ")

# Process operation
if operation == '+':
    result = num1 + num2
    print(f"\n Jarvis (in spirit): The result is {result}. You’re a genius, Boss!")
elif operation == '-':
    result = num1 - num2
    print(f"\n The result is {result}. Precision at its finest, just like your armor plating.")
elif operation == '*':
    result = num1 * num2
    print(f"\n Multiplication complete. {num1} × {num2} = {result}. Power levels rising ⚡")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\n Division done. {num1} ÷ {num2} = {result:.2f}")
    else:
        print("\n Jarvis Warning: Division by zero detected. Even Stark tech can’t compute that!")
else:
    print("\n Invalid operation. Looks like you’ve been working too late again, Tony.")

# Exit line
print("\n Tony Mode: Calculation complete. Time to save the world again, Boss!")

# Day 5 - Random Password Generator
# Project: Generate a secure, randomized password using loops and random module

import random

print("Welcome to the Python Password Generator!")

# Character sets
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+@?")

# Function to safely get an integer input
def get_int_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid positive number.\n")

# Get user input safely
num_letters = get_int_input("How many letters would you like in your password? ")
num_symbols = get_int_input("How many symbols would you like? ")
num_numbers = get_int_input("How many numbers would you like? ")

# Build password components
password_chars = []

for _ in range(num_letters):
    password_chars.append(random.choice(letters))

for _ in range(num_symbols):
    password_chars.append(random.choice(symbols))

for _ in range(num_numbers):
    password_chars.append(random.choice(numbers))

# Shuffle for randomness
random.shuffle(password_chars)

# Combine into final password
password = "".join(password_chars)

print("\nYour generated password is:", password)
print("Tip: Save it somewhere safe.")

# Day 6 - The Number Guessing Game
# Project: Guess the random number using hints and limited attempts

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it?\n")

# Generate random number
target_number = random.randint(1, 100)
attempts = 0
guessed = False

# Function to safely get integer input
def get_int_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid number.\n")

# Main guessing loop
while not guessed:
    guess = get_int_input("Enter your guess: ")
    attempts += 1

    if guess < 1 or guess > 100:
        print("Your guess is out of range! Try a number between 1 and 100.\n")
        continue

    if guess < target_number:
        print("Too low! Try again.\n")
    elif guess > target_number:
        print("Too high! Try again.\n")
    else:
        guessed = True
        print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")

# Game summary
if attempts <= 3:
    print("Excellent! You’ve got sharp instincts.")
elif attempts <= 7:
    print("Nice work! You’re getting the hang of it.")
else:
    print("You got it! A little practice will make you faster next time.")

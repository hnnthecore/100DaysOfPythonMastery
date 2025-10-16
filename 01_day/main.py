# Day 1 - Working with Variables in Python


# Prints a welcome message
print("🍷 Welcome to The Family! 🍷")

# Ask the user for their name and store it in a variable called 'name'
name = input("What is your name, my friend? ")

# Ask for their age and convert the input (which is a string) into an integer
age = int(input("And how old are you? "))

# f-string (formatted string):
# The 'f' before the string lets you embed variables directly inside curly braces { }.
# It automatically handles type conversion and makes string concatenation cleaner.
# You can even use expressions inside it, such as {age + 1}.
print(f"Ahh {name}, in a year you’ll be {age + 1}... even wiser, like Don Vito Corleone himself.")


# Notice the 'f' before the string to ensure variable substitution
print(f"Remember, {name}... 'Great coders aren't born great, they grow great... through practice.'")

# End with a friendly sign-off
print("Now go make your offer to Python that it can't refuse!")

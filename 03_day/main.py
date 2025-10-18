# Day 3 - Strings, Slicing & The Time Traveler’s Code
# Project: Transform a user’s message using string operations

print("⏳ Welcome, Time Traveler!")
print("Your mission: encode your message so only those from the past can read it.\n")

# Step 1: Get message input
message = input("Enter your secret phrase: ")

# Step 2: Apply transformations
reversed_message = message[::-1]                # This is used to reverse the string
encoded_message = reversed_message.replace("a", "@").replace("e", "3") \
                                   .replace("i", "!").replace("o", "0").replace("u", "µ")

# Step 3: Create a time code (length + count of vowels)
vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in message if ch in vowels)
time_code = len(message) * vowel_count

# Step 4: Display final result
print("\n Transmission complete!")
print(f" Original Message: {message}")
print(f" Encoded Message: {encoded_message}")
print(f" Time Code (Length × Vowels): {time_code}")

# Step 5: Print the output
print("\n Keep this code safe, traveler. Only those who know Python can decode it again.")

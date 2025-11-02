# Day 18 - ChatMind: Offline AI Chatbot
# A simple rule-based chatbot that remembers your past messages.

import json
import random
import os
import datetime

LOG_FILE = "chatmind_memory.json"

# ------------------------------------------------------------
# Core memory handling
# ------------------------------------------------------------
def load_memory():
    """Load chat history from JSON file."""
    if not os.path.exists(LOG_FILE):
        return {"history": []}
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(memory):
    """Save updated memory to JSON file."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4)


# ------------------------------------------------------------
# Response Logic
# ------------------------------------------------------------
def get_greeting():
    """Random friendly greeting."""
    greetings = [
        "Hey there, human!",
        "Hello 👋 How’s your day?",
        "Welcome back to ChatMind!",
        "Good to see you again.",
        "Hi there! Ready to chat?",
    ]
    return random.choice(greetings)


def simple_response(user_input):
    """Return rule-based responses."""
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return get_greeting()

    elif "how are you" in user_input:
        return "I'm just code, but feeling quite alive today!"

    elif "name" in user_input:
        return "You can call me ChatMind — your friendly offline assistant."

    elif "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."

    elif "date" in user_input:
        return f"Today's date is {datetime.datetime.now().strftime('%A, %d %B %Y')}."

    elif "joke" in user_input:
        jokes = [
            "Why did the developer go broke? Because he used up all his cache.",
            "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.'",
            "Why do Java developers wear glasses? Because they can’t C#.",
        ]
        return random.choice(jokes)

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye for now! I’ll remember this chat."

    else:
        fallback = [
            "Hmm… I’m still learning. Tell me more.",
            "That’s interesting. What makes you say that?",
            "I didn’t quite catch that — could you explain a bit?",
            "Fascinating. Keep going!",
        ]
        return random.choice(fallback)


# ------------------------------------------------------------
# Chat loop
# ------------------------------------------------------------
def chat():
    print("=" * 60)
    print(" CHATMIND – OFFLINE AI CHATBOT ".center(60))
    print("=" * 60)
    print("Type 'exit' anytime to end the chat.\n")

    memory = load_memory()
    print(get_greeting())

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "bye"]:
            response = simple_response(user_input)
            print(f"ChatMind: {response}")
            break

        response = simple_response(user_input)
        print(f"ChatMind: {response}")

        memory["history"].append(
            {"timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             "user": user_input,
             "bot": response}
        )
        save_memory(memory)


if __name__ == "__main__":
    chat()

from engine import Life
from data import ACTIONS

life = Life()

print("🎮 Welcome to Life Simulator")
print("Survive. Thrive. Or fail.\n")

while True:
    print("📊 Stats:", life.stats)

    if life.is_game_over():
        print("\n💀 Game Over. Your life collapsed.")
        break

    print("\nChoose an action:")
    for action in ACTIONS:
        print("-", action)

    choice = input("> ").strip()

    if choice not in ACTIONS:
        print("❌ Invalid choice.")
        continue

    event_text = life.apply_action(choice)

    if event_text:
        print("⚠️ Event:", event_text)

    print("-" * 40)

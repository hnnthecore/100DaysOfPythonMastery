# Day 11 - Escape the Labyrinth (Text Adventure Game)
# A story-driven game where every choice affects your path.
# Focus: conditionals, loops, random events, dictionaries, and functions.

import random
import time

# Game map layout (you can expand this later)
rooms = {
    "entrance": {"desc": "a dark, damp room with faint light from the ceiling.",
                 "paths": {"north": "hall", "east": "trap"}},
    "hall": {"desc": "a long corridor lined with torches. The air feels heavy.",
             "paths": {"south": "entrance", "east": "treasure", "north": "exit"}},
    "trap": {"desc": "a narrow passage. You hear strange whispers...",
             "paths": {"west": "entrance"}},
    "treasure": {"desc": "a glittering chamber filled with golden coins and relics.",
                 "paths": {"west": "hall"}},
    "exit": {"desc": "a tall stone door with sunlight peeking through the cracks.",
             "paths": {}}
}

# Random events that might happen in certain rooms
events = [
    "You found an old rusty sword — might be useful later.",
    "A hidden dart flies past your ear! That was close.",
    "You hear footsteps behind you... but see nothing.",
    "You found a mysterious key. It hums with faint energy.",
    "A cold wind whispers your name. Creepy..."
]

def slow_print(text, delay=0.03):
    """Print text with a typewriter-like delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def explore_room(room_name):
    """Describe current room and trigger possible events."""
    room = rooms[room_name]
    slow_print(f"\nYou are in {room['desc']}")
    if random.random() < 0.4:  # 40% chance of random event
        event = random.choice(events)
        slow_print(event)
    return room['paths']

def game_intro():
    """Display game introduction."""
    print("===================================")
    print(" 🧭 WELCOME TO ESCAPE THE LABYRINTH 🧭")
    print("===================================\n")
    slow_print("You awaken in total darkness...")
    slow_print("Your head aches, your torch flickers, and you realize you are trapped.")
    slow_print("You must find a way out before the torch dies.\n")

def play_game():
    """Main game loop."""
    game_intro()
    current_room = "entrance"
    torch_timer = 10  # limited moves before torch burns out

    while True:
        if torch_timer == 0:
            slow_print("\n💀 Your torch dies out. You’re lost forever in the darkness...")
            break

        paths = explore_room(current_room)
        torch_timer -= 1

        if current_room == "exit":
            slow_print("\n🌄 You push open the stone door and escape into daylight!")
            slow_print("You survived the labyrinth. Well done, adventurer!")
            break

        slow_print(f"\nAvailable paths: {', '.join(paths.keys())}")
        move = input("Which direction do you go? ").lower().strip()

        if move in paths:
            current_room = paths[move]
        else:
            slow_print("You bump into a wall — that direction doesn’t exist!")

        # Random chance of torch flickering
        if random.random() < 0.2:
            slow_print("Your torch flickers... the light weakens.")

    slow_print("\nWould you like to play again? (y/n)")
    choice = input("> ").lower()
    if choice == "y":
        play_game()
    else:
        slow_print("\nFarewell, brave explorer.")

# Run the game
if __name__ == "__main__":
    play_game()

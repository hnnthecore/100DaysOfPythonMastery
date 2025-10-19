# Day 4 - The Treasure Hunt Adventure Game 🗺️

# Project: Text-based Adventure using Conditional Statements

print("Welcome to Treasure Island!")
print("Your mission is to find the lost treasure of Eldorado.")
print("Make your choices wisely — one wrong move could cost you the game!\n")

# First Decision: Crossroad
choice1 = input("You’re at a crossroad. Do you want to go 'left' or 'right'? ").lower()

if choice1 == "left":
    print("\nYou take the forest path. It’s dark, and you hear strange noises...")
    
    # Second Decision: Forest Encounter
    choice2 = input("A wild monkey blocks your way! Do you 'feed' it a banana or 'ignore' it? ").lower()
    
    if choice2 == "feed":
        print("\nThe monkey becomes your friend and guides you to a riverbank.")
        print("You find an old boat tied to a tree.\n")
        
        # Third Decision: River Crossing
        choice3 = input("Do you 'use boat' to cross or 'walk' along the river? ").lower()
        
        if choice3 == "use boat":
            print("\nYou paddle carefully across the river...")
            print("Halfway through, a crocodile bumps the boat! You stay calm and make it across safely.\n")
            
            # Fourth Decision: The Ancient Temple
            choice4 = input("You find a temple with three entrances — 'gold', 'stone', and 'wood'. Which do you choose? ").lower()
            
            if choice4 == "stone":
                print("\nThe stone door opens to a glowing chamber filled with treasure!")
                print("Congratulations, adventurer! You found the lost treasure of Eldorado!")
            elif choice4 == "gold":
                print("\nThe gold door seals behind you — it was a trap! You’re locked in forever. Game Over.")
            elif choice4 == "wood":
                print("\nThe wooden door collapses, releasing snakes from inside. Game Over.")
            else:
                print("\nThat door doesn’t exist... and neither do you anymore. Game Over.")
        
        elif choice3 == "walk":
            print("\nYou walk for hours and run out of water. The sun scorches the land. Game Over.")
        else:
            print("\nYou hesitate too long... and night falls. Strange eyes watch you from the forest. Game Over.")
    
    elif choice2 == "ignore":
        print("\nYou walk past the monkey — it gets angry and throws coconuts at you! You’re knocked out cold. Game Over.")
    else:
        print("\nYou do nothing. The jungle takes you. Game Over.")

elif choice1 == "right":
    print("\nYou take the mountain path. The climb is steep, and rocks crumble beneath your feet.")
    choice5 = input("You find a cave halfway up. Do you 'enter' or 'keep climbing'? ").lower()
    
    if choice5 == "enter":
        print("\n💎 Inside the cave, you find ancient carvings and a glowing chest!")
        print("But as you approach, the floor collapses beneath you... Game Over.")
    elif choice5 == "keep climbing":
        print("\n🦅 You reach the peak and find a majestic view of the island — but no treasure.")
        print("At least you lived to tell the tale!")
    else:
        print("\nYou lose your footing and fall down the cliff. Game Over.")

else:
    print("\nYou wander aimlessly and get lost in the mist. Game Over.")

print("\nThanks for playing Treasure Island! Come back to try a new path.")

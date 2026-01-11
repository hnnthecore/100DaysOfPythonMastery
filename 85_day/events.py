import random
from world import DANGERS


def world_event(world):
    """
    Random events that affect the world.
    """
    if random.random() < 0.4:
        event = random.choice(DANGERS)

        if event == "Storm":
            world.resources["Food"] -= 15
            return "⛈ A massive storm destroyed crops."

        if event == "Wild Beasts":
            world.danger_level += 2
            return "🐺 Wild beasts are roaming the land."

        if event == "Drought":
            world.resources["Water"] -= 20
            return "🌵 A severe drought hit the world."

        if event == "Earthquake":
            world.resources["Gold"] -= 10
            return "🌍 An earthquake shook the mountains."

    return None

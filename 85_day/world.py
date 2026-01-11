import random

BIOMES = ["Forest", "Desert", "Ocean", "Mountains"]
RESOURCES = ["Food", "Water", "Gold", "Wood"]
DANGERS = ["Storm", "Wild Beasts", "Drought", "Earthquake"]


class World:
    def __init__(self):
        # Core world state
        self.biome = random.choice(BIOMES)
        self.resources = {r: random.randint(20, 100) for r in RESOURCES}
        self.danger_level = random.randint(1, 10)
        self.age = 0

    def describe(self):
        return {
            "Biome": self.biome,
            "Resources": self.resources,
            "Danger Level": self.danger_level,
            "World Age": self.age
        }

    def age_world(self):
        """
        Each year changes the world slightly.
        """
        self.age += 1

        # Resources naturally fluctuate
        for r in self.resources:
            self.resources[r] += random.randint(-10, 10)
            self.resources[r] = max(self.resources[r], 0)

        # Danger slowly increases with age
        if random.random() < 0.3:
            self.danger_level += 1

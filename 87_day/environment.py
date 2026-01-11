import random

class Environment:
    def __init__(self):
        self.food = random.randint(80, 120)
        self.water = random.randint(80, 120)
        self.danger = random.randint(1, 5)

    def tick(self):
        # World slowly degrades
        self.food -= random.randint(3, 8)
        self.water -= random.randint(3, 8)

        if random.random() < 0.4:
            self.danger += 1

        self.food = max(self.food, 0)
        self.water = max(self.water, 0)

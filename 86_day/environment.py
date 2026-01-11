import random

class Environment:
    def __init__(self):
        self.food = random.randint(30, 60)
        self.water = random.randint(30, 60)
        self.danger = random.randint(1, 5)

    def tick(self):
        """
        Environment naturally degrades over time.
        """
        self.food -= random.randint(1, 4)
        self.water -= random.randint(1, 4)

        if random.random() < 0.3:
            self.danger += 1

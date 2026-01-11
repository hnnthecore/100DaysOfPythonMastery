import random

class Agent:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 50
        self.energy = 50
        self.alive = True

    def decide(self, env):
        # Priority-based survival logic
        if self.hunger < 30 and env.food > 0:
            return "eat"
        if self.energy < 25:
            return "rest"
        if env.danger > 8:
            return "hide"
        return "explore"

    def act(self, action, env):
        if not self.alive:
            return

        if action == "eat" and env.food > 0:
            env.food -= 10
            self.hunger += 20

        elif action == "rest":
            self.energy += 15

        elif action == "hide":
            self.energy -= 5

        elif action == "explore":
            self.energy -= 10
            self.hunger -= 5
            if random.random() < 0.4:
                env.food += 5

        # Natural decay
        self.hunger -= 2
        self.energy -= 1

        # Death check
        if self.hunger <= 0 or self.energy <= 0:
            self.alive = False

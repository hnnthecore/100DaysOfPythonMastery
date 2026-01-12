import random

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role  # producer or consumer
        self.money = 50
        self.hunger = 50
        self.alive = True

    def act(self, economy, demand):
        if not self.alive:
            return

        if self.role == "producer":
            economy.produce("food", 5)
            self.money += 10

        elif self.role == "consumer":
            if economy.supply["food"] > 0 and self.money >= economy.prices["food"]:
                economy.consume("food", 5)
                self.money -= economy.prices["food"]
                self.hunger += 15
                demand["food"] += 5
            else:
                self.hunger -= 10

        # Death condition
        if self.hunger <= 0:
            self.alive = False

class Agent:
    def __init__(self):
        self.health = 100
        self.hunger = 50
        self.energy = 50

    def decide(self, env):
        """
        Decision logic (heuristics):
        Priority-based survival decisions.
        """
        if self.hunger < 30 and env.food > 0:
            return "eat"
        if self.energy < 30:
            return "rest"
        if env.danger > 7:
            return "hide"
        return "explore"

    def act(self, action, env):
        """
        Applies the chosen action.
        """
        if action == "eat" and env.food > 0:
            env.food -= 10
            self.hunger += 20

        elif action == "rest":
            self.energy += 20

        elif action == "hide":
            self.energy -= 5

        elif action == "explore":
            self.energy -= 10
            self.hunger -= 5
            env.food += 5

        # Natural decay
        self.hunger -= 2
        self.energy -= 1

    def is_alive(self):
        return self.hunger > 0 and self.energy > 0 and self.health > 0

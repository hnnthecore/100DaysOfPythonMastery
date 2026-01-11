from data import ACTIONS, random_event

class Life:
    def __init__(self):
        self.stats = {
            "health": 100,
            "money": 50,
            "happiness": 50,
            "energy": 50
        }

    def apply_action(self, action):
        effects = ACTIONS.get(action, {})

        for key, value in effects.items():
            if key == "risk":
                continue
            self.stats[key] += value

        # Random event chance
        if action in ["work", "invest"]:
            event = random_event()
            for k, v in event.items():
                if k != "text":
                    self.stats[k] += v
            return event.get("text")

    def is_game_over(self):
        return (
            self.stats["health"] <= 0 or
            self.stats["happiness"] <= 0 or
            self.stats["energy"] <= 0
        )

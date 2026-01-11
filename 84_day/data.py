import random

ACTIONS = {
    "work": {"money": +20, "energy": -15, "happiness": -5},
    "rest": {"energy": +20, "happiness": +5},
    "study": {"energy": -10, "happiness": -5, "money": -5},
    "party": {"energy": -20, "happiness": +20, "money": -10},
    "invest": {"money": +30, "risk": True}
}

EVENTS = [
    {"text": "You got sick.", "health": -20},
    {"text": "You got a bonus!", "money": +25},
    {"text": "You feel burned out.", "happiness": -15},
    {"text": "Nothing unusual happened.",}
]


def random_event():
    return random.choice(EVENTS)

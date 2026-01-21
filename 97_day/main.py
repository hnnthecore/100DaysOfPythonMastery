"""
Smart Decision Advisor
----------------------
A lightweight, rule-based decision engine that recommends
the best option based on user inputs and weighted logic.

This demonstrates:
- conditional logic
- scoring systems
- clean function design
- explainable decisions (why an option was chosen)
"""

def ask_int(prompt, min_val=1, max_val=5):
    """Safely ask for an integer within a range."""
    while True:
        try:
            value = int(input(f"{prompt} ({min_val}-{max_val}): "))
            if min_val <= value <= max_val:
                return value
            print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")


def collect_inputs():
    """Collects user preferences."""
    print("\n🧠 Answer a few questions to get a recommendation.\n")

    return {
        "logic_interest": ask_int("How much do you enjoy problem-solving?"),
        "creativity": ask_int("How important is creativity to you?"),
        "time_commitment": ask_int("How much time can you commit daily?"),
        "career_focus": ask_int("How career-focused is this decision?")
    }


def score_options(inputs):
    """
    Scores each option using weighted rules.
    Options can easily be changed or extended.
    """
    scores = {
        "Build a Data Project": 0,
        "Create a GUI Application": 0,
        "Learn Backend Concepts": 0
    }

    # Rule-based scoring
    scores["Build a Data Project"] += inputs["logic_interest"] * 2
    scores["Build a Data Project"] += inputs["career_focus"] * 2

    scores["Create a GUI Application"] += inputs["creativity"] * 2
    scores["Create a GUI Application"] += inputs["time_commitment"]

    scores["Learn Backend Concepts"] += inputs["career_focus"] * 3
    scores["Learn Backend Concepts"] += inputs["logic_interest"]

    return scores


def explain_choice(best_option, scores):
    """Explains why the option was selected."""
    print("\n📊 Decision Breakdown")
    print("-" * 30)
    for option, score in scores.items():
        print(f"{option}: {score} points")

    print("\n✅ Recommended Path:")
    print(best_option)
    print("\n💡 Reason:")
    print(
        "This option best aligns with your priorities based on the "
        "weighted evaluation of your responses."
    )


def main():
    print("🤖 SMART DECISION ADVISOR")
    print("=" * 35)

    inputs = collect_inputs()
    scores = score_options(inputs)

    best_option = max(scores, key=scores.get)
    explain_choice(best_option, scores)


if __name__ == "__main__":
    main()

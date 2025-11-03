# Day 19 - NumbrIQ: Math Solver & Step Explainer
# A smart math assistant that explains calculations step-by-step.

import sympy as sp
import json
import datetime
import os

HISTORY_FILE = "numbrIQ_history.json"

# --------------------------------------------------
# Utility: Manage history
# --------------------------------------------------
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)

# --------------------------------------------------
# Core solver
# --------------------------------------------------
def explain_expression(expr):
    """Solve and explain the math expression step-by-step."""
    steps = []
    try:
        expression = sp.sympify(expr)
    except Exception:
        return ["❌ Invalid expression. Please check your input."]

    # Simplify step-by-step
    steps.append(f"Input Expression: {expr}")
    simplified = sp.simplify(expression)
    if simplified != expression:
        steps.append(f"Simplified: {simplified}")

    # Evaluate numeric results if applicable
    if simplified.is_Number:
        steps.append(f"Final Answer: {simplified}")
    else:
        try:
            evaluated = simplified.evalf()
            if evaluated != simplified:
                steps.append(f"Evaluated Numerically: {evaluated}")
        except Exception:
            pass

    # Try solving equations
    if isinstance(simplified, sp.Equality):
        x = list(simplified.free_symbols)
        if x:
            var = x[0]
            sol = sp.solve(simplified, var)
            steps.append(f"Solving for {var}: {sol}")
        else:
            steps.append("No variables to solve for.")

    # Derivatives and integrals if user included them
    if "diff(" in expr:
        steps.append("Detected derivative expression → using differentiation.")
        diff_expr = sp.diff(expression)
        steps.append(f"Result: {diff_expr}")

    if "integrate(" in expr:
        steps.append("Detected integral expression → using integration.")
        int_expr = sp.integrate(expression)
        steps.append(f"Result: {int_expr}")

    # Add timestamp
    steps.append(f"[Solved on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    return steps


# --------------------------------------------------
# CLI interface
# --------------------------------------------------
def main():
    print("=" * 60)
    print(" NUMBRIQ – MATH SOLVER & STEP EXPLAINER ".center(60))
    print("=" * 60)
    print("Type an expression (e.g. 2*x + 3*x - 5 or diff(x**2, x))")
    print("Type 'exit' to quit.\n")

    history = load_history()

    while True:
        expr = input("Enter expression: ").strip()
        if expr.lower() in ["exit", "quit"]:
            print("👋 Exiting NumbrIQ. Goodbye!")
            break
        if not expr:
            continue

        steps = explain_expression(expr)
        print("\n".join(steps))
        print("-" * 60)

        history.append({"expression": expr, "steps": steps})
        save_history(history)


if __name__ == "__main__":
    main()

"""
AI Personal Knowledge Engine
----------------------------
A lightweight AI-style system that stores knowledge,
processes questions, and returns the most relevant
answer with reasoning.

This demonstrates:
- text preprocessing
- semantic scoring
- memory-based reasoning
- explainable AI output
"""

import os
import re
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KB_FILE = os.path.join(BASE_DIR, "knowledge_base.txt")


def preprocess(text):
    """
    Normalize text and extract keywords.
    """
    text = text.lower()
    return re.findall(r"\b[a-z]{3,}\b", text)


def load_knowledge():
    """
    Load and structure the knowledge base.
    """
    knowledge = []
    current_category = None

    with open(KB_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("category:"):
                current_category = line.split("category:")[1]
            elif line and current_category:
                knowledge.append({
                    "category": current_category,
                    "text": line,
                    "tokens": preprocess(line)
                })
    return knowledge


def score_knowledge(question_tokens, knowledge):
    """
    Score each knowledge entry based on keyword overlap.
    """
    scores = []

    q_counts = Counter(question_tokens)

    for entry in knowledge:
        e_counts = Counter(entry["tokens"])
        overlap = set(q_counts) & set(e_counts)

        score = sum(q_counts[w] * e_counts[w] for w in overlap)

        scores.append({
            "entry": entry,
            "score": score,
            "matched_terms": overlap
        })

    return sorted(scores, key=lambda x: x["score"], reverse=True)


def answer_question(question, knowledge):
    question_tokens = preprocess(question)
    scored = score_knowledge(question_tokens, knowledge)

    best = scored[0]

    return best


def main():
    if not os.path.exists(KB_FILE):
        print("Knowledge base not found.")
        return

    knowledge = load_knowledge()

    print("AI Personal Knowledge Engine")
    print("=" * 40)

    question = input("\nAsk a question:\n> ")

    result = answer_question(question, knowledge)

    if result["score"] == 0:
        print("\nNo relevant knowledge found.")
        return

    entry = result["entry"]

    print("\nAnswer")
    print("-" * 40)
    print(entry["text"])

    print("\nReasoning")
    print("-" * 40)
    print("Matched terms:", ", ".join(sorted(result["matched_terms"])))
    print("Category:", entry["category"])
    print("Confidence score:", result["score"])


if __name__ == "__main__":
    main()

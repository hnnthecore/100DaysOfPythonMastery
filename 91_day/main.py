import os
from collections import Counter
import re

def analyze_text(text):
    words = re.findall(r"\b\w+\b", text.lower())
    sentences = re.split(r"[.!?]", text)

    word_count = len(words)
    sentence_count = len([s for s in sentences if s.strip()])
    common_words = Counter(words).most_common(5)

    avg_words_per_sentence = (
        word_count / sentence_count if sentence_count else 0
    )

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_words_per_sentence": round(avg_words_per_sentence, 2),
        "common_words": common_words
    }

def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(BASE_DIR, "sample.txt")

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    report = analyze_text(text)

    print("📊 Smart Text Analysis Report")
    print("-" * 40)
    print(f"Words: {report['word_count']}")
    print(f"Sentences: {report['sentence_count']}")
    print(f"Avg Words/Sentence: {report['avg_words_per_sentence']}")

    print("\nMost Common Words:")
    for word, count in report["common_words"]:
        print(f"- {word}: {count}")

if __name__ == "__main__":
    main()

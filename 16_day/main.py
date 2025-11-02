# Day 16 - Text Summarizer
# Project: Extractive text summarizer with sentence ranking and logging.

import re
import math
import json
import time
from collections import Counter

LOG_FILE = "summarizer_log.json"

STOPWORDS = set("""
a an the and or but if while of at by for with about against between into through during
before after above below to from up down in out on off over under again further then once
here there when where why how all any both each few more most other some such no nor not
only own same so than too very s t can will just don should now is am are was were be been
being have has had having do does did doing would could should might must i me my myself we
our ours ourselves you your yours yourself yourselves he him his himself she her hers herself
it its itself they them their theirs themselves what which who whom this that these those
""".split())

def load_text_from_file(path: str) -> str:
    """Read and return text content from a file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def split_into_sentences(text: str):
    """Split text into sentences by punctuation marks."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]

def tokenize(text: str):
    """Split text into lowercase words, removing punctuation."""
    return re.findall(r'\b[a-zA-Z]+\b', text.lower())

def compute_word_frequencies(words):
    """Return normalized frequency of non-stopwords."""
    freq = Counter(w for w in words if w not in STOPWORDS)
    if not freq:
        return {}
    max_freq = max(freq.values())
    for w in freq:
        freq[w] /= max_freq
    return freq

def score_sentences(sentences, word_freq):
    """Score each sentence based on word frequencies."""
    scores = {}
    for sent in sentences:
        words = tokenize(sent)
        if not words:
            continue
        sentence_score = sum(word_freq.get(w, 0) for w in words)
        scores[sent] = sentence_score / len(words)
    return scores

def generate_summary(sentences, scores, n_sentences=3):
    """Return top N sentences as a summary."""
    top_sentences = sorted(scores, key=scores.get, reverse=True)[:n_sentences]
    summary = " ".join([s for s in sentences if s in top_sentences])
    return summary.strip()

def log_summary(summary, source="manual"):
    """Log generated summaries with timestamp."""
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": source,
        "summary_preview": summary[:120] + ("..." if len(summary) > 120 else "")
    }
    try:
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = json.load(f)
        except FileNotFoundError:
            logs = []
        logs.append(entry)
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4)
    except Exception as e:
        print(f"Warning: could not write log file ({e}).")

def main():
    print("=" * 60)
    print(" TEXT SUMMARIZER ".center(60, "="))
    print("=" * 60)

    choice = input("Load text from file (f) or paste manually (m)? ").strip().lower()
    if choice == "f":
        path = input("Enter path to .txt file: ").strip()
        try:
            text = load_text_from_file(path)
            source = path
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Paste your text below. End input with an empty line:")
        lines = []
        while True:
            line = input()
            if not line.strip():
                break
            lines.append(line)
        text = "\n".join(lines)
        source = "manual"

    sentences = split_into_sentences(text)
    if len(sentences) < 2:
        print("Not enough text to summarize.")
        return

    words = tokenize(text)
    word_freq = compute_word_frequencies(words)
    scores = score_sentences(sentences, word_freq)

    try:
        n = int(input("How many sentences should the summary contain (default 3)? ") or 3)
    except ValueError:
        n = 3

    summary = generate_summary(sentences, scores, n)
    print("\n" + "=" * 60)
    print(" SUMMARY ".center(60, "="))
    print("=" * 60)
    print(summary)
    print("=" * 60)

    # Save summary file
    filename = f"summary_{int(time.time())}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"\nSummary saved as {filename}")

    log_summary(summary, source)
    print("Log updated successfully.\n")

if __name__ == "__main__":
    main()

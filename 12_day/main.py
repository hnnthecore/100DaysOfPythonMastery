# Day 12 - Mood Visualizer 2.0
# Project: Emotion Dashboard – analyze, visualize, and track your mood history.

import json
import os
import random
import time

DATA_FILE = "mood_data.json"

# Mood database with (energy, positivity) values
MOODS = {
    "happy": (85, 90),
    "sad": (25, 25),
    "angry": (70, 20),
    "calm": (40, 80),
    "anxious": (65, 35),
    "excited": (90, 85),
    "tired": (35, 45),
    "bored": (30, 40),
    "love": (80, 95),
    "confused": (50, 50),
    "focused": (75, 70),
    "lonely": (20, 30),
    "grateful": (78, 90),
    "stressed": (68, 35)
}


def slow_print(text, delay=0.03):
    """Print text with a typewriter-like animation."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()


def load_data():
    """Load previous mood data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_data(data):
    """Save all mood data entries."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def detect_mood(user_input):
    """Detect mood keywords in user text."""
    text = user_input.lower()
    detected = [m for m in MOODS if m in text]
    if detected:
        return random.choice(detected)
    return random.choice(list(MOODS.keys()))


def display_bar(label, value, width=40):
    """Draw a horizontal bar chart line."""
    filled = int(value / 100 * width)
    bar = "█" * filled + "░" * (width - filled)
    print(f"{label:<12}: {bar} {value:>3}%")


def show_summary(data):
    """Show mood trend summary."""
    if not data:
        print("\nNo previous mood data found.\n")
        return

    print("\n📊 Mood History Overview\n" + "-" * 45)
    moods = [entry["mood"] for entry in data]
    common = max(set(moods), key=moods.count)
    avg_energy = sum(e["energy"] for e in data) / len(data)
    avg_pos = sum(e["positivity"] for e in data) / len(data)

    print(f"Most frequent mood : {common.capitalize()}")
    print(f"Average Energy     : {avg_energy:.1f}%")
    print(f"Average Positivity : {avg_pos:.1f}%")

    print("\nRecent Entries:")
    for entry in data[-5:]:
        print(f"{entry['date']} → {entry['mood'].capitalize()} "
              f"(E:{entry['energy']}  P:{entry['positivity']})")
    print()


def mood_summary_chart(data):
    """Display a visual chart of recent moods."""
    if not data:
        return
    print("Recent Mood Trend:\n")
    for entry in data[-5:]:
        mood = entry["mood"].capitalize()
        val = (entry["energy"] + entry["positivity"]) // 2
        filled = int(val / 100 * 30)
        print(f"{mood:<12}: {'█' * filled} {val}%")
    print()


def main():
    print("=" * 50)
    print("🌈  MOOD VISUALIZER 2.0 – THE EMOTION DASHBOARD  🌈")
    print("=" * 50)

    # Load existing mood data
    mood_data = load_data()
    if mood_data:
        show_summary(mood_data)
        mood_summary_chart(mood_data)

    # Ask user for today’s mood
    user_input = input("Describe your current mood or how your day was:\n> ").strip()
    slow_print("\nAnalyzing emotional tone...\n")
    time.sleep(1)

    # Detect mood and calculate values
    detected_mood = detect_mood(user_input)
    energy, positivity = MOODS[detected_mood]
    energy += random.randint(-5, 5)
    positivity += random.randint(-5, 5)
    energy, positivity = max(0, min(energy, 100)), max(0, min(positivity, 100))

    # Display results
    print(f"Detected Mood : {detected_mood.upper()}")
    display_bar("Energy", energy)
    display_bar("Positivity", positivity)
    slow_print("\nVisualizing emotional spectrum...\n", 0.02)
    time.sleep(1)

    # Log new entry
    mood_data.append({
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "mood": detected_mood,
        "energy": energy,
        "positivity": positivity
    })
    save_data(mood_data)

    # Show updated summary
    show_summary(mood_data)
    mood_summary_chart(mood_data)
    slow_print("✨ Mood entry saved successfully!\n")


if __name__ == "__main__":
    main()

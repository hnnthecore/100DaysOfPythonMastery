import csv
import os
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.csv")


def load_data(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def detect_column_types(rows):
    """
    Detect numeric vs text columns based on first row.
    """
    types = {}
    for key, value in rows[0].items():
        try:
            float(value)
            types[key] = "numeric"
        except ValueError:
            types[key] = "text"
    return types


def analyze_numeric(column, values):
    numbers = [float(v) for v in values]
    return {
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "avg": round(sum(numbers) / len(numbers), 2)
    }


def analyze_text(values):
    counts = Counter(values)
    top = counts.most_common(3)
    return top


def main():
    if not os.path.exists(DATA_FILE):
        print("❌ data.csv not found")
        return

    rows = load_data(DATA_FILE)
    if not rows:
        print("❌ No data available")
        return

    column_types = detect_column_types(rows)

    print("📊 DATA → INSIGHT REPORT")
    print("=" * 35)

    for column, col_type in column_types.items():
        values = [row[column] for row in rows]

        print(f"\n🔹 Column: {column} ({col_type})")

        if col_type == "numeric":
            stats = analyze_numeric(column, values)
            for k, v in stats.items():
                print(f"{k.capitalize()}: {v}")
        else:
            top = analyze_text(values)
            print("Top values:")
            for val, count in top:
                print(f"- {val}: {count}")

    print("\n✅ Analysis complete")


if __name__ == "__main__":
    main()

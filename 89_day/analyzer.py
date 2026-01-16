from collections import Counter

def analyze_logs(entries):
    report = {}

    levels = [e["level"] for e in entries]
    report["level_counts"] = Counter(levels)

    messages = [e["message"] for e in entries]
    report["frequent_messages"] = Counter(messages).most_common(3)

    report["anomalies"] = [
        msg for msg, count in Counter(messages).items() if count >= 3
    ]

    return report

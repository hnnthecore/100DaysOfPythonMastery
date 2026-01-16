from parser import parse_log_line
from analyzer import analyze_logs
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "sample.log")

log_entries = []

with open(LOG_FILE) as f:
    for line in f:
        log_entries.append(parse_log_line(line))

report = analyze_logs(log_entries)

print("📊 Log Analysis Report")
print("-" * 40)

print("Log Levels:")
for level, count in report["level_counts"].items():
    print(f"{level}: {count}")

print("\nFrequent Messages:")
for msg, count in report["frequent_messages"]:
    print(f"{msg} → {count} times")

print("\n⚠️ Anomalies Detected:")
for anomaly in report["anomalies"]:
    print("-", anomaly)

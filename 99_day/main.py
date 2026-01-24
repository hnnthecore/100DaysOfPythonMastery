"""
Event Processing Pipeline
-------------------------
A lightweight system that simulates how backend services
process, validate, route, and log events.

This demonstrates:
- event-driven architecture
- pipeline stages
- system-level thinking
- clean separation of concerns
"""

import time
import random
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "events.log")


# -----------------------------
# EVENT GENERATION
# -----------------------------
def generate_event():
    event_types = ["USER_LOGIN", "FILE_UPLOAD", "DATA_REQUEST", "ERROR"]
    return {
        "id": random.randint(1000, 9999),
        "type": random.choice(event_types),
        "timestamp": datetime.now().isoformat()
    }


# -----------------------------
# VALIDATION STAGE
# -----------------------------
def validate_event(event):
    required_keys = {"id", "type", "timestamp"}
    return required_keys.issubset(event.keys())


# -----------------------------
# ROUTING STAGE
# -----------------------------
def route_event(event):
    if event["type"] == "ERROR":
        return handle_error
    elif event["type"] == "USER_LOGIN":
        return handle_login
    elif event["type"] == "FILE_UPLOAD":
        return handle_upload
    else:
        return handle_generic


# -----------------------------
# HANDLERS
# -----------------------------
def handle_login(event):
    return f"Login processed for event {event['id']}"


def handle_upload(event):
    return f"File upload stored for event {event['id']}"


def handle_error(event):
    return f"Error escalated for event {event['id']}"


def handle_generic(event):
    return f"Generic event handled for event {event['id']}"


# -----------------------------
# LOGGING
# -----------------------------
def log_event(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")


# -----------------------------
# PIPELINE EXECUTION
# -----------------------------
def process_event(event):
    if not validate_event(event):
        log_event("Invalid event discarded")
        return "Invalid event"

    handler = route_event(event)
    result = handler(event)
    log_event(result)
    return result


def main():
    print("Event Processing Pipeline")
    print("=" * 40)

    processed = 0

    for _ in range(5):
        event = generate_event()
        result = process_event(event)
        print(result)
        processed += 1
        time.sleep(0.5)

    print("\nSystem Summary")
    print("-" * 40)
    print(f"Events processed: {processed}")
    print(f"Log file: {LOG_FILE}")


if __name__ == "__main__":
    main()

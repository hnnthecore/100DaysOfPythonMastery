from datetime import datetime

def parse_log_line(line):
    """
    Converts a raw log line into structured data.
    """
    parts = line.strip().split(" ", 3)
    timestamp = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S")
    level = parts[2]
    message = parts[3]

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }

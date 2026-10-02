import csv
from collections import defaultdict, deque
from datetime import datetime, timedelta
from pathlib import Path

project = Path(__file__).resolve().parent.parent
log_file = project / "sample-logs" / "synthetic-login-events.csv"

with log_file.open(newline="") as file:
    events = list(csv.DictReader(file))

for event in events:
    event["time"] = datetime.fromisoformat(event["timestamp"])

events.sort(key=lambda event: event["time"])

failures = defaultdict(deque)
window = timedelta(minutes=5)
threshold = 5
alert_count = 0

for event in events:
    key = (event["username"], event["source_ip"], event["host"])
    recent_failures = failures[key]
    cutoff = event["time"] - window

    while recent_failures and recent_failures[0] < cutoff:
        recent_failures.popleft()

    if event["result"] == "failure":
        recent_failures.append(event["time"])

    elif event["result"] == "success":
        if len(recent_failures) >= threshold:
            alert_count += 1
            print(
                f"ALERT: {event['username']} | "
                f"IP: {event['source_ip']} | "
                f"Host: {event['host']} | "
                f"{len(recent_failures)} failures within 5 minutes "
                f"before success at {event['timestamp']}"
            )

        recent_failures.clear()

print(f"\nTotal alerts: {alert_count}")

import csv
from pathlib import Path

project = Path(__file__).resolve().parent.parent
log_file = project / "sample-logs" / "synthetic-group-changes.csv"

alert_count = 0

with log_file.open(newline="") as file:
    for event in csv.DictReader(file):
        group = event["group"].strip().casefold()
        action = event["action"].strip().casefold()

        if group == "administrators" and action == "member_added":
            alert_count += 1
            print(
                f"ALERT: Administrative group addition | "
                f"Time: {event['timestamp']} | "
                f"Host: {event['host']} | "
                f"Actor: {event['actor']} | "
                f"Added user: {event['target_user']}"
            )

print(f"\nTotal alerts: {alert_count}")

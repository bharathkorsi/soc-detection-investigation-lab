import csv
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

project = Path(__file__).resolve().parent.parent
script = project / "detections" / "detect_admin_group_changes.py"

if not script.is_file():
    sys.exit(f"Missing detection script: {script}")

fields = ["timestamp", "host", "actor", "target_user", "group", "action"]

def event(group, action):
    return [
        "2026-10-04T10:00:00Z", "LAB-PC", "lab-admin",
        "support-user", group, action
    ]

cases = [
    ("Administrators addition",
     [event("Administrators", "member_added")], 1),
    ("Ordinary Users addition",
     [event("Users", "member_added")], 0),
    ("Administrators removal",
     [event("Administrators", "member_removed")], 0),
    ("Uppercase names",
     [event("ADMINISTRATORS", "MEMBER_ADDED")], 1),
    ("Surrounding spaces",
     [event(" Administrators ", " member_added ")], 1),
    ("Mixed group changes",
     [event("Administrators", "member_added"),
      event("Users", "member_added"),
      event("Administrators", "member_removed")], 1),
    ("Empty dataset", [], 0),
]

results = []
failed = 0

for name, rows, expected in cases:
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "detections").mkdir()
        (root / "sample-logs").mkdir()

        copied_script = root / "detections" / script.name
        shutil.copy2(script, copied_script)

        data = root / "sample-logs" / "synthetic-group-changes.csv"
        with data.open("w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(rows)

        run = subprocess.run(
            [sys.executable, str(copied_script)],
            capture_output=True, text=True, check=True
        )

        actual = sum(
            line.startswith("ALERT:")
            for line in run.stdout.splitlines()
        )
        passed = (
            actual == expected
            and f"Total alerts: {expected}" in run.stdout.splitlines()
        )
        failed += not passed
        status = "PASS" if passed else "FAIL"
        result = f"{status}: {name} | expected={expected}, actual={actual}"
        results.append(result)
        print(result)

output = project / "reports" / "admin-group-validation.txt"
output.write_text("\n".join(results) + "\n", encoding="utf-8")

print(f"\nSaved results to reports/{output.name}")
sys.exit(1 if failed else 0)

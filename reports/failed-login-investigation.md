# Investigation: Failed Logins Followed by Success

## Scope
This investigation uses eight fictional login events.
It demonstrates alert analysis using synthetic data.

## Alert Summary
- Username: lab-user
- Source IP: 192.0.2.10
- Host: LAB-PC
- Failed logins: 5
- Successful login: 2026-10-02T10:02:30Z
- Detection threshold: at least 5 failures within the previous 5 minutes

## Timeline
All timestamps are UTC on 2026-10-02.

| Time | User | Result |
|---|---|---|
| 10:00:00 | lab-user | Failure |
| 10:00:30 | lab-user | Failure |
| 10:01:00 | lab-user | Failure |
| 10:01:30 | lab-user | Failure |
| 10:02:00 | lab-user | Failure |
| 10:02:30 | lab-user | Success |

All six events share the same source IP and host.

## Analysis
The successful login followed five failed attempts within
two minutes and thirty seconds, meeting the detection rule.

Possible explanations include a legitimate user correcting
a password or someone guessing a password successfully.

The dataset contains no evidence of activity after login,
device ownership, or user confirmation.

The normal-user account had one failure followed by success.
It did not meet the five-failure threshold.

## Verdict
The alert correctly matches the configured rule.

Whether the activity is malicious remains undetermined.
A rule match alone does not prove account compromise.

## Follow-up for a Real Investigation
- Confirm whether the user recognizes the login.
- Check whether the source IP and device are expected.
- Review authentication and MFA details.
- Review processes, network activity, and account changes after login.
- Apply containment if additional evidence supports compromise.

These follow-up steps were not performed in this synthetic lab.

## Evidence
- [Sample dataset](../sample-logs/synthetic-login-events.csv)
- [Detection rule](../detections/failed-login-rule.md)
- [Detection output](failed-login-output.txt)
- [Validation results](failed-login-validation.txt)

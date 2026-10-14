# Administrators Group Addition Detection

## Purpose
Flag additions to the Administrators group for review.

## Data Source
Fictional CSV events in:
`sample-logs/synthetic-group-changes.csv`

These are synthetic records, not collected Windows event logs.

## Detection Logic
Generate one alert per event when:
- `group` equals `Administrators`
- `action` equals `member_added`

Matching ignores capitalization and surrounding spaces.

Each alert includes the timestamp, host, actor, and added user.

## Sample Result
The three-event sample produces one alert:
- Actor: lab-admin
- Added user: support-user
- Host: LAB-PC

The Users group addition and Administrators removal do not trigger alerts.

## Validation
Seven automated checks passed:

| Scenario | Expected alerts | Observed alerts |
| --- | --- | --- |
| Administrators addition | 1 | 1 |
| Ordinary Users addition | 0 | 0 |
| Administrators removal | 0 | 0 |
| Uppercase names | 1 | 1 |
| Surrounding spaces | 1 | 1 |
| Mixed group changes | 1 | 1 |
| Empty dataset | 0 | 0 |

Run the checks from the project folder:
`python3 tests/validate_admin_group_changes.py`

## Investigation Questions
- Was the membership change approved?
- Was the actor authorized to make it?
- Does the added user need administrative access?
- What activity followed the change?

## Limitations
- An alert does not establish malicious activity.
- Approved administrative changes also trigger alerts.
- Only the English group name Administrators is matched.
- Missing fields and malformed records are not handled.
- Duplicate events can produce duplicate alerts.
- Real Windows log ingestion and SIEM integration are not implemented.

## Evidence
- [Detection script](detect_admin_group_changes.py)
- [Synthetic dataset](../sample-logs/synthetic-group-changes.csv)
- [Detection output](../reports/admin-group-output.txt)
- [Validation script](../tests/validate_admin_group_changes.py)
- [Validation results](../reports/admin-group-validation.txt)

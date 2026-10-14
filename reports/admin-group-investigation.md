# Investigation: Synthetic Administrators Group Addition

## Scope
This exercise uses three fictional group-change events.
No real account or system was modified.

## Alert Summary
- Timestamp: 2026-10-04T10:00:00Z
- Host: LAB-PC
- Actor: lab-admin
- Added user: support-user
- Group: Administrators
- Action: member_added

## Event Timeline

| Time (UTC) | Actor | Target user | Group | Action |
| --- | --- | --- | --- | --- |
| 10:00 | lab-admin | support-user | Administrators | Added |
| 10:05 | lab-admin | normal-user | Users | Added |
| 10:10 | lab-admin | support-user | Administrators | Removed |

## Findings
The detection correctly flagged the Administrators addition.

The Users addition and Administrators removal did not match
this rule. The removal remains relevant investigation context.

The sample records show support-user being added to
Administrators and removed ten minutes later. They do not
establish why the changes occurred or what access was used.

## Possible Explanations
- Approved temporary administrative access.
- An administrator correcting an accidental change.
- Unauthorized elevation of access.

The available evidence cannot distinguish these explanations.

## Assessment
Detection result: Expected rule match.
Malicious activity: Undetermined.
Business authorization: Unknown.

Seven automated checks passed for matching, nonmatching,
capitalization, whitespace, mixed-event, and empty-input cases.
These checks validate rule behavior, not real-world effectiveness.

## Proposed Follow-up
For a real investigation:
1. Check the approval ticket and access policy.
2. Verify the actor's identity and authorization.
3. Review the target user's logins and process activity.
4. Confirm the membership removal in the source system.
5. Escalate if the change was unauthorized.

These follow-up actions were not performed in this exercise.

## Evidence
- [Synthetic events](../sample-logs/synthetic-group-changes.csv)
- [Detection script](../detections/detect_admin_group_changes.py)
- [Detection rule](../detections/admin-group-rule.md)
- [Detection output](admin-group-output.txt)
- [Validation script](../tests/validate_admin_group_changes.py)
- [Validation results](admin-group-validation.txt)

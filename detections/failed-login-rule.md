# Failed Logins Followed by Success

## Purpose
Flag repeated login failures followed by a successful login
for further investigation.

## Data Source
Eight synthetic CSV records created for this exercise.
These are fictional records, not collected Windows events.

## Detection Logic
- Match the same username, source IP, and host.
- Count failures during the five minutes before a success.
- Include failures exactly five minutes before the success.
- Alert when the count is five or more.
- Clear the failure history for that group after a success.

## Initial Validation
- lab-user: five failures followed by success produced one alert.
- normal-user: one failure followed by success produced no alert.
- Total alerts observed: one.

## Investigation
Review whether the login was expected, verify the source,
and examine activity after the successful login.

## Limitations
- A matching pattern does not prove compromise.
- Legitimate password mistakes may trigger the rule.
- Attempts spread across different IP addresses are not combined.
- Only two simple scenarios have been checked.
- This Python exercise does not validate SIEM or Windows collection.

## Run
python3 detections/detect_failed_logins.py

## Saved Output
reports/failed-login-output.txt

## Additional Validation Results
Seven automated checks passed:

| Test | Expected alerts | Observed alerts |
|---|---:|---:|
| Five failures followed by success | 1 | 1 |
| Four failures followed by success | 0 | 0 |
| Failures exactly five minutes old | 1 | 1 |
| Failures older than five minutes | 0 | 0 |
| Success with a different username | 0 | 0 |
| Success from a different source IP | 0 | 0 |
| Success on a different host | 0 | 0 |

These checks used temporary synthetic datasets.
The original eight-event dataset was preserved.

The tests verify threshold, time-window, and grouping behavior.
They do not establish effectiveness against real attacks.

Validation output: reports/failed-login-validation.txt

Remaining checks include out-of-order input, reset after success,
and handling invalid or missing fields.

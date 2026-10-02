# soc-detection-investigation-lab
# SOC Detection Engineering and Incident Investigation Lab

## Project Status
Planning phase — lab setup and detection testing have not started.

## Overview
This is a personal cybersecurity lab for practicing security
monitoring, threat detection, alert investigation, and incident
reporting using controlled test activity.

## Objective
Collect Windows security events in a SIEM, create three detection
rules, validate their behavior, and document one investigation.

## Planned Detection Scenarios

### 1. Repeated Failed Logins Followed by Success
Identify multiple failed login attempts followed by a successful
login involving the same account.

Investigate whether the activity reflects normal user mistakes
or potentially suspicious access.

### 2. Privileged Group Membership Change
Identify when an account is added to a privileged local group.

Investigate who made the change, which account was added, and
whether the change was expected.

### 3. Suspicious PowerShell Activity
Identify a selected suspicious PowerShell command pattern.

Use harmless lab commands to test the rule and examine the
process context before deciding whether an alert is concerning.

## Planned Tools
- Windows lab machine
- Windows Security event logs
- Sysmon for additional system activity
- One SIEM: Splunk or Microsoft Sentinel, to be selected
- Python for a small alert-summary utility
- GitHub for documentation and version history

## Planned Deliverables
- Lab setup guide
- Architecture diagram
- Three detection queries
- Detection validation results
- One incident investigation report
- A small Python alert-summary script
- Dashboard screenshots
- Short demonstration video

## Scope
All testing will use systems I own or am authorized to test.
Published evidence will contain only sanitized lab data.
Simulated activity will be clearly labeled.

## Success Criteria
- Required logs are searchable in the SIEM.
- Each rule detects its intended lab test.
- Each rule is also tested against legitimate activity.
- False positives and limitations are documented.
- Another person can understand and reproduce the setup.

## Progress
- [x] Defined the project objective
- [x] Selected three detection scenarios
- [x] Created the project repository
- [ ] Prepared the lab environment
- [ ] Configured log collection
- [ ] Built and validated detection rules
- [ ] Completed an investigation report
- [ ] Added Python automation
- [ ] Published the portfolio case study

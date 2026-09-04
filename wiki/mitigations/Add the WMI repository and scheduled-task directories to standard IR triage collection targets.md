---
id: LWM-1229
type: mitigation
name: Add the WMI repository and scheduled-task directories to standard IR triage collection targets
source_refs:
  - LWCite-1240
updated_at: 2026-08-13
status: complete
---

# Add the WMI repository and scheduled-task directories to standard IR triage collection targets

## Summary

Extend standard IR triage checklists and collection scripts to always capture the WMI repository (`%SystemRoot%\System32\wbem\Repository\`) and the scheduled-task directory (`%SystemRoot%\System32\Tasks\` plus the `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\` registry key), closing an empirically demonstrated collection gap at near-zero implementation cost.

## Addresses

- [[weaknesses/Standard IR triage packages omit WMI repository and scheduled-task collection despite both being recoverable non-volatile artifacts]]

## How To Apply

Update triage scripts (Kansa, IR-Rescue, CyLR, or an in-house equivalent) to always collect the three WMI repository files (`objects.data`, `index.btr`, mapping file) and the Tasks directory/registry hive alongside Windows Event Logs, prefetch, and registry hives already collected by default. Parse the WMI repository with a purpose-built tool (e.g., Velociraptor's `WMI.PersistenceSubscriptions` artifact or `python-evtx`) rather than treating it as an opaque binary blob, and additionally enable the `WMI-Activity/Operational` event log (EventIDs 5857, 5858, 5860, 5861) as a prospective monitoring control so future incidents leave a corroborating log trail alongside the repository itself.

## References

- [LWCite-1240] Paul, 2026, "Forensic visibility gaps in fileless malware incidents: An empirical analysis of artefact survival rates across 49 confirmed intrusions", FSI: Digital Investigation 57, 302112.

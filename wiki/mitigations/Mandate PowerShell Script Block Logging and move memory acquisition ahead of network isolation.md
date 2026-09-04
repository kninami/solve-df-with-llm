---
id: LWM-1230
type: mitigation
name: Mandate PowerShell Script Block Logging and move memory acquisition ahead of network isolation
source_refs:
  - LWCite-1240
updated_at: 2026-08-13
status: complete
---

# Mandate PowerShell Script Block Logging and move memory acquisition ahead of network isolation

## Summary

Close the two structural fileless-forensics gaps proactively: mandate GPO-enforced PowerShell Script Block Logging (EventID 4104) with a minimum 90-day retention window as a baseline control before an incident occurs, and revise first-response protocols so volatile memory is acquired before network isolation or any other action that would trigger a shutdown, rather than after.

## Addresses

- [[weaknesses/Fileless PowerShell and memory-resident execution evidence is unrecoverable without prospective logging or early volatile-memory acquisition]]

## How To Apply

Enable `HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging\EnableScriptBlockLogging` via Group Policy across all environments where PowerShell is permitted, with retention extended to at least 90-180 days to cover long-dwell intrusions. Separately, revise IR runbooks so that memory acquisition (via Volatility, Velociraptor, WinPmem, or FTK Imager, all freely available) is the first response action performed once a compromised host is identified, preceding network isolation and disk imaging wherever operationally feasible, since neither logging deployment nor memory content can be recovered after the fact once the relevant window has passed.

## References

- [LWCite-1240] Paul, 2026, "Forensic visibility gaps in fileless malware incidents: An empirical analysis of artefact survival rates across 49 confirmed intrusions", FSI: Digital Investigation 57, 302112.

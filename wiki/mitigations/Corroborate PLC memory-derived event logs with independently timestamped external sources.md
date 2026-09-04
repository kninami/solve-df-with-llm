---
id: LWM-1277
type: mitigation
name: Corroborate PLC memory-derived event logs with independently timestamped external sources
source_refs:
  - LWCite-1304
updated_at: 2026-08-14
status: complete
---

# Corroborate PLC memory-derived event logs with independently timestamped external sources

## Summary

Cross-reference the relative sequence of events recovered from a PLC's memory dump against independently timestamped external evidence sources — network traffic captures, SCADA/historian system logs, engineering-workstation event logs, or physical process sensor records — to anchor the PLC's own untimestamped event sequence to an absolute timeline.

## Addresses

- [[weaknesses/PLC memory-derived event logs lack creation timestamps, limiting timeline reconstruction]]

## How To Apply

Collect and preserve every available timestamped evidence source touching the same control-system environment as early as possible in the investigation — network traffic captures showing engineering-software-to-PLC communication, SCADA historian data logs, and the engineering workstation's own file-system and event-log timestamps for project downloads. Match the relative sequence of PLC-memory-recovered events (project downloads, mode changes) against the content and ordering of these external sources — for example, matching a recovered project-download event to the corresponding network capture showing the file transfer, whose packet timestamps then anchor that event's absolute time. Document any recovered PLC event that cannot be matched to a timestamped external source as time-unresolved, rather than assuming an approximate or estimated time for it.

## References

- [LWCite-1304] Rais, Awad, Lopez and Ahmed, 2022, "Memory forensic analysis of a programmable logic controller in industrial control systems", DFRWS 2022 EU; FSI: Digital Investigation 40, 301339.

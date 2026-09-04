---
id: LWM-1289
type: mitigation
name: Apply temporal or checkpoint-record event filtering before relying on NTFS data-run history events
source_refs:
  - LWCite-1319
updated_at: 2026-08-15
status: complete
---

# Apply temporal or checkpoint-record event filtering before relying on NTFS data-run history events

## Summary

Before relying on a generated NTFS data-run history event as evidence of a file's data location at a given time, filter out intermediate, spurious events using one of two complementary methods: grouping events by identical event time and keeping only the last event before the time changes, or using $LogFile checkpoint records (generated automatically every 5 seconds) as filtering boundaries.

## Addresses

- [[weaknesses/Simulated MFT-transaction data-run history generation can produce spurious intermediate events not representing the file's actual data location]]

## How To Apply

When using [[techniques/Reconstruct a file's complete data history from NTFS $LogFile transaction replay]], do not treat every generated data-run history event as independently meaningful. Where multiple historical events share the same event time (a signal that they arose from a single logical modification split across several `UpdateMappingPairs` records), retain only the last event before the event time changes. Where event-time grouping is ambiguous or unavailable, use $LogFile checkpoint records as an alternative filtering boundary. Cross-check any data-run location cited as evidence against the filtered result before including it in a report.

## References

- [LWCite-1319] Oh, Lee, and Hwang, 2021, "NTFS Data Tracker: Tracking file data history based on $LogFile", FSI: Digital Investigation 39, 301309.

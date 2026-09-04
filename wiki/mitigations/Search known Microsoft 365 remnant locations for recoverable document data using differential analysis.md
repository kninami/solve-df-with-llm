---
id: LWM-1146
type: mitigation
name: Search known Microsoft 365 remnant locations for recoverable document data using differential analysis
source_refs:
  - LWCite-1142
updated_at: 2026-08-12
status: complete
---

# Search known Microsoft 365 remnant locations for recoverable document data using differential analysis

## Summary

When investigating deleted or overwritten Microsoft 365 documents, extend the examination beyond unallocated-space recovery to include known cache, sync-log, and activity-tracking locations (e.g., `OfficeFileCache`, `TapCache`, `FileActivityStoreV3`, `MruServiceCache`, `BackstageInAppNavCache`), and use before/after differential snapshot comparison to surface any as-yet-undocumented remnant files for a given application version.

## Addresses

- [[weaknesses/Standard deleted-file recovery misses document data remnants left by Microsoft 365 applications]]

## How To Apply

Maintain and consult a database of documented Data Remnants Files (DRFs) for the Microsoft 365 application versions relevant to the case, checking each known location under `%UserProfile%\AppData\Local\Microsoft\Office`, `\OneDrive`, and `\Teams` for filename, path, timestamp, or content remnants of the target document. When investigating a newer application version not yet covered by the DRF database, reproduce the suspected user action (create, copy/share, download/upload, open/access, or modify) in a matched test environment, image the system before and after, and use differential analysis to isolate any newly discovered remnant files for future reference, then cross-check the recovered "potential" file list against files still existing on the target system to establish which documents were deleted.

## References

- [LWCite-1142] Joun, Lee and Park, 2023, "Data remnants analysis of document files in Windows: Microsoft 365 as a case study", FSI: Digital Investigation 46.

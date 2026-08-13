---
id: DFM-1221
type: mitigation
name: Compare backup-catalog records sharing the same file identity for mismatched creation timestamps to detect restore-based file hiding
source_refs:
  - DFCite-1233
updated_at: 2026-08-13
status: complete
---

# Compare backup-catalog records sharing the same file identity for mismatched creation timestamps to detect restore-based file hiding

## Summary

When examining File History's `Catalog.edb`, group `namespace`-table records by shared `childId`/`parentId` (path identity) and inspect any group containing more than one distinct `fileCreated` value, since this pattern indicates a restore operation replaced one file's backup history with another's at the same path.

## Addresses

- [[weaknesses/File History's restore operation lets a user hide a file behind an identically-pathed decoy without altering the visible backup history]]

## How To Apply

Parse `Catalog.edb`'s `namespace` table and group records by their `childId`/`parentId` pair, which together identify a specific file path. For any group containing records with differing `fileCreated` values, treat this as an indicator that a Previous-Versions restore operation was performed at that path and examine `Restore.log` (if still present) for the corresponding restore event's size, path, USN, and timestamp details. Extract and preserve every backed-up version associated with that path — not just the version currently visible in the live file system — since the restore may have deliberately concealed content by making an earlier, sensitive version indistinguishable from routine version history at a glance.

## References

- [DFCite-1233] Choi, Park and Lee, 2021, "Forensic exploration on windows File History", FSI: Digital Investigation 36, 301134.

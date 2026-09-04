---
id: LWM-1012
type: mitigation
name: Cross-reference File IDs and folder IDs across linked Google application databases
source_refs:
  - LWCite-1006
updated_at: 2026-08-09
status: complete
---

# Cross-reference File IDs and folder IDs across linked Google application databases

## Summary

Do not rely on a single Google application's database to determine a file's origin or path between applications; extract the shared File ID, folder ID, or server_perm_id from each connected application's database and match them to reconstruct the actual sequence of user actions.

## Addresses

- [[weaknesses/Google file-sharing activity untraceable within a single app's own artifacts]]

## How To Apply

When investigating a file found in Google Drive, check Chrome's records for a matching "Saved from Chrome" folder ID, Gmail's `searchsqlitedb`/`sqlitedb` for a matching attachment identifier, and Google Classroom/Calendar/Chat/Docs Editor databases for matching identifiers, depending on which applications are present on the device. Where feasible, use or build tooling that automates this identifier-matching step across all locally available Google application databases rather than manually cross-referencing each pair, since the number of pairwise combinations scales quickly with the number of installed apps.

## References

- [LWCite-1006] Park et al., 2025, "A comprehensive artifact analysis of Google applications on Android and iOS platforms", FSI: Digital Investigation 55.

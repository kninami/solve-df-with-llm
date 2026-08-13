---
id: DFM-1204
type: mitigation
name: Confirm the target application's database schema uses FTS-indexed tables before relying on FTS-based deleted-message recovery
source_refs:
  - DFCite-1217
updated_at: 2026-08-13
status: complete
---

# Confirm the target application's database schema uses FTS-indexed tables before relying on FTS-based deleted-message recovery

## Summary

Before relying on SQLite FTS shadow-table recovery to argue that no deleted-message evidence exists, first confirm the target application's database schema actually uses FTS-indexed tables for the relevant content, and separately verify empirically what the application's own delete function does and does not clear.

## Addresses

- [[weaknesses/FTS-based deleted-message recovery depends on the target application's database schema retaining undeleted FTS shadow-table remnants]]

## How To Apply

Inspect the target database's schema for FTS3/4/5 companion tables (named with `_content`, `Search_content`, `_data`, `_segdir`, or `_docsize` suffixes alongside a main table). If present, send a test message in a controlled test instance of the application, delete it using each of the application's available delete functions, and check whether the FTS shadow table retains the original content under the same row ID; document exactly which delete function(s) leave recoverable remnants and which do not, since a single application can offer multiple, differently-behaving deletion functions (e.g. Webex's "delete message" versus "leave room"). If no FTS tables exist for the relevant content, fall back to a different deleted-data-recovery approach (unused-page analysis, rollback-journal recovery) rather than reporting an absence of deleted-message evidence.

## References

- [DFCite-1217] Hur et al., 2023, "Forensic analysis for multi-platform Cisco Webex", FSI: Digital Investigation 47, 301659.

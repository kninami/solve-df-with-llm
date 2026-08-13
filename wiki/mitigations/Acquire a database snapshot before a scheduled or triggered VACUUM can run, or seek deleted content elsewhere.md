---
id: DFM-1213
type: mitigation
name: Acquire a database snapshot before a scheduled or triggered VACUUM can run, or seek deleted content elsewhere
source_refs:
  - DFCite-1225
updated_at: 2026-08-13
status: complete
---

# Acquire a database snapshot before a scheduled or triggered VACUUM can run, or seek deleted content elsewhere

## Summary

Where a target application is known or suspected to run SQLite's VACUUM command, prioritize early acquisition to capture deleted-record remnants before a VACUUM operation permanently overwrites them, and do not expect standard unallocated-space carving of the live database to succeed once VACUUM has run.

## Addresses

- [[weaknesses/SQLite VACUUM overwrites freed record data with null bytes, preventing deleted-message recovery]]

## How To Apply

Test a candidate application's deletion behavior in a controlled environment before relying on unallocated-space carving in casework, to confirm whether the application invokes VACUUM (either explicitly, or implicitly via `auto_vacuum`) and, if so, how promptly after deletion. Where VACUUM is confirmed, prioritize rapid acquisition after a device is seized to maximize the chance of capturing a database state before pending deletions are vacuumed, and pursue alternative recovery avenues (device backups taken before the deletion, cloud sync copies, or memory acquisition while the app is running) rather than relying on carving the live database file for content already vacuumed.

## References

- [DFCite-1225] Akinbi and Ojie, 2021, "Forensic analysis of open-source XMPP multi-client social networking apps on iOS devices", FSI: Digital Investigation 36.

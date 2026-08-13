---
id: DFM-1151
type: mitigation
name: Corroborate remote-access session activity using memory and cross-device artifacts beyond log files
source_refs:
  - DFCite-1148
updated_at: 2026-08-12
status: complete
---

# Corroborate remote-access session activity using memory and cross-device artifacts beyond log files

## Summary

When investigating a remote-access application session, do not rely on the application's log files as a complete record; corroborate them with registry artifacts, a live or recently acquired process memory dump, clipboard/cache files, and the counterpart device's own artifacts, since each source records a different, only partially overlapping subset of session activity.

## Addresses

- [[weaknesses/Remote-access application logs fail to record all session actions consistently across platforms]]

## How To Apply

Treat the application's session log as one of several partial sources rather than the authoritative record. Cross-reference it with the registry (which may retain account, buddy-list, and configuration artifacts the log omits), a memory dump (which may retain dynamic passwords, screenshot/nudge/uninstall command traces, and clipboard content not present in any log), and clipboard/cache directories on both the local and counterpart device. When possible, obtain and compare both endpoints' independent artifact sets for the same session, since a command or credential omitted from one side's log or one artifact category is frequently recoverable from the counterpart device or from a different artifact category on the same device.

## References

- [DFCite-1148] Soni, Kaur and Aziz, 2024, "Decoding digital interactions: An extensive study of TeamViewer's Forensic Artifacts across Windows and android platforms", FSI: Digital Investigation 51.

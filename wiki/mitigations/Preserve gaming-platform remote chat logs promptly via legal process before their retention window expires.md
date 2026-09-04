---
id: LWM-2132
type: mitigation
name: Preserve gaming-platform remote chat logs promptly via legal process before their retention window expires
source_refs:
  - LWCite-2151
updated_at: 2026-08-16
status: complete
---

# Preserve gaming-platform remote chat logs promptly via legal process before their retention window expires

## Summary

As soon as a device examination establishes that a gaming platform account was used for text or voice chat, immediately initiate a preservation request or legal process (e.g., a preservation letter or subpoena to the platform vendor) for that account's remote chat logs, rather than waiting until local analysis is complete, since such logs may be retained by the vendor for only a short fixed window.

## Addresses

- [[weaknesses/Gaming console chat and voice communication content is not stored locally, only remotely with limited retention]]

## How To Apply

Identify the platform account ID(s) associated with the device early in the examination (e.g., from local login/registry artifacts), and submit a preservation request to the platform vendor for that account's chat/communication logs as soon as possible, independent of how long the rest of the local device analysis takes. Where the vendor exposes a user-accessible account data export (requiring the account credentials and any second factor), obtain that export directly if lawful access to the credentials exists, rather than relying only on the vendor's formal legal-process turnaround time.

## References

- [LWCite-2151] Eichhorn et al., 2024, "Well Played, Suspect! - Forensic examination of the handheld gaming console 'Steam Deck'", FSI: Digital Investigation 48.

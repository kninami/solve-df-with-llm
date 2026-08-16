---
id: DFM-2127
type: mitigation
name: Root the target device before local-data extraction when a stalkerware app disables Android backup
source_refs:
  - DFCite-2148
updated_at: 2026-08-16
status: complete
---

# Root the target device before local-data extraction when a stalkerware app disables Android backup

## Summary

When a detected stalkerware app's manifest disables Android's application-backup functionality, fall back to rooting the device so the app's internal storage directory can be browsed and pulled directly, rather than treating the failed non-rooted backup attempt as evidence that the app stores nothing locally.

## Addresses

- [[weaknesses/Non-rooted local-data extraction from a stalkerware app fails when its manifest disables Android backup]]

## How To Apply

Check the target app's manifest (or simply attempt a backup and observe whether it is rejected) before concluding local extraction is not possible; if backup is disabled, root the phone (where forensically and legally appropriate) to access the app's private storage directory directly and pull its local files and SQLite databases, then convert the recovered databases into readable text for analysis as with the non-rooted path.

## References

- [DFCite-2148] Mangeard et al., 2024, "WARNE: A stalkerware evidence collection tool", FSI: Digital Investigation 48.

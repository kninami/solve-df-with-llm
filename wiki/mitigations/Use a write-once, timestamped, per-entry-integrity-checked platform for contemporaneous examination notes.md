---
id: LWM-1131
type: mitigation
name: Use a write-once, timestamped, per-entry-integrity-checked platform for contemporaneous examination notes
source_refs:
  - LWCite-1128
updated_at: 2026-08-12
status: complete
---

# Use a write-once, timestamped, per-entry-integrity-checked platform for contemporaneous examination notes

## Summary

Record contemporaneous notes in a system that prevents committed entries from being edited or deleted, hashes or otherwise verifies each entry's integrity, and automatically timestamps the start, finish, and each individual note as it is added, so the note record itself can be trusted as an accurate audit trail.

## Addresses

- [[weaknesses/Contemporaneous note-taking platforms without write-once integrity protections allow undetected retrospective editing]]

## How To Apply

Adopt a digital note-taking platform (a dedicated case-noting tool where available) that supports write-once, read-many entries with per-entry hashing or an equivalent integrity check, and verify that timestamps for the start, finish, and each individual entry are accurate and preserved. If an earlier note is found to be erroneous, add a new, clearly-linked follow-up entry that clarifies or corrects it rather than editing or removing the original — this preserves transparency and keeps the full history available for future review. Where written (paper) notes must be used, apply equivalent physical integrity controls, such as controlled storage/archiving, since white-space insertion and similar tampering are harder to detect than in a properly integrity-checked digital system.

## References

- [LWCite-1128] Horsman, 2021, "Contemporaneous notes for digital forensic examinations", FSI: Digital Investigation 37, 301173.

---
id: LWW-2086
type: weakness
name: Closing a cloud-opened or remote-desktop-opened document drastically reduces its RAM-recoverable content compared to a local document
description: Once a document opened from cloud storage or a remote desktop connection is closed, the amount of its content recoverable from a subsequent RAM image drops sharply compared to the same document opened from local storage, and for remote desktop connections the closed-state recovery can approach zero, so an investigator who captures memory only after such a document is closed may find little to no recoverable content even though the document was genuinely viewed or edited.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2086
source_refs:
  - LWCite-2101
updated_at: 2026-08-16
status: complete
---

# Closing a cloud-opened or remote-desktop-opened document drastically reduces its RAM-recoverable content compared to a local document

## Summary

Averaged across all tested formats, the successfully-recovered content ratio for an opened document sits around 60%, but drops to around 20% once the document is closed -- and this drop is far more severe for documents opened via cloud storage or, especially, a remote desktop connection than for documents opened from local storage, where a comparatively high recovery ratio persists even after closing. A remote desktop connection in particular showed the worst recovery of any storage medium tested, often near zero regardless of open/closed state, because most of the document's actual content resides on the remote host rather than the client machine being imaged.

## Why It Matters

An investigator who captures a memory image only after a document has been closed, or who examines a client machine that accessed a document via a remote desktop connection, risks concluding that little or no relevant document content exists in memory -- when in fact the content may simply be unrecoverable given the storage medium and timing, not because it was never present or is investigatively insignificant. Failing to account for this timing- and medium-dependent recovery gap could lead an investigator to prematurely deprioritize memory forensics for a case involving cloud-based document access, or to misinterpret a low-recovery result as evidence the document was never substantively viewed or edited.

## Related Mitigations

- [[mitigations/Capture memory while a cloud or remote-desktop-accessed document remains open, and treat post-closure recovery gaps as expected rather than significant]]

## Used By

- [[techniques/Recover a document's content from RAM by accounting for its file format and storage-media source]]

## References

- [LWCite-2101] Al-Sharif, Al-Senjalawi, and Alzoubi, 2024, "The effects of document's format, size, and storage media on memory forensics", FSI: Digital Investigation 48, 301692.

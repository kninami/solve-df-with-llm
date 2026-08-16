---
id: DFM-2086
type: mitigation
name: Capture memory while a cloud or remote-desktop-accessed document remains open, and treat post-closure recovery gaps as expected rather than significant
source_refs:
  - DFCite-2101
updated_at: 2026-08-16
status: complete
---

# Capture memory while a cloud or remote-desktop-accessed document remains open, and treat post-closure recovery gaps as expected rather than significant

## Summary

When a case involves a document accessed via cloud storage or a remote desktop connection, prioritize capturing a memory image while the document remains open where operationally feasible, and interpret a low or absent recovery result from a post-closure memory image as an expected limitation of the storage medium and timing rather than as evidence the document lacked forensic significance.

## Addresses

- [[weaknesses/Closing a cloud-opened or remote-desktop-opened document drastically reduces its RAM-recoverable content compared to a local document]]

## How To Apply

Where a live-response scenario allows a choice of timing, prioritize memory acquisition while a document of interest remains open, particularly if it was accessed via cloud storage or a remote desktop connection, since this timing has the largest single effect on recoverable content of the factors studied. Where memory could only be captured after the document was closed, do not treat a low RAM-recovery result for a cloud- or remote-desktop-accessed document as evidence the document was insignificant or never substantively accessed; instead, pursue complementary evidence sources for that document (local application caches, cloud-provider access logs, or file-system artifacts) rather than relying on memory forensics alone for that class of source. Document the storage medium and open/closed timing explicitly in reporting, since these materially affect how a negative or partial memory-recovery result should be interpreted.

## References

- [DFCite-2101] Al-Sharif, Al-Senjalawi, and Alzoubi, 2024, "The effects of document's format, size, and storage media on memory forensics", FSI: Digital Investigation 48, 301692.

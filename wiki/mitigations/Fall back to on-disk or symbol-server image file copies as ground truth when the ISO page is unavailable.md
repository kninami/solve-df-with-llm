---
id: LWM-2134
type: mitigation
name: Fall back to on-disk or symbol-server image file copies as ground truth when the ISO page is unavailable
source_refs:
  - LWCite-2155
updated_at: 2026-08-17
status: complete
---

# Fall back to on-disk or symbol-server image file copies as ground truth when the ISO page is unavailable

## Summary

When a memory-resident Image Section Object page needed for byte-level comparison is unavailable, substitute a memory-mapped copy of the corresponding on-disk image file, or, if the local file system is unavailable or its trustworthiness is in question, an image file retrieved from a vendor symbol server, as an alternative ground truth for the comparison.

## Addresses

- [[weaknesses/Byte-level MMIF modification detection degrades to whole-page reporting when the ISO page is not memory-resident]]

## How To Apply

When an ISO page is found to be evicted (in SUBSEC state), locate the corresponding image file on the acquired disk image or file system and memory-map the matching page for comparison instead; since a locally sourced file could itself have been tampered with on a compromised system, prefer a copy obtained independently from a vendor symbol server (which, for Microsoft binaries, can supply the image file itself alongside debug symbols) when available and when its provenance is more trustworthy than the system under examination. Apply the same byte-by-byte comparison and benign-modification filtering logic used for ISO-based comparison to the substitute ground truth.

## References

- [LWCite-2155] Block, 2023, "Windows memory forensics: Identification of (malicious) modifications in memory-mapped image files", FSI: Digital Investigation 45.

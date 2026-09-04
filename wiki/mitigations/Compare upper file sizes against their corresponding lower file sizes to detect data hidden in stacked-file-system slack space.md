---
id: LWM-1223
type: mitigation
name: Compare upper file sizes against their corresponding lower file sizes to detect data hidden in stacked-file-system slack space
source_refs:
  - LWCite-1234
updated_at: 2026-08-13
status: complete
---

# Compare upper file sizes against their corresponding lower file sizes to detect data hidden in stacked-file-system slack space

## Summary

For each upper file recovered via correlation, compute its expected lower-file size(s) given the stacked file system's known block/extent-size rules, and flag any lower file that is larger than expected or whose replicas across multiple bricks/servers differ in size, as a candidate for hidden data.

## Addresses

- [[weaknesses/Stacked file systems expose lower-file and extra lower-file slack space that can be used to hide data]]

## How To Apply

Determine the specific stacked file system's block-alignment or extent-size rule (e.g. MooseFS's fixed 0x10000-byte content blocks plus checksum footer, eCryptfs's default 4 KiB extent padding) and calculate each upper file's expected minimum lower-file size from its reported content size. Compare this against the actual size of each corresponding lower file (or, for replicated/distributed volumes, across all replicas of the same file), and treat any lower file materially larger than the expected minimum, or any size mismatch between otherwise-identical replicas, as an indicator of possible hidden data in lower-file or extra-lower-file slack space. Where a mismatch is found, extract and analyze the excess bytes directly, and note that native software used to reconstruct dispersed/erasure-coded volumes may itself surface or corrupt hidden data depending on which replica or shard was chosen as authoritative during reconstruction.

## References

- [LWCite-1234] Hilgert, Lambertz and Baier, 2024, "Forensic implications of stacked file systems", DFRWS EU 2024; FSI: Digital Investigation 48, 301678.

---
id: DFM-1124
type: mitigation
name: Corroborate Coffee file system version ordering with sector-allocation and write-pattern evidence rather than content similarity alone
source_refs:
  - DFCite-1118
updated_at: 2026-08-12
status: complete
---

# Corroborate Coffee file system version ordering with sector-allocation and write-pattern evidence rather than content similarity alone

## Summary

Before relying on content-similarity diffing to establish a Coffee file's version chronology, first characterize the file's actual write pattern (gradual incremental change vs. whole-file rewrite) from the recovered versions themselves, and treat content-similarity-derived ordering as unreliable for files that rewrite wholesale, falling back to sector-allocation and flash-wear metadata to bound the possible ordering instead.

## Addresses

- [[weaknesses/Coffee file system version-ordering by content similarity fails once whole-file changes and intervening sectors are erased]]

## How To Apply

Before drawing conclusions from a similarity-based version ordering, inspect the recovered versions to determine whether the file's content changes gradually or is rewritten wholesale between versions; only trust similarity-trend-based ordering for the former. For wholesale-rewrite files, or wherever intervening sectors have already been erased, corroborate ordering using independent evidence such as flash sector allocation order, wear-leveling counters, or any timestamps embedded in the file's own content, and explicitly flag in the report when chronological order could not be established with confidence.

## References

- [DFCite-1118] Sandvik et al., 2021, "Coffee forensics - Reconstructing data in IoT devices running Contiki OS", FSI: Digital Investigation 37.

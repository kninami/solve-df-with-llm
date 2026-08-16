---
id: DFW-2096
type: weakness
name: Exact-match generic metadata time carving misses filesystem metadata records with similar but non-identical co-located timestamps
description: The original Generic Metadata Time Carving method requires a metadata record's co-located timestamps to be byte-for-byte identical to be detected as a candidate, but real-world filesystem metadata records frequently contain timestamps that are close but not exactly equal (e.g. differing by seconds or in a less-significant byte), causing the exact-match method to miss a large proportion of genuinely recoverable metadata records.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2097
source_refs:
  - DFCite-2113
updated_at: 2026-08-16
status: complete
---

# Exact-match generic metadata time carving misses filesystem metadata records with similar but non-identical co-located timestamps

## Summary

On a large real-world NTFS forensic image, exact-match Generic Metadata Time Carving recovered only 41.6% of $MFT records present in the ground-truth region examined, whereas allowing an approximate (prefix-based) timestamp match with a moderate prefix length recovered 97.2% of the same records with no reduction in precision -- demonstrating that the overwhelming majority of the exact-match method's missed records were not truly absent from the image, but were present with co-located timestamps that were merely similar rather than byte-identical.

## Why It Matters

An investigator relying on exact-match Generic Metadata Time Carving to recover filesystem metadata from damaged, reformatted, or otherwise non-standard filesystem structures risks concluding that far less metadata is recoverable than actually is, since the method's low recall in this scenario stems from an overly strict matching criterion rather than genuine data loss. Because Generic Metadata Time Carving is specifically intended for cases where standard filesystem structures are damaged or overwritten (the exact scenario where every recoverable record matters most), understating its achievable recall in precisely these cases is a significant practical limitation.

## Related Mitigations

- [[mitigations/Use prefix-based approximate timestamp matching instead of exact-match generic metadata time carving to improve recall]]

## Used By

- [[techniques/Recover fragmented filesystem metadata using prefix-based generic metadata time carving]]

## References

- [DFCite-2113] Porter, Nordvik, Toolan, and Axelsson, 2021, "Timestamp prefix carving for filesystem metadata extraction", FSI: Digital Investigation 38, 301266.

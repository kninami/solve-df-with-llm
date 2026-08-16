---
id: DFM-2097
type: mitigation
name: Use prefix-based approximate timestamp matching instead of exact-match generic metadata time carving to improve recall
source_refs:
  - DFCite-2113
updated_at: 2026-08-16
status: complete
---

# Use prefix-based approximate timestamp matching instead of exact-match generic metadata time carving to improve recall

## Summary

When metadata carving is needed because a filesystem's standard structures are damaged, overwritten, or otherwise inaccessible, use [[techniques/Recover fragmented filesystem metadata using prefix-based generic metadata time carving]]'s prefix-based approximate timestamp matching rather than the original exact-match Generic Metadata Time Carving method, to substantially improve recall with little to no cost in precision.

## Addresses

- [[weaknesses/Exact-match generic metadata time carving misses filesystem metadata records with similar but non-identical co-located timestamps]]

## How To Apply

When applying Generic Metadata Time Carving to a disk image, use a prefix-matching implementation rather than requiring exact timestamp equivalence, and select a prefix length that balances recall against the increased filesystem-parser runtime shorter prefixes incur (empirically, a moderate prefix length such as `p=2` for NTFS $MFT records achieved close to full attainable recall at 100% precision, while very short prefixes yield diminishing recall gains for substantially increased parser runtime). Always pass the carver's output through a filesystem-specific parser as a verification step, since the parser -- not the prefix length -- is what keeps precision high even as more false-positive candidate timestamps are generated at shorter prefix lengths. Where computational time is constrained, start with a longer prefix and reduce it only if recall proves insufficient for the case at hand.

## References

- [DFCite-2113] Porter, Nordvik, Toolan, and Axelsson, 2021, "Timestamp prefix carving for filesystem metadata extraction", FSI: Digital Investigation 38, 301266.

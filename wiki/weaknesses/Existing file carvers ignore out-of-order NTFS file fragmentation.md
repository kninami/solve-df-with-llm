---
id: DFW-1014
type: weakness
name: Existing file carvers ignore out-of-order NTFS file fragmentation
description: The great majority of file carving research and tooling assumes recovered file fragments are stored in-order on disk and searches only forward from a first fragment for later ones, but a contemporary measurement found 46.4% of fragmented NTFS files are fragmented out-of-order, meaning such carvers systematically fail to reconstruct close to half of all fragmented files.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1014
source_refs:
  - DFCite-1008
updated_at: 2026-08-09
status: complete
---

# Existing file carvers ignore out-of-order NTFS file fragmentation

## Summary

A carver that only extends a candidate fragment by searching for the next block at a higher disk offset will never find an out-of-order second fragment, which is stored at a lower offset than the first. Measured across a corpus of 220 privately owned Windows laptops, 46.4% of fragmented files exhibited out-of-order fragmentation, with an average out-of-orderness (OoO'ness) of 29.9%, and this proportion varies substantially by file type -- bmp, png, and raw images in particular show out-of-order rates above one-third of their fragmented population.

## Why It Matters

Because forward-only file carving is the dominant approach in practical tooling and much of the academic literature, files affected by out-of-order fragmentation are silently under-recovered or entirely missed during file carving-based investigations (e.g., recovering deleted images or documents from unallocated space), without any indication to the examiner that a systematic gap in recovery coverage exists. Since this is a property of how NTFS allocates blocks under normal operation -- not an anti-forensic technique -- it affects ordinary digital investigations at a scale (nearly half of fragmented files) too large to dismiss as an edge case.

## Related Mitigations

- [[mitigations/Extend file carving tools to search bidirectionally using carving-distance gap estimates]]

## Used By

- [[techniques/Carve out-of-order file fragments]]

## References

- [DFCite-1008] van der Meer et al., 2021, "A contemporary investigation of NTFS file fragmentation", FSI: Digital Investigation 38.

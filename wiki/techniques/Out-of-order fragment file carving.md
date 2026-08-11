---
id: DFT-1014
type: technique
name: Out-of-order fragment file carving
description: When carving a fragmented file whose later fragment is stored at a lower disk offset than an earlier one, search both backward and forward from a candidate fragment rather than assuming forward-only disk order, using empirical gap-size statistics to bound the search.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1014
aliases:
  - Out-of-order gap carving distance estimation
source_refs:
  - DFCite-1008
updated_at: 2026-08-09
status: complete
---

# Out-of-order fragment file carving

## Summary

A contemporary measurement of 220 privately owned Windows laptops found that 46.4% of fragmented NTFS files are fragmented out-of-order (a later-stored fragment logically precedes an earlier one), with an average out-of-orderness of 29.9% — meaning a carver that only searches forward for a next, higher-offset fragment will fail to reconstruct nearly half of all fragmented files. The carving-distance metric — the shortest distance an out-of-order carver would need to search, including the length of the still-unknown fragment — showed a strong preference for power-of-two gap sizes on NTFS, giving carvers a concrete, file-system-specific search-space heuristic.

## Details

Three metrics can describe the gap between two fragments of a bi-fragmented, out-of-order file: tail-head distance (total span including both fragments), shortest-gap distance (distance between the two fragments' nearest ends), and carving distance (the distance a carver must actually traverse, including the length of the unknown intervening fragment). Out-of-order fragmentation rates vary substantially by file type — 44.1% of fragmented `.bmp`, 38.0% of `.png`, and 37.6% of `.raw` images were out-of-order, versus lower rates for videos and most office documents — and observed carving-distance gap sizes clustered strongly around powers of two, a pattern attributable to how NTFS allocates blocks.

## Examples

- 40,660 of 72,351 fragmented NTFS-compressed files, and 14,259 of 34,720 fragmented hardlinked files, in the measured corpus were fragmented out-of-order, none of which a forward-only carver could correctly reassemble.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Existing file carvers ignore out-of-order NTFS file fragmentation]]

## References

- [DFCite-1008] van der Meer et al., 2021, "A contemporary investigation of NTFS file fragmentation", FSI: Digital Investigation 38.

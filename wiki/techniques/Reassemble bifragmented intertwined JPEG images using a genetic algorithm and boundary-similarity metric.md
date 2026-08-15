---
id: DFT-2007
type: technique
name: Reassemble bifragmented intertwined JPEG images using a genetic algorithm and boundary-similarity metric
description: The process of recovering a JPEG image whose data blocks are split into two fragments that are intertwined in the disk scan area with another JPEG or non-JPEG file's blocks, by removing structurally invalid blocks, locating the fragmentation point via a pixel-boundary similarity metric, and using a genetic algorithm to search for the lowest-cost correct block sequencing.
objective_ids:
  - DFO-1002
weakness_ids:
  - DFW-2007
aliases:
  - MHRI (Meta-Heuristic Reassemble Images)
  - Coherence of Euclidean Distance metric (CoED)
source_refs:
  - DFCite-2007
updated_at: 2026-08-14
status: partial
---

# Reassemble bifragmented intertwined JPEG images using a genetic algorithm and boundary-similarity metric

## Summary

When a JPEG image's data blocks in the disk scan area are interleaved with blocks belonging to a second JPEG image or an unrelated file format (rather than being contiguous or simply out of order), a standard sequential file carver cannot reassemble it. An investigator instead applies a three-rule pipeline that strips out structurally invalid ("strange") blocks using the JPEG restart-marker pattern, locates likely fragmentation points using a pixel-boundary similarity metric across candidate block adjacencies, and finally runs a genetic algorithm that treats each candidate block ordering as a chromosome, evolving toward the lowest-cost (most internally consistent) full reassembly.

## Details

DFCite-2007's MHRI method operationalizes this as three sequential rules, each triggered only if the prior rule fails to fully recover the image: Rule 1 (Restart Marker Algorithm) removes blocks whose byte pattern does not follow the expected `0xFF` DRI/RSTn marker structure, since these do not contain valid decoded JPEG pixel data; Rule 2 computes a Coherence of Euclidean Distance metric (CoED_m = |ED_boundary - ED_nearby|) comparing RGB pixel similarity across vertical/horizontal block boundaries to pinpoint the fragmentation point between two intertwined JPEG images; Rule 3 encodes each block sequence as a genetic-algorithm chromosome (each gene labeled by which file/image it belongs to) and searches, via selection/crossover/mutation, for the block ordering minimizing a cost function combining total CoED, real-vs-decoded MCU count mismatch, and non-decoded block count. The method assumes fragments are stored in a single contiguous run per fragment (linear order) and does not currently handle non-consecutive fragment order or missing fragments.

## Examples

- DFCite-2007's evaluation on 25 public DFRWS-2006/2007 cases and 6 private cases: Rule 1 alone fully recovered 4/31 images, Rule 2 recovered a further 6/31, and Rule 3's genetic algorithm recovered a further 5/31, for 15/31 (48.4%) full recovery overall, versus 2-9/31 for the compared RXmK/XmK/mK/RevIt baselines.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/Genetic-algorithm JPEG reassembly leaves the majority of bifragmented intertwined images unrecovered]]

## References

- [DFCite-2007] Ali et al., "A meta-heuristic method for reassemble bifragmented intertwined JPEG image files in digital forensic investigation", IEEE Access, 2023 — source of the MHRI three-rule method and its DFRWS-dataset evaluation results.

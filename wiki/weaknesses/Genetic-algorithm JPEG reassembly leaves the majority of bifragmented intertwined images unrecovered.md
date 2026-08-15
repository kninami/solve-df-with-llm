---
id: DFW-2007
type: weakness
name: Genetic-algorithm JPEG reassembly leaves the majority of bifragmented intertwined images unrecovered
description: The MHRI method fully recovers only 48.4% of tested bifragmented intertwined JPEG cases and explicitly cannot handle images with missing fragments or fragments stored in non-consecutive order, leaving a large share of real-world fragmentation cases outside its scope.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2007
source_refs:
  - DFCite-2007
updated_at: 2026-08-14
status: partial
---

# Genetic-algorithm JPEG reassembly leaves the majority of bifragmented intertwined images unrecovered

## Summary

Across 31 tested public and private DFRWS cases, MHRI fully recovered only 15 (48.4%). The paper's own results table shows several cases explicitly out of scope because they involve a missing fragment or fragments stored in non-consecutive disk order — conditions the restart-marker, CoED, and genetic-algorithm rules were not designed to handle, and which the authors identify as future work rather than solved problems.

## Why It Matters

An investigator relying on MHRI to recover an evidentiary image should not assume that a failed or partial reassembly means the image is unrecoverable by any method; more than half of the tested cases, and specifically those with missing or non-consecutively ordered fragments, fall outside the tool's current capability, meaning genuinely recoverable evidence could be treated as lost if no supplementary carving approach is attempted.

## Related Mitigations

- [[mitigations/Escalate JPEG carving cases with missing or non-consecutive fragments to supplementary recovery methods beyond MHRI]]

## Used By

- [[techniques/Reassemble bifragmented intertwined JPEG images using a genetic algorithm and boundary-similarity metric]]

## References

- [DFCite-2007] Ali et al., 2023 — Tables 2-4 and Figure 7/8 report a 48.4% overall accuracy and explicitly list missing-fragment and non-consecutive-order cases as unrecovered and out of the paper's scope.

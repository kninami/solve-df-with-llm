---
id: LWM-2007
type: mitigation
name: Escalate JPEG carving cases with missing or non-consecutive fragments to supplementary recovery methods beyond MHRI
source_refs:
  - LWCite-2007
updated_at: 2026-08-14
status: partial
---

# Escalate JPEG carving cases with missing or non-consecutive fragments to supplementary recovery methods beyond MHRI

## Summary

Before concluding that a fragmented, intertwined JPEG image cannot be recovered, check whether the case involves a missing fragment or fragments in non-consecutive disk order; if so, do not rely on the restart-marker/CoED/genetic-algorithm pipeline alone, and instead escalate to complementary carving methods, partial-image analysis, or manual examiner review.

## Addresses

- [[weaknesses/Genetic-algorithm JPEG reassembly leaves the majority of bifragmented intertwined images unrecovered]]

## How To Apply

Inspect the genetic algorithm's cost-function output: a case that cannot reach a near-zero cost after the maximum generation/iteration limit likely falls outside the method's linear-order, no-missing-fragment assumptions. For such cases, attempt other published carving methods (e.g. RXmK, XmK) that may recover a partial or different subset of cases, or fall back to manual block-by-block examiner reconstruction using the recovered strange-block and fragmentation-point reports as a starting point.

## References

- [LWCite-2007] Ali et al., 2023 — the paper's own conclusion identifies non-consecutive-order and missing-fragment recovery as future work not yet addressed by MHRI.

---
id: DFM-1036
type: mitigation
name: Report a worst-case bound alongside unstable LR values derived from sparse reference data
source_refs:
  - DFCite-1026
updated_at: 2026-08-09
status: complete
---

# Report a worst-case bound alongside unstable LR values derived from sparse reference data

## Summary

When a likelihood ratio's distance/angle probability for a proposition is derived from a small number of reference measurements, do not present the raw computed value as though it were stable; also calculate and report a conservative worst-case estimate to give the court a defensible lower bound.

## Addresses

- [[weaknesses/LR location evidence evaluation becomes unstable with too few reference measurements]]

## How To Apply

Where the number of reference measurements informing a proposition's probability is low, recompute the analysis after adding one additional hypothetical reference measurement that perfectly matches the observed evidence, and report the resulting value as a conservative "worst case" lower-bound probability alongside the originally computed value. Where feasible, collect additional reference measurements at the specific location in question before finalizing the analysis, since a larger and more representative reference dataset directly reduces this instability rather than merely bounding it.

## References

- [DFCite-1026] Spichiger, 2023, "A likelihood ratio approach for the evaluation of single point device locations", FSI: Digital Investigation 44.

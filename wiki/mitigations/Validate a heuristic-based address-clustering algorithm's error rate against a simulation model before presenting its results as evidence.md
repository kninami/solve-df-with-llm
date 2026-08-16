---
id: DFM-2076
type: mitigation
name: Validate a heuristic-based address-clustering algorithm's error rate against a simulation model before presenting its results as evidence
source_refs:
  - DFCite-2081
updated_at: 2026-08-16
status: complete
---

# Validate a heuristic-based address-clustering algorithm's error rate against a simulation model before presenting its results as evidence

## Summary

Before relying on a heuristic-based Bitcoin (or other blockchain) address-clustering result as investigative evidence, measure that heuristic's error rate against a sensitivity-analyzed simulation model with known ground truth, and disclose the resulting error rate alongside the clustering conclusion rather than presenting the clustering as definitive.

## Addresses

- [[weaknesses/Heuristic-based Bitcoin address clustering has a high inherent misattribution error rate]]

## How To Apply

Construct or obtain a blockchain simulation model that has itself been validated via sensitivity analysis (confirming its output behavior — transaction-type distribution, address-reuse rate, and input/output-count distribution — is stable and consistent with the real blockchain's characteristics under repeated runs and reasonable parameter variation). Run the candidate address-clustering heuristic against the validated model's known-ground-truth address clusters, compute its average error rate, and report that error rate alongside any clustering-derived conclusion presented in an investigation or court proceeding, using [[techniques/Measure heuristic-based Bitcoin address-clustering error rates using a validated blockchain simulation model]]. Prefer combining multiple heuristics (e.g. multi-input plus one-time-change) where the combination's measured error rate is lower than either heuristic alone, and treat any single-heuristic clustering result as provisional pending corroboration.

## References

- [DFCite-2081] Gong, Chow, Yiu, and Ting, 2022, "Sensitivity analysis for a Bitcoin simulation model", FSI: Digital Investigation 43, 301449.

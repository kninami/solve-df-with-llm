---
id: DFM-2016
type: mitigation
name: Chain a second complementary perceptual hash algorithm to filter first-pass matches before analyst review
source_refs:
  - DFCite-2016
updated_at: 2026-08-14
status: partial
---

# Chain a second complementary perceptual hash algorithm to filter first-pass matches before analyst review

## Summary

Do not present a single perceptual hash algorithm's raw match list to a human analyst; run a second, complementary perceptual hash algorithm (e.g. a conservative, low-false-positive algorithm like chHash) against the first algorithm's candidate matches to eliminate the bulk of false positives before manual review.

## Addresses

- [[weaknesses/Single-iteration perceptual hash image matching produces a high false-positive rate]]

## How To Apply

Use a broader/more sensitive first-iteration algorithm (e.g. dHash) to avoid missing true positives, then re-filter its output with a stricter second algorithm known to have a low false-positive cleaning efficiency for the target transformation types (e.g. chHash for general modifications, domiHash where rotation is the primary concern), and only pass the second iteration's surviving matches to a human analyst for final visual confirmation.

## References

- [DFCite-2016] dos Santos et al., 2024 — Tables 3, 5, and 7 demonstrate that pairing dHash with chHash (or dHash-v with chHash) as a second iteration consistently achieves the highest true-positive filtering rates (up to 100%) across the paper's simulated and real-image test sets.

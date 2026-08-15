---
id: DFW-2016
type: weakness
name: Single-iteration perceptual hash image matching produces a high false-positive rate
description: Running only one perceptual hash algorithm to flag visually similar images returns a large share of visually dissimilar false-positive matches alongside genuine ones, requiring a human analyst to wade through many irrelevant results, or a second filtering pass, before the flagged set is reliable.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-2016
source_refs:
  - DFCite-2016
updated_at: 2026-08-14
status: partial
---

# Single-iteration perceptual hash image matching produces a high false-positive rate

## Summary

The source paper's own first-iteration results show that even the best-performing single algorithm (chHash) only cleaned 43.75% of false positives at a Hamming-distance threshold, with pHash at 37.50% and other algorithms performing markedly worse; a worked example shows dHash alone returning 31 genuinely similar images out of 105 total flagged files (a 29.52% positivity rate), meaning 74 of the flagged files were visually dissimilar false positives that a human analyst would otherwise need to manually discard. The paper also notes that raising the Hamming-distance threshold above 20 bits causes an unworkable surge in false positives regardless of algorithm.

## Why It Matters

A forensic analyst manually reviewing perceptual-hash search results for CSAM or other illicit content is directly burdened by every false positive returned, both in wasted review time and in unnecessary secondary exposure to disturbing content that turns out to be irrelevant. Relying on a single hash algorithm's raw output without a filtering step therefore risks inefficient triage and, in high-volume operations, could cause a genuine match to be lost among a large volume of noise if review time is constrained.

## Related Mitigations

- [[mitigations/Chain a second complementary perceptual hash algorithm to filter first-pass matches before analyst review]]

## Used By

- [[techniques/Detect visually similar or modified images using a two-iteration perceptual hash pairing]]

## References

- [DFCite-2016] dos Santos et al., 2024 — Section VI.D-E and Table 3 report first-iteration false-positive rates and cleaning efficiencies for all six tested perceptual hash algorithms.

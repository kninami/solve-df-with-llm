---
id: LWM-1245
type: mitigation
name: Select higher-entropy perceptual hash algorithms validated by large-scale distance-distribution benchmarking
source_refs:
  - LWCite-1259
updated_at: 2026-08-13
status: complete
---

# Select higher-entropy perceptual hash algorithms validated by large-scale distance-distribution benchmarking

## Summary

Before deploying a perceptual hashing algorithm for content matching at scale, benchmark its inter-image and intra-image Hamming-distance distributions on a large, representative dataset, and choose an algorithm demonstrated to have tight, well-separated distributions (e.g., PDQ) rather than one shown to produce large accidental-collision equivalence classes (e.g., ColourHash, WaveHash).

## Addresses

- [[weaknesses/Low-entropy perceptual hash algorithms produce large equivalence classes that falsely match unrelated images]]

## How To Apply

Run (or consult published results from) a large-scale inter/intra-score distribution evaluation — see [[techniques/Evaluate perceptual hashing algorithm robustness using large-scale Hamming-distance distribution analysis]] — for any perceptual hashing algorithm before adopting it for automated content matching, and prefer algorithms whose inter-score distribution shows minimal large-equivalence-class clustering. Where an already-deployed pipeline is found to rely on a poorly-discriminating algorithm, treat any positive match it reports with additional caution and, where feasible, corroborate with a second, independently-validated hashing algorithm before acting on the match.

## References

- [LWCite-1259] McKeown and Buchanan, 2023, "Hamming distributions of popular perceptual hashing techniques", FSI: Digital Investigation 44, 301509.

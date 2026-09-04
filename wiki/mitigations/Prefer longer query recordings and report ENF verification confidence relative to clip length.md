---
id: LWM-2014
type: mitigation
name: Prefer longer query recordings and report ENF verification confidence relative to clip length
source_refs:
  - LWCite-2014
updated_at: 2026-08-14
status: partial
---

# Prefer longer query recordings and report ENF verification confidence relative to clip length

## Summary

When performing ENF-based time-of-recording verification, use the longest available portion of the query recording, apply the adaptive segmentation scheme and any complementary ENF-accuracy enhancement (e.g. RFA, E-MLE) to maximize the extracted ENF signal's length and distinctiveness, and explicitly report the technique's documented, clip-length-dependent match-rate uncertainty rather than presenting a match or non-match as a categorical conclusion.

## Addresses

- [[weaknesses/ENF-based time-of-recording verification has low match accuracy for short recordings]]

## How To Apply

Where the available recording is short (under about 6 minutes), qualify any ENF-based time verification finding with the benchmark true-match rate reported for that clip length and segmentation/enhancement configuration (e.g. ~54-62% for 2-minute clips versus ~85-94% for 6-10-minute clips), and prefer combining the adaptive segmentation scheme with an existing ENF-accuracy enhancement strategy to raise reliability wherever computational cost permits.

## References

- [LWCite-2014] Yalinkilic and Vatansever, 2024 — the paper's own Table 7 shows combining the segmentation scheme with existing enhancement strategies (RFA, E-MLE) meaningfully raises true-match rates across all tested clip lengths.

---
id: DFW-1121
type: weakness
name: HC-based authorship verification accuracy is unreliable for short text samples
description: Higher-Criticism-based authorship verification's accuracy scales strongly with the amount of combined text available, performing close to chance on short samples (roughly 1,000-2,000 characters) and only becoming reliable once combined text length reaches tens of thousands of characters, limiting its usefulness against accounts or messages with a sparse writing history.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1121
source_refs:
  - DFCite-1115
updated_at: 2026-08-12
status: complete
---

# HC-based authorship verification accuracy is unreliable for short text samples

## Summary

Evaluated across text-length intervals, accuracy for the shortest interval (1,000-2,000 characters) was only 0.645 with an F1 of 0.6785 — barely above chance for a binary same/different-author decision — and accuracy stayed below 0.75 for all intervals under roughly 6,000 characters. Accuracy rose to above 0.8 only once combined text length reached roughly 11,000-12,000 characters, and its best reported result (0.94 accuracy) required 29,000-30,000 characters of combined text.

## Why It Matters

An investigator applying this technique to an account or individual with a limited writing history — few posts, short messages, or a recently created account — risks a verification decision no more reliable than a coin flip, even though the algorithm still returns a confident-looking probability score. Because the paper's own dataset (informal Reddit comments and posts) already represents a favorable case for accumulating sufficient combined text, the technique may be even less reliable in investigative contexts involving shorter-form communication (e.g. individual chat messages) unless many messages are aggregated first.

## Related Mitigations

- [[mitigations/Aggregate sufficient combined text length and report a confidence level tied to the validated accuracy curve before relying on HC-based authorship verification]]

## Used By

- [[techniques/Verify authorship of two text samples using a Higher-Criticism-based similarity algorithm]]

## References

- [DFCite-1115] Le et al., 2021, "ChunkedHCs algorithm for authorship verification problems: Reddit case study", FSI: Digital Investigation 37.

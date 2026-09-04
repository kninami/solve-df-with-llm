---
id: LWW-1076
type: weakness
name: DTW-based signature verification misclassifies roughly one in five imitated signatures as genuine
description: The dynamic-feature DTW similarity method achieved only a 78.5% true negative rate on the evaluated dataset, meaning approximately 21.5% of imitated test signatures were misclassified as genuine, and a qualitative case review found at least one instance where the method's output was wrong and an examiner correctly disregarded it in favor of their own independent traditional evaluation.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-1076
source_refs:
  - LWCite-1066
updated_at: 2026-08-10
status: complete
---

# DTW-based signature verification misclassifies roughly one in five imitated signatures as genuine

## Summary

Across the evaluated dataset, the DTW-based majority-voting method reached 87.7% true positive rate (correctly recognizing genuine signatures) but only 78.5% true negative rate (correctly flagging imitations) — the authors note the method is "slightly biased towards sensitivity," meaning it more often accepts a forgery than it wrongly rejects a genuine signature. In one qualitative test case, the method failed to correctly recognize an imitation that the human examiner had already correctly identified.

## Why It Matters

Because the method is intended to provide "additional numerical strength" to an examiner's determination rather than replace it, a practitioner who defers to the method's output in a borderline case risks accepting a forged signature roughly one time in five, a meaningfully higher error rate than the method's performance on genuine signatures would suggest if only the overall accuracy figure is reported without breaking out the asymmetry between the two error types.

## Related Mitigations

- [[mitigations/Treat DTW signature-verification output as advisory and never let it override an examiner's independent qualitative judgment]]

## Used By

- [[techniques/Examine forensic signatures using DTW-based dynamic-feature similarity]]

## References

- [LWCite-1066] Mazzolini et al., 2021, "An easy-to-explain decision support framework for forensic analysis of dynamic signatures", FSI: Digital Investigation 38.

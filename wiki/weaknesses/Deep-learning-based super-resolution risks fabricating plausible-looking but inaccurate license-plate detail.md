---
id: DFW-1299
type: weakness
name: Deep-learning-based super-resolution risks fabricating plausible-looking but inaccurate license-plate detail
description: A deep-learning super-resolution model can hallucinate visually plausible character shapes or fine detail that were not actually present in the low-resolution source frames, biased by whatever patterns its training dataset over-represents, so an enhanced license plate image can look legible and convincing while depicting characters, textures, or details that do not match the true target.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-1301
source_refs:
  - DFCite-1332
updated_at: 2026-08-15
status: complete
---

# Deep-learning-based super-resolution risks fabricating plausible-looking but inaccurate license-plate detail

## Summary

The source research explicitly excludes deep-learning-based super-resolution methods from its own forensic-use recommendation, citing "the black-box approach and the bias that can be introduced by the training dataset" as reasons to consider such methods "less favorable for a forensic setting" — even while acknowledging that cutting-edge deep-learning super-resolution methods are reviewed as part of the broader technical landscape. This reflects a well-established risk: a generative or learned upscaling model can produce output detail statistically consistent with its training distribution rather than genuinely derived from the specific input frames, since the model is filling in information the low-resolution source did not actually contain.

## Why It Matters

An investigator who presents a deep-learning-super-resolved license plate image as evidence, without disclosing the method's generative nature, risks the enhanced image depicting a character sequence, texture, or fine detail that the model inferred from its training data rather than genuinely recovered from the source footage — a fabrication that a viewer (including a judge or jury) could easily mistake for a faithful reconstruction. This is functionally an "extra data" problem: information appears in the output that was not verifiably present in the original evidence.

## Related Mitigations

- [[mitigations/Prefer geometry-based multi-frame super-resolution over deep-learning upscaling for evidentiary image enhancement]]

## Used By

- [[techniques/Reconstruct a legible license plate from surveillance video using perspective-registered multi-frame super-resolution]]

## References

- [DFCite-1332] Guarnieri, Fontani, Guzzi, Carrato, and Jerian, 2021, "Perspective registration and multi-frame super-resolution of license plates in surveillance videos", FSI: Digital Investigation 36, 301087.

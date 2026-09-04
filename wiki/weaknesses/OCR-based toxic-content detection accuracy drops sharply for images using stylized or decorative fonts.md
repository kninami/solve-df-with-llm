---
id: LWW-2117
type: weakness
name: OCR-based toxic-content detection accuracy drops sharply for images using stylized or decorative fonts
description: An OCR-plus-classifier pipeline for detecting toxic content embedded as text within images degrades from roughly 92% accuracy on standard-font images to as low as 62% on images using stylized or decorative fonts, because OCR misreads of the underlying text propagate directly into the downstream classifier regardless of the classifier's own accuracy on correctly-transcribed text.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2118
source_refs:
  - LWCite-2137
updated_at: 2026-08-16
status: complete
---

# OCR-based toxic-content detection accuracy drops sharply for images using stylized or decorative fonts

## Summary

Because the RNN classifier only ever sees whatever text the OCR stage produced, an OCR misread does not simply reduce classification confidence -- it can change the actual words the classifier evaluates, producing a wrong classification regardless of how accurate the classifier itself is on correctly-transcribed text. Testing across different font styles found accuracy dropping from approximately 92% on standard, clearly-legible fonts to a range of roughly 62-88% depending on the specific stylized or decorative font used.

## Why It Matters

A user seeking to evade automated toxic-content detection has a direct incentive to use a stylized or decorative font specifically to defeat OCR extraction, meaning the failure mode this weakness describes is not merely a random accuracy limitation but a foreseeable evasion vector. An investigator relying on this pipeline's automated flagging to triage a large image corpus risks systematically under-detecting toxic content in exactly the images most likely to have been deliberately obscured this way, while the pipeline's overall reported accuracy figure (calculated across a font-style mix that may not match a specific real-world case's images) could understate the risk for a corpus skewed toward stylized fonts.

## Related Mitigations

- [[mitigations/Manually review OCR-flagged low-confidence or stylized-font images before relying on automated toxic-content classification]]

## Used By

- [[techniques/Detect toxic content embedded in social media images using OCR text extraction and RNN classification]]

## References

- [LWCite-2137] "Using deep learning to detect social media 'trolls'", FSI: Digital Investigation 48, 2024.

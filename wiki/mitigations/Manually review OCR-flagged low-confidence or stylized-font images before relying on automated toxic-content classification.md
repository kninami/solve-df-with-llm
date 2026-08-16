---
id: DFM-2118
type: mitigation
name: Manually review OCR-flagged low-confidence or stylized-font images before relying on automated toxic-content classification
source_refs:
  - DFCite-2137
updated_at: 2026-08-16
status: complete
---

# Manually review OCR-flagged low-confidence or stylized-font images before relying on automated toxic-content classification

## Summary

When using an OCR-plus-classifier pipeline to detect toxic content embedded in images, manually review images the OCR stage flags as low-confidence or that visibly use a stylized or decorative font, rather than trusting the pipeline's classification for every image uniformly.

## Addresses

- [[weaknesses/OCR-based toxic-content detection accuracy drops sharply for images using stylized or decorative fonts]]

## How To Apply

Where the OCR engine reports a per-character or per-word confidence score, flag images falling below a chosen confidence threshold for manual review rather than trusting the downstream classifier's output on a low-confidence transcription. Even without a formal confidence score, visually scan a sample of images classified as non-toxic for stylized or decorative fonts likely to have defeated OCR, since these represent the pipeline's known highest-risk failure category, and prioritize manual review of that subset specifically. Where feasible, supplement OCR with a font-style detector or image-based (rather than text-based) toxicity classifier as a second signal for images OCR is likely to have handled poorly.

## References

- [DFCite-2137] "Using deep learning to detect social media 'trolls'", FSI: Digital Investigation 48, 2024.

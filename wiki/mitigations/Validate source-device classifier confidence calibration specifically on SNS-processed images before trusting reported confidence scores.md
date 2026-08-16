---
id: DFM-2112
type: mitigation
name: Validate source-device classifier confidence calibration specifically on SNS-processed images before trusting reported confidence scores
source_refs:
  - DFCite-2130
updated_at: 2026-08-16
status: complete
---

# Validate source-device classifier confidence calibration specifically on SNS-processed images before trusting reported confidence scores

## Summary

Before treating a source-device classifier's confidence score as meaningful for an SNS-processed evidence image, confirm the classifier was specifically trained, adapted, or calibrated for SNS-processed images (via [[techniques/Authenticate an SNS-processed image's source device using confidence-calibrated multimodal feature fusion]] or an equivalent approach), rather than trusting a confidence score from a classifier validated only on raw images.

## Addresses

- [[weaknesses/Zero-shot source-device classifiers trained on raw images produce confidently wrong predictions on SNS-processed images]]

## How To Apply

Determine whether an evidence image has passed through social-media platform processing (re-encoding, resizing) before relying on any source-device classification result for it; where the image's provenance is unclear, treat it as potentially SNS-processed and apply the more conservative validation standard below. Confirm the classifier being used was adapted for the SNS-processed domain specifically (style normalization, transfer learning, or fine-tuning on platform-processed images), not only validated on raw images, and confirm it includes an explicit confidence-calibration step rather than reporting its base model's raw output probability as a confidence score. Where a classifier's SNS-specific validation and calibration status is unknown, do not treat a high reported confidence score as evidence of reliability, since raw-image-trained models have been shown to report high confidence even at near-zero accuracy on SNS-processed images.

## References

- [DFCite-2130] "Uncovering the impact of SNS processing on device source authentication", FSI: Digital Investigation 56, 2026.

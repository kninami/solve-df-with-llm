---
id: LWW-2111
type: weakness
name: Zero-shot source-device classifiers trained on raw images produce confidently wrong predictions on SNS-processed images
description: A source-device identification classifier trained only on raw, unprocessed images and applied without adaptation to an image that has passed through a social networking service's re-encoding and resizing pipeline can produce a classification that is both essentially always wrong and reported with high apparent confidence, because SNS processing homogenizes the device-specific fingerprint features the classifier relies on without altering the shape of its output probability distribution.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-2112
source_refs:
  - LWCite-2130
updated_at: 2026-08-16
status: complete
---

# Zero-shot source-device classifiers trained on raw images produce confidently wrong predictions on SNS-processed images

## Summary

Applying a raw-image-trained source-device classifier directly (zero-shot, with no adaptation) to SNS-processed images measured approximately 0% classification accuracy, while the same classifier's average reported confidence for those wrong predictions remained around 81-82% -- essentially indistinguishable from the confidence it would report on images it classifies correctly. This "false confidence" pattern arises because SNS processing degrades the underlying discriminative signal (device-specific fingerprint features) without correspondingly degrading the model's own internal certainty calibration, which was never trained to recognize this specific failure condition.

## Why It Matters

An investigator relying on a source-device classifier's reported confidence score as a proxy for reliability has no warning signal in this scenario: the model reports high confidence precisely when it is most likely to be wrong, inverting the usual assumption that low confidence flags an unreliable prediction. Because social-media-sourced images are common in real casework (evidence images are frequently recovered from platforms rather than as pristine originals), an investigator applying an off-the-shelf, raw-image-validated source-device classifier to platform-sourced evidence without specific SNS-robustness validation risks confidently misattributing an image's source device.

## Related Mitigations

- [[mitigations/Validate source-device classifier confidence calibration specifically on SNS-processed images before trusting reported confidence scores]]

## Used By

- [[techniques/Authenticate an SNS-processed image's source device using confidence-calibrated multimodal feature fusion]]

## References

- [LWCite-2130] "Uncovering the impact of SNS processing on device source authentication", FSI: Digital Investigation 56, 2026.

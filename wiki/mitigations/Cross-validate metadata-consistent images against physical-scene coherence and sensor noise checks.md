---
id: LWM-1108
type: mitigation
name: Cross-validate metadata-consistent images against physical-scene coherence and sensor noise checks
source_refs:
  - LWCite-1102
updated_at: 2026-08-12
status: complete
---

# Cross-validate metadata-consistent images against physical-scene coherence and sensor noise checks

## Summary

Do not treat metadata, quantization-table, or compression-statistic consistency alone as sufficient evidence that an image is an unaltered native capture; supplement these checks with analysis the counter-forensic firmware-reinjection technique cannot forge — physical-scene plausibility (lighting, shadow, and perspective consistency), localized splicing/copy-move artifact detection, and sensor-noise (PRNU) consistency when a specific source camera is claimed.

## Addresses

- [[weaknesses/Metadata, quantization-table, and compression-statistic authenticity checks fail to detect firmware-reprocessed tampered images]]

## How To Apply

When metadata, quantization tables, and compression statistics all report a clean, native-camera-consistent result, do not close the authenticity assessment there. Check the image for physical-based inconsistencies (implausible lighting, shadow, or perspective) and for localized tampering artifacts (splicing or copy-move boundaries) that firmware-reinjection anti-forensics does not remove. Where the image claims to originate from a specific camera model or device, additionally verify sensor pattern noise (PRNU) against a reference from that device, since the technique cannot currently inject a different camera's genuine sensor noise.

## References

- [LWCite-1102] Baracchi et al., 2021, "Camera Obscura: Exploiting in-camera processing for image counter forensics", FSI: Digital Investigation 38.

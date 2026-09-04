---
id: LWM-1016
type: mitigation
name: Cross-validate frequency-domain deepfake detection with compression-robust detectors
source_refs:
  - LWCite-1010
updated_at: 2026-08-09
status: complete
---

# Cross-validate frequency-domain deepfake detection with compression-robust detectors

## Summary

For deepfake video evidence known or suspected to be heavily compressed, do not rely solely on a detector whose primary signal is high-frequency image content; corroborate its verdict with a detector specifically validated for compression robustness, or with independent forensic indicators, before drawing conclusions about authenticity.

## Addresses

- [[weaknesses/Deepfake detectors relying on high-frequency artifacts lose accuracy on heavily compressed video]]

## How To Apply

Before applying a frequency-domain or high-frequency-reconstruction deepfake detector to evidentiary video, assess its compression level (e.g., via container/codec metadata or visible compression artifacts); for heavily compressed footage, run a second detector benchmarked specifically on low-quality/highly-compressed datasets (such as one designed for the FaceForensics++ LQ subset) and treat disagreement between detectors as grounds for manual frame-level review rather than trusting a single score. Document which detector(s) were used and their known performance characteristics on comparably compressed data when presenting findings.

## References

- [LWCite-1010] Jin et al., 2024, "A dual descriptor combined with frequency domain reconstruction learning for face forgery detection in deepfake videos", FSI: Digital Investigation 49.

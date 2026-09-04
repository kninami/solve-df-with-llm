---
id: LWW-1016
type: weakness
name: Deepfake detectors relying on high-frequency artifacts lose accuracy on heavily compressed video
description: Deepfake detection models that draw their primary discriminative signal from high-frequency image content, including frequency-domain reconstruction approaches, underperform on heavily compressed (low-quality) video relative to detectors purpose-built for compression robustness, because video compression disproportionately destroys the high-frequency detail the detector depends on.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1016
source_refs:
  - LWCite-1010
updated_at: 2026-08-09
status: complete
---

# Deepfake detectors relying on high-frequency artifacts lose accuracy on heavily compressed video

## Summary

On the FaceForensics++ low-quality (LQ, heavily compressed) subset, a state-of-the-art high-frequency reconstruction and dual-descriptor detection model scored 1.16 percentage points lower in accuracy than F3-Net, a detector specifically designed for highly compressed deepfake video, despite the same model achieving the best reported performance on the high-quality (HQ) subset. The authors attribute this to significant texture-information loss under high compression, which disproportionately affects the spatial-domain and high-frequency cues the model relies on.

## Why It Matters

Real-world deepfake video encountered in an investigation (e.g., footage shared via social media or messaging apps) is frequently re-compressed multiple times, often at higher compression ratios than curated research benchmarks. A detector validated primarily on uncompressed or lightly compressed video may perform materially worse in the field than its published benchmark numbers suggest, and relying on a single detector's verdict for authenticity determination on heavily compressed evidentiary video risks both false negatives (missed forgeries) and reduced confidence in the reported score.

## Related Mitigations

- [[mitigations/Cross-validate frequency-domain deepfake detection with compression-robust detectors]]

## Used By

- [[techniques/Detect deepfakes using frequency-domain analysis]]

## References

- [LWCite-1010] Jin et al., 2024, "A dual descriptor combined with frequency domain reconstruction learning for face forgery detection in deepfake videos", FSI: Digital Investigation 49.

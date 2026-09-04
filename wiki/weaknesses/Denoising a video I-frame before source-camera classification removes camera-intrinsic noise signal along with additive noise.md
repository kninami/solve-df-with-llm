---
id: LWW-1250
type: weakness
name: Denoising a video I-frame before source-camera classification removes camera-intrinsic noise signal along with additive noise
description: Unconditionally denoising a video I-frame before feeding it to a deep-learning source-camera classifier strips genuine, discriminative camera-intrinsic noise patterns along with the unwanted additive noise, degrading classification accuracy on already low-noise frames or on devices with advanced built-in noise reduction that leave comparatively little additive noise to remove in the first place.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1251
source_refs:
  - LWCite-1265
updated_at: 2026-08-13
status: complete
---

# Denoising a video I-frame before source-camera classification removes camera-intrinsic noise signal along with additive noise

## Summary

A CNN-based source-camera classifier trained on video I-frames learns to distinguish cameras partly from intrinsic sensor noise patterns present in each frame. A denoising step applied indiscriminately to every frame, regardless of how much additive noise it actually contains, removes not only the targeted additive noise (dark current, shot, quantization noise) but also some of this discriminative intrinsic signal — a trade-off that becomes more damaging on datasets from newer smartphones whose in-camera processing already applies advanced noise reduction, leaving little additive noise for the denoiser to usefully remove.

## Why It Matters

A forensic examiner applying an always-denoise source-camera-identification pipeline uniformly across a mixed set of videos from older and newer devices risks systematically lower classification accuracy on the newer-device subset specifically because of the denoising step itself, not because those devices are inherently harder to attribute — potentially leading to unwarranted low confidence, or missed matches, purely as an artifact of the chosen processing pipeline rather than the underlying evidence.

## Related Mitigations

- [[mitigations/Apply Hybrid DN-MobileNet's noise-threshold-gated selective denoising before source-camera CNN classification]]

## Used By

- [[techniques/Identify a video's source camera using noise-threshold-gated denoising and CNN classification]]

## References

- [LWCite-1265] Tigga and Sitara, 2026, "Hybrid DN-MobileNet: A study on an effective framework for source camera identification from videos", FSI: Digital Investigation 57, 302090.

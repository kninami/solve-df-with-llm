---
id: LWW-1161
type: weakness
name: PRNU video source-camera correlation degrades under stabilization and compression
description: Video-specific processing — camera-applied stabilization that crops, warps, and translates frames, and lossy video compression codecs that attenuate high-frequency sensor noise — substantially lowers PRNU correlation scores (NCC/PCE) relative to still images, so a genuine source-camera match can fall below the detection threshold and be missed, and platform re-encoding on social media compounds the effect further.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - LWM-1161
source_refs:
  - LWCite-1164
updated_at: 2026-08-12
status: complete
---

# PRNU video source-camera correlation degrades under stabilization and compression

## Summary

Peak-to-correlation-energy (PCE) values measured on video are consistently lower overall than on still images from the same sensor, because video is typically far more heavily compressed and frequently subject to in-camera stabilization that has no equivalent step in still-photo processing. Stabilization applies an undocumented, per-frame geometric transformation (translation, scaling, warping) to compensate for camera shake, misaligning the pixel grid the PRNU pattern is anchored to; heavy H.264/AVC-style compression separately suppresses the high-frequency noise signal PRNU correlation relies on, and further downsizing or re-encoding by a social media platform compounds the loss.

## Why It Matters

An investigator who applies a still-image PRNU workflow directly to video, or who uses a fixed PCE threshold calibrated on images, risks a false negative: failing to match a video to its true source camera even though the camera genuinely recorded it, simply because signal strength has been degraded by stabilization and compression rather than because no relationship exists. Since low correlation scores can arise from either a genuine non-match or from video-specific signal degradation, a naive interpretation of a below-threshold score risks misinterpreting the result as excluding a candidate camera that in fact recorded the video.

## Related Mitigations

- [[mitigations/Invert stabilization transformations and use high-quality I-frames before correlating video PRNU patterns]]

## Used By

- [[techniques/Identify a video's source camera using PRNU noise-pattern correlation]]

## References

- [LWCite-1164] Akbari et al., 2022, "Digital forensic analysis for source video identification: A survey", FSI: Digital Investigation 41, 301390.

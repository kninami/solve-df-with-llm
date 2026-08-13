---
id: DFT-1157
type: technique
name: Identify a video's source camera using PRNU noise-pattern correlation
description: Determine whether a video was recorded by a specific candidate camera by extracting each frame's sensor pattern noise (photo response non-uniformity, PRNU) via a denoising-filter residual, averaging enough frames to build a reference pattern, and correlating a query video's estimated pattern against the candidate camera's reference pattern using normalized cross-correlation (NCC) or peak-to-correlation energy (PCE).
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1161
aliases:
  - Photo response non-uniformity (PRNU) video source camera identification
  - Sensor pattern noise (SPN) video device attribution
source_refs:
  - DFCite-1164
updated_at: 2026-08-12
status: complete
---

# Identify a video's source camera using PRNU noise-pattern correlation

## Summary

Every camera sensor's manufacturing imperfections imprint a unique, device-specific noise pattern (PRNU) onto every frame it captures. Extracting this pattern from a query video and correlating it against a reference pattern built from a candidate camera's known-source frames establishes, to a quantifiable confidence level, whether that camera recorded the query video — the same underlying principle used for source-camera identification on still images, but applied per-frame to video.

## Details

For each of the video's N frames I_i, a denoising filter F (wavelet-based filters typically outperform simpler Wiener/median filters) removes scene content, leaving a per-frame noise residual n_i = I_i - F(I_i); averaging enough residuals (N > 50 is recommended) produces a smoother, more reliable reference pattern P_V. The query pattern is then compared to a candidate camera's reference pattern via normalized cross-correlation (NCC) or the resolution-independent peak-to-correlation energy (PCE) metric, and a match is declared if the resulting score exceeds a set threshold. Video-specific factors substantially complicate this process relative to still images: heavy video compression (H.264/AVC and similar codecs) attenuates the PRNU signal, so PCE values for video are markedly lower overall than for images, even for genuine matches — of the three H.264 frame types (I, P, B), analysis is generally restricted to I-frames since they are intra-coded and do not depend on other frames for decoding. Video stabilization (optical or digital) crops, warps, and translates frames to compensate for camera shake, breaking the pixel-to-pixel spatial correspondence PRNU correlation depends on; since this transformation is generally undocumented, it must be blindly inverted (searched over candidate geometric transformation parameters) before correlation can succeed, and some cameras apply stabilization even to a video's first frame. Further downsizing, cropping, or re-encoding by social media platforms compounds signal loss.

## Examples

- Reference PRNU patterns are typically built from a large set (often 50+) of flat-field or high-texture-variance frames/images from the same candidate camera, per the same averaging approach used in image-based PRNU identification.
- NCC/PCE similarity matrices visibly differ between a genuine (positive) match, which shows a sharp correlation peak at the true alignment offset, and a non-match (negative), which shows only diffuse, near-zero correlation with no distinct peak.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/PRNU video source-camera correlation degrades under stabilization and compression]]

## References

- [DFCite-1164] Akbari et al., 2022, "Digital forensic analysis for source video identification: A survey", FSI: Digital Investigation 41, 301390.

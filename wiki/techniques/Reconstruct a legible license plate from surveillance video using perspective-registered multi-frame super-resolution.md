---
id: DFT-1289
type: technique
name: Reconstruct a legible license plate from surveillance video using perspective-registered multi-frame super-resolution
description: Produce a single, higher-resolution, lower-noise image of a vehicle's license plate (or other planar target) from a low-quality surveillance video by first accurately tracking the plate's perspective transformation (motion, scaling, and skew) across multiple frames using a fast Kanade-Lucas-Tomasi-inspired registration algorithm, then combining the perspective-corrected frames via multi-frame super-resolution, rather than relying on a single frame or simple interpolation.
objective_ids:
  - DFO-1009
weakness_ids:
  - DFW-1299
aliases:
  - Perspective-registered multi-frame license-plate super-resolution
source_refs:
  - DFCite-1332
updated_at: 2026-08-15
status: complete
---

# Reconstruct a legible license plate from surveillance video using perspective-registered multi-frame super-resolution

## Summary

Surveillance video frequently captures a target of interest — most commonly a vehicle's license plate — at a resolution too low or noisy for reliable recognition from a single frame, due to the combined effects of sensor noise, motion blur, and limited spatial sampling. When multiple frames of the same target are available, combining them can produce a lower-noise, higher-resolution composite, but only if the target's frame-to-frame motion is registered accurately first; because real surveillance footage of vehicles exhibits genuine perspective change (not just simple translation), a registration algorithm capable of accurately tracking a full perspective transformation, not merely translation, is required.

## Details

The registration algorithm computes the perspective transformation describing a quadrilateral-shaped planar object's motion (its primary intended application being vehicle license plates) by minimizing the squared distance between a perspective-transformed candidate frame and a reference frame, computed over a user-defined region of interest, using partial derivatives to substantially speed up the computation — an approach directly inspired by the Kanade-Lucas-Tomasi feature tracker used in general object-tracking frameworks, adapted here for perspective-plane tracking under the low-quality, low-resolution, high-compression, low-contrast conditions typical of surveillance footage where feature-based methods like SIFT are known to fail. Once frames are accurately registered to a common perspective, they are combined using a custom fast multi-frame super-resolution framework to produce the final composite image. The authors deliberately avoided deep-learning-based super-resolution methods for this forensic application despite their prevalence in the broader super-resolution literature, citing the black-box nature of such models and the risk of the training dataset introducing bias into the reconstructed output — a concern directly relevant to a forensic setting where the reconstructed image may be relied upon as evidence.

## Examples

- Because existing public super-resolution research datasets (including a large recent collection) exhibit only very limited perspective change between frames — unrepresentative of the perspective variation seen in genuine forensic license-plate scenarios — the authors built and released their own realistic forensic-use dataset for comprehensive testing of the full registration-plus-super-resolution pipeline.
- The proposed registration-and-super-resolution pipeline outperformed two standard interpolators, a conventional reconstruction-based super-resolution method (L1BTV), and a forensic super-resolution tool designed specifically for license plate recognition, in nearly all conducted tests.

## Related Objectives

- `DFO-1009` Create visualizations

## Related Weaknesses

- [[weaknesses/Deep-learning-based super-resolution risks fabricating plausible-looking but inaccurate license-plate detail]]

## References

- [DFCite-1332] Guarnieri, Fontani, Guzzi, Carrato, and Jerian, 2021, "Perspective registration and multi-frame super-resolution of license plates in surveillance videos", FSI: Digital Investigation 36, 301087.

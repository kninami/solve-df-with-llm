---
id: LWT-1232
type: technique
name: Identify a video's source camera using noise-threshold-gated denoising and CNN classification
description: Determine a video's source camera device, model, or brand by feeding each I-frame to a lightweight CNN classifier (MobileNetV3-Small), first selectively denoising only frames whose estimated noise level exceeds a validation-derived threshold, so genuinely low-noise frames retain their intrinsic camera signal while noisy frames are cleaned before classification.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1250
aliases:
  - Hybrid DN-MobileNet
  - Selective-denoising source camera identification from video (SCIV)
source_refs:
  - LWCite-1265
updated_at: 2026-08-13
status: complete
---

# Identify a video's source camera using noise-threshold-gated denoising and CNN classification

## Summary

Source camera identification from video (SCIV) is complicated by compression and stabilization artifacts, and by the fact that additive noise (dark current, shot, quantization noise) can either help or hurt a deep-learning classifier depending on how much of it is present in a given I-frame. Rather than always denoising or never denoising, the Hybrid DN-MobileNet approach estimates each I-frame's noise level and only applies a denoising step when that level exceeds a threshold, before feeding the (possibly denoised) I-frame to a MobileNetV3-Small CNN classifier trained per candidate camera set.

## Details

A 17-layer DnCNN-based denoiser (trained on the Smartphone Image Denoising Dataset) is available to strip additive noise from an I-frame before classification, but denoising uniformly is counterproductive on frames that are already low-noise, since it also strips genuine camera-intrinsic signal the classifier could otherwise learn from — devices with more advanced built-in noise reduction lose comparatively little from skipping denoising, while older or noisier devices benefit more from it. The hybrid framework resolves this per-frame: each I-frame's noise level is estimated using a Laplacian filter combined with a robust median-absolute-deviation (MAD) estimator, and frames scoring above a predefined threshold (set near the median noise level observed across the validation set) are routed through the DnCNN denoiser before classification, while frames at or below the threshold are classified directly. In both cases, the (possibly denoised) I-frame — rather than a raw noise residue or a PRNU pattern extracted from it — is fed to MobileNetV3-Small, a lightweight CNN architecture using depthwise-separable convolutions and squeeze-and-excitation modules that runs efficiently even on GPU/CPU-constrained devices; a softmax layer over the trained camera classes performs the final classification, and for open-set scenarios (videos from cameras absent from the training set), thresholding the softmax max-class probability against a validation-derived cutoff assigns unknown-camera videos to an "unknown" class rather than forcing a false match. Center-cropping each I-frame to 224x224 pixels before processing focuses the classifier on the frame's least stabilization-affected central region and reduces computational overhead.

## Examples

- On the VISION dataset (35 devices, 29 models, 11 brands), the hybrid selective-denoising approach achieved 79.71% device-level video-level test accuracy on frames unaffected by stabilization and 79.79% on digitally stabilized videos, compared to 81.47% device-level accuracy for stabilization-off videos using the always-denoise (DN-MobileNet) variant — showing the hybrid approach's accuracy holds up comparably well whether or not stabilization is applied.
- Evaluated against videos re-encoded and shared via WhatsApp and YouTube (introducing additional compression and information loss), the hybrid approach achieved comparable video-level accuracy for social-media-sourced videos (79.14%) and native videos (83.80%), indicating robustness to compression artifacts introduced by common sharing platforms.
- In an open-set evaluation using VISION as the "known" set and QUFVD devices as "unknown" (and vice versa), softmax-threshold-based rejection correctly flagged videos from cameras absent from training as "unknown" at accuracies in the 60-90% range depending on which and how many devices were held out, rather than forcing every video into one of the known classes.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Denoising a video I-frame before source-camera classification removes camera-intrinsic noise signal along with additive noise]]

## References

- [LWCite-1265] Tigga and Sitara, 2026, "Hybrid DN-MobileNet: A study on an effective framework for source camera identification from videos", FSI: Digital Investigation 57, 302090.

---
id: LWT-1200
type: technique
name: Reconstruct an image's manipulation-operator chain using a dual-stream residual network
description: Classify the sequence of editing operations (e.g. median filtering, Gaussian blur, resampling) applied to an image, including after the image has been lossy JPEG re-compressed, by combining a compression-feature-extraction stream (DCT-domain artifacts) with a noise-residual-extraction stream in a dual-stream residual CNN, rather than relying on spatial-domain clues alone that JPEG re-compression tends to erase.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1209
aliases:
  - ReMReNet
  - JPEG-resistant image operator chain detection
source_refs:
  - LWCite-1222
updated_at: 2026-08-13
status: complete
---

# Reconstruct an image's manipulation-operator chain using a dual-stream residual network

## Summary

Prior manipulation-history classifiers work well on uncompressed images but degrade sharply once an image has been lossy re-compressed, because JPEG's own blocking artifacts erase or mask the spatial-domain traces earlier manipulations left behind. Fusing a compression-feature-extraction (DCT-domain) stream with a noise-residual-extraction stream in a single dual-stream residual network preserves both high-level compression artifacts and low-level manipulation noise traces through re-compression, letting the network classify not just whether an image was manipulated but the specific order in which multiple editing operations were applied.

## Details

The compression feature extraction (CFE) stream converts the input image to its DCT-domain representation and applies a high-pass filter (adapted from steganalysis work) to surface blocking-artifact information indicative of JPEG re-compression and its interaction with earlier edits, while the noise residual extraction (NRE) stream avoids pooling layers in its early convolutional blocks specifically to preserve fine-grained noise-level inconsistencies between manipulated and unmanipulated regions that pooling would otherwise wash out. Both streams' deep features are concatenated and passed through residual blocks (using skip connections to mitigate vanishing gradients) before a final fully-connected classification layer, which is sized differently depending on the task: binary (manipulated vs. original), multi-class (which single manipulation was applied), or full operator-chain classification (which manipulations were applied, and in what order, e.g. Gaussian-blur-then-resampling vs. resampling-then-Gaussian-blur). The network is trained and evaluated specifically under a "post-lossy-compression" protocol — every training and test image is JPEG-compressed a second time after manipulation, simulating typical social-media re-compression — rather than only on pristine, uncompressed manipulated images.

## Examples

- On the RAISE dataset with a mismatched-source DRESDEN test set, the dual-stream network achieved 91.98% or higher accuracy classifying which of nine two-step manipulation-operator chains (e.g. median-filter-then-resample vs. resample-then-median-filter) had been applied to a re-compressed image, compared to markedly lower accuracy for single-stream (compression-only or noise-only) baselines in an ablation study.
- Single-manipulation detection accuracy exceeded 98.6% for blurring, noise addition, and resampling operations under re-compression, outperforming prior constrained-CNN and dual-stream-VGG baselines evaluated under the same post-compression protocol.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Supervised image-manipulation-chain classifiers cannot recognize manipulation types or parameter values outside their training set]]

## References

- [LWCite-1222] Kadha et al., 2023, "Forensic analysis of manipulation chains: A deep residual network for detecting JPEG-manipulation-JPEG", FSI: Digital Investigation 47.

---
id: DFT-1151
type: technique
name: Detect deepfakes using face-background noise trace comparison
description: Train a Siamese noise extractor on paired face-crop and background-crop squares from the same video frame so it learns to expose the distinct forensic noise trace of a synthesized face versus an unmodified background, then classify a candidate frame by feeding a similarity-matrix comparison of the two extracted noise traces into a deepfake classifier.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1154
aliases:
  - Siamese noise extractor deepfake detection
  - Face-background forensic noise trace investigation
source_refs:
  - DFCite-1152
updated_at: 2026-08-12
status: complete
---

# Detect deepfakes using face-background noise trace comparison

## Summary

Rather than classifying purely on spatial or frequency-domain image content, this technique targets the underlying forensic noise trace introduced by the deepfake generation process itself. A Siamese noise extractor is trained on a novel face-background pairing strategy — every training example pairs a cropped face square with a cropped background square from the same frame — so the extractor learns to isolate noise differences between a (potentially synthesized) face region and its (unmodified) surrounding background, independent of which specific manipulation algorithm produced the face.

## Details

For each candidate frame, a face square and a background square are cropped and separately passed through the Siamese noise extractor (shared weights across both branches), which is trained using a face-background pairing strategy so its output responds to the presence of synthesis-induced noise rather than to face content per se. A similarity matrix module then quantifies the noise-trace difference between the two extracted representations, and this similarity signal feeds a final deepfake/real classifier. Because the approach targets a noise-level artifact common to deepfake generation pipelines generally — rather than an artifact specific to one manipulation method's training distribution — the authors report it is comparatively more resistant to overfitting on a single manipulation type than several state-of-the-art comparison models. The extracted noise traces can also be visualized directly (frozen extractor weights applied to a face-background pair), giving investigators a visual evidentiary artifact alongside the statistical classification score, rather than only an opaque decision score or a generic feature-activation heatmap.

## Examples

- Trained and tested on Celeb-DF: 99.15% frame-level accuracy and 99.92% AUC on the normal (in-distribution) testing set, outperforming MesoNet, Capsule, FFD, Ensemble, Two-Stream, and TAR baselines trained/tested identically.
- Evaluated on a high-quality, highly difficult 518-video unknown-attack challenge dataset that had defeated many well-known deepfake detectors: the noise-trace model reached 88.95% AUC, the highest of all compared models (next best, Two-Stream, at 84.19%).
- Visualized noise traces showed complicated, colorful patterns concentrated on synthesized face regions for fake frames, and near-blank traces for both real faces and all backgrounds (real or fake), directly localizing which facial regions were synthesized.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Noise-based deepfake detectors are not validated against adversarial perturbation or distortion attacks]]

## References

- [DFCite-1152] Wang et al., 2022, "Deepfake noise investigation and detection", FSI: Digital Investigation 42.

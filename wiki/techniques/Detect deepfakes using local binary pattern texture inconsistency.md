---
id: LWT-1250
type: technique
name: Detect deepfakes using local binary pattern texture inconsistency
description: Convert a detected face region to a Local Binary Pattern (LBP) texture-coded image — which captures each pixel's local intensity relationship to its 3x3 neighborhood rather than raw pixel intensity — and classify the LBP-coded image with a CNN, exploiting the irregular texture patterns (blurring, blending seams, disrupted fine detail around eyes/nose/lips) that deepfake generation methods introduce but preserve pixel-intensity-based detectors may miss.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1265
aliases:
  - LBPNet
source_refs:
  - LWCite-1288
updated_at: 2026-08-14
status: complete
---

# Detect deepfakes using local binary pattern texture inconsistency

## Summary

Deepfake generation (whether encoder-decoder face-swap or GAN-based) systematically disrupts a face's natural texture continuity around blending boundaries and swapped facial regions, even when the resulting image looks visually convincing at the pixel level; encoding a preprocessed face crop as an LBP texture image (each pixel replaced by an 8-bit code describing whether its 8 neighbors are brighter or darker) before CNN classification exposes this location-and-intensity texture information directly, rather than relying on the CNN to learn it implicitly from raw pixels.

## Details

Preprocessing extracts the face region via MTCNN (with gamma correction for low-contrast frames and inter-frame facial-embedding similarity matching via FaceNet to filter out non-primary or falsely detected faces), then computes the LBP code for each pixel by thresholding its 3x3 neighborhood against the center pixel's own intensity (1 if a neighbor is brighter or equal, 0 if darker) and concatenating the resulting 8 bits clockwise into a decimal value that replaces the original pixel. Because LBP-coded images retain both the location and relative intensity of texture irregularities (unlike an LBP-coded histogram, which retains only aggregate intensity information and discards spatial location), a moderately deep CNN (14 convolution/batch-norm/ReLU blocks, 2 fully connected layers) trained on these LBP images can learn from relatively few epochs while achieving competitive accuracy with far fewer trainable parameters than comparable deep architectures. Video-level prediction aggregates frame-level predictions across ten sampled frames per video (rather than trusting a single frame), since some frames exhibit more texture inconsistency than others and multi-frame aggregation measurably improves accuracy over single-frame prediction.

## Examples

- Frame-level accuracy of 83.9%, 75.7%, 87.56%, and 92.38% was reported on DeeperForensics, DFDC, Celeb-DF, and FF++ respectively, improving to 86.4%, 80%, 92%, and 99.1% at video level via ten-frame aggregation.
- Testing against real-life-style manipulation from the FaceApp and First Order Motion (FOM) mobile-app-generated datasets (fine-tuned on Celeb-DF-trained weights) reached 92% and 91.2% accuracy respectively, demonstrating applicability beyond the benchmark research datasets the model was originally trained on.
- LBPNet outperformed a prior LBP-histogram-based technique (iCaps-Dfake) by 3 percentage points on DFDC-P and 2 points on Celeb-DF while using roughly one-tenth as many trainable parameters (1.1M vs. 11.7M).

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Deepfake detectors trained on one manipulation type generalize poorly to unseen manipulation types]]

## References

- [LWCite-1288] Kingra, Aggarwal and Kaur, 2022, "LBPNet: Exploiting texture descriptor for deepfake detection", FSI: Digital Investigation 42-43, 301452.

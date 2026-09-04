---
id: LWT-1016
type: technique
name: Detect deepfakes using frequency-domain analysis
description: Transform a face image into the frequency domain (e.g., via discrete cosine transform) and exploit differences between real and generated content in specific frequency bands — often the high-frequency band — to flag deepfake video frames independent of which generation algorithm produced them.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1016
aliases:
  - Frequency-domain deepfake detection
  - High-frequency DCT reconstruction deepfake detection
  - HFIR deepfake detection
  - dual descriptor deepfake detection
source_refs:
  - LWCite-1010
updated_at: 2026-08-09
status: complete
---

# Detect deepfakes using frequency-domain analysis

## Summary

Real face images retain consistent, symmetric high-frequency detail (e.g., matching texture around both eyes), while GAN- or autoencoder-generated deepfake frames typically lose or distort this high-frequency information. One instance combines a DCT-based high-frequency image reconstructor (HFIR) with a spatial dual-descriptor: a learnable filter isolates the high-frequency band, an unsupervised encoder-decoder reconstructs it, and the resulting encoding is concatenated with local/global spatial features for classification.

## Details

The DCT converts an RGB face crop into a frequency-domain spectrogram in which high-frequency content occupies the lower-right region; a fixed base filter plus a learnable filter isolate the target frequency band, and an inverse DCT restores a band-limited spatial image. In the HFIR instance, this image is passed through a 5-layer convolutional encoder-decoder trained with reconstruction (MSE) loss, producing an encoding vector that captures unknown/unseen forgery patterns without relying on labels specific to any one deepfake generation method. This unsupervised frequency-domain signal is combined with supervised spatial-domain features (e.g., local descriptor with dilated convolutions and self-attention, global descriptor with Gem pooling) before a final classification layer — the general pattern of exploiting frequency-domain artifacts extends to other transforms (DFT, wavelet) and other frequency bands beyond this specific high-frequency instance.

## Examples

- On FaceForensics++ (HQ), the HFIR + dual-descriptor combination reached 97.96% accuracy and 99.82% AUC; on cross-dataset generalization (trained on FF++, tested on Celeb-DFv2) it reached 73.65% AUC, exceeding all compared prior methods in the study.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Deepfake detectors relying on high-frequency artifacts lose accuracy on heavily compressed video]]

## References

- [LWCite-1010] Jin et al., 2024, "A dual descriptor combined with frequency domain reconstruction learning for face forgery detection in deepfake videos", FSI: Digital Investigation 49.

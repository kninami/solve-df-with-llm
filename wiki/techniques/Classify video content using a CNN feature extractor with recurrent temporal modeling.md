---
id: DFT-1149
type: technique
name: Classify video content using a CNN feature extractor with recurrent temporal modeling
description: Extract per-frame visual features with a CNN backbone, feed the resulting feature sequence into a recurrent network (an LSTM or bidirectional GRU) to aggregate temporal context across frames or sliding windows, and classify the video with a final dense layer — a general video-classification pattern applied in forensic research to both deepfake detection and pornographic-content detection.
objective_ids:
  - DFO-1019
  - DFO-1012
weakness_ids:
  - DFW-1152
aliases:
  - Recurrent convolutional forgery detection
  - CNN+LSTM deepfake video classification
  - CNN+bidirectional-GRU pornography video classification
source_refs:
  - DFCite-1151
  - DFCite-1156
updated_at: 2026-08-12
status: complete
---

# Classify video content using a CNN feature extractor with recurrent temporal modeling

## Summary

Rather than classifying each video frame independently, a CNN backbone (e.g., XceptionNet, EfficientNet, MesoNet, or MobileNetV2) first extracts a per-frame feature vector, and a recurrent layer (a vanilla LSTM, or two stacked bidirectional GRUs) then aggregates that feature sequence across a sliding window of frames before a dense classifier produces a video- or segment-level label. Two independent forensic research lines apply this same feedforward-CNN-plus-recurrent-layer pattern to different binary video-classification problems: detecting deepfake face-swap manipulation, and detecting pornographic video content.

## Details

For deepfake detection, a face-crop is passed through a CNN backbone per frame, and a vanilla LSTM is added on top to exploit inter-frame consistency that a purely feedforward (frame-by-frame) CNN cannot see; both feedforward and recurrent variants are typically compared against each other and against a set of image-perturbation-augmented training runs (horizontal flipping, cropping, and visual perturbations simulating social-media re-compression) to test whether video-based temporal modeling and/or perturbation augmentation improve robustness to previously unseen manipulation methods. For pornography detection, a lightweight MobileNetV2 extracts a 1024-dimensional feature vector per frame, a sliding window of frame features feeds two stacked bidirectional GRU layers (with dropout and batch normalization between them), and a three-layer fully-connected classifier produces a binary pornographic/benign label per window, which is then used both for video-level classification and for localizing which segments of a longer video contain pornographic content.

## Examples

- Deepfake detection: EfficientNet+LSTM ("EffLSTM"), plain EfficientNet, MesoNet+LSTM ("MesoLSTM"), and plain MesoNet were each trained on clean and perturbation-augmented data and evaluated in-sample (Celeb-DF hold-out, 79-95% accuracy) and out-of-sample (previously unencountered manipulation methods, 55-63% accuracy) — none of the four model/augmentation combinations showed a consistent, statistically clear advantage over the others on out-of-sample data.
- Pornography detection: on the APD-VIDEO dataset (15,910 video segments), the CNN+bi-GRU model reached 96.67% precision / 99.02% recall (F1) on pornographic-segment classification, matching or exceeding prior CNN-only and 3D-CNN approaches while additionally supporting segment-level localization within a video.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies
- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/CNN-RNN video classifiers produce overconfident, poorly calibrated scores on out-of-distribution content]]

## References

- [DFCite-1151] Chamot et al., 2022, "Deepfake forensics: Cross-manipulation robustness of feedforward- and recurrent convolutional forgery detection methods", FSI: Digital Investigation 40.
- [DFCite-1156] Borg et al., 2022, "Detecting and ranking pornographic content in videos", FSI: Digital Investigation 42-43.

---
id: LWM-1152
type: mitigation
name: Recalibrate CNN-RNN video classifier confidence thresholds using out-of-distribution validation data
source_refs:
  - LWCite-1151
  - LWCite-1156
updated_at: 2026-08-12
status: complete
---

# Recalibrate CNN-RNN video classifier confidence thresholds using out-of-distribution validation data

## Summary

Do not rely on a CNN-RNN video classifier's training-time classification threshold (typically 0.5) or raw softmax score when scoring content that may fall outside its training distribution; instead, hold out or construct an out-of-distribution validation set (content from unseen manipulation methods, or unseen sources/styles) and derive a re-calibrated operating threshold, or apply a calibration technique such as label smoothing during training, before deploying scores for investigative decisions.

## Addresses

- [[weaknesses/CNN-RNN video classifiers produce overconfident, poorly calibrated scores on out-of-distribution content]]

## How To Apply

Before relying on a deployed CNN-RNN video classifier's score, evaluate it against held-out content that is deliberately out-of-distribution relative to training (a different deepfake generation method, a different pornographic content source) and inspect whether the optimal decision threshold on this set differs materially from the training-time threshold; if it does, use the recalibrated threshold operationally rather than the default. Where feasible, apply score calibration during training itself (e.g., label smoothing, temperature scaling) rather than only post-hoc threshold adjustment, and treat any single confidence score as provisional pending independent human review when the input is known or suspected to differ from the training distribution.

## References

- [LWCite-1151] Chamot et al., 2022, "Deepfake forensics: Cross-manipulation robustness of feedforward- and recurrent convolutional forgery detection methods", FSI: Digital Investigation 40.
- [LWCite-1156] Borg et al., 2022, "Detecting and ranking pornographic content in videos", FSI: Digital Investigation 42-43.

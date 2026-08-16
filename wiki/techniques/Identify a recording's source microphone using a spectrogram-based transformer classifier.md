---
id: DFT-2099
type: technique
name: Identify a recording's source microphone using a spectrogram-based transformer classifier
description: Determine which specific microphone (or microphone model) recorded a given digital audio file by converting the audio into a Mel-spectrogram, dividing it into fixed-size patches, and classifying it with an attention-based transformer encoder (an Audio Spectrogram Transformer architecture), used both to distinguish between different microphone models (inter-model classification) and between individual microphones of the same brand and model (intra-model classification).
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-2105
aliases:
  - AST-based microphone classification
source_refs:
  - DFCite-2124
updated_at: 2026-08-16
status: complete
---

# Identify a recording's source microphone using a spectrogram-based transformer classifier

## Summary

Microphone forensics aims to establish that an audio recording was captured by a specific microphone, or to determine an unknown recording's likely microphone brand or model, both of which support establishing evidence authenticity and origin in digital audio forensics. Applying a transformer-based deep-learning architecture -- originally developed for natural language processing but adapted here to operate on an audio signal's Mel-spectrogram representation -- to microphone classification achieves higher accuracy than prior CNN- and classical-feature-based (MFCC, LPCC) approaches, and works both at the coarser microphone-model level and the harder microphone-individual level within the same model.

## Details

Raw audio is first converted to a Mel-spectrogram via short-time FFT, pre-emphasis filtering, Hamming windowing, and Mel-scale triangular filtering, producing a 2D time-frequency representation of the signal. This spectrogram is divided into fixed-size (16x16) patches, analogous to how a Vision Transformer processes image patches, each flattened into a low-dimensional linear embedding; positional encoding is added to preserve the patches' spatial/temporal ordering before the resulting sequence is fed into a transformer encoder, whose multi-head self-attention mechanism lets the model weigh relationships between different time-frequency regions of the spectrogram when forming its classification decision. Using a model pre-trained on both ImageNet (general image classification) and AudioSet (a large audio-event dataset) substantially outperforms training the transformer from scratch, and increasing the audio segment's duration (number of time-frequency frames fed to the model) improves accuracy up to a point of diminishing returns, since longer segments give the attention mechanism more context to work with.

## Examples

- Evaluated on the Audio Forensic Dataset for Digital Multimedia Forensics (AF-DB: 22 microphones across 7 brands, recorded in 6 environments) for inter-model classification (distinguishing microphone model/brand), the transformer achieved 94.18% overall accuracy, with the best-performing environments being lab and classroom (quiet, non-reverberant) and the worst being garden (noisy, outdoor) -- confirming that ambient noise and reverberation degrade classification accuracy for this task.
- On the same dataset for intra-model classification (distinguishing individual microphones of the same brand and model, the harder task since manufacturing consistency makes same-model units more electronically similar to each other), the transformer achieved 84.19% overall accuracy, exceeding a prior Gabor-plus-PCA-KNN baseline (77.46% average) for every microphone model tested where a direct comparison was available.
- On the King Saud University speech database (KSU-DB), where each "microphone" class in fact corresponds to a specific microphone-plus-recording-device combination rather than an isolated microphone, the transformer reached 99.38% overall accuracy, exceeding a prior CNN-with-LSTM (CRNN) baseline's 98.43% on the same dataset.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Microphone-classification accuracy can conflate the microphone's own fingerprint with the connected recording device's fingerprint]]

## References

- [DFCite-2124] Qamhan, Alotaibi, and Selouani, 2023, "Transformer for authenticating the source microphone in digital audio forensics", FSI: Digital Investigation 45, 301539.

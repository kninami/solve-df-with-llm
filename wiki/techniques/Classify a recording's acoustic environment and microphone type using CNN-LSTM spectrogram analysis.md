---
id: DFT-2022
type: technique
name: Classify a recording's acoustic environment and microphone type using CNN-LSTM spectrogram analysis
description: The process of determining both the acoustic environment (e.g. quiet room, office, noisy cafeteria) and the recording device quality class of a questioned audio file by converting its spectrogram into 2D image segments and classifying them with a hybrid CNN plus bidirectional-LSTM (CRNN) deep-learning model, supporting audio authentication and source verification.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1093
aliases:
  - Acoustic source identification (CRNN)
source_refs:
  - DFCite-2022
updated_at: 2026-08-14
status: partial
---

# Classify a recording's acoustic environment and microphone type using CNN-LSTM spectrogram analysis

## Summary

A digital audio recording's acquisition device and acoustic environment each leave characteristic artifacts (device-related noise, reverberations, background noise) in the signal even when the spoken content is unrelated to either. An investigator verifying a claim about where or with what equipment a recording was made converts the audio's spectrogram into 2D image segments and classifies them using a hybrid CNN-plus-bidirectional-LSTM (CRNN) model trained to distinguish among known environment types and microphone/recording-device quality classes.

## Details

DFCite-2022 first segments each speech signal into voiced and unvoiced phonemes using pitch/fundamental-frequency detection, since speech content itself interferes with (and is largely irrelevant to) identifying the recording device and environment; classifying using only unvoiced segments reduced processing time to about a third of using the full signal while matching or exceeding whole-signal accuracy. Short-Time-Fourier-Transform spectrograms of fixed-size frame segments are fed as 2D images into a CRNN: three convolutional+max-pooling blocks (16/24/32 filters) extract spatial features, followed by a 128-unit bidirectional LSTM layer that models temporal dependencies across the segment, then a fully connected sigmoid output layer producing per-segment class probabilities that are averaged across all of a file's segments to reach a final file-level decision. The model is evaluated on the KSU-DB Arabic speech corpus (3 environments, 4 recording-device quality classes, 136 speakers, 3600 recordings), and both the environment and microphone classifiers substantially exceeded a 10-subject human perceptual test baseline (98.0% vs. 72% for environment; 98.57% vs. 68% for microphone), with the CRNN outperforming a CNN-only baseline in both tasks.

## Examples

- DFCite-2022's environment confusion matrix: 99.55% office accuracy, 99.58% silent-room accuracy, 97.89% cafeteria accuracy (cafeteria's background noise made it the easiest for human listeners but not meaningfully different for the CRNN); microphone confusion matrix: 100% for the high-quality Yamaha Mixer, 97.13% for the Mobile-Mic in the noisiest environment.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Closed-set source-recording-device recognition cannot identify a device absent from its training set]]

## References

- [DFCite-2022] Qamhan et al., "Digital audio forensics: Microphone and environment classification using deep learning", IEEE Access, 2021 — source of the unvoiced-segment CRNN spectrogram classification method and its KSU-DB evaluation results.

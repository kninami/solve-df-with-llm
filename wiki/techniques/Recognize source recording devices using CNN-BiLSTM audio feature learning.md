---
id: DFT-1087
type: technique
name: Recognize source recording devices using CNN-BiLSTM audio feature learning
description: Identify which specific device (make/model) recorded a questioned audio file by extracting a temporal "Sequential Gaussian Mean Matrix" (SGMM) feature from segmented acoustic characteristics, then applying a structured representation-learning model combining a Convolutional Neural Network (for spatial/bottleneck feature condensation) with a Bidirectional LSTM (for temporal modeling) to classify the recording against a trained set of candidate source devices.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1093
aliases:
  - CNN-BiLSTM structured representation learning of SGMM audio features for source recording device recognition
  - SGMM
source_refs:
  - DFCite-1085
updated_at: 2026-08-10
status: complete
---

# Recognize source recording devices using CNN-BiLSTM audio feature learning

## Summary

Prior source-recording-device recognition methods often relied on features (e.g. MFCC, GSV, I-vector) that underutilize the available spatial and temporal information in an audio signal, limiting accuracy. Combining a purpose-built temporal feature (SGMM, derived from temporally segmented acoustic features) with a CNN-BiLSTM model that jointly condenses spatial information via convolutional bottleneck representation and models temporal dynamics via BiLSTM improves recognition accuracy over prior state-of-the-art methods.

## Details

The method was benchmarked against MFCC, GSV, I-vector, and BED features using a standard SVM classifier, and against four prior state-of-the-art recording-device-recognition methods evaluated on the same dataset. The proposed structured CNN-BiLSTM representation-learning approach achieved 98.78% recognition accuracy, improving on the authors' own prior best benchmark (97.3%) by an absolute 1.48 percentage points, and outperformed all compared methods and feature types tested.

## Examples

- A controlled experiment varying the frequency-band filter thresholds used during MFCC extraction found that source-device-related information is not uniformly distributed across the audio frequency spectrum, informing which frequency ranges are most useful to emphasize during feature extraction for this task.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Closed-set source-recording-device recognition cannot identify a device absent from its training set]]

## References

- [DFCite-1085] Zeng et al., 2024, "Audio source recording device recognition based on representation learning of sequential Gaussian mean matrix", FSI: Digital Investigation 48.

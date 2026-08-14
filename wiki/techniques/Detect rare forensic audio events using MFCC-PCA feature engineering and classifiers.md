---
id: DFT-2005
type: technique
name: Detect rare forensic audio events using MFCC-PCA feature engineering and classifiers
description: The process of identifying forensically significant rare sound events (e.g. gunshots, screams, glass breaking, explosions) embedded within noisy background audio by extracting cepstral/spectral features, reducing them with PCA, and classifying frames with a trained machine-learning model.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-2005
aliases:
  - Audio anomaly detection and rare event classification (ADS)
source_refs:
  - DFCite-2005
updated_at: 2026-08-14
status: partial
---

# Detect rare forensic audio events using MFCC-PCA feature engineering and classifiers

## Summary

An investigator analyzing surveillance or scene audio (e.g. for a gunshot that a camera missed) extracts a feature ensemble - Mel-frequency cepstral coefficients (MFCCs), spectral rolloff, spectral centroid, spectral contrast, spectral bandwidth, and zero-crossing rate - from framed audio, reduces the feature set with Principal Component Analysis, and passes the result to a trained classifier to both detect that an anomalous/rare event occurred and identify which type of event (e.g. gunshot vs. scream vs. glass break) it was, even when the event is embedded in loud, variable background noise.

## Details

DFCite-2005 extracts 270 raw characteristics per audio file across four feature groups (39 MFCCs, 4 spectral features, zero-crossing rate, root-mean-square signal energy), then applies PCA to select 65 components retaining 97% explained variance before feeding them to SVM, KNN, XGBoost, MLP, Random Forest, and Logistic Regression classifiers. The approach is built and evaluated on a purpose-built 8,922-clip, ~75-hour dataset that synthetically mixes 7 rare forensic sound events at random event-to-background ratios and positions into 15 real-world background environments (TUT Acoustic Scenes 2016 corpus: beach, bus, cafe, car, city center, forest path, grocery store, home, library, metro station, office, park, residential area, train, tram), deliberately including loud environmental noise to stress-test detection. MLP was the most consistently strong classifier (up to 99.08% accuracy, 99.04% precision/recall/F1 on the cafe scene), and the approach outperformed CAE and WaveNet deep-learning baselines by up to 31 percentage points of AUC on some scenes.

## Examples

- DFCite-2005's public Kaggle dataset (7 rare events x 15 backgrounds, 8,922 clips) used to benchmark SVM/KNN/XGBoost/MLP/RF/LR classifiers per environment.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Rare-event audio anomaly classifiers show inconsistent accuracy across classifier-environment combinations]]

## References

- [DFCite-2005] Abbasi et al., "A large-scale benchmark dataset for anomaly detection and rare event classification for audio forensics", IEEE Access, 2022 — source of the MFCC-PCA feature pipeline, the benchmark dataset, and the per-scene classifier evaluation.

---
id: LWT-2025
type: technique
name: Select a 2D or 3D CNN architecture to detect facial presentation attacks based on deployment constraints
description: The process of detecting physical facial presentation attacks (printed-photo spoofs, video-replay spoofs) in surveillance video by choosing between a spatio-temporal 3D CNN (higher accuracy, higher compute) and a spatial-only 2D CNN (lower compute, faster inference) based on whether the deployment context prioritizes forensic-grade reliability or real-time edge throughput.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2025
aliases:
  - Dual 2D/3D CNN presentation attack detection framework
source_refs:
  - LWCite-2025
updated_at: 2026-08-14
status: partial
---

# Select a 2D or 3D CNN architecture to detect facial presentation attacks based on deployment constraints

## Summary

Detecting whether a face captured by a traffic or access-control surveillance camera is a live subject or a physical presentation attack (a printed photo held up, or a video replayed on a screen) benefits from modeling motion over time - genuine faces exhibit natural micro-movements, blinking, and depth cues that static or looping spoofs do not reproduce convincingly. An investigator or system designer chooses a 3D CNN, which processes 16-frame spatio-temporal clips to capture these motion cues at higher computational cost, for centralized, high-security, or forensic post-event analysis where any missed spoof is unacceptable, and a 2D CNN, which classifies individual frames using only spatial features at a fraction of the compute cost, for real-time edge-based surveillance where latency and throughput matter more than eliminating every marginal false negative.

## Details

LWCite-2025 benchmarks both architectures (four-block sequential Conv+MaxPool+BatchNorm+ReLU stacks, differing only in whether convolutions operate on 3D spatio-temporal tensors or independent 2D frames) plus seven traditional ML baselines (RF, SVM, LR, QDA, DT, KNN, MLP trained on LBP+HOG handcrafted features) on the FRAUD1 (live vs. print/replay, 10 subjects) and FRAUD2 (cross-dataset generalization, 5 unseen subjects/lighting conditions) datasets, using a strict video-disjoint and subject-disjoint 10-fold cross-validation split to prevent data leakage. The 3D CNN reached 100% accuracy/precision/recall/F1/specificity (0% FN, 0% FP) at 35.4 GFLOPs per 16-frame clip and 20.6 FPS, while the 2D CNN reached 98.85% accuracy and 98.9% F1 at only 3.8 GFLOPs per frame and 80.6 FPS - over 20x less compute for a roughly 1.15-percentage-point accuracy gap. Traditional ML baselines trained on handcrafted LBP/HOG features remained competitive (MLP: 99.70% accuracy, 99.69% F1; RF: 99.40%), suggesting a lightweight ML-on-handcrafted-features pipeline can sometimes rival a dedicated 2D CNN when temporal modeling is not required.

## Examples

- LWCite-2025's proposed deployment guideline: choose the 3D CNN when server/cloud-side compute is available and zero-false-negative detection is required (e.g. post-event forensic verification, high-security access control); choose the 2D CNN, or a top-performing ML model (MLP/RF) on handcrafted features, for edge-device deployment or real-time high-throughput surveillance prioritizing speed.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/A 2D CNN presentation-attack detector misses subtle temporal spoofing artifacts that a 3D CNN catches]]

## References

- [LWCite-2025] Dessouky et al., "Efficient deep learning forensics detection system for traffic video surveillance", IEEE Access, 2026 — source of the dual 2D/3D CNN comparative benchmark and deployment guideline described above.

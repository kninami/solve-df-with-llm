---
id: LWT-2075
type: technique
name: Detect deepfakes using a Swin-Transformer spatio-temporal architecture
description: Detect manipulated facial video by extracting per-frame spatial features with a Swin Transformer (a hierarchical, shifted-window vision transformer) and analyzing the resulting feature sequence for temporal inconsistencies with a transformer-encoder block, rather than the CNN-plus-LSTM/GRU or 3D-convolutional architectures more commonly used for combined spatio-temporal deepfake detection.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1265
aliases:
  - SFormer
source_refs:
  - LWCite-2083
updated_at: 2026-08-16
status: complete
---

# Detect deepfakes using a Swin-Transformer spatio-temporal architecture

## Summary

CNN-based spatial-analysis deepfake detectors focus on local spatial features and cannot easily capture correlations between distant regions of a frame, and prior spatio-temporal approaches typically bolt a recurrent (LSTM/GRU) layer onto CNN-extracted per-frame features, which limits their global view of both space and time and has been shown to overfit and generalize poorly to unseen data. SFormer instead uses transformer layers end-to-end for both stages: a Swin Transformer captures long-range spatial dependencies within each frame via a shifted-window self-attention mechanism, and a subsequent transformer-encoder block analyzes the resulting per-frame feature sequence for temporal inconsistencies across frames.

## Details

Input video frames are pre-processed with MTCNN face detection (with gamma correction applied first for low-contrast/dark frames) and, for multi-face sequences, FaceNet embeddings with Euclidean-distance matching ensure faces of the same individual are tracked consistently across frames rather than mixed between subjects. Detected faces (resized to 224x224x3) are passed through a Swin-tiny transformer for spatial feature extraction: images are partitioned into patches, processed through four hierarchical stages of shifted-window multi-head self-attention (alternating regular and shifted window attention between consecutive blocks) with patch merging between stages, yielding a compact 1000-dimensional spatial feature vector per frame. The resulting per-frame feature sequence feeds a temporal transformer block (layer normalization, multi-head self-attention, and two 1D-convolutional layers with iterative pruning applied during training to reduce overfitting), followed by an MLP classification head (with dense-layer sparsity likewise increased progressively during training) producing a final real/fake sigmoid output. Because only a subset of the Swin Transformer's layers are trained (rather than the full network) and both temporal-block convolutions and the final dense layer are progressively pruned during training, the architecture is designed specifically to resist the overfitting-to-spatial-features problem that limits generalization in CNN-based detectors.

## Examples

- Evaluated in-dataset (single-subsequence prediction) on five benchmark datasets, SFormer reached 91.88% accuracy on DFDC, 95.04% on Celeb-DF, 94.56% on DFD, 99.67% on Deeper-Forensics, and 97.5% on a self-produced FOM-generated dataset; using multiple-subsequence prediction (aggregating predictions across several 20-frame subsequences per video) raised these to 93.67%, 99.1%, 97.81%, 100%, and 99.25% respectively.
- Cross-dataset generalization experiments (training on one dataset, testing on another) demonstrated SFormer outperforming existing spatio-temporal and transformer-based baselines compared in the paper, supporting its design goal of improved generalization relative to CNN-LSTM/GRU architectures.
- An ablation study varying batch size (8, 16, 32) during training found batch size 16 gave the best precision-recall trade-off; larger batch sizes caused overfitting that prevented convergence to the most effective parameter values.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Deepfake detectors trained on one manipulation type generalize poorly to unseen manipulation types]]

## References

- [LWCite-2083] Kingra, Aggarwal, and Kaur, 2024, "SFormer: An end-to-end spatio-temporal transformer architecture for deepfake detection", FSI: Digital Investigation 51, 301817.

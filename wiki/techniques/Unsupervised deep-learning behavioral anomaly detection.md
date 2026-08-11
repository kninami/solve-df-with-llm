---
id: DFT-1001
type: technique
name: Unsupervised deep-learning behavioral anomaly detection
description: Train a deep model (e.g., a Bidirectional GAN, or a CNN-BiLSTM autoencoder) exclusively on normal/attack-free behavioral data — ICS sensor/actuator telemetry, or surveillance video of routine activity — to fingerprint what "normal" looks like, then score later deviations from that fingerprint (via discriminator loss, reconstruction error, or both) as candidate attacks or anomalous events.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1001
  - DFW-1052
aliases:
  - GAN-based ICS behavioral anomaly fingerprinting
  - BiGAN ICS anomaly detection
source_refs:
  - DFCite-1001
  - DFCite-1042
updated_at: 2026-08-09
status: complete
---

# Unsupervised deep-learning behavioral anomaly detection

## Summary

Because labeled anomaly/attack data is scarce, imbalanced, and often environment-specific, unsupervised or semi-supervised deep models trained only on normal data avoid needing labeled anomaly examples at all. The same underlying principle — learn a compact model of "normal," then flag high deviation from it — has been applied to at least two forensically relevant modalities: ICS sensor/actuator telemetry (via a BiGAN's discriminator loss plus reconstruction residual) and multi-modal RGB-D surveillance video of human behavior in critical environments such as Bank-ATMs (via a CNN feature extractor feeding a Bidirectional LSTM autoencoder, thresholding on reconstruction error).

## Details

For ICS telemetry, a BiGAN's encoder E learns a latent representation z of multivariate sensor/actuator data x; the discriminator D distinguishes real data-and-latent pairs from generated ones; the generator G reconstructs expected behavior from z; and a weighted sum of the discriminator loss and the l1-norm reconstruction residual produces a per-timestep irregularity score. For video, RGB and Depth frames are each passed through a compact pre-trained CNN (e.g., MobileNet) to extract per-frame features (avoiding the computational cost of reconstructing raw pixels), the concatenated RGB+Depth feature sequence is fed to a two-level Bidirectional LSTM autoencoder trained only on normal activity segments, and a video segment is flagged anomalous when its reconstruction error at the decoder exceeds a threshold (e.g., mean + 0.5 standard deviations of the training reconstruction error). In both modalities, training exclusively on normal instances sidesteps the class-imbalance problem inherent to real-world anomaly data and avoids needing an explicit model of every possible attack/anomaly type; the general pattern extends to other behavioral data streams (network traffic, application logs) that share the same normal-data-only training constraint.

## Examples

- Small-scale water treatment plant (SWaT) testbed: a BiGAN-based fingerprint inferred 32 of 36 labeled cyber attacks across six treatment stages (P1-P6), evaluated using Energy Distance and Maximum Mean Discrepancy for fingerprint quality.
- A collected RGB+Depth Bank-ATM surveillance dataset (HARD-ATM, 240 video samples): the CNN-BiLSTM autoencoder achieved precision 0.990, recall 0.908, and f-measure 0.949 combining RGB and Depth features, and separately reached 89.1% and 91.1% accuracy on the public Avenue and UCF-Crime2Local benchmark datasets respectively.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/ICS anomaly score remains elevated during post-attack recovery causing false positives]]
- [[weaknesses/Video behavioral anomaly definitions are context- and environment-dependent]]

## References

- [DFCite-1001] Neshenko et al., 2021, "A behavioral-based forensic investigation approach for analyzing attacks on water plants using GANs", FSI: Digital Investigation 37.
- [DFCite-1042] Khaire and Kumar, 2022, "A semi-supervised deep learning based video anomaly detection framework using RGB-D for surveillance of real-world critical environments", FSI: Digital Investigation 40.

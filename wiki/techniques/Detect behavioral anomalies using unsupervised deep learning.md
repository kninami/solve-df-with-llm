---
id: DFT-1001
type: technique
name: Detect behavioral anomalies using unsupervised deep learning
description: Train a deep model (e.g., a Bidirectional GAN, a CNN-BiLSTM autoencoder, or a Variational Autoencoder-LSTM) exclusively on normal/attack-free behavioral data — ICS sensor/actuator telemetry, surveillance video of routine activity, or blockchain transaction attributes — to fingerprint what "normal" looks like, then score later deviations from that fingerprint (via discriminator loss, reconstruction error, or both) as candidate attacks or anomalous events.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1001
  - DFW-1052
  - DFW-1129
  - DFW-1258
aliases:
  - Unsupervised deep-learning behavioral anomaly detection
  - GAN-based ICS behavioral anomaly fingerprinting
  - BiGAN ICS anomaly detection
  - VAE-LSTM blockchain transaction anomaly detection
  - Cascaded-autoencoder insider threat prediction (CPJOS)
source_refs:
  - DFCite-1001
  - DFCite-1042
  - DFCite-1158
  - DFCite-1276
updated_at: 2026-08-14
status: complete
---

# Detect behavioral anomalies using unsupervised deep learning

## Summary

Because labeled anomaly/attack data is scarce, imbalanced, and often environment-specific, unsupervised or semi-supervised deep models trained only on normal data avoid needing labeled anomaly examples at all. The same underlying principle — learn a compact model of "normal," then flag high deviation from it — has been applied to at least three forensically relevant modalities: ICS sensor/actuator telemetry (via a BiGAN's discriminator loss plus reconstruction residual), multi-modal RGB-D surveillance video of human behavior in critical environments such as Bank-ATMs (via a CNN feature extractor feeding a Bidirectional LSTM autoencoder, thresholding on reconstruction error), and blockchain transaction records (via a Variational Autoencoder ensemble augmented with LSTM layers, thresholding on reconstruction error over raw transaction attributes).

## Details

For ICS telemetry, a BiGAN's encoder E learns a latent representation z of multivariate sensor/actuator data x; the discriminator D distinguishes real data-and-latent pairs from generated ones; the generator G reconstructs expected behavior from z; and a weighted sum of the discriminator loss and the l1-norm reconstruction residual produces a per-timestep irregularity score. For video, RGB and Depth frames are each passed through a compact pre-trained CNN (e.g., MobileNet) to extract per-frame features (avoiding the computational cost of reconstructing raw pixels), the concatenated RGB+Depth feature sequence is fed to a two-level Bidirectional LSTM autoencoder trained only on normal activity segments, and a video segment is flagged anomalous when its reconstruction error at the decoder exceeds a threshold (e.g., mean + 0.5 standard deviations of the training reconstruction error). In all three modalities, training exclusively on normal instances sidesteps the class-imbalance problem inherent to real-world anomaly data and avoids needing an explicit model of every possible attack/anomaly type or an accessible ground-truth label set; the general pattern extends to other behavioral data streams (network traffic, application logs) that share the same normal-data-only training constraint. For blockchain transactions, the model trains solely on raw per-transaction attributes (amount, fee, gas price, mining pool, currency, frequency, and z-score deviations) rather than on graph structure or labeled fraud examples, and a per-transaction reconstruction-error anomaly score is complemented with SHAP and permutation-based feature-importance analysis so investigators can see which specific attributes (e.g., fee-to-amount ratio, gas price) drove a given flag, rather than receiving an opaque score alone.

For proactive insider threat prediction from organizational log data (device, email, file, HTTP, and logon events), a cascaded chain of autoencoders first performs unsupervised data purification: each autoencoder in the chain is trained on the current sample pool, the samples with the largest reconstruction error are dropped, and the remaining, more purely "normal" samples pass to the next autoencoder in the chain, progressively filtering out anomalous behavior sequences without ever using labels. The purified normal data then feeds a joint-optimization network (a final autoencoder's latent+reconstruction-error representation concatenated into a feed-forward network trained jointly with a Gaussian Mixture Model density estimator) rather than training the dimension-reduction and density-estimation stages separately, avoiding the sub-optimal local minima that decoupled two-stage training is prone to. A Bidirectional LSTM automatically learns abstract behavioral features from each user's per-day, tier-encoded behavior sequence, removing the need for hand-crafted feature engineering.

## Examples

- Small-scale water treatment plant (SWaT) testbed: a BiGAN-based fingerprint inferred 32 of 36 labeled cyber attacks across six treatment stages (P1-P6), evaluated using Energy Distance and Maximum Mean Discrepancy for fingerprint quality.
- A collected RGB+Depth Bank-ATM surveillance dataset (HARD-ATM, 240 video samples): the CNN-BiLSTM autoencoder achieved precision 0.990, recall 0.908, and f-measure 0.949 combining RGB and Depth features, and separately reached 89.1% and 91.1% accuracy on the public Avenue and UCF-Crime2Local benchmark datasets respectively.
- A public blockchain transaction dataset: the VAE-LSTM model reduced mean squared reconstruction error to 0.0025 (MAE 0.04) — an order of magnitude improvement over Isolation Forest, One-Class SVM, and Local Outlier Factor baselines — while maintaining a Silhouette score of approximately 0.58; SHAP analysis identified fee-related features and gas prices as the primary drivers of anomaly decisions.
- The CMU insider threat test dataset (r6.2, 4,000 simulated users' actions over 516 days): the cascaded-autoencoder-plus-joint-optimization framework achieved 0.925 recall, 0.051 false-positive rate, and 0.932 AUC identifying 73 true insider-threat behavior sequences among 1,394,010 total sequences — outperforming One-Class SVM, an unsupervised DNN, One-Class AE, DAGMM, and a prior semi-supervised insider-threat baseline (MAIDF) on the same dataset, with a false-positive rate less than one quarter of the smallest achieved by any baseline model.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/ICS anomaly score remains elevated during post-attack recovery causing false positives]]
- [[weaknesses/Video behavioral anomaly definitions are context- and environment-dependent]]
- [[weaknesses/Unsupervised financial anomaly detection and clustering cannot be validated against ground truth and may misassign heterogeneous accounts]]
- [[weaknesses/Unsupervised anomaly-based insider threat detection produces a high false-positive rate because not all behavioral anomalies indicate malicious insider action]]

## References

- [DFCite-1001] Neshenko et al., 2021, "A behavioral-based forensic investigation approach for analyzing attacks on water plants using GANs", FSI: Digital Investigation 37.
- [DFCite-1042] Khaire and Kumar, 2022, "A semi-supervised deep learning based video anomaly detection framework using RGB-D for surveillance of real-world critical environments", FSI: Digital Investigation 40.
- [DFCite-1158] Song, 2026, "Detection and prediction of transactional anomalies in blockchain based accounting using mining behavior with Autoencoder-LSTM", FSI: Digital Investigation 58.
- [DFCite-1276] Wei, Chow and Yiu, 2021, "Insider threat prediction based on unsupervised anomaly detection scheme for proactive forensic investigation", FSI: Digital Investigation 38, 301126.

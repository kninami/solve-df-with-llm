---
id: DFT-2048
type: technique
name: Train federated deepfake detectors across forensic labs using threshold-based sparsity sharing
description: The process of collaboratively training a shared deepfake-video detection model across multiple forensic labs, law-enforcement agencies, or other data-siloed organizations without any raw video or full model weights ever leaving a client, by having each client share only a compact, per-filter pruning threshold vector that the server aggregates into a common sparsity pattern.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-2048
aliases:
  - TFD (Threshold-Aware Federated Deepfake Detection)
source_refs:
  - DFCite-2049
updated_at: 2026-08-14
status: partial
---

# Train federated deepfake detectors across forensic labs using threshold-based sparsity sharing

## Summary

Deepfake and other AI-manipulated video evidence is often distributed across separate organizations (forensic labs, law-enforcement agencies, social media platforms) that cannot share raw video due to privacy, legal, or security restrictions, while standard federated learning still requires exchanging full multi-million-parameter model updates every round - a bandwidth bottleneck for resource-constrained clients like mobile devices or edge servers in the field. An investigator or forensic-network operator instead deploys a federated training scheme in which each client trains a shared 3D CNN backbone locally but transmits only a compact vector of learned per-filter pruning thresholds (on the order of a few kilobytes) to the server, which aggregates these thresholds into a common, structured sparsity pattern shared across all clients while each client's actual weights and data remain entirely local.

## Details

DFCite-2049's Threshold-Aware Federated Deepfake Detection (TFD) framework associates a trainable threshold with each convolutional filter in an R(2+1)D-18 spatiotemporal backbone; a filter is kept active on a given client if its average weight magnitude exceeds the (globally shared) threshold, and pruned (zeroed) otherwise, using a differentiable piecewise-linear surrogate for gradient-based learning of the thresholds alongside the weights. After each local training round, a client uploads only its updated 512-element threshold vector - not its (still-dense) local weights - to the server, which performs simple federated averaging over the received threshold vectors to produce the next round's global threshold, broadcast back to all clients. Because all clients converge toward the same set of globally-agreed-important filters (those useful to many clients keep low thresholds and stay active; those useful to none get pruned by all), the approach yields a consistent sparse model structure across the federation while still letting each client's retained weights adapt to its own local data distribution - a form of built-in personalization not present in standard FedAvg.

## Examples

- DFCite-2049's FaceForensics++/Celeb-DF benchmark (10 clients, 200 rounds, IID stratified splits): TFD's cumulative communication after 200 rounds was about 194 million bytes versus FedAvg's 56.6 billion bytes (roughly a 290x reduction), while final validation accuracy (0.918 vs. 0.932), AUROC (0.934 vs. 0.943), and F1 (0.896 vs. 0.911) remained within a small margin of full FedAvg, and TFD pruned roughly 70% of filters, cutting per-clip compute from 40.5 to about 4.0 GFLOPs.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Threshold-averaging aggregation in federated deepfake detection is not robust to adversarial client manipulation]]

## References

- [DFCite-2049] Al-Fehani et al., "TFD-Video: Threshold-aware federated deepfake detection for video forensics", IEEE Access, 2026 — source of the TFD threshold-gated sparsity mechanism and its communication/accuracy benchmark results described above.

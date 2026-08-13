---
id: DFM-1129
type: mitigation
name: Corroborate unsupervised financial anomaly and clustering output with independent forensic accounting before treating it as confirmed
source_refs:
  - DFCite-1125
  - DFCite-1158
updated_at: 2026-08-12
status: complete
---

# Corroborate unsupervised financial anomaly and clustering output with independent forensic accounting before treating it as confirmed

## Summary

Treat graph neural network anomaly flags and K-means behavioral clusters as investigative leads for prioritizing further inquiry, not as validated findings, since their true false-positive/false-negative rate cannot be measured without ground-truth labels and mean-based clustering can group behaviorally distinct accounts together.

## Addresses

- [[weaknesses/Unsupervised financial anomaly detection and clustering cannot be validated against ground truth and may misassign heterogeneous accounts]]

## How To Apply

When an anomaly-detection or clustering model flags an account or groups accounts together, route the finding to forensic accounting review, additional data sources, or external intelligence for corroboration rather than presenting the model's output alone as evidence of illicit activity. Where accounts within the same cluster show meaningfully different transaction-value dynamics over time (visible in a time-series or dimensionality-reduction plot), investigate them individually rather than assuming shared cluster membership implies shared behavior, and consider supplementing K-means with a density-based or distance-preserving method (such as the same GNN model used for anomaly scoring) when transaction profiles are known to be highly heterogeneous. For reconstruction-error-based anomaly scoring on blockchain transactions specifically, use the model's own feature-attribution output (e.g., SHAP, permutation importance) to check whether a flagged transaction's driving features have a plausible innocent explanation (network congestion, portfolio diversification) before escalating it as a suspected-fraud lead, and route confirmed leads to blockchain-specific forensic accounting/investigation rather than acting on the anomaly score alone.

## References

- [DFCite-1125] Oliveira et al., 2025, "Complex networks-based anomaly detection for financial transactions in anti-money laundering", FSI: Digital Investigation 55, 302005.
- [DFCite-1158] Song, 2026, "Detection and prediction of transactional anomalies in blockchain based accounting using mining behavior with Autoencoder-LSTM", FSI: Digital Investigation 58.

---
id: LWT-1126
type: technique
name: Cluster financial transaction behavior using K-means with engineered temporal features
description: Group bank accounts under investigation into behavioral clusters using K-means on PCA-reduced features engineered from transaction amounts over multiple time windows, to prioritize which accounts and individuals warrant closer examination.
objective_ids:
  - DFO-1005
weakness_ids:
  - LWW-1129
aliases:
  - K-means financial behavioral clustering for AML prioritization
  - Temporal-feature transaction clustering
source_refs:
  - LWCite-1125
updated_at: 2026-08-12
status: complete
---

# Cluster financial transaction behavior using K-means with engineered temporal features

## Summary

Rather than treating every flagged account identically, K-means clustering over features engineered from transaction amounts across multiple time windows groups accounts by behavioral similarity, helping investigators prioritize targets, allocate resources, and identify recurring or coordinated transactional patterns such as drug trafficking, arms trading, or fraud rings.

## Details

Eighteen temporal features (count, sum, mean, minimum, maximum, and standard deviation of transaction amounts over 7-day, 60-day, and 180-day rolling windows) are derived per account, filtered for redundancy using a Pearson-correlation threshold, and reduced via Principal Component Analysis (PCA) to a small number of components (three components explained 88% of variance in the case study). K-means with Euclidean distance is then applied, with the Silhouette score, Davies-Bouldin index, and Within-Cluster Sum of Squares jointly used to select the number of clusters. Correspondence Analysis (CA) subsequently visualizes which behavioral clusters are most strongly associated with which investigated individual, and a descriptive time-series analysis of cluster membership over rolling windows reveals distinct magnitude/dynamics regimes — for example a cluster showing a sustained ascending transaction-value trajectory across the investigation period — that can flag periods of intensified financial activity warranting closer review. This descriptive layer is explicitly not a substitute for formal investigative procedures such as forensic accounting; it is intended to guide where those procedures should be focused.

## Examples

- In a real case study of four investigated individuals, K-means identified three well-separated clusters (the largest accounting for 70.7% of all observed transactions), and Correspondence Analysis showed two of the four individuals were both most strongly associated with the same high-volume, low-per-transaction-value cluster, flagging their profiles as comparable and worth cross-referencing.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/Unsupervised financial anomaly detection and clustering cannot be validated against ground truth and may misassign heterogeneous accounts]]

## References

- [LWCite-1125] Oliveira et al., 2025, "Complex networks-based anomaly detection for financial transactions in anti-money laundering", FSI: Digital Investigation 55, 302005.

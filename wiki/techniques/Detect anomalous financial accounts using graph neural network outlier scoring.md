---
id: DFT-1125
type: technique
name: Detect anomalous financial accounts using graph neural network outlier scoring
description: Model bank accounts and their transactions as a directed graph and score each account's anomalousness using a graph neural network outlier-detection model, trained on account-level financial indicators, to separate accounts with atypical transaction behavior from normal ones during a money-laundering investigation.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1129
aliases:
  - LUNAR-based financial account anomaly detection
  - GNN anti-money-laundering anomaly detection
source_refs:
  - DFCite-1125
updated_at: 2026-08-12
status: complete
---

# Detect anomalous financial accounts using graph neural network outlier scoring

## Summary

Financial transactions between bank accounts can be represented as a directed graph in which accounts are nodes and transactions are weighted, directed edges. A graph neural network outlier-detection model (LUNAR) trained on account-level financial indicators derived from this graph separates accounts with atypical transaction behavior from normal ones, supporting anti-money-laundering (AML) investigations.

## Details

Financial indicators — sum, count, mean, and standard deviation of amounts sent and received per account, plus in-degree and out-degree in the transaction graph — are computed from real, anonymized bank transaction data gathered during an active money-laundering investigation. LUNAR (Unifying Local Outlier Detection Methods via Graph Neural Networks) scores anomalies using graph-based distance/reachability measures between an account and its neighbors rather than raw feature values directly, which makes it robust to distance-preserving transformations such as rotation or translation of the underlying feature space. Hyperparameters (neighbor count, training epochs, learning rate, and contamination factor) are tuned via k-fold cross-validation, selecting the configuration with the best combined Silhouette-score/Davies-Bouldin-index performance (ESSDBI). A Kruskal-Wallis test can then confirm whether the flagged-anomalous and normal account groups differ significantly in their underlying transaction-value distributions, adding statistical support beyond the clustering-quality metrics alone. Complex-network techniques — community detection, graph density, and cycle analysis — serve as complementary exploratory steps that characterize network structure (e.g. identifying tightly-interconnected account communities or unusually high graph density) to support, though not substitute for, the anomaly-detection stage.

## Examples

- Applied to 9,322 real transactions across four investigated individuals, the tuned LUNAR model (5 neighbors, 50 epochs, 0.01 learning rate, 0.05 contamination factor) reached a test-set Silhouette score of 0.83 and Davies-Bouldin index of 0.65, flagging between 5 and 18 destination accounts per individual as anomalous out of 781 accounts analyzed, of which 39 showed statistically significant atypical behavior via the Kruskal-Wallis test.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Unsupervised financial anomaly detection and clustering cannot be validated against ground truth and may misassign heterogeneous accounts]]

## References

- [DFCite-1125] Oliveira et al., 2025, "Complex networks-based anomaly detection for financial transactions in anti-money laundering", FSI: Digital Investigation 55, 302005.

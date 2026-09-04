---
id: LWT-2040
type: technique
name: Detect phishing URLs using a ResNeXt-GRU ensemble deep learning model
description: The process of classifying a URL or webpage encountered during an investigation (e.g. in a suspect's browser history, email, or messaging app) as phishing or legitimate, by extracting structural URL/webpage features, balancing the training data with SMOTE, and classifying with a ResNeXt-GRU deep learning ensemble tuned via the Jaya optimization algorithm.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2040
aliases:
  - RNT-J
  - Intelligent Phishing Detection System (IPDS)
source_refs:
  - LWCite-2041
updated_at: 2026-08-14
status: partial
---

# Detect phishing URLs using a ResNeXt-GRU ensemble deep learning model

## Summary

When a URL or webpage recovered during a cybercrime investigation is suspected of being part of a phishing scheme, an investigator can classify it automatically rather than relying solely on static blocklists (which miss new, not-yet-listed malicious URLs). RNT-J extracts a broad set of structural features from a URL/webpage (hostname length, subdomain level, path structure, presence of suspicious symbols, external-resource ratios, form-action anomalies) and classifies it as phishing or legitimate using a deep learning ensemble.

## Details

LWCite-2041's pipeline first addresses severe class imbalance in the training data (phishing instances form a small minority) using SMOTE to synthesize balanced training examples, then extracts an ensemble feature vector by combining autoencoder-based unsupervised feature learning with ResNet-derived hierarchical features (concatenated or weighted-averaged into a single "EARN" ensemble representation). This ensemble feature vector feeds a ResNeXt-GRU (RNT) architecture: ResNeXt's cardinality-based parallel convolutional paths extract spatial feature representations, which are then processed by a GRU layer to capture sequential/contextual patterns in the URL's structure, with an attention mechanism weighting the most informative parts of the sequence before a final phishing-probability output layer. Hyperparameters (population size, ResNeXt block configuration, GRU hidden units, learning rate) are tuned via the Jaya optimization algorithm, which iteratively updates candidate configurations toward better and away from worse-performing ones without needing algorithm-specific control parameters.

## Examples

- LWCite-2041's benchmark on a 10,000-instance Kaggle phishing dataset: RNT-J reached 98.0% accuracy, 98.5% precision, and 97.8% F1-score, outperforming compared SVM (56.3%), CNN (86.0%), DenseNet121 (89.2%), ResNet (92.5%), and BERT (91.3%) by 11-19 percentage points, with a mean execution time of 36.99 seconds per training run.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Phishing-detection accuracy reported on SMOTE-balanced data may not reflect real-world class-imbalance precision]]

## References

- [LWCite-2041] Alsubaei et al., "Enhancing phishing detection: A novel hybrid deep learning framework for cybercrime forensics", IEEE Access, 2024 — source of the RNT-J architecture, EARN feature ensemble, and benchmark results described above.

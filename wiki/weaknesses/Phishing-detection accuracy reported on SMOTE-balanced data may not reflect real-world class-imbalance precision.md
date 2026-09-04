---
id: LWW-2040
type: weakness
name: Phishing-detection accuracy reported on SMOTE-balanced data may not reflect real-world class-imbalance precision
description: A phishing-URL classifier's headline accuracy is measured on a SMOTE-balanced dataset where phishing and legitimate instances are roughly equal, but genuine phishing prevalence in real-world traffic is far lower, and the paper's own results show accuracy dropping substantially when SMOTE is not applied, so the reported figure may overstate real-world precision.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-2040
source_refs:
  - LWCite-2041
updated_at: 2026-08-14
status: partial
---

# Phishing-detection accuracy reported on SMOTE-balanced data may not reflect real-world class-imbalance precision

## Summary

The source paper's own Table 6 shows the proposed model's accuracy dropping from 97.99% (with SMOTE) to 92.99% (without SMOTE) on one feature-selection configuration, and comparable drops for every other tested algorithm, confirming that reported performance is substantially dependent on the synthetic class-balancing step. The paper itself acknowledges the underlying imbalance is severe, stating phishing instances are a small minority of real-world traffic, but does not report a genuinely independent, realistically-imbalanced held-out evaluation; its 98% headline accuracy comes from a train/test split of the same SMOTE-balanced dataset. A classifier that performs excellently when phishing and legitimate cases are roughly equal in the test set can still generate a high volume of false positives when applied to real traffic where legitimate URLs vastly outnumber phishing ones (the base-rate effect).

## Why It Matters

An investigator or SOC deploying this class of phishing classifier operationally, expecting the paper's reported ~98% accuracy to hold, may be surprised by a higher false-positive rate in practice than the balanced-dataset benchmark suggests, since the true operational class distribution (few phishing URLs among many legitimate ones) is far more imbalanced than the training/test conditions used to produce the headline figure.

## Related Mitigations

- [[mitigations/Validate phishing classifiers on a realistically imbalanced holdout set before trusting reported balanced-dataset accuracy]]

## Used By

- [[techniques/Detect phishing URLs using a ResNeXt-GRU ensemble deep learning model]]

## References

- [LWCite-2041] Alsubaei et al., 2024 — Table 6 directly compares with-SMOTE and without-SMOTE accuracy for every tested model, and Section III.B/IV.A discuss the underlying real-world class imbalance the SMOTE step is meant to compensate for.

---
id: LWM-2040
type: mitigation
name: Validate phishing classifiers on a realistically imbalanced holdout set before trusting reported balanced-dataset accuracy
source_refs:
  - LWCite-2041
updated_at: 2026-08-14
status: partial
---

# Validate phishing classifiers on a realistically imbalanced holdout set before trusting reported balanced-dataset accuracy

## Summary

Before relying on a phishing classifier's reported accuracy for operational triage or investigative use, test it (or request test results) against a held-out sample matching real-world phishing prevalence, rather than a SMOTE-balanced dataset, and track precision specifically (not just accuracy) given legitimate traffic's much larger real-world share.

## Addresses

- [[weaknesses/Phishing-detection accuracy reported on SMOTE-balanced data may not reflect real-world class-imbalance precision]]

## How To Apply

Where feasible, evaluate a candidate phishing classifier against a naturally imbalanced sample of real traffic (not synthetically balanced), and report precision and false-positive rate alongside accuracy, since accuracy alone is a poor indicator of real-world reliability under severe class imbalance. Treat a classifier's balanced-dataset benchmark figures as an upper bound on achievable performance rather than an operational guarantee.

## References

- [LWCite-2041] Alsubaei et al., 2024 — the paper's own with/without-SMOTE comparison (Table 6) demonstrates how strongly reported accuracy depends on class-balancing, motivating independent validation under realistic imbalance before operational deployment.

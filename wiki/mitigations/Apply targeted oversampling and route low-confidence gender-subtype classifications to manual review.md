---
id: DFM-2045
type: mitigation
name: Apply targeted oversampling and route low-confidence gender-subtype classifications to manual review
source_refs:
  - DFCite-2046
updated_at: 2026-08-14
status: partial
---

# Apply targeted oversampling and route low-confidence gender-subtype classifications to manual review

## Summary

Given gender-based cyberbullying's consistently weaker classification quality across methods, apply targeted data augmentation or oversampling specifically for the gender subtype during training, and use the neutrosophic model's own indeterminacy-membership score to route low-confidence gender-subtype classifications to manual investigator review rather than accepting the automated label outright.

## Addresses

- [[weaknesses/Gender-based cyberbullying classification is consistently the least accurate subtype across all tested methods]]

## How To Apply

When preparing or retraining a fine-grained cyberbullying classifier, prioritize collecting or synthetically augmenting additional labeled gender-subtype examples beyond what generic class-balancing (e.g. SMOTE) provides, given this subtype's persistent underperformance even after standard imbalance correction. In deployment, treat instances where the neutrosophic indeterminacy-membership (I) is elevated for a gender-subtype prediction as a signal for manual review rather than trusting the automated top-probability class, since the paper's own methodology already surfaces this uncertainty value per instance.

## References

- [DFCite-2046] Ibrahim et al., 2024 — the paper's own data-augmentation experiment (Table 6) demonstrates measurable accuracy gains from targeted synthetic example generation, and its neutrosophic-set methodology (Section III) already computes a per-instance indeterminacy value usable for confidence-based triage.

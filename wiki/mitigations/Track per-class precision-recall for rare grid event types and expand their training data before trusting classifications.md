---
id: LWM-2046
type: mitigation
name: Track per-class precision-recall for rare grid event types and expand their training data before trusting classifications
source_refs:
  - LWCite-2047
updated_at: 2026-08-14
status: partial
---

# Track per-class precision-recall for rare grid event types and expand their training data before trusting classifications

## Summary

Before relying on a synchrophasor event classifier's output for rare event types, require per-class precision and recall (not just aggregate accuracy or F1) to be reported, and prioritize expanding the training dataset with additional real or synthetic examples of underrepresented event classes rather than trusting the classifier's aggregate performance figure for those classes.

## Addresses

- [[weaknesses/Grid frequency event classifier accuracy is inflated by severe class imbalance among rare event types]]

## How To Apply

Request or compute a per-class confusion matrix and precision/recall breakdown for the deployed classifier, paying particular attention to classes with few training/test examples (long oscillatory events, sustained frequency excursions, impulsive events), and treat classifications of those rare types with additional scrutiny or independent corroboration (e.g. cross-checking against SCADA alarms or operator logs) until the classifier's rare-class performance has been separately validated. Where feasible, expand the training dataset with additional labeled examples of underrepresented event types, potentially via synthetic event simulation, before relying on the classifier for those specific categories.

## References

- [LWCite-2047] Gopinathan and Shanmugam, 2024 — the paper's own discussion of accuracy's limitations under class imbalance (Section III) is the direct basis for this mitigation's per-class reporting recommendation.

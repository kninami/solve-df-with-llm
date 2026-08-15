---
id: DFM-1271
type: mitigation
name: Retrain or validate metadata-based file-triage classifiers against the specific case type and platform before relying on them operationally
source_refs:
  - DFCite-1298
updated_at: 2026-08-14
status: complete
---

# Retrain or validate metadata-based file-triage classifiers against the specific case type and platform before relying on them operationally

## Summary

Before deploying a metadata-based file-triage classifier operationally, confirm its training data's case type and mobile platform match the case at hand, and retrain or independently re-validate it against a representative labeled sample from the actual case type and platform when they differ from what it was trained on.

## Addresses

- [[weaknesses/Metadata-based smartphone file-triage classifiers trained on one case type or platform may not generalize to a different one]]

## How To Apply

Document which case type(s) and mobile operating system(s) a given triage classifier was trained and validated on, and treat its published performance figures as applicable only within that scope. Where a new case falls outside that scope, either retrain the classifier on a representative labeled sample from the new case type/platform before relying on it, or run it in an audit-only mode on a subset of the new case's files (with results manually checked against expert-assigned labels) to measure real-world precision and recall before trusting its output to filter files from full review. Where retraining is not feasible, disclose the scope mismatch and treat the classifier's output as a lower-confidence prioritization signal rather than a basis for excluding files from examination entirely.

## References

- [DFCite-1298] Serhal and Le-Khac, 2021, "Machine learning based approach to analyze file meta data for smart phone file triage", DFRWS 2021 USA; FSI: Digital Investigation 37, 301194.

---
id: DFM-1231
type: mitigation
name: Route ambiguous or low-confidence multi-class email threat classifications to human forensic linguistic review
source_refs:
  - DFCite-1242
updated_at: 2026-08-13
status: complete
---

# Route ambiguous or low-confidence multi-class email threat classifications to human forensic linguistic review

## Summary

Use a hybrid AI-plus-human triage workflow: apply the automated classifier to bulk-triage the clear-cut, high-precision categories, but flag emails whose predicted-class probability is low or that fall into empirically confusion-prone category pairs (e.g. Anonymous vs. Subtle Threats) for a forensic linguistics expert's manual review rather than acting on the model's label directly.

## Addresses

- [[weaknesses/Multi-class email threat classifiers confuse semantically overlapping threat categories]]

## How To Apply

Compute the per-class confusion matrix and precision/recall on a validation set specific to the deployed model and dataset, identify which category pairs show elevated off-diagonal error rates, and configure the triage pipeline to route emails predicted into those pairs — or emails with low prediction-confidence margins between the top two candidate classes — to a human analyst with forensic linguistics training before any downstream action (escalation, charging referral) is taken. Retain the model's full probability distribution over classes, not just the top label, so reviewers can see which alternative categories the model considered plausible.

## References

- [DFCite-1242] Srivastava et al., 2026, "Forensically-integrated machine learning model for multi-class email threat detection using a high-fidelity synthetic dataset", FSI: Digital Investigation 57, 302108.

---
id: DFW-1231
type: weakness
name: Multi-class email threat classifiers confuse semantically overlapping threat categories
description: A multi-class email threat classifier's off-diagonal confusion errors cluster on categories whose defining language genuinely overlaps (e.g., vague anonymous tips versus subtle veiled threats), so a high overall accuracy figure can mask systematic misclassification exactly on the ambiguous, legally consequential cases where correct categorization matters most.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1231
source_refs:
  - DFCite-1242
updated_at: 2026-08-13
status: complete
---

# Multi-class email threat classifiers confuse semantically overlapping threat categories

## Summary

Even the best-performing classifier (fine-tuned BERT, 0.933 overall accuracy) showed reduced precision (0.82) specifically on Anonymous Threats, driven by semantic overlap with Subtle Threats: both categories rely on vague, cautionary, or implicature-laden language rather than the explicit, formulaic phrasing that near-perfectly discriminates classes like Formal Complaint Threats or Ransomware Threats.

## Why It Matters

An investigator who treats a multi-class threat-email classifier's high macro-accuracy as evidence the tool is reliable across all classes risks acting on a misclassified label precisely for the categories where legal consequence hinges most on correct characterization — for example, treating an ambiguous anonymous tip as a subtle threat, or vice versa, changes both the urgency of response and the legal framing of any resulting case. Because these errors are forensically logical (they occur where human analysts would also find the distinction genuinely difficult) rather than random model noise, a per-class confusion analysis is necessary before any classifier output is used to drive triage or charging decisions.

## Related Mitigations

- [[mitigations/Route ambiguous or low-confidence multi-class email threat classifications to human forensic linguistic review]]

## Used By

- [[techniques/Classify threatening email content into a forensic taxonomy using an ML and transformer ensemble]]

## References

- [DFCite-1242] Srivastava et al., 2026, "Forensically-integrated machine learning model for multi-class email threat detection using a high-fidelity synthetic dataset", FSI: Digital Investigation 57, 302108.

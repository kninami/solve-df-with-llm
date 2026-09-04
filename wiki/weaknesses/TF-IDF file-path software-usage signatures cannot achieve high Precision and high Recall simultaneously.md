---
id: LWW-1156
type: weakness
name: TF-IDF file-path software-usage signatures cannot achieve high Precision and high Recall simultaneously
description: Across 576 tested TF-IDF file-path software-signature model configurations, only a minority reach near-perfect Precision (about 38%) and a smaller, largely non-overlapping minority reach near-perfect Recall (about 18%), with the design-parameter choices that favor one metric (e.g., larger similarity thresholds) tending to work against the other, so no single default configuration reliably delivers both.
categories:
  - ASTM_INCOMP
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-1156
source_refs:
  - LWCite-1157
updated_at: 2026-08-12
status: complete
---

# TF-IDF file-path software-usage signatures cannot achieve high Precision and high Recall simultaneously

## Summary

The study's own parameter sweep across 576 SSDE model configurations found systematically different design-parameter values associated with high-Precision models (e.g., larger similarity thresholds) than with high-Recall models, and only about 38% of configurations achieved near-perfect Precision versus about 18% achieving near-perfect Recall — indicating that selecting for one metric tends to come at the expense of the other rather than both improving together.

## Why It Matters

A software-usage triage tool tuned for high Precision (fewer false positives, i.e., fewer applications incorrectly flagged as having run) will tend to miss genuine software usage (lower Recall), while a tool tuned for high Recall risks flagging applications as present when they were not actually used, adding investigative noise. Because digital forensic investigations generally weight missed evidence (a false negative that omits an actually-relevant application) as more costly than extra investigative leads to check, defaulting to a Precision-optimized configuration without deliberate consideration risks silently omitting evidence of software usage that a court or downstream investigation might need.

## Related Mitigations

- [[mitigations/Configure software-usage signature detection thresholds to prioritize Recall over Precision in forensic triage]]

## Used By

- [[techniques/Detect software usage on a compromised system using TF-IDF file-path signatures]]

## References

- [LWCite-1157] Soltani and Hosseini Seno, 2023, "Detecting the software usage on a compromised system: A triage solution for digital forensics", FSI: Digital Investigation 44.

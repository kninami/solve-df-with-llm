---
id: LWM-2001
type: mitigation
name: Corroborate ML-based facial identity comparisons with additional biometric modalities and expert review
source_refs:
  - LWCite-2001
updated_at: 2026-08-14
status: partial
---

# Corroborate ML-based facial identity comparisons with additional biometric modalities and expert review

## Summary

Treat a landmark-ratio-based facial same/different classification as investigative lead evidence, not standalone proof of identity, and corroborate it with additional biometric modalities (e.g. iris, gait, DNA where available) and a qualified forensic examiner's independent review before relying on it to identify a specific individual, particularly where identical twins or known look-alikes are a live possibility in the case.

## Addresses

- [[weaknesses/Facial identification classifiers misattribute identity between look-alikes and identical twins]]

## How To Apply

Report the classifier's own accuracy/AUC figures alongside its same/different decision rather than presenting the decision alone. Where the case specifically raises a twin or look-alike hypothesis, escalate to multi-modal biometric comparison (as recommended as future work by the source paper) and to manual expert facial-comparison review rather than relying on a single ML model's output as sufficient identification evidence.

## References

- [LWCite-2001] Sanil et al., 2023 — the paper's own conclusion and future work recommends a multi-modal FRS combining several biometric modalities to address the identical-twin/look-alike identification limitation of a single facial-landmark-ratio classifier.

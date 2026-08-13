---
id: DFM-1127
type: mitigation
name: Prefer binary child-adult classification over multi-class or regression models for indecent-image age triage
source_refs:
  - DFCite-1122
updated_at: 2026-08-12
status: complete
---

# Prefer binary child-adult classification over multi-class or regression models for indecent-image age triage

## Summary

When deploying deep-learning age estimation for indecent-image triage, use a binary child/adult classifier rather than a multi-class age-band or continuous-age regression model, since binary classification achieved materially better child-detection performance in comparative evaluation, and select the model configuration that minimizes the child-class error rate specifically.

## Addresses

- [[weaknesses/Regression and multi-class age-estimation models under-detect child images despite reasonable aggregate accuracy]]

## How To Apply

When integrating an age-estimation model into a forensic image-review workflow, configure it for binary child/adult classification rather than a finer-grained age-band or regression output, and when comparing candidate model architectures, evaluate and report the child-class error rate (recall/false-negative rate on child images) separately from overall accuracy, since aggregate accuracy can look acceptable while child-class detection remains poor. If a specific estimated age or age band is genuinely required for a case (e.g. to support offender sentencing considerations), treat that output as a secondary, lower-confidence result to be corroborated rather than the primary triage mechanism.

## References

- [DFCite-1122] Roopak et al., 2023, "Comparison of deep learning classification models for facial image age estimation in digital forensic investigations", FSI: Digital Investigation 47, 301637.

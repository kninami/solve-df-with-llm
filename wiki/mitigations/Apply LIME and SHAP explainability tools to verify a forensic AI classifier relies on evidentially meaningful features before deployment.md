---
id: DFM-2103
type: mitigation
name: Apply LIME and SHAP explainability tools to verify a forensic AI classifier relies on evidentially meaningful features before deployment
source_refs:
  - DFCite-2119
updated_at: 2026-08-16
status: complete
---

# Apply LIME and SHAP explainability tools to verify a forensic AI classifier relies on evidentially meaningful features before deployment

## Summary

Before relying on a machine-learning classifier's predictions as digital forensic evidence, apply LIME and/or SHAP to a representative set of the classifier's predictions to verify it is basing its decisions on genuinely meaningful evidentiary features, rather than accepting a high aggregate accuracy score alone as sufficient validation.

## Addresses

- [[weaknesses/Black-box AI classifiers used in digital forensic investigations provide no way to verify predictions rely on evidentially meaningful features]]

## How To Apply

Use [[techniques/Generate explainable predictions for a digital-forensic AI classifier using LIME and SHAP]] to generate per-prediction feature-contribution explanations for a representative sample of the classifier's predictions across its validation set, and have a domain expert review whether the highlighted contributing features make evidentiary sense for the classification task at hand. Where LIME and SHAP explanations disagree meaningfully about a feature's importance, or where either tool highlights an unexpected or evidentially meaningless feature as highly influential, treat this as a signal warranting further investigation (retraining with a corrected dataset, or feature engineering) before the model is relied upon operationally. For case-specific predictions offered as evidence, generate and retain the corresponding explanation alongside the prediction, so the reasoning is available for review or challenge.

## References

- [DFCite-2119] "Towards a unified XAI-based framework for digital forensic investigations", FSI: Digital Investigation 48, 2024.

---
id: DFT-2097
type: technique
name: Generate explainable predictions for a digital-forensic AI classifier using LIME and SHAP
description: Apply model-agnostic explainable-AI (XAI) tools -- LIME (Local Interpretable Model-agnostic Explanations) and SHAP (SHapley Additive exPlanations) -- to a black-box machine-learning classifier used in a digital forensic investigation (e.g. malware detection from memory artifacts), producing a per-feature contribution breakdown for each individual prediction so an investigator or model developer can verify the classifier's decision relied on evidentially meaningful features rather than a spurious correlation.
objective_ids:
  - DFO-1004
  - DFO-1019
weakness_ids:
  - DFW-2102
aliases:
  - XAI-DF
  - Unified XAI-based framework for digital forensic investigations
source_refs:
  - DFCite-2119
updated_at: 2026-08-16
status: complete
---

# Generate explainable predictions for a digital-forensic AI classifier using LIME and SHAP

## Summary

Machine-learning classifiers are increasingly used in digital forensic tooling (e.g. malware detection, artifact classification) but most operate as black boxes, providing only a final prediction with no account of which input features drove that decision -- a significant problem for evidentiary use, since a court or investigator has no way to assess whether the model's reasoning was evidentially sound. LIME and SHAP are model-agnostic explainability techniques that work with any underlying classifier architecture: LIME builds a locally faithful, interpretable approximation of the model's behavior around a specific prediction, while SHAP assigns each input feature a Shapley-value-based contribution score quantifying how much it pushed the prediction toward or away from the model's baseline output.

## Details

LIME operates by perturbing the input around the specific instance being explained (e.g. slightly varying feature values) and fitting a simple, interpretable model (such as a linear model) to the black-box classifier's predictions on these perturbed samples, producing a local explanation of which features mattered most for that specific prediction, without needing access to the target model's internal architecture or training process. SHAP instead computes each feature's Shapley value -- a concept from cooperative game theory that fairly distributes credit for a prediction's deviation from a baseline average among all contributing features, accounting for feature interactions -- providing both per-prediction (local) and aggregate (global) feature-importance summaries. Applying both tools to the same digital-forensic classifier and comparing their explanations provides two independent perspectives on the model's decision process, since LIME and SHAP make different underlying assumptions and can occasionally disagree about a given feature's relative importance, which itself can be a useful diagnostic signal warranting closer manual investigation.

## Examples

- The related literature includes a well-known cautionary tale directly relevant to this technique's motivation: a computer-vision system reportedly trained to classify military tanks was later found to have learned to distinguish images based on background sky brightness (correlated with which archive each training image came from) rather than any feature of the tank itself, illustrating how a black-box classifier can achieve high accuracy on a test set while relying on an evidentially meaningless spurious correlation -- exactly the failure mode LIME/SHAP explanation is intended to surface before such a model is relied upon operationally.
- Applied to a malware-detection classifier operating on memory-forensics-derived features, SHAP's global feature-importance summary and LIME's per-instance local explanations were used together to verify which specific extracted features (e.g. specific memory artifact patterns) most influenced the classifier's malicious/benign predictions.

## Related Objectives

- `DFO-1004` Conduct research
- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Black-box AI classifiers used in digital forensic investigations provide no way to verify predictions rely on evidentially meaningful features]]

## References

- [DFCite-2119] "Towards a unified XAI-based framework for digital forensic investigations", FSI: Digital Investigation 48, 2024.

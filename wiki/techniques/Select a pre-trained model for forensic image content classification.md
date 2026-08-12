---
id: DFT-1038
type: technique
name: Select a pre-trained model for forensic image content classification
description: Build a digital forensic image-classification tool by directly integrating an existing general-purpose, pre-trained computer vision model (rather than training or fine-tuning a new one), selecting among candidate models using a weighted decision matrix built from forensically relevant performance metrics rather than published general-purpose benchmark accuracy alone.
objective_ids:
  - DFO-1012
weakness_ids:
  - DFW-1039
aliases:
  - Pre-trained model selection for forensic image content classification
source_refs:
  - DFCite-1029
updated_at: 2026-08-09
status: complete
---

# Select a pre-trained model for forensic image content classification

## Summary

Because most forensic investigation teams lack dedicated data-science expertise to train or fine-tune custom computer vision models, this approach instead selects the best-suited model from several freely available, pre-trained (e.g., ImageNet-trained) candidates and integrates it as-is into a forensic triage tool. Model selection uses a decision matrix prioritizing metrics that matter for realistic, imbalanced forensic data — recall ranked above false-positive rate, which is ranked above precision — over the top-K accuracy figures typically reported in general-purpose computer vision benchmarks.

## Details

Candidate pre-trained models are first evaluated on a balanced, forensically-labeled dataset (e.g., annotated gun/not-gun images) and ranked via a decision matrix weighting recall, false positive rate, precision, processing time, and Matthew's Correlation Coefficient (MCC, preferred over F-measure for its robustness to class imbalance and interpretability). The top-ranked model is then validated against a second, more realistically imbalanced dataset (mirroring the low base-rate of relevant content typical in real forensic acquisitions) before being integrated into a prototype tool and evaluated for usability (e.g., via the System Usability Scale) with practicing forensic examiners, following the design science research methodology's problem-identification, development, demonstration, and evaluation steps.

## Examples

- Evaluating InceptionV3, Xception, ResNet, and VGG16 (all pre-trained on ImageNet, used without fine-tuning) for handgun image classification: InceptionV3 was selected via the decision matrix (recall 1.00, FPR 0.19 on the balanced dataset) and achieved recall of 0.9847 with accuracy 0.8400 on a highly imbalanced 1.10%-positive test dataset.

## Related Objectives

- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Pre-trained image classifiers trained on clean data misclassify occluded or filtered forensic images]]

## References

- [DFCite-1029] Del Mar-Raave et al., 2021, "A machine learning-based forensic tool for image classification - A design science approach", FSI: Digital Investigation 38.

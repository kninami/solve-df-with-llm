---
id: LWM-1039
type: mitigation
name: Validate pre-trained classifiers against occluded and filtered forensic images before deployment
source_refs:
  - LWCite-1029
updated_at: 2026-08-09
status: complete
---

# Validate pre-trained classifiers against occluded and filtered forensic images before deployment

## Summary

Before deploying a pre-trained image classifier for forensic evidentiary triage, deliberately test it against a validation set that includes occluded, partially framed, and filtered (e.g., black-and-white) images representative of real-world acquisition conditions, rather than relying only on its performance on clean, curated data.

## Addresses

- [[weaknesses/Pre-trained image classifiers trained on clean data misclassify occluded or filtered forensic images]]

## How To Apply

When constructing or selecting a validation dataset for a forensic image-classification tool, deliberately include a representative proportion of occluded, partial, and filter-altered images (matching conditions plausible for the target evidence type), not only clean, well-framed examples. If false negatives on these degraded-condition images exceed an acceptable threshold, plan to fine-tune or re-train the model using additional examples of these conditions before relying on the tool's output as comprehensive for evidentiary triage, and communicate the known gap to examiners in the interim.

## References

- [LWCite-1029] Del Mar-Raave et al., 2021, "A machine learning-based forensic tool for image classification - A design science approach", FSI: Digital Investigation 38.

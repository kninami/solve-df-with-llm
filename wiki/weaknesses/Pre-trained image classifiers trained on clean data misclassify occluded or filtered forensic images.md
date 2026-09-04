---
id: LWW-1039
type: weakness
name: Pre-trained image classifiers trained on clean data misclassify occluded or filtered forensic images
description: A general-purpose pre-trained image classifier, evaluated without modification against forensically realistic images containing occlusion, partial framing, or a black-and-white filter, produces a measurable increase in false negatives, since the training data the model originally learned from did not represent these degraded, real-world-acquisition conditions.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1039
source_refs:
  - LWCite-1029
updated_at: 2026-08-09
status: complete
---

# Pre-trained image classifiers trained on clean data misclassify occluded or filtered forensic images

## Summary

In the study's prototype evaluation phase (Dataset 3), the investigators discovered after the fact that the unbalanced, realistic test dataset contained occluded images, partial images, and images with a black-and-white filter, and that "images with the said filter, in particular, were classified wrongly by the model," causing an increase in undesired false negatives (a gun predicted as a non-gun) that "lowered the metrics dramatically" relative to the model's performance on the earlier, cleaner evaluation and selection datasets.

## Why It Matters

Real-world forensic images recovered from a seized device are far more likely than a curated benchmark dataset to include exactly these degraded conditions — a partially obscured weapon in a photo, a black-and-white security camera still, or a cropped image — meaning a classifier's benchmark-reported accuracy can substantially overstate its real-world reliability for evidentiary triage. Because these false negatives mean relevant images are missed rather than merely mislabeled among flagged results, an investigator relying on the tool's output alone could fail to surface genuinely relevant evidence without realizing coverage was incomplete.

## Related Mitigations

- [[mitigations/Validate pre-trained classifiers against occluded and filtered forensic images before deployment]]

## Used By

- [[techniques/Select a pre-trained model for forensic image content classification]]

## References

- [LWCite-1029] Del Mar-Raave et al., 2021, "A machine learning-based forensic tool for image classification - A design science approach", FSI: Digital Investigation 38.

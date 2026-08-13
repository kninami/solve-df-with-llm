---
id: DFT-1123
type: technique
name: Estimate victim age in indecent images using binary child-adult classification
description: Classify a facial image as depicting a child or an adult using a fine-tuned deep convolutional network, rather than predicting a specific age number or age band, to triage suspected indecent images of children (IIoC) during a digital forensic investigation.
objective_ids:
  - DFO-1003
weakness_ids:
  - DFW-1127
aliases:
  - Binary child/adult deep-learning age classification for IIoC triage
  - ResNet50 IIoC age triage
source_refs:
  - DFCite-1122
updated_at: 2026-08-12
status: complete
---

# Estimate victim age in indecent images using binary child-adult classification

## Summary

To speed up age detection in cases suspected of containing indecent images of children (IIoC) and reduce the manual review workload on investigators, facial images can be screened using a deep-learning model. Comparing binary classification, multi-class age-group classification, and continuous-age regression across four pre-trained CNN architectures found binary child/adult classification to be the most accurate and forensically reliable strategy.

## Details

The comparative evaluation fine-tunes VGG16, ResNet50, InceptionV3, and Xception on a combined public face-image dataset (approximately 20,806 images for the binary/multi-class adult dataset) under each of three prediction strategies. Binary classification consistently and substantially outperformed the other two strategies: ResNet50 achieved 91.70% accuracy, 91.70% recall, and 91.50% precision on unseen test images, with high recall and precision indicating few false positives or negatives. Regression prediction achieved its lowest mean-absolute-error around age 35 but could not reliably detect child images at all, and multi-class age-group classification (ResNet50: 69% accuracy) offered no advantage over binary classification while adding age-band granularity that the underlying models could not support reliably. Because a missed child image is operationally far more costly than a false alarm on an adult image, the child-class error rate specifically (not overall accuracy) should drive model selection for this application.

## Examples

- ResNet50 binary classification reached 91.70% accuracy on unseen test images with an error rate of only 0.080 for the child class, versus InceptionV3 (the worst-performing model), which reached a 0.202 error rate on the child class despite training/validation accuracy above 80%.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Regression and multi-class age-estimation models under-detect child images despite reasonable aggregate accuracy]]

## References

- [DFCite-1122] Roopak et al., 2023, "Comparison of deep learning classification models for facial image age estimation in digital forensic investigations", FSI: Digital Investigation 47, 301637.

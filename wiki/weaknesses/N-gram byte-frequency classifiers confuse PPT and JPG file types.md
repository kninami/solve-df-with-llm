---
id: DFW-1005
type: weakness
name: N-gram byte-frequency classifiers confuse PPT and JPG file types
description: Neural network and SVM classifiers trained on n-gram byte frequency distributions consistently misclassify PowerPoint (.ppt) files as JPEG images and vice versa, across independent studies and multiple classifier types.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1005
source_refs:
  - DFCite-1003
updated_at: 2026-08-09
status: complete
---

# N-gram byte-frequency classifiers confuse PPT and JPG file types

## Summary

Across every tested configuration (neural network n=1/n=2, SVM with linear and RBF kernels at n=1/n=2), `.ppt` files showed the lowest per-type classification accuracy, most often being confused with `.jpg`, and `.jpg` files showed a reciprocal tendency to be misclassified as `.ppt`. This same PPT/JPG confusion pattern was independently reported in a separate study with a different dataset and feature set, suggesting the two formats share statistically similar byte-frequency structure (likely because legacy `.ppt` files commonly embed JPEG image streams).

## Why It Matters

A file-type identification tool relying solely on n-gram byte-frequency features can misdirect an investigation -- e.g., presenting an embedded or spoofed PowerPoint file as an image, or vice versa -- when the classifier's confusion is not otherwise flagged. Since this weakness recurs across independent studies and classifier families rather than being an artifact of one dataset, it represents a structural limitation of pure byte-frequency n-gram analysis rather than a tunable hyperparameter issue.

## Related Mitigations

- [[mitigations/Validate ambiguous n-gram file-type classifications with signature-based verification]]

## Used By

- [[techniques/Identify file types using n-gram analysis]]

## References

- [DFCite-1003] Sester et al., 2021, "A comparative study of support vector machine and neural networks for file type identification using n-gram analysis", FSI: Digital Investigation 36.

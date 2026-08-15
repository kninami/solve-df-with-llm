---
id: DFT-1005
type: technique
name: Identify file types using n-gram analysis
description: Classify unknown file fragments by type using n-gram (byte frequency distribution) features fed into a statistical or machine-learning classifier, independent of which specific classifier algorithm is used.
objective_ids:
  - DFO-1002
weakness_ids:
  - DFW-1005
  - DFW-2012
aliases:
  - N-gram-based file type identification
  - N-gram SVM file type identification
  - n-gram file type identification
source_refs:
  - DFCite-1003
  - DFCite-2012
updated_at: 2026-08-14
status: complete
---

# Identify file types using n-gram analysis

## Summary

A file (or fragment) is converted into a normalized n-gram byte frequency distribution (e.g., monogram n=1 or bigram n=2), which is fed into a classifier trained per file-type. Compared across csv, doc, jpg, ppt, txt, and xls file types on the public RealDC corpus, a linear-kernel SVM using monograms achieved the highest overall accuracy (91.49%), outperforming both an RBF-kernel SVM and a comparable multi-layer neural network in most configurations — the underlying n-gram feature representation, not the specific classifier, is the reusable core of the technique.

## Details

Each file is truncated to remove the header/magic-byte region before analysis, so classification relies purely on content statistics rather than signature bytes. The byte frequency distribution is normalized to sum to one, then used as a feature vector for whichever classifier is chosen (SVM with a linear or RBF kernel, and multi-layer neural networks, have both been evaluated). Increasing n from 1 to 2 improved a linear-kernel SVM only marginally and degraded it in one configuration, indicating diminishing returns from increasing n without addressing the method's exponential scalability cost as n grows.

## Examples

- RealDC corpus (Carnegie Mellon Digital Corpora, govdocs1 subset): linear-kernel SVM, n=1, 5241 test files, 91.49% overall classification accuracy.

## Related Objectives

- `DFO-1002` Extract data from specific formats

## Related Weaknesses

- [[weaknesses/N-gram byte-frequency classifiers confuse PPT and JPG file types]]
- [[weaknesses/ML-based file fragment classifiers are vulnerable to byte-level adversarial perturbations]]

## References

- [DFCite-1003] Sester et al., 2021, "A comparative study of support vector machine and neural networks for file type identification using n-gram analysis", FSI: Digital Investigation 36.
- [DFCite-2012] Mary and Sreeja, 2026, "Adversarial shadows in digital forensics: New insights into file fragment classification vulnerabilities and defenses", IEEE Access 14 — surveys how byte-level statistical classifiers of this kind (n-gram/byte-frequency-based) are specifically susceptible to statistically-stealthy adversarial byte manipulation.

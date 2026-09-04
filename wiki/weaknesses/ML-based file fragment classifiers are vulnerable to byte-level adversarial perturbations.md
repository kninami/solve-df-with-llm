---
id: LWW-2012
type: weakness
name: ML-based file fragment classifiers are vulnerable to byte-level adversarial perturbations
description: Machine-learning and deep-learning file fragment classifiers that rely on statistical byte-level features (byte-frequency histograms, entropy, n-gram distributions) can be induced to misclassify a fragment's file type through deliberately crafted, format-preserving byte-level perturbations such as bit-flipping, byte substitution, byte reordering, entropy manipulation, and padding manipulation.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-2012
source_refs:
  - LWCite-2012
updated_at: 2026-08-14
status: partial
---

# ML-based file fragment classifiers are vulnerable to byte-level adversarial perturbations

## Summary

Because file fragment classification (FFC) models operate on raw byte streams with no semantic structure, and typically exclude headers/footers from training data to avoid overfitting to signature bytes, they classify based almost entirely on learned statistical regularities such as byte-frequency distributions, entropy, and n-gram patterns. The source survey shows that a range of byte-level manipulation strategies - bit-flipping in low-entropy regions, byte substitution/replacement, byte reordering (for sequence-aware models), entropy manipulation via selective compression/decompression, and padding/structural insertion in slack space or unused sections - can shift these statistics enough to flip a classifier's output while keeping the fragment format-plausible and statistically stealthy (within benign-looking entropy/n-gram ranges). Low-entropy, structured fragments are most vulnerable; highly entropic (compressed/encrypted) fragments are comparatively more resistant since randomness limits the attacker's statistical leverage.

## Why It Matters

An adversary who anticipates automated ML-based file-type triage can deliberately mislabel fragments belonging to executables, encrypted volumes, or contraband file types as benign document or image types, causing them to be filtered out, deprioritized, or missed entirely by forensic tools that rely on automated classification to scope investigator attention. Because file fragments are not human-interpretable the way images or natural-language text are, an investigator has no straightforward visual or readability cue that a classification has been adversarially manipulated, making this a particularly hard-to-detect anti-forensic vector.

## Related Mitigations

- [[mitigations/Apply constraint-preserving adversarial training and confidence-based escalation to ML file fragment classifiers]]

## Used By

- [[techniques/Identify file types using n-gram analysis]]

## References

- [LWCite-2012] Mary and Sreeja, 2026 — Sections III-V present the FFC-specific adversarial taxonomy, byte-level perturbation techniques (Table 3), and their differential effectiveness against low- vs. high-entropy fragments.

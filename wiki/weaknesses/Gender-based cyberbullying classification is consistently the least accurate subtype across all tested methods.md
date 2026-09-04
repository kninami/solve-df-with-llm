---
id: LWW-2045
type: weakness
name: Gender-based cyberbullying classification is consistently the least accurate subtype across all tested methods
description: Across every classifier and experiment tested in the source paper, including the proposed neutrosophic-MLP model, comparison ML baselines, a fuzzy-logic variant, and a BERT-augmented variant, the "gender" cyberbullying subtype consistently shows the lowest precision, recall, and F1-score of the five classified subtypes, indicating a systematic, method-independent difficulty distinguishing gender-based cyberbullying from other categories.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-2045
source_refs:
  - LWCite-2046
updated_at: 2026-08-14
status: partial
---

# Gender-based cyberbullying classification is consistently the least accurate subtype across all tested methods

## Summary

Across the source paper's Table 1 (proposed model: gender precision 0.89, recall 0.92, F1 0.91 - the lowest of the five classes on Dataset 1), Table 2 (RF: 0.92/0.84/0.88; LR: 0.97/0.74/0.84; SVM: 0.83/0.81/0.82 - gender lowest or near-lowest in every algorithm), Table 4 (fuzzy-logic comparator: 0.90/0.87/0.89), and Table 5 (BERT-augmented variant: 0.90/0.92/0.91), the gender subtype's classification quality lags every other cyberbullying subtype (age, ethnicity, religion, other) in every configuration tested, regardless of which classification technique or preprocessing pipeline is used.

## Why It Matters

Because this weakness recurs across every method tested in the same study rather than being specific to one algorithm, it points to something inherent in how gender-based cyberbullying is expressed or labeled in the underlying data (e.g. greater linguistic overlap with other subtypes, or labeling ambiguity) rather than a fixable weakness of any one classifier. An investigator relying on an automated fine-grained cyberbullying classification for a gender-based harassment case should expect materially lower classification reliability for that specific subtype than for others, and should not assume improving the classifier algorithm alone will resolve the gap.

## Related Mitigations

- [[mitigations/Apply targeted oversampling and route low-confidence gender-subtype classifications to manual review]]

## Used By

- [[techniques/Classify social media cyberbullying types using neutrosophic-logic-enhanced MLP classification]]

## References

- [LWCite-2046] Ibrahim et al., 2024 — Tables 1, 2, 4, and 5 report the per-class precision/recall/F1 figures discussed above across every method variant tested in the paper.

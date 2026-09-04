---
id: LWW-2068
type: weakness
name: Inter-annotator disagreement in manually categorizing dark web content degrades the reliability of ML classifiers trained on it
description: Different human investigators annotating and categorizing the same dark web content do not always agree, and since these manual categorizations become the ground-truth training data for downstream ML classifiers, disagreement between annotators is a source of label noise that propagates into the reliability of any automated classification built on it.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-2069
source_refs:
  - LWCite-2072
updated_at: 2026-08-15
status: complete
---

# Inter-annotator disagreement in manually categorizing dark web content degrades the reliability of ML classifiers trained on it

## Summary

When two investigators independently categorized the same 95-page demonstration data set, the measured Cohen's kappa inter-annotator agreement was 0.84 overall, but dropped notably for specific categories: the annotators disagreed on 5 of 21 items categorized as "Dark Marketplace" and 2 of 6 items categorized as "Steroids." Because these manual categorizations directly become the labelled ground-truth training data used to build ML classifiers for automatically categorizing unseen web pages, any systematic disagreement between annotators about what a given category actually means for a piece of content is a source of label noise baked into the resulting classifier.

## Why It Matters

An investigator who trusts a classifier's automated categorization of new dark web content as reliable, without first checking the inter-annotator agreement score for the categories involved, risks acting on categorizations trained from inconsistently-labelled ground truth — particularly for ambiguous or borderline categories where human annotators themselves disagreed most, which is exactly where an automated classifier is also likely to be least reliable.

## Related Mitigations

- [[mitigations/Calculate and review inter-annotator agreement before relying on dark web content categorizations or classifiers trained from them]]

## Used By

- [[techniques/Collect and annotate dark web content for investigation using a forensically sound, hash-verified toolset]]

## References

- [LWCite-2072] Bergman & Popov, 2022, "The Digital Detective's Discourse: A Toolset for Forensically Sound Collaborative Dark Web Content Annotation and Collection", JDFSL 17(5). Reports the 0.84 overall Cohen's kappa score and identifies the "Dark Marketplace" and "Steroids" categories as having the lowest per-category agreement.

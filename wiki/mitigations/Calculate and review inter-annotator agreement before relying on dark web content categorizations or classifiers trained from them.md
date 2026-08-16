---
id: DFM-2069
type: mitigation
name: Calculate and review inter-annotator agreement before relying on dark web content categorizations or classifiers trained from them
source_refs:
  - DFCite-2072
updated_at: 2026-08-15
status: complete
---

# Calculate and review inter-annotator agreement before relying on dark web content categorizations or classifiers trained from them

## Summary

Compute an inter-annotator agreement score (e.g., Cohen's kappa for two annotators) per category when multiple investigators categorize the same dark web content, and treat categories with low agreement as requiring additional review or a clearer category definition before using them — or any classifier trained on them — as a basis for investigative conclusions.

## Addresses

- [[weaknesses/Inter-annotator disagreement in manually categorizing dark web content degrades the reliability of ML classifiers trained on it]]

## How To Apply

Where more than one investigator annotates overlapping dark web content, periodically calculate the inter-annotator agreement score per category and flag categories falling below an agreed threshold for review; refine ambiguous category definitions or require a third annotator's tie-breaking judgment for low-agreement categories before treating them as reliable ground truth. When a classifier trained on the annotation data set outputs a categorization for new content, weight confidence in that output by the training data's per-category agreement score, and manually review classifier outputs in categories known to have had low inter-annotator agreement rather than treating them as equally reliable to high-agreement categories.

## References

- [DFCite-2072] Bergman & Popov, 2022, "The Digital Detective's Discourse: A Toolset for Forensically Sound Collaborative Dark Web Content Annotation and Collection", JDFSL 17(5). Implements Cohen's kappa inter-annotator-agreement calculation as a built-in D3-Analyser component specifically to evaluate categorization reliability before use.

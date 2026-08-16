---
id: DFW-2119
type: weakness
name: Low-recall evidence-category image classifiers used for triage miss a substantial proportion of relevant images
description: Specialized image classifiers used to triage large evidence collections into categories (e.g. firearms, ammunition, identity documents) can have recall in only the 0.6-0.8 range for some object subcategories, meaning a meaningful proportion of images genuinely containing the target evidence type are never flagged for investigator review at all, independent of any subsequent manual review step.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2120
source_refs:
  - DFCite-2139
updated_at: 2026-08-16
status: complete
---

# Low-recall evidence-category image classifiers used for triage miss a substantial proportion of relevant images

## Summary

Evaluated firearm, ammunition, and identity-document classifiers each showed precision and recall in the 0.6-0.8 range depending on the specific object subcategory being detected -- meaning that for the lower end of this range, roughly one in three or more genuinely relevant images can fail to be flagged by the classifier at all, receiving no priority elevation for investigator review.

## Why It Matters

Because a triage pipeline's entire purpose is to direct limited investigator attention toward the most relevant images within a large collection, a classifier's recall gap directly translates into evidence that may never be manually reviewed if an investigator relies solely on classifier-flagged images rather than examining the full collection. Unlike a false positive (which merely costs review time on an irrelevant image), a false negative in this context represents evidence silently never surfacing at all -- a risk an investigator cannot detect from the triage pipeline's own output, since a missed image looks identical to a genuinely irrelevant one from the investigator's vantage point.

## Related Mitigations

- [[mitigations/Treat microservice classifier triage output as prioritization only and periodically sample unflagged images for manual review]]

## Used By

- [[techniques/Triage large-scale criminal evidence image collections using a microservice-based multi-classifier pipeline]]

## References

- [DFCite-2139] "Using micro-services and artificial intelligence to analyze images in criminal evidences", FSI: Digital Investigation 48, 2024.

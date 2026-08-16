---
id: DFM-2120
type: mitigation
name: Treat microservice classifier triage output as prioritization only and periodically sample unflagged images for manual review
source_refs:
  - DFCite-2139
updated_at: 2026-08-16
status: complete
---

# Treat microservice classifier triage output as prioritization only and periodically sample unflagged images for manual review

## Summary

Treat a microservice-based image-triage pipeline's classifier flags as a prioritization aid that speeds up finding relevant images, not as a filter that reliably identifies every relevant image, and periodically sample unflagged images for manual review to catch the classifiers' known recall gap.

## Addresses

- [[weaknesses/Low-recall evidence-category image classifiers used for triage miss a substantial proportion of relevant images]]

## How To Apply

Where case time and resources allow, review flagged images first (as the highest-likelihood subset) but also periodically sample a proportion of unflagged images for manual spot-checking, particularly for the object subcategories a given classifier is known to have lower recall against. Where a case's outcome depends heavily on completeness of a specific evidence category (e.g. confirming the absence of firearm imagery, not merely its presence), do not rely on the classifier's negative results alone; supplement with targeted manual review appropriate to the case's stakes. Track and periodically re-evaluate each microservice classifier's measured precision/recall as new evaluation data becomes available, and prioritize retraining or replacing whichever classifier's recall gap poses the greatest practical risk for the agency's typical casework.

## References

- [DFCite-2139] "Using micro-services and artificial intelligence to analyze images in criminal evidences", FSI: Digital Investigation 48, 2024.

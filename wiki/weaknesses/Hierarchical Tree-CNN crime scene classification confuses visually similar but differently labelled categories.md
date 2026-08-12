---
id: DFW-1095
type: weakness
name: Hierarchical Tree-CNN crime scene classification confuses visually similar but differently labelled categories
description: Because the Tree-CNN model classifies images through a hierarchy of parent nodes before reaching more specific child categories, an image can be misclassified at a high-level parent node when its content closely visually resembles a different category with similar visual content (e.g. a packaging-logo image versus a concealment image), causing the misclassification to propagate and produce a false result at the final, specific category level.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1095
source_refs:
  - DFCite-1087
updated_at: 2026-08-10
status: complete
---

# Hierarchical Tree-CNN crime scene classification confuses visually similar but differently labelled categories

## Summary

The paper illustrates this directly with an example image assigned to the PACKLOGO (Packaging logo) category on one side and CONC (Concealment) on the other, "both having very similar image content" — demonstrating that visual similarity between semantically distinct categories can defeat the classifier regardless of which specific category boundary is actually being tested. The authors note that greater attention at the parent-node model specifically could help reduce false positives caused by this kind of high-level misclassification.

## Why It Matters

A practitioner using the Tree-CNN model to triage casework images could have an image assigned to the wrong high-level category early in the classification hierarchy, causing it to be filed or reviewed under an incorrect workflow — this risk is systematic for categories that happen to share visual characteristics (like packaging materials that could also represent concealment methods), not a rare or random error, meaning it will recur predictably wherever such visually-overlapping category pairs exist in the taxonomy.

## Related Mitigations

- [[mitigations/Manually review Tree-CNN classifications for visually similar category pairs and use the model for semi-automated triage only]]

## Used By

- [[techniques/Classify crime scene images for casework triage using Tree-CNN and BoVW-SVM]]

## References

- [DFCite-1087] Abraham et al., 2021, "Automatically classifying crime scene images using machine learning methodologies", FSI: Digital Investigation 39.

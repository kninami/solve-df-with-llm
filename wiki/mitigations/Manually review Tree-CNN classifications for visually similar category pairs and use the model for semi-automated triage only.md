---
id: DFM-1095
type: mitigation
name: Manually review Tree-CNN classifications for visually similar category pairs and use the model for semi-automated triage only
source_refs:
  - DFCite-1087
updated_at: 2026-08-10
status: complete
---

# Manually review Tree-CNN classifications for visually similar category pairs and use the model for semi-automated triage only

## Summary

Use the Tree-CNN crime scene image classifier as a semi-automated triage aid requiring practitioner review, not a fully automated classification system, with particular attention to categories known or suspected to share visually similar content.

## Addresses

- [[weaknesses/Hierarchical Tree-CNN crime scene classification confuses visually similar but differently labelled categories]]

## How To Apply

Identify which category pairs in the taxonomy are visually similar in content (e.g. packaging materials versus concealment methods) and flag classifications into or near those categories for mandatory manual review rather than automatic acceptance. Treat the model's output as a practitioner-assisting first pass across the full taxonomy, not a substitute for review, until parent-node-level accuracy is further improved.

## References

- [DFCite-1087] Abraham et al., 2021, "Automatically classifying crime scene images using machine learning methodologies", FSI: Digital Investigation 39.

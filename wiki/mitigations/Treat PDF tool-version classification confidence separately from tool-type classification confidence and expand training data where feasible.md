---
id: DFM-2100
type: mitigation
name: Treat PDF tool-version classification confidence separately from tool-type classification confidence and expand training data where feasible
source_refs:
  - DFCite-2116
updated_at: 2026-08-16
status: complete
---

# Treat PDF tool-version classification confidence separately from tool-type classification confidence and expand training data where feasible

## Summary

When reporting a byte-frequency-and-entropy classification result, explicitly distinguish whether the finding is a tool-type identification (high confidence, 90%+ accuracy achievable) or a tool-version identification (materially lower confidence, roughly 60-85% depending on model), and expand the training dataset for the specific version pair in question where a version-level conclusion is important to the case.

## Addresses

- [[weaknesses/PDF creator-tool classification accuracy is markedly lower for version-level identification than tool-level identification]]

## How To Apply

Use [[techniques/Identify the creator tool of a PDF document using byte-frequency and entropy machine-learning classification]] for tool-type identification with confidence in its high accuracy, but when a case specifically requires distinguishing between versions of the same tool, report the correspondingly lower measured accuracy for that classification task rather than implying version-level and tool-level findings carry equal reliability. Where feasible, collect and label additional documents known to have been created with the specific tool versions relevant to the case to retrain or fine-tune the classifier with a larger, more balanced sample per version, since the accuracy gap observed in the source study was attributed in part to limited per-version training data rather than an inherent ceiling on what the byte-level features can distinguish.

## References

- [DFCite-2116] Zia and Adedayo, 2025, "Tool type identification for forensic digital document examination", FSI: Digital Investigation 54, 301972.

---
id: DFM-1121
type: mitigation
name: Aggregate sufficient combined text length and report a confidence level tied to the validated accuracy curve before relying on HC-based authorship verification
source_refs:
  - DFCite-1115
updated_at: 2026-08-12
status: complete
---

# Aggregate sufficient combined text length and report a confidence level tied to the validated accuracy curve before relying on HC-based authorship verification

## Summary

Before treating an HC-based authorship verification result as reliable, aggregate enough combined text from both accounts to reach a length interval with validated accuracy well above chance, and report the result together with the accuracy/F1 expected at that specific combined text length rather than as an undifferentiated pass/fail decision.

## Addresses

- [[weaknesses/HC-based authorship verification accuracy is unreliable for short text samples]]

## How To Apply

Before running the comparison, sum the character length of all available text from both accounts and check it against the accuracy achieved at that length in the algorithm's validated accuracy table; if the combined length falls in a low-reliability interval (roughly below 10,000-15,000 characters based on the source study), either collect additional text (further posts, comments, or messages) before concluding, or explicitly caveat the result's low reliability in the investigation report rather than presenting it as a firm attribution.

## References

- [DFCite-1115] Le et al., 2021, "ChunkedHCs algorithm for authorship verification problems: Reddit case study", FSI: Digital Investigation 37.

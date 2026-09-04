---
id: LWM-1076
type: mitigation
name: Treat DTW signature-verification output as advisory and never let it override an examiner's independent qualitative judgment
source_refs:
  - LWCite-1066
updated_at: 2026-08-10
status: complete
---

# Treat DTW signature-verification output as advisory and never let it override an examiner's independent qualitative judgment

## Summary

Use the DTW-based similarity score as one additional input to a forensic handwriting examiner's determination, not as a standalone verdict, and be aware the method's false-negative rate for imitations (roughly 21.5%) is higher than its false-positive rate for genuine signatures.

## Addresses

- [[weaknesses/DTW-based signature verification misclassifies roughly one in five imitated signatures as genuine]]

## How To Apply

Report the DTW similarity result alongside, not in place of, the examiner's own qualitative traditional evaluation, and require the examiner to independently justify any case where the two disagree rather than automatically deferring to the numerical score, especially when the score indicates "genuine" (the error mode where the method is weakest).

## References

- [LWCite-1066] Mazzolini et al., 2021, "An easy-to-explain decision support framework for forensic analysis of dynamic signatures", FSI: Digital Investigation 38.

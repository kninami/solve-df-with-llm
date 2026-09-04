---
id: LWM-1200
type: mitigation
name: Combine multiple magic-number-based file type identification tools to raise identification accuracy
source_refs:
  - LWCite-1211
updated_at: 2026-08-13
status: complete
---

# Combine multiple magic-number-based file type identification tools to raise identification accuracy

## Summary

Rather than trusting a single file type identification tool, run a primary magic-number-based tool and fall back to a second, independent magic-number-based tool whenever the first reports the type as unknown, which raises overall accuracy and coverage beyond either tool alone while remaining robust to extension tampering.

## Addresses

- [[weaknesses/Failure to rely on magic-number signatures causes file type identification tools to be defeated by extension tampering]]

## How To Apply

Before adopting a file type identification tool, verify its actual mechanism (content-signature-based versus extension-dependent) rather than trusting its stated purpose or reputation, using a test set with extensions deliberately altered or removed. Where feasible, combine two independently maintained magic-number-based tools by applying the more accurate one first and using the second only as a fallback for files the first cannot classify (the GreycFiletype combination of Fidentify and ForENSIque raised accuracy from 94.4% to 96.2% on a 17,500-file dataset, and from 98.1% to 98.3% on a 1,000,000-file dataset, at some additional computation-time cost).

## References

- [LWCite-1211] Dubettier et al., 2023, "File type identification tools for digital investigations", FSI: Digital Investigation 46, 301574.

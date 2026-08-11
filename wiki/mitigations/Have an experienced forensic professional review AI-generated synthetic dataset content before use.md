---
id: DFM-1069
type: mitigation
name: Have an experienced forensic professional review AI-generated synthetic dataset content before use
source_refs:
  - DFCite-1059
updated_at: 2026-08-10
status: complete
---

# Have an experienced forensic professional review AI-generated synthetic dataset content before use

## Summary

Do not adopt AI-generated storyboard or dataset content directly; have an experienced forensic professional review it for completeness and plausibility, since the toolchain's own automated checks only catch syntactic errors, not factual or contextual implausibility.

## Addresses

- [[weaknesses/LLM-generated synthetic mobile forensic dataset content can be factually incorrect or incomplete without expert validation]]

## How To Apply

Route every AI-generated storyboard or injected content set through a human-in-the-loop review step performed by someone with forensic domain expertise before the resulting dataset is used for training or validating tools/methods, removing or correcting any implausible, factually incorrect, or biased content identified during review.

## References

- [DFCite-1059] Pawlaszczyk et al., 2025, "AI-driven dataset creation in mobile forensics using LLM-based storyboards", FSI: Digital Investigation 55.

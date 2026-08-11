---
id: DFM-1023
type: mitigation
name: Prefer non-destructive ISP extraction and reserve chip-off for when ISP access is unavailable
source_refs:
  - DFCite-1016
updated_at: 2026-08-09
status: complete
---

# Prefer non-destructive ISP extraction and reserve chip-off for when ISP access is unavailable

## Summary

Before resorting to destructive chip-off, evaluate whether the target flash chip exposes sufficient in-system programming (ISP) test points to dump its contents non-destructively; only proceed to chip-off when ISP access points are absent, insufficient (e.g., too few exposed I/O lines for the required protocol), or otherwise non-functional, and document the decision.

## Addresses

- [[weaknesses/Chip-off flash extraction is irreversible and precludes non-destructive re-examination]]

## How To Apply

Inspect and, where necessary, X-ray the target board to determine whether the flash chip's required interface lines (all control, I/O, and power/ground pins needed for the relevant protocol) are exposed at accessible test points — see [[techniques/In-system programming eMMC extraction]] for the non-destructive alternative. Only when this is confirmed insufficient should chip-off proceed, and the decision, along with the specific technical justification (e.g., "only 1 of 8 required I/O lines exposed"), should be documented in the case file given the irreversible nature of the step.

## References

- [DFCite-1016] Barral et al., 2022, "A forensic analysis of the Google Home: repairing compressed data without error correction", FSI: Digital Investigation 42-43.

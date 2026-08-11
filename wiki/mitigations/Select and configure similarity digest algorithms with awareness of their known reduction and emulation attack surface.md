---
id: DFM-1105
type: mitigation
name: Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface
source_refs:
  - DFCite-1100
updated_at: 2026-08-10
status: complete
---

# Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface

## Summary

When selecting or relying on a similarity digest (fuzzy hashing) algorithm for forensic matching, account for its specific known reduction and emulation attack surface based on its internal design characteristics (feature length, mapping function, storing structure, coverage), rather than treating all similarity digest algorithms as equally robust.

## Addresses

- [[weaknesses/Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification]]

## How To Apply

Before relying on a similarity digest match or non-match as significant evidence, identify which specific algorithm produced it and consult its known attack surface (e.g. minimum-commonality thresholds for ssdeep, partial-coverage tolerance for sdhash) to assess how easily a sophisticated adversary could have manipulated the result. Where the stakes warrant it, cross-validate a similarity finding using a second algorithm with a different internal design, since an attack effective against one algorithm's specific characteristics will often not transfer to a structurally different one.

## References

- [DFCite-1100] Martín-Pérez et al., 2021, "Bringing order to approximate matching: Classification and attacks on similarity digest algorithms", FSI: Digital Investigation 36.

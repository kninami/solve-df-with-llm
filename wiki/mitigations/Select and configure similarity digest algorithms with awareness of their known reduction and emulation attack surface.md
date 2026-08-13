---
id: DFM-1105
type: mitigation
name: Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface
source_refs:
  - DFCite-1100
  - DFCite-1209
  - DFCite-1249
updated_at: 2026-08-13
status: complete
---

# Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface

## Summary

When selecting or relying on a similarity digest (fuzzy hashing) algorithm for forensic matching, account for its specific known reduction and emulation attack surface based on its internal design characteristics (feature length, mapping function, storing structure, coverage), rather than treating all similarity digest algorithms as equally robust.

## Addresses

- [[weaknesses/Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification]]

## How To Apply

Before relying on a similarity digest match or non-match as significant evidence, identify which specific algorithm produced it and consult its known attack surface (e.g. minimum-commonality thresholds for ssdeep, partial-coverage tolerance for sdhash) to assess how easily a sophisticated adversary could have manipulated the result. Where the stakes warrant it, cross-validate a similarity finding using a second algorithm with a different internal design, since an attack effective against one algorithm's specific characteristics will often not transfer to a structurally different one. FbHash and its memory-optimized variant [[techniques/Compute a file similarity digest using Bloom-filter-approximated frequency hashing]] (FbHash-E) are a concrete example of a similarity digest family reported resistant to the active reduction/emulation attacks that affect ssdeep, sdhash, LZJD, and mvHash-B, making them a reasonable choice where robustness against a knowledgeable adversary is the primary concern — though FbHash-E's Bloom-filter approximation introduces its own, unrelated accuracy trade-off (see [[weaknesses/Bloom-filter-approximated similarity hashing systematically inflates similarity scores relative to exact frequency calculation]]) that must be accounted for separately. Rather than relying on published attack analyses alone, run a candidate algorithm through [[techniques/Benchmark approximate matching algorithms using an automated test framework]] (FRASHER) to empirically measure its own digest-generation-impediment and digest-comparison-impediment thresholds before selecting it for an operational filter or blacklist.

## References

- [DFCite-1100] Martín-Pérez et al., 2021, "Bringing order to approximate matching: Classification and attacks on similarity digest algorithms", FSI: Digital Investigation 36.
- [DFCite-1209] Singh et al., 2022, "FbHash-E: A time and memory efficient version of FbHash similarity hashing algorithm", FSI: Digital Investigation 41, 301375.
- [DFCite-1249] Göbel et al., 2022, "FRASHER -- A framework for automated evaluation of similarity hashing", FSI: Digital Investigation 42, 301407.

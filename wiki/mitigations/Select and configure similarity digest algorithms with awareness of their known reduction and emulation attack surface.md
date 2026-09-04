---
id: LWM-1105
type: mitigation
name: Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface
source_refs:
  - LWCite-1100
  - LWCite-1209
  - LWCite-1249
  - LWCite-2092
  - LWCite-2131
updated_at: 2026-08-16
status: complete
---

# Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface

## Summary

When selecting or relying on a similarity digest (fuzzy hashing) algorithm for forensic matching, account for its specific known reduction and emulation attack surface based on its internal design characteristics (feature length, mapping function, storing structure, coverage), rather than treating all similarity digest algorithms as equally robust.

## Addresses

- [[weaknesses/Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification]]

## How To Apply

Before relying on a similarity digest match or non-match as significant evidence, identify which specific algorithm produced it and consult its known attack surface (e.g. minimum-commonality thresholds for ssdeep, partial-coverage tolerance for sdhash) to assess how easily a sophisticated adversary could have manipulated the result. Where the stakes warrant it, cross-validate a similarity finding using a second algorithm with a different internal design, since an attack effective against one algorithm's specific characteristics will often not transfer to a structurally different one. FbHash and its memory-optimized variant [[techniques/Compute a file similarity digest using Bloom-filter-approximated frequency hashing]] (FbHash-E) are a concrete example of a similarity digest family reported resistant to the active reduction/emulation attacks that affect ssdeep, sdhash, LZJD, and mvHash-B, making them a reasonable choice where robustness against a knowledgeable adversary is the primary concern — though FbHash-E's Bloom-filter approximation introduces its own, unrelated accuracy trade-off (see [[weaknesses/Bloom-filter-approximated similarity hashing systematically inflates similarity scores relative to exact frequency calculation]]) that must be accounted for separately. Rather than relying on published attack analyses alone, run a candidate algorithm through [[techniques/Benchmark approximate matching algorithms using an automated test framework]] (FRASHER) to empirically measure its own digest-generation-impediment and digest-comparison-impediment thresholds before selecting it for an operational filter or blacklist. If ssdeep specifically is the chosen algorithm, apply the ssdeeper patch set on top of the stock reference implementation before relying on its output for casework: the `-bugfix` modification (removes the last-segment-dropping bug), `-no32lim` (removes the 32-character limit on the second signature, increasing coverage and accuracy at some cost to backward-compatibility with existing hash databases), and, where a higher detection rate matters more than raw comparison speed, `-4b`/`-djb2` (a larger trigger-progression constant and a replacement rolling hash function, together increasing hash reliability); avoid the `-nocommonsub` and `-nopa` optimizations for security-sensitive filtering use cases, since they weaken obfuscation resistance and increase the false-negative rate in exchange for faster comparisons. When using similarity hashing to expand malware-detection coverage or perform family clustering, select the similarity threshold according to the specific task rather than an arbitrary default: a low or loose threshold suits broad triage where missed detections are costlier than false positives, while a high or strict threshold (up to requiring near-exact compatibility) suits specialized remediation contexts where false positives are costly, and report which threshold was used alongside any similarity-derived conclusion so the result's precision/recall trade-off is clear to a reader. Be aware that malware packing reduces (but does not eliminate) similarity-hashing's ability to detect relatedness between a packed sample and its unpacked original, so a low similarity score between two samples one of which is packed should not be treated as ruling out a shared origin.

## References

- [LWCite-1100] Martín-Pérez et al., 2021, "Bringing order to approximate matching: Classification and attacks on similarity digest algorithms", FSI: Digital Investigation 36.
- [LWCite-1209] Singh et al., 2022, "FbHash-E: A time and memory efficient version of FbHash similarity hashing algorithm", FSI: Digital Investigation 41, 301375.
- [LWCite-1249] Göbel et al., 2022, "FRASHER -- A framework for automated evaluation of similarity hashing", FSI: Digital Investigation 42, 301407.
- [LWCite-2092] Jakobs, Lambertz, and Hilgert, 2022, "ssdeeper: Evaluating and improving ssdeep", FSI: Digital Investigation 42, 301402. Source for the specific ssdeep patch-set recommendations (`-bugfix`, `-no32lim`, `-4b`, `-djb2`, and the security trade-offs of `-nocommonsub`/`-nopa`).
- [LWCite-2131] Botacin, Galhardo Moia, and Ceschin, 2021, "Understanding uses and misuses of similarity hashing functions for malware detection and family clustering in actual scenarios", FSI: Digital Investigation 38, 301220. Source for the task-dependent threshold-selection guidance and the malware-packing similarity-reduction caveat.

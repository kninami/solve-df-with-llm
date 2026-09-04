---
id: LWM-1128
type: mitigation
name: Verify per-level-pair accuracy before relying on optimization-level predictions between similarly optimized binaries
source_refs:
  - LWCite-1124
updated_at: 2026-08-12
status: complete
---

# Verify per-level-pair accuracy before relying on optimization-level predictions between similarly optimized binaries

## Summary

Before citing a compiler-provenance classifier's optimization-level prediction as evidence, check the published or independently-measured accuracy for the specific pair of optimization levels being distinguished, since a single headline accuracy figure can mask near-chance performance on harder pairs such as O3 versus Os or O0 versus Os.

## Addresses

- [[weaknesses/Vision-transformer compiler-provenance classifiers cannot reliably distinguish similarly optimized binaries]]

## How To Apply

When reporting or relying on a compiler-optimization-level classification result, state which specific optimization levels were compared and cite the accuracy figure for that specific pair rather than an overall or best-case figure from the source study. Where the compared levels are known to produce similar compiled output (e.g. O3 and Os, both aggressive optimization profiles), treat the classifier's output as low-confidence and seek independent corroborating evidence (such as compiler-specific artifacts, build metadata, or known toolchain fingerprints) before relying on it for attribution conclusions.

## References

- [LWCite-1124] Khan et al., 2024, "Compiler-provenance identification in obfuscated binaries using vision transformers", FSI: Digital Investigation 49, 301764.

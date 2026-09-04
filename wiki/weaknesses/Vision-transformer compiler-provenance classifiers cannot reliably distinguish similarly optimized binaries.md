---
id: LWW-1128
type: weakness
name: Vision-transformer compiler-provenance classifiers cannot reliably distinguish similarly optimized binaries
description: Compiler-provenance classifiers that perform well distinguishing dissimilar optimization levels drop to near-chance accuracy when the compared optimization levels produce similar runtime behavior, such as O3 versus Os or O0 versus Os.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1128
source_refs:
  - LWCite-1124
updated_at: 2026-08-12
status: complete
---

# Vision-transformer compiler-provenance classifiers cannot reliably distinguish similarly optimized binaries

## Summary

While vision-based compiler-provenance classifiers reach 94-98%+ accuracy distinguishing binaries built with clearly different optimization levels (e.g. O0, unoptimized, versus O3, aggressively optimized), performance collapses for optimization-level pairs whose code structure is closer: O3 versus Os accuracy fell to 0.607-0.671 for the best pre-trained models, and for O0 versus Os "none of the classifiers was able to achieve better classification performance," with the best model only "slightly better than the random classifier."

## Why It Matters

An investigator citing this technique's headline accuracy figure (94-98%+) without checking which specific optimization-level pair was being classified would be misled about how reliable a given provenance conclusion actually is. Since the technique is intended to support authorship attribution and malware-origin analysis, an unqualified near-chance result being reported as if it carried the same confidence as an easy-pair result risks an incorrect or unsupportable provenance conclusion being relied upon in an investigation.

## Related Mitigations

- [[mitigations/Verify per-level-pair accuracy before relying on optimization-level predictions between similarly optimized binaries]]

## Used By

- [[techniques/Identify compiler provenance from a binary using a vision transformer classifier]]

## References

- [LWCite-1124] Khan et al., 2024, "Compiler-provenance identification in obfuscated binaries using vision transformers", FSI: Digital Investigation 49, 301764.

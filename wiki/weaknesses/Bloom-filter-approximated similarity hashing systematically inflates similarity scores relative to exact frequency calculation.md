---
id: DFW-1198
type: weakness
name: Bloom-filter-approximated similarity hashing systematically inflates similarity scores relative to exact frequency calculation
description: Replacing an exact cross-corpus document-frequency lookup with a Bloom-filter/clustering approximation, as done to reduce the memory and time cost of similarity hashing, produces similarity scores that are systematically higher on average than the equivalent exact-frequency algorithm would report on the same file pair, requiring a recalibrated match threshold rather than reuse of thresholds validated for the exact-frequency version.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-1198
source_refs:
  - DFCite-1209
updated_at: 2026-08-13
status: complete
---

# Bloom-filter-approximated similarity hashing systematically inflates similarity scores relative to exact frequency calculation

## Summary

Evaluated against its exact-frequency predecessor FbHash on the same test corpus, the Bloom-filter-approximated FbHash-E algorithm reported similarity scores averaging 7.5 points higher and an approximately 3% lower F-score, a systematic (not random) bias attributable to the Bloom filter's clustered, coarser document-frequency buckets replacing exact per-chunk frequency counts; the paper's authors responded by recalibrating the tool's recommended match threshold from 16 to 28.

## Why It Matters

An investigator who applies a similarity-score threshold validated for one similarity hashing algorithm to a different, memory-optimized variant of that same algorithm risks over-matching unrelated files as similar (false positive corroboration) if the variant's approximation systematically inflates scores relative to the original, or under-matching related files if a threshold is set defensively too high without accounting for the shift. Because the bias is a structural property of the approximation technique rather than a bug specific to one implementation, it should be expected whenever a Bloom-filter or clustering-based frequency approximation is substituted into a similarity-hashing pipeline, not just for this specific tool.

## Related Mitigations

- [[mitigations/Recalibrate similarity-score thresholds for Bloom-filter-approximated similarity hashing tools]]

## Used By

- [[techniques/Compute a file similarity digest using Bloom-filter-approximated frequency hashing]]

## References

- [DFCite-1209] Singh et al., 2022, "FbHash-E: A time and memory efficient version of FbHash similarity hashing algorithm", FSI: Digital Investigation 41, 301375.

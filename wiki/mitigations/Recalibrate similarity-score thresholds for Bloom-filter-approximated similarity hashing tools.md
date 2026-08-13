---
id: DFM-1198
type: mitigation
name: Recalibrate similarity-score thresholds for Bloom-filter-approximated similarity hashing tools
source_refs:
  - DFCite-1209
updated_at: 2026-08-13
status: complete
---

# Recalibrate similarity-score thresholds for Bloom-filter-approximated similarity hashing tools

## Summary

Do not reuse a similarity-score match threshold validated for an exact-frequency similarity hashing algorithm when switching to a Bloom-filter- or clustering-approximated variant; re-derive the threshold empirically against a labeled evaluation set for the specific tool and version in use.

## Addresses

- [[weaknesses/Bloom-filter-approximated similarity hashing systematically inflates similarity scores relative to exact frequency calculation]]

## How To Apply

Before relying on a Bloom-filter-approximated similarity hashing tool's match/no-match threshold in casework, run it against a labeled known-similar and known-dissimilar file set and compare the resulting score distribution to the exact-frequency algorithm's published threshold; if scores are systematically higher (as observed for FbHash-E relative to FbHash, an average +7.5-point shift), adopt the higher, empirically re-derived threshold rather than the original algorithm's documented value.

## References

- [DFCite-1209] Singh et al., 2022, "FbHash-E: A time and memory efficient version of FbHash similarity hashing algorithm", FSI: Digital Investigation 41, 301375.

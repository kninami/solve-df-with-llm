---
id: DFW-1153
type: weakness
name: Pornographic content severity ranking relies on a non-standardized, unvalidated severity scale
description: Automated pornographic-content severity/harmfulness ranking assigns each video segment to a severity class based only on the specific sexual objects an object detector finds, using a scale devised for the study itself rather than an externally validated or legally-grounded taxonomy, because no consensus severity taxonomy for adult pornography (unlike CSAM's COPINE scale) currently exists.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1153
source_refs:
  - DFCite-1156
updated_at: 2026-08-12
status: complete
---

# Pornographic content severity ranking relies on a non-standardized, unvalidated severity scale

## Summary

The severity-ranking scheme maps detected sexual-object categories to one of four severity levels devised specifically for the study, since the authors note "a lack of consensus in general when it comes to grading pornographic material based on the severity or gravity of its content" beyond a coarse softcore/hardcore split, and existing severity taxonomies (such as the COPINE scale) are built for a different content category (CSAM) rather than adult pornography.

## Why It Matters

A ranked worklist produced by this technique reflects one research team's severity assignment choices, not a legally or institutionally validated harmfulness standard; using the resulting rank order as if it carried the same evidentiary or prioritization weight as an established scale risks inconsistent triage decisions across cases or jurisdictions, and the severity labels themselves may not align with how a given law enforcement agency or legal framework defines severity for its own purposes. Investigators should treat the ranking as a relative sorting aid for a review queue, not as a calibrated harmfulness classification.

## Related Mitigations

- [[mitigations/Cross-check automated pornography severity rankings against jurisdiction-specific legal definitions before relying on them for triage]]

## Used By

- [[techniques/Rank pornographic video severity using detected sexual object categories]]

## References

- [DFCite-1156] Borg et al., 2022, "Detecting and ranking pornographic content in videos", FSI: Digital Investigation 42-43.

---
id: DFW-1312
type: weakness
name: PRNU reliability varies unpredictably across regions of a single smartphone image
description: A smartphone image's PRNU signal is not uniformly reliable across its spatial extent — some regions carry a stronger, more discriminative sensor fingerprint than others, due to factors such as smooth or over/under-exposed areas losing texture, or localized in-pipeline processing effects — so a source-attribution result derived from an arbitrarily-selected single patch or region can differ substantially in reliability from one derived from a different region of the same image.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1314
source_refs:
  - DFCite-1353
updated_at: 2026-08-15
status: complete
---

# PRNU reliability varies unpredictably across regions of a single smartphone image

## Summary

The paper's Relative Range to Max (RRM) metric, proposed specifically to quantitatively assess this phenomenon, confirms that PRNU-based positive-sample correlation strength is regionally unstable within smartphone images — for example, smooth regions can lose texture information due to overexposure or underexposure, weakening the recoverable PRNU signal in that area, while other regions retain a stronger signal, all within the same single photograph.

## Why It Matters

An investigator who extracts PRNU from only one, arbitrarily-chosen region or patch of a smartphone image risks either a false exclusion (choosing a low-signal region that happens to produce a weak, below-threshold correlation despite the image genuinely originating from the candidate camera) or an overstated confidence in a chance strong match from an unusually favorable region, without any way to know from a single-region analysis alone which scenario applies. This regional instability is specific to smartphone imagery's processing pipelines and scene/exposure variability, and is generally more pronounced than in traditional camera imagery.

## Related Mitigations

- [[mitigations/Sample multiple regions of a smartphone image before drawing a PRNU source-attribution conclusion]]

## Used By

- [[techniques/Identify a smartphone photo's source camera using multi-patch PRNU sampling]]

## References

- [DFCite-1353] Liang, Gao, and Xu, 2025, "Research on smartphone image source identification based on PRNU features collected multivariate sampling strategy", FSI: Digital Investigation 54, 301991.

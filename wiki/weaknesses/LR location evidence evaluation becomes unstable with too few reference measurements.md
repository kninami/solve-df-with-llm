---
id: DFW-1036
type: weakness
name: LR location evidence evaluation becomes unstable with too few reference measurements
description: When too few reference measurements are available in proximity to the observed location evidence for one of the two competing propositions, the density distribution fitted to those measurements is dominated by its sparse tail, making the resulting likelihood ratio value highly sensitive to small changes and potentially not representative of a stable, well-supported estimate.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1036
source_refs:
  - DFCite-1026
  - DFCite-1294
updated_at: 2026-08-14
status: complete
---

# LR location evidence evaluation becomes unstable with too few reference measurements

## Summary

In the paper's own worked case example, one proposition's distance evaluation relied on only 19 reference measurements, with the observed evidence value situated at the sparse tail end of the fitted distribution. Re-running the analysis after adding just one additional, perfectly matching reference measurement changed that proposition's probability by four orders of magnitude (from 7×10⁻⁸ to 2×10⁻⁴), and correspondingly shifted the overall LR from 1'769'124 down to a "worst case" estimate around 648. There is currently no established, validated method for determining how many reference measurements are needed at a given location to obtain a stable distribution.

## Why It Matters

An investigator who reports an LR calculated from a sparse reference set risks presenting a value to a court that appears numerically precise but is not actually stable or well-supported — a small amount of additional data could change the conclusion's magnitude dramatically. Because sparse-data instability is not visually obvious from the LR value alone (an unstable LR looks the same as a well-supported one unless the underlying reference-data density is separately examined), this risk can go unnoticed without deliberate scrutiny of the reference dataset's size for each proposition.

## Related Mitigations

- [[mitigations/Report a worst-case bound alongside unstable LR values derived from sparse reference data]]

## Used By

- [[techniques/Evaluate single-point device location evidence using a likelihood ratio]]
- [[techniques/Evaluate iPhone Health app distance data using a likelihood ratio]]

## References

- [DFCite-1026] Spichiger, 2023, "A likelihood ratio approach for the evaluation of single point device locations", FSI: Digital Investigation 44.
- [DFCite-1294] Vink, Sjerps, Boztas and van Zandwijk, 2022, "Likelihood ratio method for the interpretation of iPhone health app data in digital forensics", FSI: Digital Investigation 41, 301389. Sensitivity analysis found LRs ranging from 10⁻¹¹ to 13 depending on how narrowly the reference dataset was filtered by case information, with the most extreme values traced to small underlying sample sizes rather than genuine discriminating power.

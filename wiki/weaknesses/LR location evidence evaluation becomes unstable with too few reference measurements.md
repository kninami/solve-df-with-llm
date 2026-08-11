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
updated_at: 2026-08-09
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

- [[techniques/Likelihood ratio evaluation of single-point device location evidence]]

## References

- [DFCite-1026] Spichiger, 2023, "A likelihood ratio approach for the evaluation of single point device locations", FSI: Digital Investigation 44.

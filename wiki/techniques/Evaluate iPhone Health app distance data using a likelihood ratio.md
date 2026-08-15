---
id: DFT-1254
type: technique
name: Evaluate iPhone Health app distance data using a likelihood ratio
description: Compute a numerical likelihood ratio for a disputed walking distance recorded by the iPhone Health app by modeling the probability density of the registered-versus-true-distance relative error (derived from an experimental reference dataset) under each of two competing hypotheses about which route or distance a person actually walked.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1036
aliases:
  - LR method for iPhone Health app step/distance data
source_refs:
  - DFCite-1294
updated_at: 2026-08-14
status: complete
---

# Evaluate iPhone Health app distance data using a likelihood ratio

## Summary

Rather than presenting an iPhone Health app's registered walking distance as literal fact or as merely "consistent" with an alleged route, this method quantifies how much more probable the registered distance is under one disputed-distance hypothesis (e.g. the prosecution's claimed route) than under a competing one (e.g. the defense's claimed route), using an experimentally derived model of how far the app's registered distance typically deviates from the true walked distance.

## Details

The method has four steps: data selection and transformation (an experimental reference dataset of paired true and iPhone-registered distances, collected across multiple iPhone models, walking/running paces, and carrying locations, is transformed into a relative-error statistic — registered distance minus true distance, divided by true distance — found to be robust/independent of the absolute true distance); modeling (a smooth probability density function of the relative error is estimated via kernel density estimation, optionally filtered to only the reference measurements matching known case information such as iPhone model, pace, or carrying location); transforming (the fitted relative-error density is mathematically transformed back into a probability density function over the registered distance itself, conditioned on each hypothesis's assumed true distance); and LR computation (the two hypothesis-conditioned densities are evaluated at the case's actual registered distance and divided to obtain the LR). Because filtering the reference dataset by more case information (e.g. a specific iPhone model *and* walking pace *and* carrying location) narrows the dataset used to estimate the density function, there is a direct trade-off between how case-specific the resulting model is and how much data remains to reliably estimate it — see [[weaknesses/LR location evidence evaluation becomes unstable with too few reference measurements]].

## Examples

- A hypothetical arson case example (iPhone 7, registered distance 1250 m) comparing H1 (walked 1600 m via an indirect route) against H2 (walked 900 m directly) produced an LR of approximately 5, offering only slightly more support for H1 — illustrating that, unlike some other LR applications, this method does not guarantee a large or decisive LR even when case information is available.
- Systematic sensitivity analysis found LRs ranged from 10⁻¹¹ to 13 depending on which combination of case information (iPhone type, pace, carrying location) was used to filter the reference dataset, with the walking-pace-and-trouser-pocket combination in particular producing extreme values attributable to a small underlying sample size rather than genuinely strong discriminating power.
- Validating the model against three known true distances (91.52 m, 247.12 m, and 450.93 m) found the discriminating power, calibration, and rate of misleading evidence varied substantially by hypothesis pair — one pair achieved near-perfect discrimination (misleading evidence rate near 0%) while another, with more overlapping true distances, produced far less extreme and more frequently misleading LRs — demonstrating that the method's performance must be validated per case-specific hypothesis pair rather than assumed generically reliable.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/LR location evidence evaluation becomes unstable with too few reference measurements]]

## References

- [DFCite-1294] Vink, Sjerps, Boztas and van Zandwijk, 2022, "Likelihood ratio method for the interpretation of iPhone health app data in digital forensics", FSI: Digital Investigation 41, 301389.

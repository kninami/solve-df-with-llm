---
id: LWT-1035
type: technique
name: Evaluate single-point device location evidence using a likelihood ratio
description: Evaluate a single mobile-device localisation trace against a pair of competing propositions (e.g., the device was at Location X vs. Location Y at time t) by computing a likelihood ratio, decomposing the evaluation into an angular probability (fraction of reference measurements within a directional wedge around the observed evidence) and a distantial probability (density-fitted distance distribution within that wedge), rather than presenting the recovered location as categorical fact.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1036
  - LWW-1240
aliases:
  - Likelihood ratio evaluation of single-point device location evidence
source_refs:
  - LWCite-1026
  - LWCite-1255
updated_at: 2026-08-13
status: complete
---

# Evaluate single-point device location evidence using a likelihood ratio

## Summary

Because localisation traces recovered from mobile devices (via A-GPS or WiFi/cell-tower fingerprinting) are subject to multiple error sources and should not be treated as ground truth, this approach quantifies how much more probable the observed location evidence is under one proposition than under a competing one. Reference measurements are collected at both candidate locations using the same device model, application, and network conditions, then compared to the evidentiary observation via the odds form of Bayes' Theorem.

## Details

The observed evidence's direction and distance relative to each proposed location are evaluated separately, since error is non-uniform across direction. The angular probability for each proposition is the fraction of that location's reference measurements falling within a wedge of width 2ε centered on the evidence's observed azimuth; the distantial probability is obtained by fitting a distribution (e.g., a t-distribution) to the subset of reference distances within that wedge and evaluating it at the evidence's observed distance. The final LR is the product of the angular and distantial likelihood ratios for the two propositions, and is typically reported to a court using a standardized verbal scale (e.g., "the observations are much more probable if P1 rather than P2 were true") rather than the raw numeric value.

A related field study directly measured how much geolocation reference data actually varies by collection point: photographs captured with two Samsung Galaxy S8 devices at 29 distributed locations, under varying GNSS and mobile-network conditions, found a median radial error of 42 m when satellite access was available (rising to a maximum of 11 km) and a median of 430 m without satellite access (rising to a maximum of 27 km). Because this variability differed substantially between locations and network conditions rather than clustering around one global figure, the study's authors caution against presenting a single, categorical accuracy statement (e.g. "smartphone geolocation is accurate to within X meters") in court, reinforcing the case for this technique's location-specific reference-measurement approach over relying on a generic published accuracy figure.

## Examples

- A simulated case (iPhone 6s, two campus locations ~200m apart) using EXIF-tagged photo coordinates as reference data: 149 reference points at Location Y and 51 at Location X yielded an LR of 1,769,124 in favor of Location X, matching the scenario's ground truth.
- The 29-location field study found no consistent relationship between a location's urban/rural character and its measured accuracy on its own; instead, accuracy depended on the specific combination of location and available network type (GNSS satellite fix, WiFi, or 2G/3G/4G cellular), underscoring why reference measurements must be collected at the specific candidate locations and network conditions relevant to a case rather than assumed from a device's general specifications.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/LR location evidence evaluation becomes unstable with too few reference measurements]]
- [[weaknesses/Categorical statements about smartphone geolocation accuracy are not supported without location-specific field testing]]

## References

- [LWCite-1026] Spichiger, 2023, "A likelihood ratio approach for the evaluation of single point device locations", FSI: Digital Investigation 44.
- [LWCite-1255] Ryser et al., 2024, "Geotagging accuracy in smartphone photography", FSI: Digital Investigation 50, 301813.

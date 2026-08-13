---
id: DFW-1240
type: weakness
name: Categorical statements about smartphone geolocation accuracy are not supported without location-specific field testing
description: A single, broad claim about how accurate smartphone photo geolocation metadata is (e.g. "accurate to within X meters") is not supported by the evidence, because measured radial error varies by roughly two orders of magnitude depending on the specific location and network conditions at the time a photo was taken, so presenting geolocation accuracy as a fixed, general property risks misrepresenting its reliability for any particular case.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1241
source_refs:
  - DFCite-1255
updated_at: 2026-08-13
status: complete
---

# Categorical statements about smartphone geolocation accuracy are not supported without location-specific field testing

## Summary

A field study across 29 distributed locations, using two Samsung Galaxy S8 devices under varying GNSS and mobile-network (2G/3G/4G/WiFi) conditions, found a median radial geolocation error of 42 m with satellite access but a maximum of 27 km without it — a spread the study's authors highlight as "the imperative for evaluative approaches to take into account the specific characteristics of each point of interest, as opposed to leaning on broad statements about the reliability of geolocation processes in general." No consistent, generalizable model relating a location's characteristics (urban/rural, network availability) to its expected accuracy was found; accuracy depended on the specific combination of location and network condition at the time of capture.

## Why It Matters

An investigator, expert witness, or court that treats smartphone photo geolocation as having a single, known accuracy figure risks either overstating confidence in a low-quality measurement (if the true error at that location and time was large) or unnecessarily discounting a high-quality one (if the true error was small), since neither can be known without measurement specific to the case's actual location and network conditions. This directly undermines any presentation of geolocation evidence as categorically reliable or unreliable without case-specific validation.

## Related Mitigations

- [[mitigations/Test geolocation accuracy at the specific case location and network conditions before presenting a categorical accuracy claim]]

## Used By

- [[techniques/Evaluate single-point device location evidence using a likelihood ratio]]

## References

- [DFCite-1255] Ryser et al., 2024, "Geotagging accuracy in smartphone photography", FSI: Digital Investigation 50, 301813.

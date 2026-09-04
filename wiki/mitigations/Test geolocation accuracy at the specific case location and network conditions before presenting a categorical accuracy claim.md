---
id: LWM-1241
type: mitigation
name: Test geolocation accuracy at the specific case location and network conditions before presenting a categorical accuracy claim
source_refs:
  - LWCite-1255
updated_at: 2026-08-13
status: complete
---

# Test geolocation accuracy at the specific case location and network conditions before presenting a categorical accuracy claim

## Summary

Before presenting a statement about a smartphone's geolocation accuracy in an investigation or in court, collect reference measurements at the specific location(s) and under the network conditions (GNSS availability, WiFi, cellular generation) relevant to the case, rather than citing a general or literature-derived accuracy figure.

## Addresses

- [[weaknesses/Categorical statements about smartphone geolocation accuracy are not supported without location-specific field testing]]

## How To Apply

Using a device of the same or comparable model, application, and network configuration as the evidentiary device, capture geotagged reference photos at the case-relevant location(s) under matching network conditions, and quantify the resulting error distribution (e.g. median and maximum radial error, or a CEP/RMSE-style metric) directly rather than relying on a generic published or textbook accuracy claim. Where a formal evidentiary comparison between candidate locations is needed, feed this location-specific reference data into [[techniques/Evaluate single-point device location evidence using a likelihood ratio]] rather than reporting the raw accuracy figure as a standalone conclusion.

## References

- [LWCite-1255] Ryser et al., 2024, "Geotagging accuracy in smartphone photography", FSI: Digital Investigation 50, 301813.

---
id: DFW-1081
type: weakness
name: IoI signatures developed on a controlled dataset produce false positives against independent third-party forensic images
description: Two of five Indicator of Inconsistency (IoI) SPARQL signatures, initially developed and validated only against a controlled five-image dataset, produced 49 spurious matches (76% specificity) when run against independent third-party forensic images, because their detection logic was scoped too broadly (e.g. matching any filename containing a keyword, or accepting a benign write pattern as corroborating evidence) in ways the controlled dataset had not exposed.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-1081
source_refs:
  - DFCite-1071
updated_at: 2026-08-10
status: complete
---

# IoI signatures developed on a controlled dataset produce false positives against independent third-party forensic images

## Summary

One rule (IOI-007) matched any file whose name merely contained the substring "Security" rather than specifically the Windows Security event log, so benign security-named runtime files triggered false detections. Another rule (IOI-002) originally accepted any `$UsnJrnl` write to a Chromium History database as corroborating tamper evidence, when a plain `DataOverwrite` write is normal behavior during ordinary browsing. After refinement, specificity across the eight-image (five controlled plus three external) test corpus rose from 76% to 100%, but the authors caution this "describes the refined signatures on this eight-image corpus, not a guarantee of false-positive-free behavior on unseen data."

## Why It Matters

An investigator who adopts a community-shared IoI signature and trusts its reported performance from the original controlled evaluation risks acting on false-positive contradiction detections when that signature is applied to real-world images with characteristics the original controlled dataset did not represent — a risk that grows as signatures are shared and reused across a community with diverse casework, exactly the scenario the framework is designed to support.

## Related Mitigations

- [[mitigations/Validate IoI signatures against independent third-party images and document known scope limitations before relying on them]]

## Used By

- [[techniques/Detect cross-artifact inconsistencies in CASE-UCO knowledge graphs using SPARQL]]

## References

- [DFCite-1071] Gunestas et al., 2026, "An indicator of inconsistency framework for detecting contradictory digital artifacts", FSI: Digital Investigation 58.

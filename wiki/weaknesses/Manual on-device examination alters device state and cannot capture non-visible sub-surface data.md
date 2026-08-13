---
id: DFW-1130
type: weakness
name: Manual on-device examination alters device state and cannot capture non-visible sub-surface data
description: Live, on-device navigation during a manual examination risks handling errors and unintended metadata changes, and can only ever capture visible surface-level content, leaving non-visible sub-surface-level data inaccessible without a formal forensic extraction.
categories:
  - ASTM_INAC_ALT
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1130
source_refs:
  - DFCite-1126
updated_at: 2026-08-12
status: complete
---

# Manual on-device examination alters device state and cannot capture non-visible sub-surface data

## Summary

A device manual examination (DME) requires directly navigating a live device, which is a greater level of interaction than a traditional forensic extraction and increases the chance that resident data changes as a result — even unintentionally or accidentally, for example through altered timestamp or metadata information caused by simply opening and viewing a file. Separately, a DME can only capture "visible surface-level data" reachable by navigating the interface; "non-visible sub-surface level data" exists on virtually every device and requires specialist forensic procedures to access, meaning a DME alone can never be assumed to be a complete data-collection method.

## Why It Matters

Because DME changes to a device are typically irreversible, and any resulting data or metadata loss "presents a real risk," a first responder who conducts a DME without first assessing these risks may unknowingly compromise data they later need to rely upon, or may wrongly conclude an inquiry is complete when in fact only the surface layer of a device's data has been reviewed and relevant sub-surface content remains uncollected. Both failure modes can be avoided by explicit, staged assessment before a DME is conducted rather than after the fact.

## Related Mitigations

- [[mitigations/Apply the manual examination procedure's staged viability assessment and escalate to formal forensic extraction when needed]]

## Used By

- [[techniques/Conduct a manual examination of a device at scene]]

## References

- [DFCite-1126] Horsman, 2022, "Conducting a 'manual examination' of a device as part of a digital investigation", FSI: Digital Investigation 40, 301331.

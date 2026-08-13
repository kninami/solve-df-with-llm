---
id: DFT-1127
type: technique
name: Conduct a manual examination of a device at scene
description: Interrogate a complainant device live, at scene, by navigating and recording its interface directly instead of seizing it for a formal forensic extraction, following a structured seven-stage viability assessment to determine when doing so is appropriate.
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1130
aliases:
  - Device manual examination (DME)
  - Manual examination procedure (MEP)
source_refs:
  - DFCite-1126
updated_at: 2026-08-12
status: complete
---

# Conduct a manual examination of a device at scene

## Summary

A device manual examination (DME) allows a first responder to quickly identify and evaluate content on a complainant's device at scene by navigating and recording it directly, rather than always seizing the device for a formal forensic extraction. The manual examination procedure (MEP) is a structured, seven-stage decision framework for determining when a DME is a viable and appropriate investigative option.

## Details

The MEP begins with a device pre-assessment (confirming the device is operational, with no damage or settings issue that would prevent safe navigation) and then works through seven staged questions before a DME may proceed: (1) what data is relevant to the inquiry, distinguishing "visible surface-level data" — recordable by navigating the interface — from "non-visible sub-surface level data" that requires specialist forensic procedures to access; (2) can all relevant data actually be gathered, both technically and practically, given its likely volume; (3) can the data be gathered without compromising it, given that live navigation risks "handling errors" and unintended metadata changes (e.g. altered timestamps from playing back media files); (4) are there concerns about the authenticity or reliability of what is visible, which a DME cannot resolve without raw file access; (5) can the relevant data be captured in sufficient detail, typically via camera recording of the screen, with any capture media first sanitized to prevent contamination; (6) can the captured data be placed into the evidence chain effectively, addressing integrity and chain-of-custody concerns for camera- or email-captured content; and (7) is a manual examination proportionate and justifiable given the inquiry, compared to formal extraction. A negative answer at any stage should trigger escalation to formal forensic extraction rather than proceeding with a DME.

## Examples

- A first responder investigating an assault complaint uses a DME to review and photograph relevant text messages directly on a complainant's phone at scene, having confirmed via the MEP that the messages are visible surface-level data capturable by camera without needing raw file access, and that their authenticity is not in dispute.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Manual on-device examination alters device state and cannot capture non-visible sub-surface data]]

## References

- [DFCite-1126] Horsman, 2022, "Conducting a 'manual examination' of a device as part of a digital investigation", FSI: Digital Investigation 40, 301331.

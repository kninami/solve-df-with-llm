---
id: DFM-1203
type: mitigation
name: Cross-correlate whichever IoT evidence sources remain available when one of device, companion app, or cloud is missing
source_refs:
  - DFCite-1216
updated_at: 2026-08-13
status: complete
---

# Cross-correlate whichever IoT evidence sources remain available when one of device, companion app, or cloud is missing

## Summary

When one of a smart device's three evidence sources (hardware, companion app, cloud) is unavailable, do not treat the investigation as blocked; analyze the remaining source(s) individually and correlate whatever combination is available, since even a two-source correlation (e.g. companion client plus cloud) can recover findings neither source alone would show.

## Addresses

- [[weaknesses/Multi-source IoT and smart-device evidence collection is incomplete when the device, companion app, or cloud source is unavailable]]

## How To Apply

At the outset of an investigation involving a smart device, identify and prioritize securing all three source types as early as possible (physical device, any paired companion clients, and cloud account access), since losing access to one narrows both direct evidence and correlation-derived findings. If a source proves unavailable, explicitly document which correlations could not be performed as a result, and proceed with correlation across whichever two (or one) sources remain, using shared identifiers (device serial numbers, account IDs, timestamps) to link artifacts across the sources that are available.

## References

- [DFCite-1216] Youn et al., 2021, "Forensic analysis for AI speaker with display Echo Show 2nd generation as a case study", FSI: Digital Investigation 38, 301130.

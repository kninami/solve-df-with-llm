---
id: LWW-1140
type: weakness
name: Failure to isolate and disable a dashcam's radio and auto-recording features before acquisition risks remote alteration or overwriting of evidence
description: If a first responder leaves a dashcam's Wi-Fi, Bluetooth, or GSM connectivity active, or leaves auto-power-on or g-sensor-triggered recording enabled, the device can receive remote commands or automatically begin a new loop-recording session that overwrites unprotected existing footage before it is preserved.
categories:
  - ASTM_INAC_ALT
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1140
source_refs:
  - LWCite-1138
updated_at: 2026-08-12
status: complete
---

# Failure to isolate and disable a dashcam's radio and auto-recording features before acquisition risks remote alteration or overwriting of evidence

## Summary

Many dashcams support Wi-Fi, Bluetooth, and/or GSM connectivity, features that can allow incoming data to modify the device's state or alert a third party to its location, and most dashcams use a loop-recording feature that automatically overwrites the oldest non-write-protected recording once storage runs out. A first responder who powers up or handles a dashcam without first isolating its radios and disabling auto-power-on/g-sensor recording risks either remote interference or the device itself silently overwriting evidentially relevant footage.

## Why It Matters

Because normal-manual recordings are not write-protected by default, any device behavior that triggers a new recording session — an auto-power-on event, a g-sensor-detected motion, or even the storage device filling up during handling — can permanently overwrite previously recorded, potentially critical footage before an investigator has a chance to image the SD card. Unlike a mobile phone, no dashcam known to the authors has a single "airplane mode" toggle, so each radio component must be identified and isolated individually, increasing the chance a step is missed under time pressure at a scene.

## Related Mitigations

- [[mitigations/Follow the dashcam first-response checklist to isolate radios and disable auto-recording before any acquisition attempt]]

## Used By

- [[techniques/Follow a structured first-response and tiered acquisition procedure for dashcam evidence]]

## References

- [LWCite-1138] Lallie, 2023, "Dashcam forensic investigation guidelines", FSI: Digital Investigation 45.

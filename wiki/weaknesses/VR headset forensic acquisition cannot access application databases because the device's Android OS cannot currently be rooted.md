---
id: DFW-2122
type: weakness
name: VR headset forensic acquisition cannot access application databases because the device's Android OS cannot currently be rooted
description: A non-rooted ADB-based logical acquisition of an Android-based VR headset cannot access installed applications' protected private-data directories, and no established method currently exists to root the headset's Android OS (file-based encryption and the lack of support in existing JTAG tools for the device's specific chipset both block known rooting approaches), so database-level artifacts such as user chat/communication logs and messages remain unrecoverable through this acquisition method.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2123
source_refs:
  - DFCite-2145
updated_at: 2026-08-16
status: complete
---

# VR headset forensic acquisition cannot access application databases because the device's Android OS cannot currently be rooted

## Summary

The Meta Quest 2 runs an Android 10-based OS that isolates and protects sensitive per-application databases from access by an unprivileged (non-root) account, and the study's own attempts to identify a rooting method found none currently established for this device: Android 10's file-based encryption and the absence of existing JTAG tool support for the headset's specific Qualcomm Snapdragon XR2 chipset both foreclose the rooting approaches that have worked for other Android device classes. As a direct consequence, artifacts requiring root-level database access -- notably user communication data such as chat logs and messages sent/received directly through the headset -- could not be recovered by this study despite a comprehensive logical acquisition otherwise succeeding.

## Why It Matters

An investigator relying solely on non-rooted ADB-based acquisition for a VR headset case involving alleged harassment, grooming, or other communication-based misconduct risks a significant completeness gap precisely in the artifact category most central to such a case, since the underlying chat/message content is exactly what root-level app-database access would be needed to recover. Because this is a foreclosed capability rather than merely an unexplored one at the time of the underlying study (no rooting method existed to attempt), an investigator cannot simply try harder with the same acquisition approach; a fundamentally different access method would be required, and none is currently available for this device class.

## Related Mitigations

- [[mitigations/Supplement non-rooted VR headset acquisition with cloud account data and monitor for future rooting method developments]]

## Used By

- [[techniques/Acquire and analyze a VR headset's live data, backup, and internal storage using ADB-based forensic acquisition]]

## References

- [DFCite-2145] Raymer, MacDermott, and Akinbi, 2023, "Virtual reality forensics: Forensic analysis of Meta Quest 2", FSI: Digital Investigation 47, 301658.

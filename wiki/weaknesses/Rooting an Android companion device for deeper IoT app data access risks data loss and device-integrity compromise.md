---
id: LWW-2114
type: weakness
name: Rooting an Android companion device for deeper IoT app data access risks data loss and device-integrity compromise
description: Non-rooted extraction from an Android IoT companion app's data directory via ADB can only access a limited subset of application data due to Android permission restrictions, but obtaining the deeper access rooting provides carries its own risk of altering or losing data during the rooting process, and the specific rooting procedure required varies by the device's operating system version, adding an additional layer of procedural risk and complexity.
categories:
  - ASTM_INCOMP
  - ASTM_INAC_ALT
mitigation_ids:
  - LWM-2115
source_refs:
  - LWCite-2134
updated_at: 2026-08-16
status: complete
---

# Rooting an Android companion device for deeper IoT app data access risks data loss and device-integrity compromise

## Summary

Software-based data extraction from an IoT companion app's storage on a non-rooted Android device using ADB can only access data the OS's permission model exposes; obtaining fuller access to the app's private data directory requires rooting the device first, but the rooting procedure itself demands administrator-level modification of the device's operating system, carries a documented risk of causing data loss during the process, and its exact steps vary depending on the specific Android OS version installed, adding both technical complexity and forensic-soundness risk relative to a non-invasive extraction.

## Why It Matters

An investigator choosing to root a companion device to access fuller IoT-app evidence is trading completeness of data access against a real risk of altering or destroying the very evidence being sought, and against the added complexity of correctly executing a version-specific rooting procedure without introducing errors. Because the decision must typically be made before knowing exactly what additional evidence rooting would reveal, an investigator cannot straightforwardly weigh this trade-off in advance for a specific case, and an incorrectly executed rooting attempt could compromise data that a purely software-based, non-rooted extraction would have preserved intact, even if incompletely.

## Related Mitigations

- [[mitigations/Attempt non-rooted extraction and hardware-level acquisition before rooting an IoT companion device, and document the rooting procedure precisely]]

## Used By

- [[techniques/Acquire forensic artifacts from a smart IoT device across hardware, companion-app, network, and cloud sources]]

## References

- [LWCite-2134] Sharma and Awasthi, 2024, "Unveiling the hidden dangers: Security risks and forensic analysis of smart bulbs", FSI: Digital Investigation 50, 301794.

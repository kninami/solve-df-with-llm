---
id: LWM-2115
type: mitigation
name: Attempt non-rooted extraction and hardware-level acquisition before rooting an IoT companion device, and document the rooting procedure precisely
source_refs:
  - LWCite-2134
updated_at: 2026-08-16
status: complete
---

# Attempt non-rooted extraction and hardware-level acquisition before rooting an IoT companion device, and document the rooting procedure precisely

## Summary

Before rooting an Android companion device to access fuller IoT app data, exhaust non-invasive collection options (non-rooted ADB extraction, and hardware-level extraction directly from the IoT device's own chip/module where feasible), and if rooting proves necessary, follow a precisely documented, OS-version-appropriate procedure with the risk of data loss disclosed.

## Addresses

- [[weaknesses/Rooting an Android companion device for deeper IoT app data access risks data loss and device-integrity compromise]]

## How To Apply

First attempt non-rooted ADB-based extraction from the companion device, and separately consider whether the target evidence might instead be recoverable directly from the IoT device's own hardware (e.g. its Wi-Fi module's flash memory, per [[techniques/Acquire forensic artifacts from a smart IoT device across hardware, companion-app, network, and cloud sources]]), potentially avoiding the need to root the companion device at all. If rooting is judged necessary because expected evidence would otherwise be inaccessible, identify and use a rooting procedure validated for the companion device's specific Android OS version, document each step taken, and be prepared to explain in reporting that the rooting process carries an inherent, disclosed risk of data alteration or loss that a non-rooted extraction would not. Where possible, image the device (or back up accessible data) before attempting to root it, so a failed or data-altering rooting attempt does not represent the sole surviving copy of any already-accessible evidence.

## References

- [LWCite-2134] Sharma and Awasthi, 2024, "Unveiling the hidden dangers: Security risks and forensic analysis of smart bulbs", FSI: Digital Investigation 50, 301794.

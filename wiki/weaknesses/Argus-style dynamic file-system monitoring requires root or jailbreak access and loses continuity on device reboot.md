---
id: LWW-1090
type: weakness
name: Argus-style dynamic file-system monitoring requires root or jailbreak access and loses continuity on device reboot
description: Differential file-system snapshot monitoring requires complete file-system access via a rooted Android device/emulator or a jailbroken iOS device; if these methods are unavailable for the target device or OS version, the methodology does not work at all, and even when available, restarting the phone during an experiment severs the monitoring connection and can destroy a non-persistent jailbreak, preventing collection of file system information for that session.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1090
source_refs:
  - LWCite-1082
  - LWCite-2095
updated_at: 2026-08-16
status: complete
---

# Argus-style dynamic file-system monitoring requires root or jailbreak access and loses continuity on device reboot

## Summary

The authors state this directly: "For correct use, Argus relies on jailbroken iOS devices and rooted Android devices or emulators. If these methods are no longer available, the proposed methodology will not work, since it requires complete access to the device file system. This way of working also limits the possibility to perform experiments in which the phone is restarted. In such cases, restarting the phone severs its connection to Argus, preventing collection of file system information and can even lead to the loss of a non-persistent jailbreak." Separately, temporary files both created and deleted within a single snapshot interval will not appear in any snapshot and so cannot be detected at all.

## Why It Matters

An investigator relying on this class of tool to build a reference library of app artifact locations is blocked entirely on devices or OS versions without a working root/jailbreak exploit — a growing constraint as platform security hardens — and any experiment requiring the target device to reboot mid-session (e.g. testing behavior across an app update, or a scenario requiring a cold boot) risks losing both the collected data and the ability to continue the experiment at all.

## Related Mitigations

- [[mitigations/Plan Argus-style dynamic monitoring experiments around root and jailbreak availability and avoid mid-experiment reboots]]

## Used By

- [[techniques/Discover and extract mobile application artifact locations]]
- [[techniques/Perform dynamic analysis of iOS applications on ARM-based macOS using differential filesystem snapshotting]] (this technique's whole motivation is avoiding the jailbreak requirement documented here for iOS specifically, by running the app natively on ARM-based macOS instead)

## References

- [LWCite-1082] Boztas et al., 2025, "Argus: A new approach for forensic analysis of apps on mobile devices", FSI: Digital Investigation 53.
- [LWCite-2095] Seiden, Webb, and Baggili, 2025, "Tapping .IPAs: An automated analysis of iPhone applications using apple silicon macs", FSI: Digital Investigation 52, 301871. Source for a jailbreak-free alternative for the iOS side of this weakness.

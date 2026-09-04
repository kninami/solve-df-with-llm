---
id: LWM-1090
type: mitigation
name: Plan Argus-style dynamic monitoring experiments around root and jailbreak availability and avoid mid-experiment reboots
source_refs:
  - LWCite-1082
  - LWCite-2095
updated_at: 2026-08-16
status: complete
---

# Plan Argus-style dynamic monitoring experiments around root and jailbreak availability and avoid mid-experiment reboots

## Summary

Before running an Argus-style dynamic file-system-diffing experiment, confirm a working root (Android) or jailbreak (iOS) method exists for the target OS version, and design the experiment to avoid device reboots mid-session; where a reboot is unavoidable, plan to re-establish root/jailbreak and restart data collection from scratch.

## Addresses

- [[weaknesses/Argus-style dynamic file-system monitoring requires root or jailbreak access and loses continuity on device reboot]]

## How To Apply

Confirm root/jailbreak availability for the specific target OS version before committing to this methodology, and use a device/emulator combination with a known-working exploit. Sequence experiment steps to avoid any action that would trigger a device reboot; if a reboot does occur, treat it as ending that experiment session, re-establish root/jailbreak access, and restart data collection rather than assuming continuity. Where a temporary file is suspected to have been both created and deleted between snapshots, note this as an acknowledged detection gap rather than a confirmed absence of activity. For iOS specifically, consider [[techniques/Perform dynamic analysis of iOS applications on ARM-based macOS using differential filesystem snapshotting]] as a jailbreak-free alternative on an ARM-based Mac before ruling out dynamic analysis entirely for a device or app where no working jailbreak is currently available.

## References

- [LWCite-1082] Boztas et al., 2025, "Argus: A new approach for forensic analysis of apps on mobile devices", FSI: Digital Investigation 53.
- [LWCite-2095] Seiden, Webb, and Baggili, 2025, "Tapping .IPAs: An automated analysis of iPhone applications using apple silicon macs", FSI: Digital Investigation 52, 301871.

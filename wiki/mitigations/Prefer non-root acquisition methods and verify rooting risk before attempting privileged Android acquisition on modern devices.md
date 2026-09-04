---
id: LWM-1086
type: mitigation
name: Prefer non-root acquisition methods and verify rooting risk before attempting privileged Android acquisition on modern devices
source_refs:
  - LWCite-1077
updated_at: 2026-08-10
status: complete
---

# Prefer non-root acquisition methods and verify rooting risk before attempting privileged Android acquisition on modern devices

## Summary

Prefer acquisition methods that do not require rooting where they exist for the target Android version, and where rooting is the only option, independently verify the specific rooting method's data-loss risk on the target device model and Android version before attempting it.

## Addresses

- [[weaknesses/Root-access-based Android acquisition is becoming ineffective against modern security and risks data loss]]

## How To Apply

Before attempting to root a modern (Android 12+) device for acquisition, research whether the specific rooting method has been validated against that exact device model and OS version, and confirm whether it is known to trigger a factory reset. Where no validated, non-destructive rooting method exists, prioritize non-root extraction avenues (cloud/backup extraction, ADB backup where available, or logical extraction) and document in the report why full private-storage access could not be obtained rather than risking evidence loss on an unvalidated rooting attempt.

## References

- [LWCite-1077] Dowrick et al., 2026, "Android anti-forensics: A systematic review of applications, techniques, and investigative challenges", FSI: Digital Investigation 58.

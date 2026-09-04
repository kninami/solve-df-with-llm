---
id: LWM-1182
type: mitigation
name: Obtain an intact reference file from the same camera model and settings before attempting energy-based PCM audio recovery
source_refs:
  - LWCite-1185
updated_at: 2026-08-12
status: complete
---

# Obtain an intact reference file from the same camera model and settings before attempting energy-based PCM audio recovery

## Summary

Before attempting energy-based recovery of an impaired dashcam MP4's audio, first obtain a normally recorded (intact) MP4 file from the same camera model and recording settings, and parse its "moov" atom to determine the channel count, sampling rate, and bytes-per-sample the impaired file's raw audio will use.

## Addresses

- [[weaknesses/Energy-based PCM audio recovery requires prior knowledge of audio format parameters from an intact reference file]]

## How To Apply

Identify the exact make and model of the dashboard camera that produced the impaired file, and either request or record a short intact sample clip using the same device and settings (or, where unavailable, an identical model configured the same way); extract the audio format parameters from that reference file's "moov" atom before running the energy-based recovery procedure, and document the reference file used as part of the recovery's methodology.

## References

- [LWCite-1185] Park et al., 2021, "Energy-based linear PCM audio recovery method of impaired MP4 file stored in dashboard camera memory", FSI: Digital Investigation 39. Describes obtaining channel count, sampling rate, and bytes-per-sample from a normally recorded MP4 from the same dashboard camera prior to recovery.

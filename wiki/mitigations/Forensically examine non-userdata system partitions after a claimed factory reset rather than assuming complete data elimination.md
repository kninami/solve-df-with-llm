---
id: LWM-1091
type: mitigation
name: Forensically examine non-userdata system partitions after a claimed factory reset rather than assuming complete data elimination
source_refs:
  - LWCite-1083
updated_at: 2026-08-10
status: complete
---

# Forensically examine non-userdata system partitions after a claimed factory reset rather than assuming complete data elimination

## Summary

When examining an Android device that has undergone a factory reset, forensically examine system partitions beyond the primary encrypted userdata partition (e.g. log/klog partitions, sensor calibration data, and other partially unencrypted system data) for surviving usage metadata, rather than assuming the reset eliminated all recoverable information.

## Addresses

- [[weaknesses/Factory reset on modern Android devices does not wipe unencrypted system-partition metadata that can reveal device usage]]

## How To Apply

Perform a low-level partition extraction of the reset device and systematically inspect non-userdata partitions for unencrypted or partially-encrypted remnant data, including log partitions, sensor/calibration data, and any device- or model-specific partitions of unclear purpose. Do not limit examination to the primary encrypted userdata partition on the assumption that its key-erasure-based reset represents the device's complete data-elimination state.

## References

- [LWCite-1083] Blankesteijn et al., 2023, "Assessing data remnants in modern smartphones after factory reset", FSI: Digital Investigation 46.

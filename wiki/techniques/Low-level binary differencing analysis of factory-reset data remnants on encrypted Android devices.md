---
id: DFT-1085
type: technique
name: Low-level binary differencing analysis of factory-reset data remnants on encrypted Android devices
description: Assess whether a factory reset actually eliminated forensically relevant data on a modern encrypted Android device by extracting low-level partition images before device use, after creating known synthetic data, and after performing a factory reset, then binary-diffing these extractions to identify which bytes and partitions were actually overwritten or reformatted versus left unchanged, rather than trusting the manufacturer's factory-reset marketing claim.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1091
aliases: []
source_refs:
  - DFCite-1083
updated_at: 2026-08-10
status: complete
---

# Low-level binary differencing analysis of factory-reset data remnants on encrypted Android devices

## Summary

Factory reset is marketed and commonly believed by end-users to restore a device to its as-shipped state, but modern Android devices primarily achieve this via secure erasure of the file-based-encryption keys rather than overwriting all user data, since only the encrypted userdata partition's keys — not necessarily every byte on every partition — need to be destroyed to render user data unreadable. Directly comparing partition-level binary extractions from before and after a reset reveals precisely what is and is not actually removed.

## Details

The method extracts recognized partitions (e.g. via `dd`) at three points — before creating synthetic user data, after creating it, and after performing a factory reset — then manually inspects binary differences between the extractions using Python scripts, applied to Google Pixel and Xiaomi Redmi devices running Android 11 and 12. Because only the file-based-encryption keys are securely erased on reset, encrypted userdata partition bytes remain physically present but unreadable in their encrypted form without the destroyed key; separately, several other partitions (e.g. system log/klog partitions, and other partially unencrypted system data) are not touched by the reset process at all and can retain plaintext or reconstructable information about prior device usage.

## Examples

- Binary diffing of a Google Pixel 3a running Android 12 found the fewest unmodified bytes in the same position after reset among tested devices (i.e. it wiped the most), while a Xiaomi Redmi 9 retained the most unmodified bytes, illustrating that reset thoroughness varies meaningfully by manufacturer and Android version even for devices marketed as equivalently "reset."

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Factory reset on modern Android devices does not wipe unencrypted system-partition metadata that can reveal device usage]]

## References

- [DFCite-1083] Blankesteijn et al., 2023, "Assessing data remnants in modern smartphones after factory reset", FSI: Digital Investigation 46.

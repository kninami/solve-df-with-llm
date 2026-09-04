---
id: LWW-1091
type: weakness
name: Factory reset on modern Android devices does not wipe unencrypted system-partition metadata that can reveal device usage
description: A factory reset on modern Android 11/12 devices securely erases only the file-based-encryption keys protecting the userdata partition rather than overwriting all user data, and other partitions (e.g. system log/klog partitions, and other partially unencrypted system data) are not touched by the reset process at all, leaving plaintext or binary information from which prior device usage can still be inferred.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1091
source_refs:
  - LWCite-1083
updated_at: 2026-08-10
status: complete
---

# Factory reset on modern Android devices does not wipe unencrypted system-partition metadata that can reveal device usage

## Summary

The study found that, next to the encrypted user data whose keys are securely erased, "there also stays some partially unencrypted system data on other partitions. In case of the klog partition some information may be deduced such as whether somebody has connected with the device. Furthermore, one could deduct how a device has been used by exploiting information such as the battery capability and calibration of certain sensors." A separately-tested Bluetooth partition on Android 12 also retained data through a reset, of unclear original purpose. Most partitions on the device are simply never written to during a few days of ordinary use, and factory reset does not proactively overwrite them regardless.

## Why It Matters

An investigator examining a device a suspect claims was "factory reset" to eliminate evidence should not assume the reset achieved complete data elimination: system partitions outside the primary encrypted userdata partition can retain plaintext metadata revealing whether and how the device was used, and this metadata survives specifically because the reset process's key-erasure strategy does not extend to those partitions at all.

## Related Mitigations

- [[mitigations/Forensically examine non-userdata system partitions after a claimed factory reset rather than assuming complete data elimination]]

## Used By

- [[techniques/Analyze factory-reset data remnants on encrypted Android devices using binary differencing]]

## References

- [LWCite-1083] Blankesteijn et al., 2023, "Assessing data remnants in modern smartphones after factory reset", FSI: Digital Investigation 46.

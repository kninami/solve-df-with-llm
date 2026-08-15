---
id: DFW-1294
type: weakness
name: Android FBE master-key RAM recovery only works on devices whose key derivation function has the vulnerable flaw
description: Because the RAM-based master-key recovery method exploits a specific flaw in Google's key derivation function implementation, it succeeds only on devices whose Android/kernel version still contains that flaw, and fails entirely against devices running a patched KDF, so a negative recovery result does not indicate the device is otherwise inaccessible — only that this specific method does not apply to it.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1295
source_refs:
  - DFCite-1326
updated_at: 2026-08-15
status: complete
---

# Android FBE master-key RAM recovery only works on devices whose key derivation function has the vulnerable flaw

## Summary

Across a 13-device evaluation spanning models released 2015-2020, only 7 devices used a key derivation function vulnerable to this recovery method; the other 6 did not. Google independently fixed the underlying KDF flaw in later kernel versions, meaning the fraction of vulnerable devices in the field will decline further as older devices are retired or updated.

## Why It Matters

An investigator who obtains a memory image from an Android device and finds this method fails to recover a master key should not conclude that master-key recovery is impossible in general, or that the device's FBE protection cannot be defeated by any means — only that this specific KDF-flaw-dependent method does not apply to that particular device's Android/kernel version. Conflating "this method failed" with "master key recovery is impossible" risks prematurely abandoning an investigation that a different, non-KDF-flaw-dependent approach (or a future patch to this method) might still succeed on.

## Related Mitigations

- [[mitigations/Determine device patch level and KDF vulnerability status before relying on FBE master-key RAM recovery]]

## Used By

- [[techniques/Recover an Android FBE master key from RAM to decrypt EXT4 file names and contents]]

## References

- [DFCite-1326] Groß, Busch, and Müller, 2021, "One key to rule them all: Recovering the master key from RAM to break Android's file-based encryption", FSI: Digital Investigation 36, 301113.

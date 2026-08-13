---
id: DFW-1192
type: weakness
name: RPMB key-extraction techniques depend on a specific vulnerable eMMC or TEE implementation
description: A published RPMB authentication-key extraction method exploits a particular vendor's choice to store the key in plain text at a discoverable location in eMMC flash rather than deriving it purely from hardware-bound secret material; the technique does not generalize to a device or eMMC part whose TEE genuinely protects the key against physical readout.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1192
source_refs:
  - DFCite-1199
updated_at: 2026-08-13
status: complete
---

# RPMB key-extraction techniques depend on a specific vulnerable eMMC or TEE implementation

## Summary

The Blackphone 2 case succeeded because its Qualcomm TrustZone/QSEE implementation programs the RPMB authentication key to the eMMC without obfuscation or hardware-backed protection beyond the eMMC's own inaccessible flash interface — a design choice, not an inherent property of RPMB itself. A TEE that instead derives the key entirely within silicon (e.g., from a device-unique key never exposed outside a secure enclave, or protects the flash region with additional read protection) would not yield its key to the same read-flash-and-descramble procedure, even though the RPMB standard and its use cases (anti-rollback, unlock-attempt counters, secure boot root of trust) are unchanged.

## Why It Matters

An investigator who successfully extracts an RPMB key from one device model should not assume the same procedure will work against a different manufacturer, chipset, or TEE version without first confirming — through the same combination of software reverse engineering (to locate the key-provisioning routine) and hardware inspection (to determine where and how the key is written to flash) — that an equivalent implementation weakness is actually present. Treating this as a general-purpose RPMB bypass risks wasted lab time devoted to hardware reverse engineering (including irreversible desoldering steps) against a device that may in fact be properly protected, or false confidence that a wiped or version-locked device cannot be restored when a different, not-yet-identified weakness might still exist.

## Related Mitigations

- [[mitigations/Verify the target eMMC or TEE's specific key-storage vulnerability before attempting RPMB key extraction]]

## Used By

- [[techniques/Extract an eMMC RPMB authentication key from flash to bypass anti-rollback protection]]

## References

- [DFCite-1199] Fukami et al., 2024, "Exploiting RPMB authentication in a closed source TEE implementation", FSI: Digital Investigation 48.

---
id: DFT-1185
type: technique
name: Extract an eMMC RPMB authentication key from flash to bypass anti-rollback protection
description: Physically read an eMMC's raw NAND flash memory (via chip-off or In-System Programming) to recover a Replay Protected Memory Block (RPMB) pre-shared authentication key stored unprotected by a vulnerable Trusted Execution Environment implementation, enabling modification of RPMB-backed anti-rollback counters and restoration of a wiped or otherwise state-locked smartphone.
objective_ids:
  - DFO-1016
weakness_ids:
  - DFW-1192
aliases:
  - RPMB authentication key extraction and anti-rollback bypass
  - Blackphone 2 RPMB key recovery
source_refs:
  - DFCite-1199
updated_at: 2026-08-13
status: complete
---

# Extract an eMMC RPMB authentication key from flash to bypass anti-rollback protection

## Summary

Modern smartphones use an eMMC's Replay Protected Memory Block (RPMB) to store tamper-resistant, authenticated data such as an anti-rollback counter, unlock-attempt counters, or a root-of-trust public key hash, protected by a pre-shared HMAC key generated inside a Trusted Execution Environment (TEE). Where a specific TEE/eMMC implementation stores that key in plain text at a predictable, accessible location in flash rather than deriving it from genuinely unrecoverable hardware-bound secret material, an investigator can read it directly from the chip and regain full read/write control over the RPMB area, including the ability to roll back an anti-rollback counter.

## Details

The technique combines software and hardware reverse engineering. First, static and dynamic analysis of the device's key-derivation and disk-encryption code (e.g., Qualcomm's QSEE running in TrustZone) establishes how and when the RPMB authentication key and anti-rollback counter are used — for example, the counter may be included in the HMAC that authenticates an encrypted on-flash keystore holding the disk-encryption key, so that restoring an earlier keystore without also restoring the matching counter value causes decryption to fail even with the correct password. Second, the eMMC's technical (non-JEDEC-standard) pins are connected to a logic analyzer while a known key is programmed to a reference chip of the same part number, to identify the NAND page-program command and target address used during key provisioning; a flash memory reader (e.g., in single-level-cell mode for reliability) then dumps the raw flash, and the extracted data is de-scrambled using a manufacturer-specific XOR pattern recovered from known-empty sectors, revealing the authentication key stored in plain text. Once the key and the RPMB write counter are known, an investigator can restore an earlier full-flash backup (including the earlier RPMB counter value) to reverse a data-wipe or version-downgrade-prevention routine, without the modification being detected by the device's own integrity checks. Access to the technical pins can be obtained non-destructively via In-System Programming header wires soldered directly to the CLK/CMD/D0 lines rather than fully desoldering the chip, once its location has been identified — see [[techniques/Extract eMMC storage using in-system programming]] and [[techniques/Read flash memory in situ via reverse-engineered PCB vias]] for related non-destructive/destructive eMMC access approaches.

## Examples

- A Blackphone 2 (Qualcomm Snapdragon 615, Silent OS 3, full-disk encryption with an RPMB-backed anti-rollback counter) had its wipe routine accidentally triggered during brute-force password testing; the RPMB authentication key was recovered from a Hynix H9TQ26ADFTMCUR eMCP chip's flash memory at a fixed offset following a `[PASS]` flag, and used to restore the pre-wipe RPMB counter value (rewritten from `0x11` back to `0x10`) alongside a full flash backup, returning the device to its original, fully decryptable working state.
- The same authors report successfully extracting RPMB authentication keys from two other eMMC parts (a Samsung KLMAG2GE4A-A001 and a Sandisk SDIN8DE4-16G) used in different smartphones, each storing the key at a different flash address, confirming the key-extraction step generalizes across vendors even though the exact storage location must be re-identified for each chip.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/RPMB key-extraction techniques depend on a specific vulnerable eMMC or TEE implementation]]

## References

- [DFCite-1199] Fukami et al., 2024, "Exploiting RPMB authentication in a closed source TEE implementation", FSI: Digital Investigation 48.

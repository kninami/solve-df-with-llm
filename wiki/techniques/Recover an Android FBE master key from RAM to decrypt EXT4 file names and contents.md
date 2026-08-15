---
id: DFT-1284
type: technique
name: Recover an Android FBE master key from RAM to decrypt EXT4 file names and contents
description: Recover the master key protecting an Android device's File-Based Encryption (FBE) EXT4 partition from a raw physical memory image (obtained via a cold boot attack or RAM module transplantation), then use it to automatically decrypt every encrypted file name and file content on the partition with extended versions of The Sleuth Kit and Plaso, restoring full forensic file system and timeline analysis on a device where prior FDE-era key-recovery tools no longer apply.
objective_ids:
  - DFO-1016
weakness_ids:
  - DFW-1294
aliases:
  - Android File-Based Encryption (FBE) master-key RAM recovery
source_refs:
  - DFCite-1326
updated_at: 2026-08-15
status: complete
---

# Recover an Android FBE master key from RAM to decrypt EXT4 file names and contents

## Summary

Google's move from Full Disk Encryption (FDE) to File-Based Encryption (FBE) as Android's default encryption scheme rendered prior FDE-era memory-forensics key-recovery tools ineffective, since FBE encrypts individual files (via per-file keys derived from a device master key) rather than an entire partition. Recovering the master key directly from a raw memory image — obtained via a classic cold boot attack (reset-and-reboot with a forensic boot loader) or by physically transplanting the device's RAM modules into an examiner-controlled system — re-enables full forensic analysis of an FBE-protected Android device by allowing every encrypted file name and file content on the partition to be decrypted automatically.

## Details

Given a raw physical memory image, the master key is located and recovered from the file-specific data encryption keys and file-specific nonces resident in RAM (extending prior academic work establishing that a master key is derivable from one file-specific key plus its nonce). The Sleuth Kit (TSK) is extended to recognize FBE-related EXT4 file attributes and to automatically decrypt both file names and file contents once given the recovered master key, restoring standard file system forensic analysis to an FBE-encrypted partition. The Plaso timeline-analysis framework is separately extended to extract timeline events directly from an FBE-encrypted partition, again requiring only the recovered master key as input. The technique's practicality stems in large part from a flaw the researchers identified in Google's key derivation function (KDF) implementation on some devices, which made master-key recovery considerably easier than it would otherwise have been; Google independently fixed this KDF flaw in later kernel versions.

## Examples

- Evaluated on 13 Android smartphones released between 2015 and 2020 (including Nexus and Pixel models), the method successfully exploited the vulnerable key derivation function on 7 of the 13 devices to recover the FBE master key from a memory image.
- Applying the recovered master key with the extended TSK and Plaso tooling automatically decrypted file names, file contents, and reconstructed timeline events from an FBE-encrypted EXT4 partition without any further manual decryption effort.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Android FBE master-key RAM recovery only works on devices whose key derivation function has the vulnerable flaw]]

## References

- [DFCite-1326] Groß, Busch, and Müller, 2021, "One key to rule them all: Recovering the master key from RAM to break Android's file-based encryption", FSI: Digital Investigation 36, 301113.

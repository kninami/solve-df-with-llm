---
id: DFM-2083
type: mitigation
name: Capture Linux encryption recovery material before powering down or logging out of a live target system
source_refs:
  - DFCite-2096
updated_at: 2026-08-16
status: complete
---

# Capture Linux encryption recovery material before powering down or logging out of a live target system

## Summary

Before powering off or logging out of a live Linux system, run [[techniques/Identify and access Linux disk and directory encryption at scene using live command-line detection]] to check for full-disk or per-directory encryption, and if present, capture the applicable recovery key, unwrapped passphrase, or a decrypted live image while the opportunity exists, rather than defaulting to an immediate shutdown.

## Addresses

- [[weaknesses/Powering off or logging out of a live Linux system with disk or directory encryption enabled permanently forecloses low-cost data access]]

## How To Apply

At scene, before shutting down or logging off a live, unlocked Linux system, check for encryption using `fdisk -l`, `blkid`, and the Disks GUI utility. If LUKS/FDE is present and the account is unlocked, take a live decrypted image (`dd` for a full physical image, `tar` for a targeted logical/filesystem-level image) of the relevant volume before shutdown; note that imaging a subdirectory such as `/home` or `/mnt` under an already-imaged root filesystem can produce recursive-compression errors, so image separate, selective locations rather than the whole tree in one pass where this is a concern. If eCryptfs/HDE is present, run `ecryptfs-unwrap-passphrase` as the logged-in user and record the output passphrase. If fscrypt/HDE is present, run `fscrypt status` to enumerate protected filesystems/directories and their lock state, and directly copy the contents of any directory found already unlocked. In every case, also review available shell-history files (`.bash_history`, `.ksh_history`) for commands revealing prior manual encryption setup or configuration details not otherwise discoverable, and document what encryption was found and what recovery material was captured, since this determines whether post-scene access will require key-recovery, password cracking, or is already assured.

## References

- [DFCite-2096] Findlay, Ben, 2024, "Techniques and methods for obtaining access to data protected by linux-based encryption -- A reference guide for practitioners", FSI: Digital Investigation 48, 301662.

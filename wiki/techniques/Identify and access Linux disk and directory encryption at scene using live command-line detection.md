---
id: LWT-2080
type: technique
name: Identify and access Linux disk and directory encryption at scene using live command-line detection
description: On a live, powered-on Linux system, use standard command-line utilities (fdisk, blkid, the Disks GUI) and shell-history review to determine whether full-disk encryption (LUKS/dm-crypt) or per-directory encryption (eCryptfs or fscrypt) is present, then capture recovery keys, unwrap passphrases, or take a decrypted logical/physical image before the system is powered off or the user account is logged out, since each of these Linux encryption technologies becomes far harder or impossible to access once the live opportunity is lost.
objective_ids:
  - DFO-1016
  - DFO-1021
weakness_ids:
  - LWW-2082
aliases:
  - Linux full disk encryption / home directory encryption at-scene identification
source_refs:
  - LWCite-2096
updated_at: 2026-08-16
status: complete
---

# Identify and access Linux disk and directory encryption at scene using live command-line detection

## Summary

Linux desktop distributions offer full-disk encryption (FDE, via LUKS/dm-crypt) and per-home-directory encryption (HDE, historically via eCryptfs, more recently via fscrypt) that a user can enable during OS installation or manually afterward, and both are typically off by default -- so an investigator cannot assume their presence or absence without actively checking. Because both technologies are far easier to access while the target system is live and the user's account is unlocked than after it has been shut down or logged out, an investigator encountering a running Linux system should first identify which (if any) encryption technology is in use, then take the corresponding live-access steps before any shutdown/logout action forecloses that opportunity.

## Details

Detection uses three complementary indicators on a live system: the `fdisk -l` command's output (permission-denied errors on `/dev/mapper/*_crypt` devices indicate LUKS is present), the `blkid` command (reporting `TYPE="crypto_LUKS"` or similar for encrypted block devices), and the OS's own Disks GUI utility (visually listing volumes and their encryption status). For LUKS/FDE, if the account is logged in and unlocked, an investigator can take a full decrypted physical image of the underlying block device using `dd`, or a filesystem-level decrypted image using `tar`, directly from the live decrypted mount point -- avoiding the need to ever crack the LUKS passphrase at all, provided this is done before shutdown. For eCryptfs/HDE, the command `ecryptfs-unwrap-passphrase` (run as the logged-in user) reveals the mount passphrase protecting the user's encrypted home directory in plaintext, which should be recorded for later use even if a live image is also taken. For fscrypt/HDE, `fscrypt status` enumerates which filesystems and directories have fscrypt policies applied and their protector details, and `fscrypt status /path/to/directory` confirms lock state for a specific encrypted subdirectory; where the directory is already unlocked (decrypted) in the current session, its content can be copied or imaged directly. Shell history files (`.bash_history`, `.ksh_history`) for any user account should also be reviewed, since they may reveal exactly which encryption commands the user previously ran, which specific directories were manually encrypted, and other configuration details not otherwise discoverable. All of the above can be performed non-destructively without requiring the encryption to actually be broken, which stands in contrast to post-scene (powered-off, logged-out) access to the same technologies, where a recovery key, cached password (e.g. via a password manager, if accessible), or password-cracking attempt (e.g. against `/etc/passwd`/`/etc/shadow`) becomes the primary remaining option.

## Examples

- On a Linux Mint system with LUKS-enabled full-disk encryption, `blkid` output showed `/dev/mapper/sda4_crypt` with `TYPE="LVM2_member"`, confirming the presence of a LUKS-encrypted logical volume underlying the mounted root filesystem.
- Running `fscrypt status` on a live, unlocked system reported one filesystem supporting encryption with one filesystem carrying active fscrypt metadata, and a subsequent `fscrypt status /home/mintfsc/Desktop/encrypted/` confirmed that specific directory was unlocked and ready for use, allowing its decrypted contents to be directly copied or imaged.
- The eCryptfs unwrap-passphrase command output a plaintext mount passphrase (e.g. `01721d4b8ee174c9a224c839da13e4e2`), which -- combined with the recovery-key backup file (`recovery.key`) some installers generate and which a suspect may have separately backed up to removable media or cloud storage -- provides two independent avenues for later decrypting the same eCryptfs-protected home directory even without the original login password.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms
- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/Powering off or logging out of a live Linux system with disk or directory encryption enabled permanently forecloses low-cost data access]]

## References

- [LWCite-2096] Findlay, Ben, 2024, "Techniques and methods for obtaining access to data protected by linux-based encryption -- A reference guide for practitioners", FSI: Digital Investigation 48, 301662.

---
id: DFT-1020
type: technique
name: Recover application credentials from memory using string-pattern search
description: Recover a password or other secret from a process memory dump by searching for a known, application-specific string pattern that the application reliably places adjacent to the secret in memory while constructing a key-derivation input or prompt, rather than searching for the secret's value directly.
objective_ids:
  - DFO-1016
weakness_ids:
  - DFW-1020
aliases:
  - Memory string-pattern recovery of application credentials
  - rclone.conf password recovery
source_refs:
  - DFCite-1014
updated_at: 2026-08-09
status: complete
---

# Recover application credentials from memory using string-pattern search

## Summary

Some applications construct a key-derivation input by concatenating the user's password with a fixed, application-specific marker string (e.g., `[password][rclone-config]`) before hashing it into an encryption key. Because the marker string is constant and known in advance (from the application's source code or reverse engineering), it can be searched for directly in a memory dump — locating the adjacent, still-plaintext password even after the originating process has terminated, without needing to guess or brute-force the password itself.

## Details

The technique requires first identifying, via static/dynamic analysis of the target application, a constant string that the application places immediately before or after the secret during key derivation or password-prompt handling. Searching a memory dump for that marker (rather than for arbitrary password-shaped strings) sharply narrows the search space and tolerates the executable being stripped of debug symbols. Multiple copies of the marker-plus-secret pair may persist in memory if the operation was performed more than once. When the exact marker cannot be found (e.g., its memory page was overwritten), a fallback is to search for other structural indicators of the application's known configuration-file format (fixed key names, section headers) to recover fragments of the underlying secret data even without the marker itself.

## Examples

- rclone constructs `[password][rclone-config]` before SHA-256-hashing it into the `rclone.conf` decryption key; searching a memory dump for the literal substring `[rclone-config]` recovered the plaintext password even after the rclone process had exited.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/In-memory credential recovery fails once the relevant memory page is overwritten]]

## References

- [DFCite-1014] Breitinger et al., 2022, "A forensic analysis of rclone and rclone's prospects for digital forensic investigations of cloud storage", FSI: Digital Investigation 43.

---
id: LWW-1061
type: weakness
name: Failure to update access timestamps under Linux's default relatime mount option undermines file-read event reconstruction
description: On Linux, the default `relatime` mount option only updates a file's last-access (A) timestamp if it was previously earlier than the modify or change timestamp, or at least a day old — meaning most ordinary file reads leave the access timestamp completely unchanged, silently deviating from POSIX's mandatory A-update requirement and making read-based event reconstruction from access timestamps unreliable unless the analyst independently confirms the mount option in effect.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1061
source_refs:
  - LWCite-1051
updated_at: 2026-08-10
status: complete
---

# Failure to update access timestamps under Linux's default relatime mount option undermines file-read event reconstruction

## Summary

The paper's compliance testing found that Linux, under its default `relatime` mount option, fails the majority of POSIX-mandated access-timestamp update tests: a file read only updates its access timestamp if the existing value was already older than the modify/change timestamp or more than a day stale. With the non-default `strictatime` option, Linux passes all other mandatory POSIX-compliance tests. OpenBSD's default `noatime`-adjacent behavior and other BSD-based systems have their own, differently limited access-update semantics.

## Why It Matters

An analyst who observes an unchanged or stale access timestamp on a Linux system and concludes the file was not read (or was last read at that stale time) can be entirely wrong under the default mount configuration, since ordinary reads are silently skipped from an access-timestamp-update standpoint. Because this happens with Linux's out-of-the-box default rather than only in an unusual configuration, this is a routine risk rather than an edge case, and the mount option in effect is not something visible from the timestamp values themselves.

## Related Mitigations

- [[mitigations/Verify OS mount-option and library-layer timestamp update behavior before interpreting MACB timestamps]]

## Used By

- [[techniques/Profile MACB timestamp compliance across the software stack]]

## References

- [LWCite-1051] Thierry and Müller, 2022, "A systematic approach to understanding MACB timestamps on Unix-like systems", FSI: Digital Investigation 40.

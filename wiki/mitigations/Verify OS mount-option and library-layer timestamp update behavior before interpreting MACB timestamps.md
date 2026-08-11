---
id: DFM-1061
type: mitigation
name: Verify OS mount-option and library-layer timestamp update behavior before interpreting MACB timestamps
source_refs:
  - DFCite-1051
updated_at: 2026-08-10
status: complete
---

# Verify OS mount-option and library-layer timestamp update behavior before interpreting MACB timestamps

## Summary

Before relying on a file's timestamps to reconstruct user or program activity on a Unix-like system, check the actual mount options in effect and consult layer-aware reference tables (kernel, filesystem, standard library, middleware, application) for the specific OS/library combination, since default configurations and known library bugs cause frequent, non-obvious deviations from naive POSIX-compliant expectations.

## Addresses

- [[weaknesses/Failure to update access timestamps under Linux's default relatime mount option undermines file-read event reconstruction]]

## How To Apply

Check `/proc/mounts` or `mount` output (or equivalent) on the source system for the atime-related mount option in effect (`relatime`, `strictatime`, `noatime`, `nodiratime`) before treating a stale or unchanged access timestamp as evidence that no read occurred. Use published or self-generated layer-aware profiling reference tables (e.g. the paper's open-source `os_timestamps` framework) matched to the specific OS version, filesystem, and any relevant middleware library or application, rather than assuming uniform POSIX-compliant behavior.

## References

- [DFCite-1051] Thierry and Müller, 2022, "A systematic approach to understanding MACB timestamps on Unix-like systems", FSI: Digital Investigation 40.

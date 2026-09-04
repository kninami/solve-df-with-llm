---
id: LWT-1057
type: technique
name: Profile MACB timestamp compliance across the software stack
description: Systematically test and profile how each layer of the software stack (kernel/filesystem, mount options, the standard C/C++ library, middleware libraries such as GIO and Qt, and applications) updates a file's Modify/Access/Change/Birth (MACB) timestamps for common operations, comparing observed behavior against POSIX's mandatory specification to build practitioner-usable reference tables and flag non-compliant or unexpected behavior on Unix-like systems.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1061
aliases:
  - Software-stack layered MACB timestamp compliance profiling
source_refs:
  - LWCite-1051
updated_at: 2026-08-10
status: complete
---

# Profile MACB timestamp compliance across the software stack

## Summary

Timestamp behavior on Unix-like systems is not fixed at a single layer: the kernel, filesystem, mount options, standard library, middleware libraries, and the application itself can each influence whether and when a MACB timestamp is updated. An automated framework that tests POSIX compliance and profiles real timestamp updates across all of these layers — rather than only observing user-facing application behavior — lets practitioners understand precisely which timestamp updates can be trusted for event reconstruction on a given OS/library/application combination.

## Details

The framework runs two kinds of tests. POSIX compliance tests check whether a single operation's timestamp update matches the mandatory ("shall") behavior specified by POSIX, using paired system-time snapshots taken before and after the operation to bound when the file-system timestamp was actually written. Automated profiling tests instead run common operations (File Creation, Read, Write, Execute, Copy, Delete, Rename) and record the resulting MACB flag pattern for each watched file/directory, without requiring a POSIX baseline, so it also captures non-POSIX-specified library and application behavior. The framework was implemented in C for OS/library-level tests (Linux, OpenBSD, FreeBSD, macOS; GIO and Qt) and in Python (using pyautogui) for GUI application tests, covering 15 popular Linux text editors. Results are compiled into layer-aware reference tables (mount options, timestamp resolution, birth-timestamp support, and per-operation MACB patterns) intended for direct use by forensic practitioners.

## Examples

- `mkfifo` on macOS marks MAC for update but does not immediately write the new values — waiting 60 seconds after running `mkfifo` and then reading the FIFO's timestamps showed they had actually been set roughly 26 seconds after the command returned, meaning a naive interpretation of the FIFO's timestamp could misplace when the command ran.
- The GIO library (used by the Nautilus file manager) truncates modification and access timestamps to microsecond resolution when copying a file via `g_file_copy`, an 11-year-old known bug; this truncation can be used to distinguish files copied via Nautilus from files copied with `cp`.
- FreeBSD and OpenBSD do not update a symbolic link's own last-access timestamp when the link is read or followed via `readlink()`, and FreeBSD additionally does not update a directory's access timestamp when the directory is listed (`ls`).

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Failure to update access timestamps under Linux's default relatime mount option undermines file-read event reconstruction]]

## References

- [LWCite-1051] Thierry and Müller, 2022, "A systematic approach to understanding MACB timestamps on Unix-like systems", FSI: Digital Investigation 40.

---
id: LWM-1142
type: mitigation
name: Examine the full external data block of every long symbolic link for content beyond its target-path string
source_refs:
  - LWCite-1139
updated_at: 2026-08-12
status: complete
---

# Examine the full external data block of every long symbolic link for content beyond its target-path string

## Summary

Rather than relying only on a resolved target-path listing of symbolic links, identify every symbolic link whose target string is long enough to require external block allocation on the file system in question, and inspect the full raw contents of that block for data beyond the terminated target-path string.

## Addresses

- [[weaknesses/Forensic tools examining a symbolic link's target string miss hidden data in the link's external block slack space]]

## How To Apply

During examination, enumerate symbolic links across the target file system and, for each, determine whether its target path is stored inline (fast symlink) or in an externally allocated block, based on the specific file system's known inline-storage threshold. For every externally-stored symlink, read the raw contents of its allocated block or extent directly rather than only calling a target-resolution API, and treat any non-zero, non-path-string content following the target path's terminator as a potential hidden-data indicator warranting further analysis. Because the amount of exploitable slack space and its behavior differs by file system, calibrate this check against the specific file system(s) present in the case rather than assuming uniform behavior across ext, XFS, BtrFS, HFS+, APFS, and NTFS.

## References

- [LWCite-1139] Toolan and Humphries, 2025, "Data hiding in symbolic link slack space", FSI: Digital Investigation 53.

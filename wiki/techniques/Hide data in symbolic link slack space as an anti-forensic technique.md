---
id: LWT-1139
type: technique
name: Hide data in symbolic link slack space as an anti-forensic technique
description: Create a symbolic link whose target-path string is long enough to force the file system to allocate a dedicated data block or extent for it, then write hidden data into the unused space in that block beyond the end of the stored target-path string, exploiting file systems that allocate a full block or cluster for an externally-stored symlink target even though the target string itself is normally much shorter.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1142
aliases:
  - Symbolic link slack space data hiding
source_refs:
  - LWCite-1139
updated_at: 2026-08-12
status: complete
---

# Hide data in symbolic link slack space as an anti-forensic technique

## Summary

Most modern file systems (including ext, XFS, BtrFS, HFS+, APFS, and NTFS) support symbolic links at the file-system level, and store a short target path inline within the link's inode/file-record metadata ("fast symlink"). Once the target path exceeds the inline storage capacity, the file system instead allocates a separate data block or extent to hold the target string; because that allocation is normally sized in whole blocks/clusters while the stored path string is typically only a few dozen bytes, most of the allocated block goes unused and can be repurposed to store arbitrary hidden data.

## Details

The paper systematically examines symbolic link implementations across ext2/3/4, XFS, BtrFS, HFS+, APFS, and NTFS to determine, for each, whether and at what target-path length the file system switches from inline (fast) symlink storage to an externally allocated block, how much slack space results from that allocation, and how effectively data written into that slack space survives normal file system use and evades users, system administrators, and forensic analysts. Because a symbolic link's externally stored target string is ordinary allocated file-system data from the file system's own point of view, forensic tools and manual analysis that examine only the target path itself (as returned by a `readlink()`-equivalent call) will not surface any data written past the end of that string within the same allocated block — the hidden data is present on disk but outside what any symlink-aware tool or API considers part of the link's content. The technique builds on prior data-hiding-in-file-systems research that has focused on individual file systems (e.g. ext, NTFS, XFS) by treating the symbolic link mechanism itself, rather than a specific file system's general slack space, as the exploitable structure, and finds that file systems and configurations differ in how much slack space is available and how reliably hidden data in it survives.

## Examples

- Creating a symbolic link with a target path just over the fast-symlink inline-storage threshold on a tested file system, so that the file system allocates a full data block for the target, then writing hidden bytes into the remainder of that block beyond the terminating end of the stored path string.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Forensic tools examining a symbolic link's target string miss hidden data in the link's external block slack space]]

## References

- [LWCite-1139] Toolan and Humphries, 2025, "Data hiding in symbolic link slack space", FSI: Digital Investigation 53.

---
id: LWT-2101
type: technique
name: Recover deleted files from UBIFS flash file systems using journal-based scanning
description: Analyze a raw NAND/NOR flash image from an IoT or embedded device (e.g. a camera, drone, or router) using the layered MTD/UBI/UBIFS abstraction stack to parse the Unsorted Block Images File System (UBIFS), recovering both live and deleted files -- including their metadata -- by scanning UBIFS's write-ahead journal for reference nodes not yet reflected in the on-flash B+-tree index, rather than relying on the index alone.
objective_ids:
  - DFO-1013
  - DFO-1018
weakness_ids:
  - LWW-2107
aliases:
  - UBI Forensic Toolkit
  - UBIFT
source_refs:
  - LWCite-2126
updated_at: 2026-08-16
status: complete
---

# Recover deleted files from UBIFS flash file systems using journal-based scanning

## Summary

UBIFS is a flash file system increasingly found in IoT and embedded devices (cameras, drones, routers, and OpenWRT-based systems) that manages raw flash directly rather than through a traditional block-device abstraction, and its data structures are not documented from a digital forensics perspective and unsupported by existing forensic tools such as The Sleuth Kit. UBIFS stores its data in a B+-tree index on flash, but because flash's out-of-place update mechanism means every modification is buffered through a write-ahead journal before eventually being committed into that index, deleted files can be recovered by scanning the journal directly for reference nodes describing content the index no longer reflects, rather than relying solely on a straightforward index traversal that would miss this buffered, not-yet-committed information.

## Details

The tool implements a layered architecture mirroring The Sleuth Kit's abstraction-layer design, adding an additional MTD (Memory Technology Device) layer beneath UBI to bridge flash file systems into a TSK-like framework: the MTD layer provides access to physical erase blocks (and their possible out-of-band metadata) within a raw flash dump; the UBI layer maps logical erase blocks (LEBs) to physical erase blocks (PEBs), transparently handling wear-leveling and bad-block management, and is identified within an MTD partition by scanning for its erase-counter-header magic bytes; the UBIFS layer then parses the actual file system built atop a UBI volume, including its B+-tree file-system index (built from typed nodes each carrying a common `ubifs_ch` header with a distinct magic value, discoverable via straightforward magic-byte scanning across a UBI volume's LEBs) and, critically, its journal. The journal exists to reduce the number of flash write operations: rather than updating the B+-tree index on every single change, UBIFS buffers changes in a dedicated log area containing reference nodes that point to "buds" (LEBs in the main area holding the actual buffered inode, data, deletion-marker, and truncation nodes), only periodically performing a "commit" operation that folds the journal's buffered changes into the index. Because a deleted file's inode (link count set to zero) or directory-entry deletion marker may exist only within uncommitted journal buds and never reach the index at all before the device is imaged, scanning the journal's reference nodes directly recovers this information; where the journal itself is unavailable or already committed, a brute-force scan of the entire image for nodes with a zero link count or zero inode number provides a fallback, though the resulting freeable/obsolete LEBs remain vulnerable to permanent loss via UBIFS's own garbage collector.

## Examples

- Applied to a real-world Internet camera (Foscam R2) flash dump, the tool's `mtdls` command enumerated MTD partitions and identified UBI instances within them, `ubils` enumerated UBI volumes within an identified instance, and its journal-aware `fls --scan` command recovered files (including a `.ash_history` shell-history file and several plaintext credential files, `passwd`/`shadow`) that two comparison tools (UBI Reader and UBIFS Dumper) failed to recover at all, since neither tool implements journal-aware scanning; the `icat` command then extracted the recovered shell-history file's actual content, revealing commands the user had previously run including inspection of `/etc/passwd` and `/etc/shadow`.
- Comparative testing against UBI Reader and UBIFS Dumper on the same artificially-generated and real-world flash dumps found UBI Reader failed to extract any data from the Foscam dump's journal (missing forensically significant uncommitted data entirely) and UBIFS Dumper failed to correctly parse the dump at all in some configurations (reporting an "Unknown file type" error), while the new tool successfully processed both.

## Related Objectives

- `DFO-1013` Access partitions, volumes, and file systems data
- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/UBIFS deleted-file recovery becomes permanently impossible once the garbage collector erases freeable blocks]]

## References

- [LWCite-2126] Deutschmann and Baier, 2024, "Ubi est indicium? On forensic analysis of the UBI file system", FSI: Digital Investigation 48, 301689.

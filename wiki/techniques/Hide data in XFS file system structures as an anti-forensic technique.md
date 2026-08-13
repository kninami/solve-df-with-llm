---
id: DFT-1140
type: technique
name: Hide data in XFS file system structures as an anti-forensic technique
description: Conceal arbitrary data inside unused or misused regions of the XFS file system — allocation-group superblock slack, inode slack, the free list area, unused inode records, and misused nanosecond timestamp fields — so that the hidden data survives normal file system use and is not surfaced by tools that only examine allocated file content.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1143
aliases:
  - XFS superblock slack data hiding
  - XFS inode slack data hiding
  - XFS free list area data hiding
  - XFS free inode data hiding
  - XFS nanosecond timestamp data hiding
source_refs:
  - DFCite-1140
updated_at: 2026-08-12
status: complete
---

# Hide data in XFS file system structures as an anti-forensic technique

## Summary

XFS is the default file system on all Red Hat Enterprise Linux distributions and divides a volume into a number of allocation groups, each beginning with its own superblock. The paper introduces and evaluates five distinct methods of hiding data within XFS structures that are allocated by the file system but not fully used to store meaningful content, each trading off hiding capacity against detection difficulty and survivability through normal file system usage.

## Details

The five methods are: (M1) superblock slack — writing into the padding bytes that follow the defined fields of an allocation group's superblock; (M2) inode slack — writing into the unused bytes remaining within an inode record after its defined fields and any short inline data/extended-attribute content; (M3) the free list area — writing into unused entries of an allocation group's free-space B-tree/free-list block region; (M4) free inodes — repurposing the space of inode records that are marked free (not currently allocated to any file) to store hidden data; and (M5) misusing the nanosecond component of XFS's high-precision timestamp fields (creation, modification, access, change) to encode a small amount of hidden data per timestamp rather than a decodable time. Each method was evaluated using the same metrics used elsewhere in file-system data-hiding research: hiding capacity (how much data can be concealed), detection difficulty and the analyst effort required to find it, and stability (the likelihood the hidden data survives continued file system usage without being overwritten). The methods differ significantly in these properties — the free list area and free inodes methods offer larger capacity but lower stability under continued file system activity, while superblock and inode slack offer smaller, more stable hiding locations, and the nanosecond timestamp method offers very low capacity but is easy to overlook since standard tools only interpret the timestamp's decoded value, not its raw bit pattern. This work extends prior file-system data-hiding research that has focused on NTFS and the ext family to XFS, whose default status on all current Red Hat Enterprise Linux distributions makes it more prevalent than its relatively small forensic-tooling ecosystem might suggest.

## Examples

- Writing hidden bytes into the padding region following the fixed fields of an XFS allocation group's superblock, a location present once per allocation group regardless of the volume's file content.
- Encoding hidden data in the sub-second (nanosecond) component of a file's XFS timestamp fields, which most timestamp-display tooling ignores below whole-second (or coarser) resolution.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Forensic examination of XFS misses data hidden in slack, reserved, and misused structures]]

## References

- [DFCite-1140] Toolan and Humphries, 2025, "Data hiding in the XFS file system", FSI: Digital Investigation 52.

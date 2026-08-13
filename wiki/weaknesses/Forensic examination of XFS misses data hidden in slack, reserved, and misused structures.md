---
id: DFW-1143
type: weakness
name: Forensic examination of XFS misses data hidden in slack, reserved, and misused structures
description: Standard file system analysis of an XFS volume examines allocated file content and defined metadata fields but does not by default inspect superblock/inode slack space, the free list area, free inode records, or the raw sub-second bits of timestamp fields, so data hidden in any of these locations goes unnoticed unless specifically searched for.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1143
source_refs:
  - DFCite-1140
updated_at: 2026-08-12
status: complete
---

# Forensic examination of XFS misses data hidden in slack, reserved, and misused structures

## Summary

Because XFS forensic tooling is comparatively immature relative to NTFS and ext, and because slack space, reserved regions, and free records are, by definition, outside the boundaries of any currently allocated file, an examiner relying on tools that report only allocated file content and standard metadata fields will not see data an anti-forensic actor has hidden in an allocation group's superblock or inode slack, its free list area, its free inode records, or the nanosecond component of a timestamp.

## Why It Matters

An investigator who trusts a standard file listing or file-carving pass to represent "everything present" on an XFS volume may miss a meaningful volume of concealed data, since several of the five hiding locations documented for XFS have non-trivial capacity and some (the free list area and free inodes) can persist across substantial file system activity before being overwritten. Because XFS is the default file system on all current Red Hat Enterprise Linux distributions, this is not a niche concern limited to unusual deployments.

## Related Mitigations

- [[mitigations/Manually inspect XFS slack, reserved, and misused structures for hidden data]]

## Used By

- [[techniques/Hide data in XFS file system structures as an anti-forensic technique]]

## References

- [DFCite-1140] Toolan and Humphries, 2025, "Data hiding in the XFS file system", FSI: Digital Investigation 52.

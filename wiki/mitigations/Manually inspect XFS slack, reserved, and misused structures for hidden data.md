---
id: DFM-1143
type: mitigation
name: Manually inspect XFS slack, reserved, and misused structures for hidden data
source_refs:
  - DFCite-1140
updated_at: 2026-08-12
status: complete
---

# Manually inspect XFS slack, reserved, and misused structures for hidden data

## Summary

When anti-forensic data hiding is suspected on an XFS volume, extend the examination beyond allocated file content to include allocation-group superblock and inode slack space, the free list area, free inode records, and the raw sub-second bits of timestamp fields, using low-level hex or a purpose-built parser rather than relying on standard file listings alone.

## Addresses

- [[weaknesses/Forensic examination of XFS misses data hidden in slack, reserved, and misused structures]]

## How To Apply

For each allocation group on the volume, extract and hex-inspect the superblock's padding region and the padding remaining within inode records after their defined fields; parse the free list/free-space B-tree area and any inode records currently marked free for non-zero content inconsistent with an empty or reset structure; and compare the raw nanosecond field of each file's timestamps against the value that would result from normal system clock precision, flagging implausible or structured nanosecond values. Prioritize this deeper inspection when the case involves a suspect with the technical sophistication to have read the same anti-forensic research, and note that the five candidate locations differ in how long hidden data is likely to survive continued file system activity, so examine the least-volatile locations (slack space) first if time is constrained.

## References

- [DFCite-1140] Toolan and Humphries, 2025, "Data hiding in the XFS file system", FSI: Digital Investigation 52.

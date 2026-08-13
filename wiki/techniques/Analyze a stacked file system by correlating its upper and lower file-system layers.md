---
id: DFT-1211
type: technique
name: Analyze a stacked file system by correlating its upper and lower file-system layers
description: Extend standard file-system forensic analysis with a dedicated phase that identifies a stacked file system (e.g. MooseFS, GlusterFS, eCryptfs) from indicators left in its already-analyzed lower file system, then correlates each lower file with its corresponding upper file to recover file names, hierarchy, fragmentation, transformation, and timestamp information the lower file system alone cannot provide.
objective_ids:
  - DFO-1013
weakness_ids:
  - DFW-1222
aliases:
  - Stacked file system forensic analysis
  - Upper/lower file correlation for stacked file systems
source_refs:
  - DFCite-1234
updated_at: 2026-08-13
status: complete
---

# Analyze a stacked file system by correlating its upper and lower file-system layers

## Summary

A stacked file system stores its files and metadata as ordinary files ("lower files") on an underlying, separately mountable file system rather than directly on a volume, so a standard file-system forensic workflow that stops after analyzing the lower file system will overlook the upper file system's own files, names, and hierarchy entirely unless a dedicated correlation phase is added.

## Details

Extending Brian Carrier's file-system-forensic-analysis model, the added phase begins by identifying whether a lower file system is in fact hosting a stacked file system, using indicators specific to the implementation: MooseFS chunk servers create a distinctive `00`-`FF` directory hierarchy and prefix each chunk file with a `0x2000`-byte header signature; GlusterFS bricks create a hidden `.glusterfs` directory using the same hierarchy pattern and name lower files by a GlusterFS Internal File Identifier (GFID); eCryptfs lower files carry no distinguishing hierarchy but can be recognized by an XOR-derived magic marker in their header bytes. Once identified, upper-to-lower file correlation differs by architecture: local or unmanaged distributed stacked file systems (GlusterFS, eCryptfs) generally expose the mapping directly within the lower file system itself (extended attributes, inode-number matching, or a mirrored directory hierarchy using hard/soft links), while managed distributed stacked file systems (MooseFS) require extracting and parsing a separate management-server metadata store (via a vendor-provided dump utility) to obtain the mapping. This correlation additionally recovers per-upper-file fragmentation across multiple lower files, any content transformation applied by the stacked file system (encryption headers, erasure-coding), and — critically — upper-file timestamps, which in some implementations exist only as extended attributes on the lower files (e.g. GlusterFS's `trusted.glusterfs.mdata`) or are entirely absent from the upper file system and must be inferred from lower-file timestamp behavior instead.

## Examples

- Extracting and parsing MooseFS's `metadata.mfs.back` file with the `mfsmetadump` utility revealed the upper file system's directory tree as parent/child inode `EDGE` entries, each naming an upper file and linking it to the chunk IDs (and therefore lower files) that store its content.
- GlusterFS's extended attribute `trusted.glusterfs.mdata` on a lower file stored the corresponding upper file's Access/Modify/Change/Birth timestamps as an 8-byte-seconds-plus-nanoseconds Base64-encoded structure, recoverable even though GlusterFS keeps no separate external timestamp database.
- eCryptfs upper files could be matched to their lower files directly via inode-number comparison using the `ecryptfs-find` utility, and when file-name encryption was enabled, the FNEK (file-name-encryption-key) signature embedded in each encrypted lower file name allowed grouping of lower files that were encrypted under, and therefore likely mounted from, the same key.

## Related Objectives

- `DFO-1013` Access partitions, volumes, and file systems data

## Related Weaknesses

- [[weaknesses/Standard file system forensic tools cannot associate a stacked file system's lower files with their corresponding upper files]]
- [[weaknesses/Stacked file systems expose lower-file and extra lower-file slack space that can be used to hide data]]

## References

- [DFCite-1234] Hilgert, Lambertz and Baier, 2024, "Forensic implications of stacked file systems", DFRWS EU 2024; FSI: Digital Investigation 48, 301678.

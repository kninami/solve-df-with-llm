---
id: LWT-1296
type: technique
name: Parse Google Fuchsia's Zircon-FVM disk structures for dead-disk forensic analysis
description: Perform dead-disk (offline, post-mortem) forensic examination of a device running Google's Fuchsia operating system by identifying and interpreting the disk-level structures of Fuchsia's custom Fuchsia Volume Manager (FVM), its constituent partitions (including MinFS, BlobFS, and the Zircon Boot Image), and the boundaries these structures impose on evidence recovery, since Fuchsia uses a non-Linux, non-Android-derived custom microkernel (Zircon) and storage stack unfamiliar to most investigators and unsupported by existing forensic tooling.
objective_ids:
  - DFO-1013
weakness_ids:
  - LWW-1306
aliases:
  - Fuchsia FVM/Zircon/MinFS/BlobFS/ZBI forensic analysis
source_refs:
  - LWCite-1343
updated_at: 2026-08-15
status: complete
---

# Parse Google Fuchsia's Zircon-FVM disk structures for dead-disk forensic analysis

## Summary

Fuchsia is a modular, capability-based operating system Google has been developing as a possible successor to Android or a replacement for several of its other supported operating systems, targeting a range of devices from workstations and routers to IoT devices. Unlike Google's other operating systems, Fuchsia does not use a Linux kernel, instead running on a custom microkernel called Zircon with its own storage stack (FVM, MinFS, BlobFS) — meaning investigators encountering a Fuchsia device cannot assume any of the file system or partition knowledge that transfers between Android, ChromeOS, and other Google platforms, and no forensic tooling previously existed for the platform.

## Details

The examination identifies and documents the disk-level identifiers and data storage structures of Fuchsia's custom logical volume manager (the Fuchsia Volume Manager, FVM) and the partitions it manages, providing forensic examiners a breakdown of each partition's content, structure, and purpose within the wider operating system: MinFS (a general-purpose file system inspired by Unix-derived file systems such as Ext3/Ext4, expected to hold much conventional user data), BlobFS (a content-addressed file system used for immutable content blobs), and the ZIRCON partition holding a Boot File System (BootFS) disk image. Because Fuchsia's capability-based security model gives each system service and application only the minimum privileges required for its function, the operating system's handling of, and regulation of access to, underlying user data differs meaningfully from traditional OS models — with direct implications for an investigator's ability to attribute which user or application created, accessed, or modified a specific set of data, since the expected filesystem metadata trail may not exist or may not work the way an investigator familiar with conventional OSes would expect.

## Examples

- The paper documents that Fuchsia's `zxcrypt` encryption subsystem, applied to the MinFS partition, can prevent investigators from completing an examination of MinFS content without the corresponding decryption keys, directly limiting dead-disk analysis of user data on an otherwise-identified partition.
- Because Fuchsia was, at the time of the research, still under active development, the paper explicitly notes several open, unanswered questions — including the content of the BootFS disk image within the ZIRCON partition and the structure of entries within the FVM's Slice Allocation Table — that could not be fully resolved from available documentation and reverse engineering alone, and flags that findings depend on the examined partition structures not changing significantly as Fuchsia matures.

## Related Objectives

- `DFO-1013` Access partitions, volumes, and file systems data

## Related Weaknesses

- [[weaknesses/Fuchsia's zxcrypt encryption subsystem can block dead-disk examination of MinFS partition content]]

## References

- [LWCite-1343] Jarrett and Morris, 2021, "Purple dawn: Dead disk forensics on Google's Fuchsia operating system", FSI: Digital Investigation 39, 301269.

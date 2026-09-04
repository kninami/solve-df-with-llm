---
id: LWT-1078
type: technique
name: Analyze a reverse-engineered vehicle RTOS file system and recover unallocated video frames
description: Recover data from a vehicle's built-in camera (dashcam/DVRS) onboard flash memory by reverse-engineering the manufacturer's real-time-operating-system-dedicated file system driver — since standard forensic file-system tools cannot read it — to parse log files, user-setting files, and video partitions across the system's multiple partitions, and additionally recover deleted video frames by searching for deletion-marked clusters within the unallocated area of the video storage partition and applying frame-by-frame reconstruction.
objective_ids:
  - DFO-1018
weakness_ids:
  - LWW-1084
aliases:
  - Reverse-engineered RTOS-dedicated vehicle file system analysis with unallocated-space video frame recovery
source_refs:
  - LWCite-1074
updated_at: 2026-08-10
status: complete
---

# Analyze a reverse-engineered vehicle RTOS file system and recover unallocated video frames

## Summary

Vehicle built-in cameras use real-time operating systems whose file systems are custom-built per manufacturer to guarantee real-time write/read performance and avoid the fragmentation that a general-purpose file system like FAT would suffer under continuous high-volume record-and-delete video workloads — as a result, mainstream forensic tools that only understand standard file systems cannot read the partitioned dedicated file system when the camera's own onboard flash must be extracted directly (e.g. because the camera circuit itself is damaged).

## Details

The method reverse-engineers the driver file in the system area to determine the dedicated file system's structure, enabling analysis of log files and user-setting files across multiple partitions recovered from onboard flash memory (e.g. eMMC). Beyond parsing allocated data, the method searches the unallocated area of the video-storage partition (the "CAM region") for clusters marked with deletion markers and applies frame-by-frame video reconstruction to those unallocated clusters, recovering additional deleted video frames beyond what the manufacturer's own analysis method or tooling would surface. The approach was validated by comparing results against the file system manufacturer's own analysis method, confirming equivalent baseline performance while adding this unallocated-space recovery capability.

## Examples

- Applied to a Hyundai/KIA/GENESIS built-in dashcam recording system (DVRS, installed across 34+ models released since 2019), the method recovered log files, WiFi connection passcodes, and additional deleted video frames from the unallocated area of the video partition beyond what standard extraction recovered.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Reverse-engineered RTOS-dedicated file system parsers are manufacturer- and model-specific and do not generalize across vehicle platforms]]

## References

- [LWCite-1074] Lee et al., 2023, "Analysis of real-time operating systems' file systems: Built-in cameras from vehicles", FSI: Digital Investigation 44.

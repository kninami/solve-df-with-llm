---
id: LWT-1082
type: technique
name: Date non-allocated-space data on recycled storage media using FSUB-based digital stratigraphy
description: Determine whether data recovered from non-allocated space on a removable storage device could plausibly have been created by the device's current file system, or must instead predate it (a remnant from the device's prior use before recycling), by calculating the File System Upper Bound (FSUB) — the largest block number the current file system has written to — since recovered data located below the FSUB was necessarily present before the current file system's own activity could have reached that block, applying the archaeological principle that lower/older strata predate upper/newer ones.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1088
aliases:
  - FSUB-based digital stratigraphy dating of non-allocated-space data on recycled storage media
  - Digital stratigraphy
  - FSUB
source_refs:
  - LWCite-1080
updated_at: 2026-08-10
status: complete
---

# Date non-allocated-space data on recycled storage media using FSUB-based digital stratigraphy

## Summary

When incriminating evidence is found in the non-allocated space of a second-hand or recycled-component device, it creates an attribution problem: did the current user create that data, or is it a remnant from the device's prior owner or use? Applying the archaeological concept of stratigraphy — that data positioned "below" the current file system's own written extent could not have been written by that file system — gives a defensible basis for arguing that data found above the FSUB is more likely attributable to current file-system activity, while data below it cannot be.

## Details

An automated File System Activity Simulation framework was built to carry out creation, deletion, and modification actions at scale using real file system drivers (Windows 11 and Debian 11), enabling sixty controlled experiments across FAT32, exFAT, and NTFS to characterize FSUB behavior. The FSUB is calculated from the highest allocation block among live files and deleted files with recoverable metadata. For FAT32, the technique was demonstrated to the point that a case could be made in a real scenario: carved content located below the FSUB, combined with the observation that old data below the FSUB on Windows FAT32 is confined to cluster slack (a bounded, small amount), supported an argument that specific recovered content was likely part of the current file system rather than a stratigraphically older remnant.

## Examples

- A visualization tool (df_digger) plotting carved data blocks relative to the calculated FSUB was used to distinguish a case where carved data fell entirely below the FSUB (consistent with a pre-existing remnant) from a case where carved data of interest fell within/above the FSUB, interleaved with current file system activity (supporting attribution to the current file system).

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/FSUB-based digital stratigraphy dating is less reliable for NTFS due to its non-linear cluster allocation algorithm]]

## References

- [LWCite-1080] Schneider et al., 2024, "Applying digital stratigraphy to the problem of recycled storage media", FSI: Digital Investigation 49.

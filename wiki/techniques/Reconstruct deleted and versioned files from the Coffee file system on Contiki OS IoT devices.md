---
id: DFT-1119
type: technique
name: Reconstruct deleted and versioned files from the Coffee file system on Contiki OS IoT devices
description: Recover live files, deleted files, and prior versions of both from a flash memory extraction of a resource-constrained IoT device running Contiki OS by parsing its custom Coffee file system's log/base sector structures via code review and emulator-derived understanding of its behavior, since Coffee is undocumented from a forensic standpoint and has no existing forensic tool support.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1124
aliases:
  - COFFOR
  - Coffee forensics
source_refs:
  - DFCite-1118
updated_at: 2026-08-12
status: complete
---

# Reconstruct deleted and versioned files from the Coffee file system on Contiki OS IoT devices

## Summary

Contiki OS (and its active fork Contiki-NG) targets resource-constrained IoT devices such as sensor and battery-powered systems, using its own Coffee file system whose on-flash structures were never documented for forensic purposes and for which no existing forensic tool provides support. Reverse-engineering Coffee's behavior via source code review and an emulator (running Coffee as a simulated Sky Mote in Cooja) enables systematic reconstruction of live files, deleted files, and — where flash sectors have not yet been erased — a chronological history of prior file versions from a raw flash extraction.

## Details

Coffee organizes files as base and log-file sector pairs; a file's contents change over time by appending new log entries rather than rewriting in place, and old sectors are only reclaimed (erased) once needed for new writes, meaning multiple historical versions of a file can coexist on flash until their sector is overwritten. The COFFOR tool implements reconstruction of both existing and deleted files by parsing these structures directly from an extracted flash image, and additionally implements a method for establishing the chronological order of a file's version history using content-difference comparison (via the `radiff2` tool's diff algorithms) between successive versions — since the file version order is fixed within a given sector but sector-erasure timing is not directly recorded, ordering across sectors otherwise cannot be inferred once intervening versions have been erased.

## Examples

- Given a raw flash memory extraction from an emulated Sky Mote running Contiki-NG, COFFOR reconstructed both the currently active files and prior deleted/superseded versions of the same files by parsing Coffee's base and log sector structures, without requiring any prior forensic documentation of the file system.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/Coffee file system version-ordering by content similarity fails once whole-file changes and intervening sectors are erased]]

## References

- [DFCite-1118] Sandvik et al., 2021, "Coffee forensics - Reconstructing data in IoT devices running Contiki OS", FSI: Digital Investigation 37.

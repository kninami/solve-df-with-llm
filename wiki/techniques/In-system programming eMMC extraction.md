---
id: DFT-1003
type: technique
name: In-system programming eMMC extraction
description: Perform a non-destructive teardown of an IoT smart device to locate the eMMC storage chip, mark In-System Programming (ISP) access points, and physically extract a forensically sound image without desoldering the chip.
objective_ids:
  - DFO-1021
weakness_ids:
  - DFW-1003
aliases:
  - ISP eMMC extraction
source_refs:
  - DFCite-1002
updated_at: 2026-08-09
status: complete
---

# In-system programming eMMC extraction

## Summary

The device is disassembled to expose the main logic board, the eMMC chip is located and briefly removed with hot air only to identify and mark its ISP access points, then reballed and reinstalled. An ISP adapter is soldered to the marked points so the eMMC can be read directly on the board with a chip reader, producing a physical image while preserving the device's functional condition.

## Details

This method avoids permanently desoldering the eMMC chip, which reduces risk to the device and supports repeatable, reproducible extraction across multiple units of the same model. It was used to extract 8-16GB eMMC storage from Amazon Echo Show devices at voltages/frequencies matched to the chip's rated interface (e.g., 1.8V, 36MHz, 1-bit bus). The resulting physical image can be analyzed with standard forensic tools to recover SQLite databases, logs, and other local artifacts, including data that a device's manufacturer states is never transmitted to the cloud.

## Examples

- Amazon Echo Show 15 (16GB eMMC, AMlogic Pop1-C processor): eMMC removed, ISP points marked, reinstalled, then imaged via ISP to recover Visual ID facial-recognition logs and SQLite databases.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/Visual ID facial recognition metadata is unavailable from provider cloud services]]

## References

- [DFCite-1002] Lorenz et al., 2026, "A case study on the use of Amazon visual ID facial recognition metadata in investigation", FSI: Digital Investigation 57.

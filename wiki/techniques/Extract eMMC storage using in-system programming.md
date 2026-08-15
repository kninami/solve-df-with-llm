---
id: DFT-1003
type: technique
name: Extract eMMC storage using in-system programming
description: Perform a non-destructive teardown of an IoT smart device to locate the eMMC storage chip, mark In-System Programming (ISP) access points, and physically extract a forensically sound image without desoldering the chip.
objective_ids:
  - DFO-1021
weakness_ids:
  - DFW-1003
aliases:
  - In-system programming eMMC extraction
  - ISP eMMC extraction
source_refs:
  - DFCite-1002
  - DFCite-1278
updated_at: 2026-08-14
status: complete
---

# Extract eMMC storage using in-system programming

## Summary

The device is disassembled to expose the main logic board, the eMMC chip is located and briefly removed with hot air only to identify and mark its ISP access points, then reballed and reinstalled. An ISP adapter is soldered to the marked points so the eMMC can be read directly on the board with a chip reader, producing a physical image while preserving the device's functional condition.

## Details

This method avoids permanently desoldering the eMMC chip, which reduces risk to the device and supports repeatable, reproducible extraction across multiple units of the same model. It was used to extract 8-16GB eMMC storage from Amazon Echo Show devices at voltages/frequencies matched to the chip's rated interface (e.g., 1.8V, 36MHz, 1-bit bus). The resulting physical image can be analyzed with standard forensic tools to recover SQLite databases, logs, and other local artifacts, including data that a device's manufacturer states is never transmitted to the cloud.

An earlier, broader family-of-experiments study established this methodology across seven Echo Show generations (1st through 10th generation) plus the Echo Spot, publishing a per-device tear-down diagram, video guide, and ISP pinout for each; it found the 1st-generation Echo Show the most labor-intensive to tear down (requiring heat to remove screws and cutting through soldered heat shields) while later generations (Echo Show 5/8) required only flipping the logic board with no heat needed. Because Echo Show devices lack a battery, an examiner can shut a device down forensically-soundly by simply pulling power (avoiding the mute-button shutdown procedure, which itself creates additional log entries and metadata), and because powering the eMMC without booting the device's own processor does not alter its stored data, the same eMMC chip can be reballed and reinstalled after ISP pinout identification to allow repeated seeding and re-extraction cycles for controlled testing rather than requiring a fresh physical device for every test scenario. On the newest Echo Show 10 (3rd generation), which has two independent eMMC chips (an 8GB chip for the main MediaTek processor and a 4GB chip for Amazon's own AZ1 Neural Edge co-processor, the latter storing locally-processed personalized content such as per-user word lists), both chips must be extracted via ISP independently, and grounding one chip's data line prevents that chip's processor from booting while the other is extracted, avoiding cross-contamination between the two simultaneous extractions. A parallel hash comparison between an ISP-based image and a chip-off image of the same device (with power never applied to the chip during either process) produced identical hashes, confirming ISP is forensically equivalent to chip-off when performed correctly.

## Examples

- Amazon Echo Show 15 (16GB eMMC, AMlogic Pop1-C processor): eMMC removed, ISP points marked, reinstalled, then imaged via ISP to recover Visual ID facial-recognition logs and SQLite databases.
- Across all seven tested Echo Show generations and the Echo Spot, ISP extraction (with the eMMC left in place, connected via soldered breakout wires to a flasher box) recovered a full physical image without powering on the device's own processor, preserving the device's exact seized state and avoiding any accidental logged events or deletions that would occur from booting.
- On the Echo Show 10 (3rd generation), independently ISP-extracting the 8GB MediaTek eMMC and the 4GB AZ1-connected eMMC (while grounding the other chip's data line to prevent it booting) recovered a personalized word list at `data\alexahybrid\files\AmModel\nlu-personalized.OFFLINE.en-US.7.125\vocab.syms` from the 4GB chip only, confirming Amazon's stated architecture that some user-content processing happens locally on the newer co-processor rather than solely in the cloud.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/Visual ID facial recognition metadata is unavailable from provider cloud services]]

## References

- [DFCite-1002] Lorenz et al., 2026, "A case study on the use of Amazon visual ID facial recognition metadata in investigation", FSI: Digital Investigation 57.
- [DFCite-1278] Lorenz, Stinehour, Chennamaneni, Subhani and Torre, 2023, "IoT forensic analysis: A family of experiments with Amazon Echo devices", FSI: Digital Investigation 45, 301541. Establishes the ISP tear-down and pinout methodology across seven Echo Show generations plus the Echo Spot, including eMMC reinstallation for repeated testing and dual-eMMC extraction on the Echo Show 10 (3rd generation).

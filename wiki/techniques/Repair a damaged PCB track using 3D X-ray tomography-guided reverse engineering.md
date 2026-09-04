---
id: LWT-1262
type: technique
name: Repair a damaged PCB track using 3D X-ray tomography-guided reverse engineering
description: Use medical-grade 2D and 3D X-ray equipment (repurposed dental and whole-body forensic-medicine scanners) to non-destructively diagnose a damaged electronic component's internal state, then reconstruct and trace a broken internal PCB track layer-by-layer through 3D tomographic reconstruction to physically repair it with a soldered copper-wire strap, restoring the board to a readable state without needing dedicated, expensive forensic X-ray or FIB equipment.
objective_ids:
  - DFO-1021
weakness_ids:
  - LWW-1274
aliases:
  - Medical X-ray equipment for forensic PCB reverse engineering
source_refs:
  - LWCite-1302
updated_at: 2026-08-14
status: complete
---

# Repair a damaged PCB track using 3D X-ray tomography-guided reverse engineering

## Summary

A digital investigator diagnosing a damaged electronic component follows the same four-principle X-ray workflow a forensic pathologist follows when scanning a body before autopsy — establish fixation, provide traceability, indicate the orientation of further work, and target areas of interest — and can use the same or equivalent equipment: a portable 2D dental X-ray unit for rapid on-scene triage of whether a component looks repairable, and a 3D micro-tomography scanner (the same technology used for whole-body forensic autopsy scanning) in the laboratory to non-destructively image a damaged PCB's internal copper layers, vias, and bonding wires in detail sufficient to reconstruct and trace a specific broken signal path for physical repair.

## Details

2D X-ray triage at the crime scene lets an investigator pre-sort damaged electronic evidence (a memory component, USB key, or IoT device) into repairable versus clearly unrepairable categories before committing laboratory resources, applying the broader forensic-science principle of evidence prioritization when time or resources are limited. In the laboratory, 3D X-ray tomography acquires many 2D radiographic projections of the component from different angles during a full rotation, then reconstructs a 3D volume via filtered back-projection (inverting the Radon transform), which can be navigated layer-by-layer to separate and individually inspect each copper layer of a multi-layer PCB. Once a defect (a cut track, delamination, or missing ball) is localized this way, the signal's routing is traced from the point of damage to a via or contact point large enough to solder onto reliably, the protective coating over that point is removed with a surgical blade, and a fine coated copper wire is soldered between the two ends of the broken path to restore electrical continuity — effectively "strapping" around the damage rather than needing to replace the entire component or board.

## Examples

- A damaged micro-SD card's memory die was diagnosed as unrepairable directly from a binocular-microscope inspection with no visible crack, but 3D X-ray tomography subsequently revealed the underlying PCB itself (not the die) had a cut track, which 2D imaging alone could not have distinguished from a die-level fault since it could not separate the individual copper layers.
- Tracing the damaged track's routing across both PCB copper layers in the reconstructed 3D volume identified two viable via contact points (2mm diameter, easier to solder reliably than the 0.75mm damaged track itself), and soldering a 1mm coated copper wire between them fully restored the card's readability.
- On a smartphone-scale multi-layer PCB (e.g. an iPhone 7 or Samsung Galaxy S7 with up to eight copper layers), the same tomography-and-strap-repair approach was noted to require substantially more operator judgment to trace a signal path through the additional layers than the simpler two-layer micro-SD card case study.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/X-ray exposure of multi-level flash memory can introduce uncorrectable bit errors]]

## References

- [LWCite-1302] Heckmann, Souvignet, Sauveron and Naccache, 2021, "Medical Equipment Used for Forensic Data Extraction: A low-cost solution for forensic laboratories not provided with expensive diagnostic or advanced repair equipment", FSI: Digital Investigation 36, 301092.

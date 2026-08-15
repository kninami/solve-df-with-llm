---
id: DFT-2039
type: technique
name: Diagnose damaged SD card failure modes using a non-invasive-to-invasive decision protocol
description: The process of localizing and characterizing the physical fault in a damaged SD/micro-SD memory card - before attempting repair or data extraction - by working through a decision diagram that applies non-invasive diagnostic techniques (optical inspection, 2D/3D X-ray, acoustic microscopy) first, escalating to invasive techniques (electrical tests, infrared thermal analysis, chemical decapsulation) only when the non-invasive stage is inconclusive.
objective_ids:
  - DFO-1021
weakness_ids:
  - DFW-2039
aliases:
  - SD card forensic diagnostic decision diagram
  - Infrared thermal analysis for SD card diagnostics
source_refs:
  - DFCite-2039
updated_at: 2026-08-14
status: partial
---

# Diagnose damaged SD card failure modes using a non-invasive-to-invasive decision protocol

## Summary

A damaged SD card (from an accident, crash, or a deliberate attempt to destroy evidence) needs its specific point of failure identified before an investigator can decide whether and how to repair it for data extraction. Rather than guessing or applying destructive techniques immediately, an investigator works through a structured decision diagram: optical inspection for visible cracks/corrosion, 2D/3D X-ray for internal structural anomalies, and acoustic microscopy for package delamination/moisture ingress, escalating only if inconclusive to invasive techniques - basic electrical (diode) tests for shorts/open circuits, infrared thermal imaging to spot abnormal heat during powered operation, and chemical decapsulation (fuming nitric acid or laser ablation) to physically expose the chips for direct inspection or reading.

## Details

DFCite-2039's protocol is organized as two linked decision sub-diagrams. The non-invasive branch starts with optical inspection (binocular microscope, checking for package cracks, PCB track cuts, and corrosion); if inconclusive, proceeds to 2D-then-3D X-ray (identifying structural anomalies like cracked dice or broken bondings, with 3D tomography needed to disambiguate overlapping layers in dense multi-die stacks, and optionally cross-referenced against known pinout-topology databases like "PC-3000 Flash" to reverse-engineer an unknown card's bus signals); and, where corrosion/humidity is suspected, scanning acoustic microscopy (immersing the sample and measuring acoustic-wave phase disturbance to detect package delamination). The invasive branch (requiring judicial authorization given the risk of altering evidence) starts with basic electrical diode tests on each input/output pin to locate a short or open circuit; if a suspected fault isn't visible on X-ray, infrared thermal imaging (a technique introduced for the first time in SD card forensics by this paper) captures a powered-on card's heat signature over time, comparing it against a known-good control sample to localize abnormal heat build-up (e.g. at a specific die's bondings); and, as a last resort, chemical opening removes the protective resin package (via localized fuming nitric acid application or laser ablation) to directly expose and inspect the chips.

## Examples

- DFCite-2039's real case study: an SD card with its plastic package already removed and no visible manufacturer markings was diagnosed via UHS-II bus topology (from 2D X-ray) to narrow its likely manufacturer, found no visible or 3D-X-ray-detectable defect, passed basic electrical diode tests (ruling out a short), and was then infrared-imaged during a controlled read operation - revealing an abnormal, continuously rising temperature at a specific point in the memory die's bondings not detectable by any prior non-invasive method, localizing the fault to a bonding-level defect.

## Related Objectives

- `DFO-1021` Access device data for acquisition

## Related Weaknesses

- [[weaknesses/Infrared diagnostic imaging of a damaged SD card risks creating or worsening the fault it is meant to locate]]

## References

- [DFCite-2039] Thomas-Brans et al., "New diagnostic forensic protocol for damaged secure digital memory cards", IEEE Access, 2022 — source of the decision-diagram protocol, the infrared thermal analysis technique, and the real case study described above.

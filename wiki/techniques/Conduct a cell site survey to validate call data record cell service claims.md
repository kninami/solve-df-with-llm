---
id: DFT-1109
type: technique
name: Conduct a cell site survey to validate call data record cell service claims
description: Physically measure, using a phone emulator, scanner, or software-controlled radio, which cells actually serve a location of interest at a given time, in order to test whether a call data record's recorded serving cell is consistent with a proposition about where a device was.
objective_ids:
  - DFO-1001
weakness_ids:
  - DFW-1114
aliases:
  - RF survey for cell site analysis
source_refs:
  - DFCite-1108
updated_at: 2026-08-12
status: complete
---

# Conduct a cell site survey to validate call data record cell service claims

## Summary

A cell site analysis (CSA) conclusion about whether a device could plausibly have been at a location depends on knowing which cells actually serve that location, since coverage cannot reliably be predicted from network topology alone. A survey directly measures this by deploying purpose-built equipment at or around the location and recording which cells respond.

## Details

Three equipment types are available, each with distinct trade-offs: a **phone emulator** behaves like a real handset (following the same cell selection/reselection protocols) and is realistic but network- and situation-specific, potentially selecting a different cell than the target device would have at the same location and time; a **scanner** does not authenticate to a network and instead reports all cells detected within a frequency range, avoiding selection bias but not indicating which cells a real phone would actually have used for service; and a **software-controlled radio (SCR)** attempts to emulate handset cell-selection algorithms across all technologies and bands simultaneously without being locked to a single network, combining some benefits of both. Surveys can further be conducted in idle mode (listening only, reflecting most of a device's actual operating time) or dedicated/connected mode (actively in a call, which can reveal different serving cells but samples less frequently), and as a static single-location measurement (fast but demonstrably susceptible to missing legitimately serving cells) or a dynamic movement-based survey (more thorough but slower and more equipment-intensive). No single survey method or equipment type is complete; the choice must be matched to the specific question being addressed (a "presumptive" test of what a CDR might show, versus testing an existing CDR against a specific proposition, versus assessing the discriminating precision of a finding).

## Examples

- A GSM network study using a single static-mode unit found only 6 of at least 11 legitimately serving cells detected at one device location, even with a sampling period of an hour, illustrating the false-negative risk of a minimal single-unit static survey.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Static single-location cell-site surveys are susceptible to false negatives that exclude legitimately serving cells]]

## References

- [DFCite-1108] Tart et al., 2021, "Cell site analysis: use and reliability of survey methods", FSI: Digital Investigation 38.

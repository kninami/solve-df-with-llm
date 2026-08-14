---
id: DFT-2020
type: technique
name: Apply a proactive-and-reactive digital forensic process to connected autonomous vehicle incidents
description: The process of investigating a connected autonomous vehicle (CAV) incident by combining a continuous proactive component (live collection of pre-defined, priority-ordered volatile data, automated preservation, and automated suspicious-event detection generating a preliminary report) with a traditional reactive component (identification, preservation, collection, analysis, and final report) that draws on the proactive component's findings.
objective_ids:
  - DFO-1015
weakness_ids:
  - DFW-2020
aliases:
  - CAV forensics functional process (proactive/reactive)
source_refs:
  - DFCite-2020
updated_at: 2026-08-14
status: partial
---

# Apply a proactive-and-reactive digital forensic process to connected autonomous vehicle incidents

## Summary

Because a CAV generates a large, heterogeneous volume of data across event data recorders, infotainment systems, ECUs, key fobs, multiple sensors, and journey logs - much of it volatile - waiting until after a crash or cyber incident to begin evidence collection risks losing the most useful data. An investigator instead treats CAV forensics as combining two parallel components: a proactive component that continuously and automatically collects, preserves, and screens data for suspicious events even before an incident is confirmed, and a reactive component that performs the traditional post-incident identification/preservation/collection/analysis/reporting workflow, informed by whatever the proactive component already captured.

## Details

DFCite-2020's proactive component has four phases: Proactive Collection (live collection of pre-defined data prioritized by volatility), Event Triggering Function (a mechanism deciding when to escalate), Proactive Preservation (automated evidence hashing and proactive collection of data tied to suspicious events), and Proactive Analysis (automated live analysis to construct a first hypothesis of the incident) - culminating in an automated Preliminary Report that becomes the reactive investigation's starting point. The reactive component follows the traditional digital forensics process (Identification, Preservation, Collection, Analysis, Final Report), applied to both static evidence (data remaining after an occurrence, e.g. hard-drive-equivalent storage) and dynamic/live evidence (data present during/after the occurrence). An "exit investigation" decision point allows the process to loop - continuing the investigation with further reactive work if the proactive/reactive findings are insufficient, or exiting once the case is resolved. Because CAVs lack their own concrete forensic standard, the paper recommends drawing transferable methodology from four adjacent branches: digital forensics generally, cyber-physical-system forensics, software reliability analysis (to reveal component-level weaknesses across manufacturers), and penetration testing (to assess CAV IoT-device attack surface).

## Examples

- DFCite-2020's automotive forensics model (Figure 6): A. Forensics Readiness (potential-source analysis, model/vehicle-series determination, interface/data-exchange-method evaluation, tool-set determination); B. Data Acquisition (data-source analysis, relevant-data filtering, timeline/evidence-trail creation); C. Data Analysis; D. Documentation - each phase producing its own documentation output.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/No standardized forensic framework or toolset exists for connected autonomous vehicles]]

## References

- [DFCite-2020] Sharma and Gillanders, "Cybersecurity and forensics in connected autonomous vehicles: A review of the state-of-the-art", IEEE Access, 2022 — source of the proactive/reactive functional process and automotive forensics model described above.

---
id: DFT-1049
type: technique
name: Apply a structured IoT-specific digital forensic process model
description: Investigate an IoT-related incident using a formal, phased digital forensic process model (identification, preservation, collection, examination, analysis, presentation) purpose-built or adapted for IoT's distinguishing characteristics — heterogeneous devices and protocols, high data volatility, resource-constrained hardware, and distributed architectures — rather than applying a general-purpose digital forensics process model unchanged.
objective_ids:
  - DFO-1015
weakness_ids:
  - DFW-1050
  - DFW-1080
aliases:
  - Structured IoT-specific digital forensic process model application
  - Concept methodology for conducting IoT investigations using a generic forensic model as a reference
  - MAoIDFF-IoT
  - Multi-level Artifact of Interest Digital Forensics Framework for IoT
source_refs:
  - DFCite-1040
  - DFCite-1070
  - DFCite-1159
  - DFCite-1241
updated_at: 2026-08-13
status: complete
---

# Apply a structured IoT-specific digital forensic process model

## Summary

A systematic literature review of 23 IoT-specific digital forensic process models, frameworks, conceptual models, and ontologies published between 2015 and 2024 found that roughly half used a "framework" style (organized, systematic structure for scalability and complexity handling) and nearly half used "concept templates" (semantic descriptions mapping forensic data such as sensor information, communication data, and logs), while methodologies proper (documented step-by-step procedures) were comparatively rare, together reflecting the diversity of approaches taken to adapt general digital forensic process theory to IoT's specific technical constraints.

## Details

Reviewed models varied in which of the six standard forensic phases (identification, preservation, collection, examination, analysis, presentation) they explicitly addressed and treated as critical: across the 23 studies, examination (65.22%) and preservation (60.87%) were most frequently flagged as critical or challenging phases, while identification (26.09%) was least frequently addressed in depth — several works note this is likely because the diversity and volume of IoT devices makes it a genuinely harder problem, not because it is less important. A smaller subset of reviewed models incorporate blockchain architecture (for evidence immutability and traceability) or formal ISO/IEC 27043:2015 alignment, and models varied in whether they addressed data privacy considerations distinct from evidence integrity.

**Multi-level Artifact-of-Interest framework (MAoIDFF-IoT)**: a distinct six-phase model — defining potential Artifact of Interest (AoI) locations, exploring the IoT environment, preparation, acquisition & preservation, examining & analyzing, and reporting, with documentation running throughout — investigates a device at up to three levels (device, network, application) rather than treating the device as a single undifferentiated evidence source. The environment-exploration phase systematically tabulates each component's expected artifacts, expected threats, and threat consequences before acquisition begins, and the examining/analyzing phase classifies every extracted item against an explicit Action/Detection matrix (missed artifact, no artifact, useful artifact, or artifact of interest) rather than an ad hoc relevant/irrelevant judgment. Applied at the network level to a Tapo C200 smart camera, the framework combined Wireshark (encrypted-traffic capture) with a Fiddler-based MITM proxy (installed as a trusted certificate on a rooted Android emulator) to decrypt otherwise TLSv1.2-encrypted camera-to-app traffic, recovering plaintext control-plane messages — device status, camera mode, an MD5-hashed login password, and per-action requests such as lens-movement and recording-toggle commands — even though the video stream itself remained encrypted and inaccessible via Wireshark alone.

## Examples

- Models reviewed include a fog-based IoT forensics investigation framework using middleware inspired by the 2001 DFRWS process model, an ISO/IEC 27043:2015-aligned generic digital forensic investigation framework for IoT, and a blockchain-based evidence framework using a graphical model to transform raw IoT device data into traceable, security-enhanced forensic information for police investigation.
- Applying MAoIDFF-IoT to the Tapo C200 smart camera across six designed scenarios (app connection, idle streaming, voice call, lens movement, recording, app restart) yielded a useful artifact or artifact of interest from Fiddler in every scenario, while Wireshark alone classified every scenario's traffic as a missed artifact (an undifferentiated TLSv1.2 "Encrypted Alert"), demonstrating that MITM decryption tooling choice — not just process-model phase discipline — determines whether an AoI is actually recovered at the network level.
- SIIFF (Service-Interconnectivity-based IoT Forensics Framework) extends the standard phase set with two additional phases — Identification of Interconnectivity and Integration and Correlation — run iteratively after the interpretation phase: an interconnectivity module examines interpreted evidence for signs that other IoT services or devices were involved, optionally triggers acquisition of new input data about those newly-identified things, and stores discovered relationships (source, target, and connection weight) in a normalized database for correlation with other identifiers (e.g. usernames, IDs, emails) during analysis. Applied to six interconnected-device scenarios on an Android companion-device, this recovered relationships such as an IFTTT automation linking a Twitter post to an Instagram cross-post.
- A separate six-phase concept proposal (Pre-Process, Identification, Acquisition & Preservation, Analysis, Evaluation, Presentation & Post-Process) adapts Du et al.'s conventional forensic model to IoT by promoting "Identification" to its own phase (given the far larger and more heterogeneous device population than conventional scenarios) and adding a distinct "Evaluation" phase after Analysis to link and cross-check evidence recovered from multiple devices across the network. During Identification, since an IoT device's typically small memory makes examining every discovered device impractical, the model proposes ordering devices by three parameters — the lifetime, quantity, and relevance of the data a device handles, its significance in the IoT environment, and whether it has an acquirable memory and how difficult that acquisition would be — before deciding which to examine first. For Acquisition & Preservation, it ranks non-volatile memory acquisition methods by forensic soundness from least to most invasive: read-only extraction/live acquisition (only if storage is removable), JTAG (harmless for soldered storage), In-System Programming (ISP, for eMMC/eMCP chips), and chip-off (highest risk of damaging device functionality); volatile memory acquisition is recommended live wherever feasible, since cooling-based alternatives require specialized equipment.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/Most published IoT digital forensic process models lack chain-of-custody support and empirical validation]]
- [[weaknesses/IoT interconnectivity identification finds no relationship when the connected service retains no interconnection traces]]

## References

- [DFCite-1040] Silva et al., 2025, "A review study of digital forensics in IoT: Process models, phases, architectures, and ontologies", FSI: Digital Investigation 53.
- [DFCite-1070] Kim et al., 2022, "An improved IoT forensic model to identify interconnectivity between things", FSI: Digital Investigation 44.
- [DFCite-1159] Castelo Gómez et al., 2021, "Developing an IoT forensic methodology. A concept proposal", FSI: Digital Investigation 36, 301114.
- [DFCite-1241] Salem and Hamarsheh, 2024, "Forensically analyzing IoT smart camera using MAoIDFF-IoT framework", FSI: Digital Investigation 51, 301829.

---
id: DFT-1073
type: technique
name: Assess and design for digital forensic readiness
description: Improve an organization's or system's digital forensic readiness (DFR) — its ability to maximize the use of digital evidence while minimizing the cost of an investigation — either after the fact, by assessing an existing organization's maturity against a structured domain/sub-domain commonalities framework, or up front, by integrating forensic requirements into a system's design and development lifecycle ("forensic-by-design") so that forensic readiness is built in rather than bolted on.
objective_ids:
  - DFO-1015
weakness_ids:
  - DFW-1078
  - DFW-1079
aliases:
  - Digital forensic readiness assessment and by-design frameworks
  - DFRCF
  - DFMM
  - Digital Forensic Readiness Commonalities Framework
  - Forensic-by-design
  - FbD
source_refs:
  - DFCite-1068
  - DFCite-1069
updated_at: 2026-08-10
status: complete
---

# Assess and design for digital forensic readiness

## Summary

Organizations that lack a way to measure or build in their forensic readiness are exposed to greater risk from cyber crime and to weaker evidentiary outcomes when an incident occurs. Two complementary approaches address this at different points in a system's lifecycle: a maturity-assessment model an existing organization can apply retrospectively, and a forensic-by-design framework that integrates forensic requirements into a system's engineering process from the start.

## Details

**Retrospective maturity assessment (DFRCF/DFMM)**: extends a Digital Forensic Readiness Commonalities Framework (DFRCF) with structured feedback from practicing forensic experts (comparative analysis of existing DFR frameworks plus semi-structured practitioner/academic interviews), then uses that structure to build a maturity assessment model (DFMM) styled on the Deming Plan-Do-Check-Act cycle, aligning with Rowlingson's forensic-readiness guidance and the NIST cybersecurity framework. Participants preferred a checklist-style assessment, though a hybrid checklist-plus-narrative approach was also proposed.

**Forensic-by-design (FbD)**: integrates forensic requirements as first-class factors throughout the Systems and Software Engineering (SE) lifecycle — precise system-structure knowledge, iterative/recursive application of SE processes, and rigorous verification/validation of forensic capability — rather than adding forensic readiness to an already-deployed system. A six-phase research methodology mapped Cloud Forensics challenges against prior FbD key factors, finding existing FbD proposals lacked SE-standard alignment (informed by ISO/IEC 42010:2011) and needed additional key factors (security, privacy, resiliency); the resulting framework remains generic but is emphasized for cloud computing systems.

## Examples

- The DFRCF/DFMM structure was validated against feedback from 10 interviewed forensic practitioners and academics, who reshaped several of the framework's domains before the final version was produced.
- A hypothetical case study involving a federal emergency/hazard monitoring cloud system drawing on data from multiple regional Intelligent Transportation Systems (ITS) illustrated where the FbD framework's continuous monitoring and evidence collection approach applies.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/DFR maturity assessment model structure was validated with only 10 practitioners and lacks practical field testing]]
- [[weaknesses/Forensic-by-design continuous monitoring is ineffective for cloud systems with open, cross-organizational or cross-jurisdictional boundaries]]

## References

- [DFCite-1068] Bankole et al., 2022, "An extended digital forensic readiness and maturity model", FSI: Digital Investigation 40.
- [DFCite-1069] Akilal and Kechadi, 2022, "An improved forensic-by-design framework for cloud computing with systems engineering standard compliance", FSI: Digital Investigation 40.

---
id: DFT-1154
type: technique
name: Allocate a digital forensic service level using a structured decision model
description: Route a digital forensic case to one of a defined hierarchy of "Service Levels" — from a brief consultation, through client-led screened data extraction, triage/preview examination, and up to a full standard, non-standard, or expert-evaluation examination — using a structured Service Level Allocator (SLA) decision model that questions the client about device type and investigative-data understanding, so that resources deployed match actual case need rather than defaulting to a full examination for every device.
objective_ids:
  - DFO-1005
weakness_ids:
  - DFW-1157
aliases:
  - Service Level Allocator
  - SLA decision model
  - DFS Service Levels framework
source_refs:
  - DFCite-1155
updated_at: 2026-08-12
status: complete
---

# Allocate a digital forensic service level using a structured decision model

## Summary

Digital forensic science (DFS) units face chronic demand that outstrips capacity, and defaulting every submitted device to a full forensic examination wastes scarce resources on cases that do not need it. This technique formalizes seven hierarchical Service Levels — ranging from Level 0 (consultation only) through Levels 1-3 (client-led/screened/triage extraction of increasing DFS-unit involvement) to Levels 4-6 (standard, non-standard, and expert-evaluation full examinations) — and provides a Service Level Allocator (SLA) decision model that a client works through to determine the appropriate level for their case.

## Details

The SLA begins with a foundational question (is the submitted device "standard" or "non-standard"?) and proceeds through client questions about their understanding of the relevant data types and their own ability to review data, ultimately allocating a Service Level. The SLA itself can only allocate Levels 0-3; where responses cannot resolve to one of those levels, the case is referred to a Level 0 consultation with a DFS practitioner, since that indicates the complexity or the client's own limited ability to specify requirements likely warrants a Level 4-6 examination that only a practitioner can properly scope. Levels 1-3 (client-led extraction, screened extraction, and triage/preview examination) are additionally bounded by explicit "person time" and "equipment engaged time" resource delimiters so that a lower-tier allocation cannot silently balloon into full-examination-equivalent effort. Non-standard devices always route to a Level 0 consultation, since specialist knowledge is assumed necessary to determine investigative opportunities and acquisition/examination processes for them.

## Examples

- A client submitting a standard smartphone who can precisely specify the relevant data types and has in-house review capability may be routed to Service Level 1 or 2 (data extraction with packaged/screened results, reviewed off-site by the client), avoiding DFS-unit examiner time entirely; a client submitting a non-standard IoT device, or unable to specify requirements, is routed via SLA referral to a Level 0 consultation, likely escalating to Level 4-6.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/Clients expand a resource-delimited digital forensic service level beyond its allocated remit]]

## References

- [DFCite-1155] Horsman, 2021, "Defining 'service levels' for digital forensic science organisations", FSI: Digital Investigation 38.

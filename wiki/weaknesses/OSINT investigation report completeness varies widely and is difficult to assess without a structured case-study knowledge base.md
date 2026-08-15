---
id: DFW-1295
type: weakness
name: OSINT investigation report completeness varies widely and is difficult to assess without a structured case-study knowledge base
description: Without a structured, ontology-backed record of what evidence, concepts, and tools a given type of case typically involves, investigators (and trainees) have no consistent way to tell whether their own investigation or report is complete, leading to widely varying report depth and quality driven by individual source access, tool familiarity, and departmental process differences rather than the actual demands of the case.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1296
source_refs:
  - DFCite-1327
updated_at: 2026-08-15
status: complete
---

# OSINT investigation report completeness varies widely and is difficult to assess without a structured case-study knowledge base

## Summary

Reviewing hundreds of student reports produced for the same standardized training case study, the researchers found substantial variation in depth and quality — some reports ran to only about 10 pages covering basic tools and simple findings, while others exceeded 100 pages with extensive tool usage — and explicitly note that several investigators had difficulty knowing what constituted a complete investigation or what information was missing. The identified causes were the diversity of accessible information sources, the variety and constant change of investigation tools, differing OSINT process models across departments, and individual investigator knowledge and experience.

## Why It Matters

Without a way to compare an in-progress investigation against a structured record of what a similar precedent case typically covered, an investigator cannot readily tell whether they have exhausted the relevant evidence sources and tool options for their case type, risking both wasted effort (re-deriving what is already documented) and missed evidence (not knowing a relevant source or tool category exists). This inconsistency also makes it difficult for a supervisor or reviewer to judge whether a submitted investigation report is genuinely complete or merely reflects the investigator's individual experience and available time.

## Related Mitigations

- [[mitigations/Query an ontology-backed case-study repository for the evidence and tool categories associated with the current case's concept types]]

## Used By

- [[techniques/Match a cybercrime investigation to precedent case studies using an OSINT-DFINT knowledge-map ontology]]

## References

- [DFCite-1327] Ngo and Le-Khac, 2023, "Ontology-based case study management towards bridging training and actual investigation gaps in digital forensics", FSI: Digital Investigation 47, 301621.

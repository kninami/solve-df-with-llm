---
id: DFM-1296
type: mitigation
name: Query an ontology-backed case-study repository for the evidence and tool categories associated with the current case's concept types
source_refs:
  - DFCite-1327
updated_at: 2026-08-15
status: complete
---

# Query an ontology-backed case-study repository for the evidence and tool categories associated with the current case's concept types

## Summary

Before closing out an OSINT investigation, query a structured, ontology-backed case-study knowledge base for the concept types present in the current case (e.g. images, social accounts, locations) to check which evidence categories and investigative tools precedent cases of the same type typically involved, rather than relying solely on individual training and experience to judge completeness.

## Addresses

- [[weaknesses/OSINT investigation report completeness varies widely and is difficult to assess without a structured case-study knowledge base]]

## How To Apply

Where [[techniques/Match a cybercrime investigation to precedent case studies using an OSINT-DFINT knowledge-map ontology]] (or an equivalent structured case-study repository) is available, identify the concept types present in the current investigation (suspect accounts, images, locations, communications) and query the repository for the tool and evidence categories associated with each concept type in precedent cases, before concluding the investigation is complete. Use any gap between the current case's coverage and the precedent-derived checklist as a prompt for further review, and document which precedent-suggested categories were checked versus deliberately not applicable, to make report completeness auditable rather than dependent solely on the individual investigator's experience.

## References

- [DFCite-1327] Ngo and Le-Khac, 2023, "Ontology-based case study management towards bridging training and actual investigation gaps in digital forensics", FSI: Digital Investigation 47, 301621.

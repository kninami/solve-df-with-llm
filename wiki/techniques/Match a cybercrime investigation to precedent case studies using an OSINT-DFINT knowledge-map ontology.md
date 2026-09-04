---
id: LWT-1285
type: technique
name: Match a cybercrime investigation to precedent case studies using an OSINT-DFINT knowledge-map ontology
description: Bridge the gap between abstract training case studies and the diverse, complex reality of actual cybercrime investigations by encoding a Digital Forensic Intelligence (DFINT) and Open Source Intelligence (OSINT) domain's entities, relationships, and evidence-source concepts into a formal ontology, then representing both training and real investigation cases as instances against that ontology so an investigator's current case can be matched to structurally similar precedent cases and their associated concepts, evidence types, and tools.
objective_ids:
  - DFO-1015
weakness_ids:
  - LWW-1295
aliases:
  - DFOSINT ontology
  - Case Study Browser
source_refs:
  - LWCite-1327
updated_at: 2026-08-15
status: complete
---

# Match a cybercrime investigation to precedent case studies using an OSINT-DFINT knowledge-map ontology

## Summary

Digital forensics training programs teach case study models drawn from a comparatively small number of real cases, described abstractly, while actual cybercrime investigations are far more diverse and complex — leaving investigators without immediate, concrete guidance on which tools and evidence types apply to their specific situation. Encoding a DFINT/OSINT domain ontology (concepts such as suspects, social accounts, evidence artifacts, and investigative tools, and the relationships between them) and representing case studies — both training scenarios and completed real investigations — as linked instances against it allows a new investigation to be matched against structurally similar precedent cases, surfacing the concepts, evidence types, and tools that precedent found useful.

## Details

Building on Hunton's six-stage cybercrime investigation process, entities and relationships (suspects, social media/email accounts, posted messages, images, geographic locations, and the specific investigative tools used to examine each) are extracted from investigation reports or training case narratives and stored as RDF triples in a knowledge-map repository (DFKMaps), linked to root concepts defined in a purpose-built DFOSINT ontology for the OSINT/DFINT domain. Because the ontology links concept types (e.g. "Image") to the categories of forensic tool typically used to examine them (e.g. EXIF metadata tools), an investigator working a new case who identifies an object of a given concept type (a suspect's photo, say) can query the ontology to see not just what one specific training case did with that object type, but the full range of tool options the ontology associates with it — broadening a trainee's fixed, single-tool training experience into an awareness of the available alternatives. A Case Study Browser prototype lets an investigator search and browse encoded case studies by concept and by role (e.g. "suspect," "victim," "tool used") rather than only by keyword.

## Examples

- The "Lorenzo" training case study (a threat posted to a personal website, investigated via OSINT to identify the poster and assess the threat) was encoded into the DFKMaps repository; querying the ontology for the "Image" concept type used in that case surfaced not just the `exiftool` the training exercise specifically taught, but a broader list of comparable EXIF-analysis tools (EXIF.tools, ExifyMe, Exif Fixer, XnView, PhotoME) the trainee had not been exposed to.
- Comparing hundreds of student investigation reports for the same Lorenzo training case study found substantial variation in report length, depth, and completeness (from roughly 10-page reports covering only basic tools to over 100-page reports), attributed to differences in the information sources accessible to each investigator, the variety and constant change of investigation tools, differing OSINT process models across departments, and individual investigator knowledge/experience.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/OSINT investigation report completeness varies widely and is difficult to assess without a structured case-study knowledge base]]

## References

- [LWCite-1327] Ngo and Le-Khac, 2023, "Ontology-based case study management towards bridging training and actual investigation gaps in digital forensics", FSI: Digital Investigation 47, 301621.

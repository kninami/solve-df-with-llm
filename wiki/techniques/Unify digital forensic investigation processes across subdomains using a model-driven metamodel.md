---
id: LWT-2023
type: technique
name: Unify digital forensic investigation processes across subdomains using a model-driven metamodel
description: The process of resolving process redundancy and terminology ambiguity across many subdomain-specific digital forensic investigation models (database, mobile, network, IoT, cloud, drone, computer forensics) by extracting their common investigation processes via a systematic literature review and organizing them into a three-level model-driven-engineering metamodel that practitioners can instantiate for a specific case.
objective_ids:
  - DFO-1015
weakness_ids:
  - LWW-2023
aliases:
  - Digital Forensics Metamodel (DFM)
source_refs:
  - LWCite-2023
updated_at: 2026-08-14
status: partial
---

# Unify digital forensic investigation processes across subdomains using a model-driven metamodel

## Summary

Because each digital forensics subdomain (database, mobile, network, IoT, and others) has independently produced its own investigation models with overlapping but inconsistently named processes and concepts, an investigator moving between subdomains, or an organization building cross-domain tooling, lacks a single reference structure. A model-driven-engineering (MDE) metamodel built by systematically extracting, merging, and grouping the common investigation processes across many subdomain models provides that single structure, letting practitioners instantiate a case-specific model from it rather than learning each subdomain's ad hoc process vocabulary separately.

## Details

LWCite-2023 builds its Digital Forensics Metamodel (DFM) through a six-step methodology: (1) detect and nominate DF subdomain models to include, using a coverage metric favoring models applicable to many subdomains; (2) extract each selected model's investigation processes, excluding those without a clear definition/activity/task and irrelevant processes; (3) merge and group extracted processes by shared semantic or functional meaning; (4) propose one common process per group, favoring the highest-frequency process name; (5) assemble the resulting common processes into the DFM; (6) validate the DFM's completeness, logicalness, and usefulness via two techniques - comparison against existing subdomain models, and face validity (confirmatory review by domain experts). The resulting three-level structure follows classic MDE layering: the M2-Level DFM itself (meta-classes/meta-operations/meta-attributes); the M1-Level of subdomain user models (mobile, database, network, computer, IoT, cloud, and drone forensics models, each an "instance of" the DFM); and the M0-Level of user data models (nine process-data-model categories: preparation, detection, preservation, analysis, examination, incident-responding, acquisition, reconstruction, and documentation data models), each an "instance of" its M1-Level model.

## Examples

- LWCite-2023's worked example instantiates an M1-Verification Model (for the scenario "is there evidence a development server was compromised while auditing was disabled?") with activities Isolate Database Server, Search Evidence, and Identify Investigation Source, then instantiates six concrete M0-level data models from it (Identify Investigation Source, Isolate Database Server, Seize Investigation Source, Incident Responding, Acquire, and Check Available Evidence data models).

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/The digital forensics metamodel has not been validated through application to a real investigative case]]

## References

- [LWCite-2023] Al-Dhaqm et al., "Digital forensics subdomains: The state of the art and future directions", IEEE Access, 2021 — source of the DFM three-level metamodel, its six-step construction methodology, and the database-compromise worked example described above.

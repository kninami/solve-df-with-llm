---
id: LWT-1218
type: technique
name: Build a phenomenon-specific cognitive map to guide cybercrime investigative actions
description: Encode the primary and secondary crime scenes of a cybercrime phenomenon (e.g. botnet crime) as a node-link cognitive map — a meso-level knowledge representation sitting between an abstract general process model and a specific case — so investigators can see which investigative measures are available, in what order, and what artifacts each measure is expected to yield.
objective_ids:
  - DFO-1005
weakness_ids:
  - LWW-1234
aliases:
  - Cognitive map (CM) of a digital crime scene
  - Phenomenon-specific knowledge representation for cybercrime investigation
source_refs:
  - LWCite-1248
updated_at: 2026-08-13
status: complete
---

# Build a phenomenon-specific cognitive map to guide cybercrime investigative actions

## Summary

General digital-forensic process models (e.g. the criminalistic cycle, the cybercrime investigation framework) operate at a high, macro level of abstraction, while real casework is highly specific. A cognitive map (CM) bridges this gap at an intermediate, meso level: for one recurring category of cybercrime phenomenon, it visualizes the primary and secondary crime scenes as a node-link graph encoding a qualitative "mental landscape" of available data sources, applicable investigative measures, and their resulting artifacts, without being tied to any one specific case.

## Details

The CM is built from a literature-grounded knowledge repository and then validated with domain experts. Nodes represent artifacts (e.g. a mailbox, an IP-address login record, a Skype account) and investigative measures (e.g. requesting records via mutual legal assistance, obtaining usage data from an ISP); edges represent which measures a given artifact enables and which further artifacts a measure is expected to produce, letting an investigator trace multiple possible evidentiary paths through a phenomenon rather than following a single fixed checklist. Because it operates one level of abstraction below a general process model, the CM can concretize what a phase like "identification" or "acquisition" actually means for a specific phenomenon, while still remaining reusable across many individual cases of that same phenomenon (as opposed to a fully case-specific evidence map). The approach was validated by interviewing domain experts about a CM for botnet crime built from published literature, and by applying it retrospectively to two real-world cases (the Seleznev and Yakubets prosecutions), in each of which the CM's investigative options matched the measures documented as actually used.

## Examples

- An exemplary botnet-crime CM was built from a literature-derived knowledge repository and validated for intersubjective correctness (91.7% of its concepts were independently mentioned by at least one of several interviewed domain experts, 87.5% by at least two) and completeness against expert knowledge.
- Applying the botnet-crime CM retrospectively to the U.S. prosecution of Maksim Yakubets showed the CM's mapped investigative chain — mutual-legal-assistance mailbox content requests, ISP usage-data/login-IP requests, and Skype-account attribution records — matched the measures documented as having actually identified the "aqua" moniker used by Yakubets.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/Phenomenon-specific cognitive maps omit follow-up investigative measures and non-technical case context]]

## References

- [LWCite-1248] Gruber et al., 2022, "Foundations of cybercriminalistics: From general process models to case-specific concretizations in cybercrime investigations", FSI: Digital Investigation 43, 301438.

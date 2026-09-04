---
id: LWT-2019
type: technique
name: Establish CPS forensic readiness using a proactive-protective-reactive evidence lifecycle
description: The process of preparing a cyber-physical system (CPS) for post-incident investigation by embedding evidence collection and preservation across the full attack lifecycle - forensics-by-design and pre-positioned forensic components before an attack, protective systems (intrusion detection/prevention, intruder entrapment) that double as real-time evidence collectors during an attack, and dedicated investigation tooling and provenance tracking after an attack.
objective_ids:
  - DFO-1015
weakness_ids:
  - LWW-2019
aliases:
  - CPS forensic readiness
  - Proactive-protective-reactive CPS forensics lifecycle
source_refs:
  - LWCite-2019
updated_at: 2026-08-14
status: partial
---

# Establish CPS forensic readiness using a proactive-protective-reactive evidence lifecycle

## Summary

Because CPS data (sensor readings, actuator states, control commands, and network traces) is volatile and can be overwritten or lost within moments of a compromise, waiting until after an incident to begin evidence collection - the traditional reactive digital-forensics model - loses the most revealing and perishable evidence. An investigator or CPS operator instead treats forensic readiness as a continuous design property, deploying evidence-preserving capabilities across three phases: proactive measures embedded before an attack, protective measures that double as evidence collectors during an attack, and reactive investigation tooling used after an attack.

## Details

LWCite-2019 organizes current CPS forensics research into: (1) proactive/before-attack measures - forensics-by-design (embedding evidence collection and preservation directly into a CPS's design and operation rather than as an afterthought), dedicated forensic components, and continuous data collection, plus pre-attack vulnerability discovery tools (e.g. FirmFuzz) that anticipate attack vectors and inform targeted logging; (2) protective/during-attack measures - intrusion detection and prevention systems and intruder-entrapment techniques (e.g. honeypots) that function not just as defenses but as primary real-time evidence collectors, capturing an intrusion's live methods and tools before an attacker can cover their tracks; (3) reactive/after-attack measures - network forensic tools adapted from IT environments (e.g. Wireshark, Bro/Zeek) to examine captured CPS communication channels, and provenance-tracking frameworks that convert raw logs into verifiable data-lineage graphs (via provenance adaptors, notification injectors, retrieval clients, and a provenance repository) linking cyber events to their physical consequences for incident timeline reconstruction. The paper's key insight is that meaningful CPS forensic analysis requires correlating cyber artifacts (logs, network traces) with physical evidence (sensor measurements, actuator states, environmental conditions) together, not in isolation.

## Examples

- LWCite-2019's Figure 14 taxonomy of "Current CPS Forensics Research Efforts" mapping forensics-by-design/forensic-components/data-collection (before), intrusion detection/prevention/intruder-entrapment (during), and investigation-tools/approaches/incident-representation (after) as the three phases of the readiness lifecycle.
- Figure 15's provenance-collection architecture (PoM log files -> provenance adaptor -> notification injector -> retrieval client -> provenance repository -> graph browser) for converting raw CPS logs into a verifiable, queryable data-lineage record.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/CPS forensic investigations analyze cyber and physical evidence in disjointed silos]]

## References

- [LWCite-2019] K et al., "Cyber physical systems security: Bridging privacy, verification, intelligence, and forensics", IEEE Access, 2026 — source of the three-phase forensic readiness lifecycle and provenance-tracking architecture summarized above.

---
id: LWT-1134
type: technique
name: Apply a directional, condition-based translation framework between TLP and law-enforcement handling codes in cross-sector cybercrime investigations
description: Before or during a cross-sector cybercrime investigation, apply a documented, direction-specific mapping between the private sector's Traffic Light Protocol (TLP) and law enforcement's EU H0-H3 handling codes, specifying who may share what with whom, under what conditions, and with what onward-dissemination constraints, so that information can move lawfully between incident responders and criminal investigators without harmonizing or replacing either classification scheme.
objective_ids:
  - DFO-1015
weakness_ids:
  - LWW-1137
aliases:
  - Directional, condition-based translation framework for TLP and H0-H3 information sharing
source_refs:
  - LWCite-1135
updated_at: 2026-08-12
status: complete
---

# Apply a directional, condition-based translation framework between TLP and law-enforcement handling codes in cross-sector cybercrime investigations

## Summary

Private-sector incident responders classify shared information using the Traffic Light Protocol (TLP: RED/AMBER/AMBER+STRICT/GREEN/CLEAR), while European law enforcement agencies classify information using the EU H0-H3 handling codes; the two schemes do not correspond one-to-one, and forcing every exchange through an ad-hoc judgment call creates friction, delay, and inconsistent handling in large, multi-partner cybercrime investigations. This technique instead documents, in advance, an illustrative direction-by-direction translation table (private sector to law enforcement, law enforcement to victim organization, law enforcement to CSIRTs, law enforcement to public) specifying the permissible recipients and legal/procedural conditions for each flow, without attempting to merge or standardize the two underlying classification systems.

## Details

The framework was derived from a retrospective qualitative case study of the 2019 LockerGoga ransomware investigation into Norsk Hydro, in which investigators found that restrictive default handling codes (particularly H1, "not to be disclosed in judicial proceedings without the provider's permission") on data received from cooperating countries or private partners could not immediately be used in the criminal case file, requiring formal mutual legal assistance requests that sometimes took up to two years to resolve. The translation table specifies, for each flow direction, the source classification level, the corresponding target classification level, the permissible recipients, and the conditions or legal basis required for onward dissemination (for example, TLP:AMBER shared by a private partner is normally handled as H0 once incorporated into a case, but may need explicit H1 "intelligence-only" marking and provider-approved handling instructions when the source itself is a foreign intelligence contribution). The paper positions this translation framework as one of four pillars of a proposed "Preparation phase" that should be added to the Integrated Cyber Investigation Process (ICIP) model, to be agreed between law enforcement, incident responders, and victim organizations before an incident occurs rather than negotiated reactively during one. A structured case management system (e.g. the Norwegian police's Indicia platform) that records the handling code alongside every ingested item was found to support this framework operationally by giving the investigative team full traceability of what data came from where and under which handling constraints.

## Examples

- In the Hydro investigation, cryptocurrency-exchange data and infrastructure logs shared by international partners under TLP:AMBER were, by default, treated cautiously as H1 by some contributing countries even where H0 (general case-file use) would have sufficed, requiring formal requests before the data could be used in the criminal case file — a delay the paper's proposed translation table is designed to reduce by clarifying the applicable condition in advance.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/Restrictive default information-sharing handling codes delay cross-border cybercrime evidence from becoming usable in judicial proceedings]]

## References

- [LWCite-1135] Heitmann and Johnsen, 2026, "Cybercrime investigations in practice: Insights from the LockerGoga ransomware attack on Norsk Hydro", FSI: Digital Investigation 57.

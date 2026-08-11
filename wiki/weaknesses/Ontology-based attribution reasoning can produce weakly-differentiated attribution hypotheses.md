---
id: DFW-1047
type: weakness
name: Ontology-based attribution reasoning can produce weakly-differentiated attribution hypotheses
description: When case-specific evidence is limited, an ontology-enhanced attribution reasoner can still generate multiple candidate attribution hypotheses using a large number of general background-knowledge rules that are not directly relevant to the investigated attack, producing a ranked top hypothesis whose score is only weakly better-supported than the alternatives rather than confidently distinguished from them.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1047
source_refs:
  - DFCite-1037
updated_at: 2026-08-09
status: complete
---

# Ontology-based attribution reasoning can produce weakly-differentiated attribution hypotheses

## Summary

In the paper's own SolarWinds evaluation, the enhanced reasoner produced three ranked hypotheses attributing the attack to CozyBear (scores of 5, 12, and 9) and two hypotheses for Lazarus Group (scores of 8 and 6), with the top CozyBear hypothesis (12) only modestly ahead of the alternatives. The authors explicitly note that in both the SolarWinds and Belgacom cases, "a large number of applied rules were not directly relevant to the investigated attacks, leading to attribution outcomes that were weakly supported by the available evidence."

## Why It Matters

If an investigator or analyst treats the top-ranked attribution hypothesis as a confident conclusion without examining how much of its score derives from case-specific evidence versus general background-knowledge rules, they risk overstating the strength of an attribution that is, in the system's own terms, only weakly supported. Because multiple candidates can score closely together, the numeric ranking alone does not convey how confidently the evidence actually discriminates between competing explanations.

## Related Mitigations

- [[mitigations/Report the full ranked hypothesis set and evidence-derivation basis rather than only the top attribution score]]

## Used By

- [[techniques/Ontology-based cyber-attack attribution reasoning]]

## References

- [DFCite-1037] Kaur Gill and Karafili, 2026, "A novel ontology for cyber-attack attribution and investigation", FSI: Digital Investigation 57.

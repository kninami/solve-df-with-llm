---
id: DFW-2034
type: weakness
name: Ontology-based cyber-attack detection cannot recognize attacks outside the modeled Cyber Kill Chain sequence or MITRE ATT&CK catalog
description: A CKC/MITRE-ATT&CK-ontology-based cyber-attack detection system can only detect attacks whose operation follows one of the model's defined phase combinations and uses techniques already cataloged in MITRE ATT&CK, so an attack that skips or reorders phases outside the modeled combinations, or that uses a genuinely new adversarial technique, goes entirely undetected.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2034
source_refs:
  - DFCite-2034
updated_at: 2026-08-14
status: partial
---

# Ontology-based cyber-attack detection cannot recognize attacks outside the modeled Cyber Kill Chain sequence or MITRE ATT&CK catalog

## Summary

The source paper states its own limitation plainly: "Fronesis detects any cyber-attack that follows a combination of the CKC phases (i.e., COSP) and utilizes adversarial techniques defined in the MITRE ATT&CK. Therefore, the limitation of Fronesis is that it cannot detect cyber-attacks that their operation cannot be described by the CKC model or use a new adversarial technique that is not defined in MITRE ATT&CK yet." Additionally, achieving complete coverage even within the modeled scope requires an impractically large rule set (over 2 million rules for full technique coverage across all four COSPs), so real deployments are expected to start with only the ~216 rules covering commonly used techniques, leaving less-common but still-cataloged techniques undetected in practice.

## Why It Matters

An investigator or defensive team relying on this class of ontology-based detection for early warning of ongoing attacks should not treat a "no detection" result as evidence no attack is occurring; an attacker using a technique not yet added to MITRE ATT&CK, or structuring their attack in a phase sequence the model does not recognize as a valid COSP, will pass through undetected regardless of how thoroughly the digital artifacts were collected, and a real deployment covering only commonly used techniques narrows this further.

## Related Mitigations

- [[mitigations/Regularly update the ATT&CK technique ruleset and pair ontology-based detection with anomaly-based detection for uncataloged attacks]]

## Used By

- [[techniques/Detect ongoing cyber-attacks using MITRE ATT&CK and Cyber Kill Chain ontological reasoning]]

## References

- [DFCite-2034] Dimitriadis et al., 2023 — Section III explicitly states the CKC-model/MITRE-ATT&CK-catalog detection limitation, and Section IV.B.4 quantifies the rule-count scalability challenge motivating a commonly-used-technique-first rollout.

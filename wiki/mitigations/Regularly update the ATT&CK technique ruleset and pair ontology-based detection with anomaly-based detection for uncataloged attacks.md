---
id: DFM-2034
type: mitigation
name: Regularly update the ATT&CK technique ruleset and pair ontology-based detection with anomaly-based detection for uncataloged attacks
source_refs:
  - DFCite-2034
updated_at: 2026-08-14
status: partial
---

# Regularly update the ATT&CK technique ruleset and pair ontology-based detection with anomaly-based detection for uncataloged attacks

## Summary

Do not rely on an ontology/CKC-based cyber-attack detection system as the sole detection layer; keep its rule set current as MITRE ATT&CK adds new techniques, prioritize rule coverage by technique prevalence in current threat reporting, and pair it with a complementary statistics-based or behavioral anomaly-detection layer that can flag suspicious activity even when it does not match a cataloged technique or a modeled CKC phase combination.

## Addresses

- [[weaknesses/Ontology-based cyber-attack detection cannot recognize attacks outside the modeled Cyber Kill Chain sequence or MITRE ATT&CK catalog]]

## How To Apply

Periodically regenerate or extend the detection ruleset as MITRE ATT&CK's technique catalog is updated, following the practice (also recommended by MITRE) of prioritizing commonly used techniques first given the impracticality of covering every technique combination. Deploy an anomaly- or behavior-based detection system alongside the ontology-based detector so that activity outside the modeled scope still has a chance of being flagged, and treat the ontology-based detector's silence as informative only within the bounds of its known coverage.

## References

- [DFCite-2034] Dimitriadis et al., 2023 — the paper's own future-work discussion identifies extending rule coverage and investigating machine-learning-based rule generation as directions to address the coverage-scalability limitation.

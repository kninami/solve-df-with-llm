---
id: DFW-1060
type: weakness
name: Blockchain-based IoT evidence management frameworks largely neglect legal and management readiness
description: A systematic review of blockchain-based IoT digital forensic frameworks found that the published literature substantially addresses technical readiness factors (data integrity, distributed storage, authentication, transparency, security) but largely overlooks legal/regulatory compliance and organizational-management readiness (leadership, policy, training) needed to actually deploy such a framework in a real investigation.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1060
source_refs:
  - DFCite-1050
updated_at: 2026-08-09
status: complete
---

# Blockchain-based IoT evidence management frameworks largely neglect legal and management readiness

## Summary

The authors state this directly: "legality and regulations of utilizing the Blockchain into the IoT forensics have been overlooked where more practical research work is required to address the legal and ethical evidence collection and chain of custody. Additionally, management is considered a key factor in Blockchain integration readiness where a thorough investigation will be conducted as future work." Legality/regulations covers the ethical and legal aspects of digital evidence collection and chain of custody specific to a jurisdiction; management covers organizational norms, training programs, and infrastructure needed to actually support digital forensics operations.

## Why It Matters

An organization evaluating a published blockchain-based IoT forensic framework for adoption may find strong technical coverage (integrity, storage, authentication, transparency, security) while the framework is silent on whether its evidence-handling approach is legally admissible in a given jurisdiction, or what organizational processes and training are needed to operate it correctly — gaps that only become apparent when actually attempting deployment, not from reading the technical description alone.

## Related Mitigations

- [[mitigations/Separately assess legal and management readiness before adopting a blockchain-based IoT evidence framework]]

## Used By

- [[techniques/Anchor digital evidence integrity and chain of custody on a blockchain]]

## References

- [DFCite-1050] Khanji et al., 2022, "A systematic analysis on the readiness of Blockchain integration in IoT forensics", FSI: Digital Investigation 42-43.

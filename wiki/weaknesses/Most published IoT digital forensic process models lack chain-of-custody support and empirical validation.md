---
id: DFW-1050
type: weakness
name: Most published IoT digital forensic process models lack chain-of-custody support and empirical validation
description: Across a systematic review of 23 IoT-specific digital forensic process models, frameworks, and ontologies, only 17.39% explicitly and substantively address chain of custody, and 52.17% present no empirical validation method (case study, simulated scenario, controlled experiment, or proof of concept) for their proposed approach, meaning the majority of published IoT forensic models cannot be assumed reliable or complete for real casework without independent verification.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1050
source_refs:
  - DFCite-1040
updated_at: 2026-08-09
status: complete
---

# Most published IoT digital forensic process models lack chain-of-custody support and empirical validation

## Summary

The review found that "although 60.87% of the studies mention the chain of custody (CoC), only 17.39% effectively integrate it into the evidence preservation phase," and that among studies mentioning CoC at all, several do so only superficially without formal introduction as a defined process step. Separately, 52.17% of studies presented no method for empirical validation of their proposed model, with only a minority using case studies (21.74%), simulated scenarios (8.70%), or controlled experiments (4.35%).

## Why It Matters

An investigator or organization selecting an IoT forensic process model to guide a real case cannot assume that a published model adequately addresses evidence integrity and continuity (chain of custody) or that its proposed procedures have been shown to work in practice, since this is true of only a minority of the reviewed literature. Adopting an unvalidated or CoC-silent model without independently verifying or supplementing these gaps risks producing an investigation whose evidence handling or procedural soundness could later be challenged.

## Related Mitigations

- [[mitigations/Verify chain-of-custody support and empirical validation before adopting an IoT forensic process model]]

## Used By

- [[techniques/Apply a structured IoT-specific digital forensic process model]]

## References

- [DFCite-1040] Silva et al., 2025, "A review study of digital forensics in IoT: Process models, phases, architectures, and ontologies", FSI: Digital Investigation 53.

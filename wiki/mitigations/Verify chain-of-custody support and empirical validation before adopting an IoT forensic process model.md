---
id: DFM-1050
type: mitigation
name: Verify chain-of-custody support and empirical validation before adopting an IoT forensic process model
source_refs:
  - DFCite-1040
updated_at: 2026-08-09
status: complete
---

# Verify chain-of-custody support and empirical validation before adopting an IoT forensic process model

## Summary

Before adopting a specific published IoT digital forensic process model or framework for a case, verify whether it explicitly and substantively addresses chain of custody and has been empirically validated (via case study, simulated scenario, or controlled experiment); where it falls short on either, supplement it with a general-purpose standard or manual procedures rather than relying on the model alone.

## Addresses

- [[weaknesses/Most published IoT digital forensic process models lack chain-of-custody support and empirical validation]]

## How To Apply

When selecting an IoT-specific process model for an investigation, check whether its published description formally defines a chain-of-custody step within evidence preservation (not merely a passing mention of the term) and whether the authors reported any empirical validation of the model against real or simulated cases. Where the chosen model is silent or thin on chain of custody, apply established general digital forensics chain-of-custody procedures (or a standard such as ISO/IEC 27043) alongside it rather than assuming the IoT-specific model's brevity on this point means it is unnecessary for the case at hand.

## References

- [DFCite-1040] Silva et al., 2025, "A review study of digital forensics in IoT: Process models, phases, architectures, and ontologies", FSI: Digital Investigation 53.

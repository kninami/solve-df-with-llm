---
id: LWM-1175
type: mitigation
name: Adopt a sampled accredited internal diligence disclosure model for forensic tool trustworthiness
source_refs:
  - LWCite-1170
updated_at: 2026-08-12
status: complete
---

# Adopt a sampled accredited internal diligence disclosure model for forensic tool trustworthiness

## Summary

Favor forensic tools whose producers participate in a Sampled Accredited Internal Diligence (SAID) scheme — where an independent third party samples and observes the producer's own testing and development regime without exposing full implementation detail — over tools that offer no disclosure or only a vendor-published specification sheet.

## Addresses

- [[weaknesses/Forensic tool producers' non-disclosure of verification evidence prevents end-users from establishing tool trustworthiness]]

## How To Apply

When selecting or approving a forensic tool for use, check whether the producer participates in an accredited third-party diligence scheme (SAID or stronger) rather than relying on claim-free release, a specification sheet alone, or undisclosed internal testing. Where no such disclosure exists for a tool already in use, document the resulting gap in the method-validation record and budget for supplementary independent testing (e.g. via NIST CFTT/Federated Testing where applicable) to partially offset the missing producer-side evidence.

## References

- [LWCite-1170] Marshall, 2021, "Digital forensic tool verification: An evaluation of options for establishing trustworthiness", FSI: Digital Investigation 38, 301181.

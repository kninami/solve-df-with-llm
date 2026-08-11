---
id: DFM-1079
type: mitigation
name: Identify and separately address open-boundary segments before relying on forensic-by-design continuous monitoring for a cloud system
source_refs:
  - DFCite-1069
updated_at: 2026-08-10
status: complete
---

# Identify and separately address open-boundary segments before relying on forensic-by-design continuous monitoring for a cloud system

## Summary

Before relying on a forensic-by-design framework's continuous monitoring and evidence collection to provide comprehensive coverage of a cloud system, explicitly map which components or data flows cross organizational or jurisdictional boundaries, and establish binding cross-party agreements — or plan a supplementary evidence-collection approach — for those specific boundary segments.

## Addresses

- [[weaknesses/Forensic-by-design continuous monitoring is ineffective for cloud systems with open, cross-organizational or cross-jurisdictional boundaries]]

## How To Apply

During the system-engineering design phase, produce an explicit boundary map identifying every point where the cloud system depends on a component, partner, or dataset outside the deploying organization's own control or jurisdiction. For each such boundary, either negotiate a binding monitoring/evidence-sharing agreement with the responsible party before deployment, or document the boundary as an acknowledged forensic gap requiring a different (reactive) evidence-collection approach rather than assuming forensic-by-design coverage extends across it.

## References

- [DFCite-1069] Akilal and Kechadi, 2022, "An improved forensic-by-design framework for cloud computing with systems engineering standard compliance", FSI: Digital Investigation 40.

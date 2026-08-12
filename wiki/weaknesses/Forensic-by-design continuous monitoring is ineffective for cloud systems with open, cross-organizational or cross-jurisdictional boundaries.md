---
id: DFW-1079
type: weakness
name: Forensic-by-design continuous monitoring is ineffective for cloud systems with open, cross-organizational or cross-jurisdictional boundaries
description: The system-engineering-integrated forensic-by-design framework's continuous evidence-monitoring and collection approach cannot be envisioned beyond a system's own organizational or software boundaries without clear, abiding cross-party agreements, and becomes substantially more complex — and potentially ineffective — for cloud systems whose components or data span multiple organizations or legal jurisdictions.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1079
source_refs:
  - DFCite-1069
updated_at: 2026-08-10
status: complete
---

# Forensic-by-design continuous monitoring is ineffective for cloud systems with open, cross-organizational or cross-jurisdictional boundaries

## Summary

The authors confirm this as one of their two starting hypotheses: forensic-by-design "is not effective for some open boundaries systems." Specifically, continuous monitoring beyond a system's own boundaries requires clear, binding agreements between the parties involved, and even where such agreements exist, the soundness of evidence collection and admissibility still depend entirely on the trustworthiness of the signatories — a dependency that becomes materially harder to satisfy once the system spans multiple jurisdictions.

## Why It Matters

An organization that adopts forensic-by-design expecting it to provide comprehensive, continuous evidentiary coverage for a cloud system built on components or partners outside its own organizational boundary may find significant, unaddressed forensic blind spots at exactly those boundaries — precisely the points where multi-tenant, multi-organization, or cross-border cloud architectures are most likely to need evidence in an investigation.

## Related Mitigations

- [[mitigations/Identify and separately address open-boundary segments before relying on forensic-by-design continuous monitoring for a cloud system]]

## Used By

- [[techniques/Assess and design for digital forensic readiness]]

## References

- [DFCite-1069] Akilal and Kechadi, 2022, "An improved forensic-by-design framework for cloud computing with systems engineering standard compliance", FSI: Digital Investigation 40.

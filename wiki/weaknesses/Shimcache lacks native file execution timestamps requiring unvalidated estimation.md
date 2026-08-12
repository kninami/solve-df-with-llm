---
id: DFW-1010
type: weakness
name: Shimcache lacks native file execution timestamps requiring unvalidated estimation
description: The Windows Application Compatibility Cache (Shimcache) does not itself record when a referenced file was executed, so any execution-time value derived from it is the output of an estimation algorithm whose accuracy has not been broadly validated across different Windows environments.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1010
source_refs:
  - DFCite-1005
updated_at: 2026-08-09
status: complete
---

# Shimcache lacks native file execution timestamps requiring unvalidated estimation

## Summary

Shimcache entries confirm that a file was present and referenced by the OS compatibility subsystem, but the artifact was never designed to log execution time. Approaches such as XTEC address this gap with an interval-estimation algorithm layered on top of Shimcache parsing, meaning any timestamp an investigator sees attached to a Shimcache-derived event is inferred rather than directly recorded by Windows.

## Why It Matters

Treating an estimated execution-time interval as if it were an authoritative logged timestamp risks introducing timeline errors into event reconstruction, particularly in cross-examination contexts where the provenance of a timestamp matters. The estimation algorithm's accuracy was demonstrated only within a specific case-study environment (a live-fire cyber defense exercise), so its interval precision may not generalize to other Windows versions, configurations, or system loads without further validation.

## Related Mitigations

- [[mitigations/Cross-validate Shimcache execution-time estimates against other artifacts]]

## Used By

- [[techniques/Estimate file execution times from Shimcache]]

## References

- [DFCite-1005] Dunsin et al., 2024, "A comprehensive analysis of the role of artificial intelligence and machine learning in modern digital forensics and incident response", FSI: Digital Investigation 48.

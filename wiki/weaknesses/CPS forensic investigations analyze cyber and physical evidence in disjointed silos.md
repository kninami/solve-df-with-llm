---
id: LWW-2019
type: weakness
name: CPS forensic investigations analyze cyber and physical evidence in disjointed silos
description: Existing cyber-physical-system forensic solutions generally address either cyber evidence (logs, network traces) or physical evidence (sensor measurements, actuator states) separately rather than in an integrated investigation, leaving investigators without a complete picture of how a cyber compromise produced a physical-world consequence.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2019
source_refs:
  - LWCite-2019
updated_at: 2026-08-14
status: partial
---

# CPS forensic investigations analyze cyber and physical evidence in disjointed silos

## Summary

The source survey's own CPS-forensics gaps discussion states plainly that "existing solutions are generally disjointed, only tackling either cyber evidence or physical evidence, but not the two in an integrated approach to the investigation." It further notes there is no accepted standard for CPS forensics, so practitioners use inconsistent methodologies, which has reduced the admissibility of resulting evidence in legal or regulatory situations, and that many existing CPS forensic tools still require manual extraction and analysis rather than automated, integrated correlation.

## Why It Matters

A CPS incident (e.g. a manipulated sensor reading causing an unsafe actuator command) only makes full sense when its cyber trace (the falsified data, the network path it traveled, the log entries around it) is correlated with its physical trace (the actual sensor/actuator state and environmental conditions at the time). An investigator who examines only the cyber logs or only the physical telemetry in isolation risks reconstructing an incomplete or misleading account of what happened and why, and risks producing evidence whose admissibility is undermined by the lack of a standardized, integrated methodology.

## Related Mitigations

- [[mitigations/Correlate cyber logs with physical sensor and actuator evidence using a provenance-tracking data lineage graph]]

## Used By

- [[techniques/Establish CPS forensic readiness using a proactive-protective-reactive evidence lifecycle]]

## References

- [LWCite-2019] K et al., 2026 — Section VIII.D "Gaps & Future Work" explicitly lists disjointed cyber/physical evidence handling, inconsistent methodologies, and manual/non-automated tooling as unresolved CPS forensics challenges.

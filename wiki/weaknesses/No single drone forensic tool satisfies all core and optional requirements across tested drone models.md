---
id: DFW-1178
type: weakness
name: No single drone forensic tool satisfies all core and optional requirements across tested drone models
description: When systematically tested against a specification of drone-relevant artifact-category requirements, no individual drone forensic tool satisfies every applicable requirement across all tested drone models, and support for newer or less common models is often incomplete or missing entirely.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1178
source_refs:
  - DFCite-1179
  - DFCite-1180
updated_at: 2026-08-12
status: complete
---

# No single drone forensic tool satisfies all core and optional requirements across tested drone models

## Summary

Applying the CFTT-aligned drone forensic tool testing methodology to commercial, open-source, and web-based tools against DJI drone models, the authors report as a headline finding that "no single tool satisfied all applicable requirements across all tested drone models," with notably inconsistent support for a newer model (DJI Mini 3 Pro) whose flight-log format and model-specific data structures were not fully handled by any tested tool. This gap was independently identified as a structural problem for the field by a contemporaneous survey, which found that "there is currently no standardised benchmarking framework to evaluate [drone forensic tools'] forensic reliability or operational effectiveness," leaving law enforcement agencies "limited ability to compare tools beyond functionality descriptions or anecdotal use cases."

## Why It Matters

An investigator who selects a single drone forensic tool based on its general reputation or vendor claims risks either missing artifact categories the tool does not fully support, or missing model-specific data structures for newer or less common drones, without necessarily being alerted to the gap — this is a direct threat to completeness of the resulting evidence set and, per the corroborating survey, to procurement decisions and admissibility arguments that currently have no standardized empirical basis to draw on.

## Related Mitigations

- [[mitigations/Re-validate drone forensic tool conformance against each target drone model or firmware release using the specification's test cases]]

## Used By

- [[techniques/Validate a drone forensic tool's conformance using a CFTT-aligned specification]]

## References

- [DFCite-1179] Lee et al., 2026, "Drone forensic tool testing: Methodology and applications", FSI: Digital Investigation 58. Reports that no tested tool satisfied all applicable requirements across all tested drone models, with the DJI Mini 3 Pro notably underserved.
- [DFCite-1180] Thantilage et al., 2025, "Drone forensics in law enforcement: Assessing utilisation, challenges, and emerging necessities", FSI: Digital Investigation 55. Independently identifies the absence of a standardised benchmarking framework for drone forensic tools as a barrier to trust, admissibility, and procurement.

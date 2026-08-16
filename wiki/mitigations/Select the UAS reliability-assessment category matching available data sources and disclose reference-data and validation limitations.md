---
id: DFM-2105
type: mitigation
name: Select the UAS reliability-assessment category matching available data sources and disclose reference-data and validation limitations
source_refs:
  - DFCite-2122
updated_at: 2026-08-16
status: complete
---

# Select the UAS reliability-assessment category matching available data sources and disclose reference-data and validation limitations

## Summary

When assessing UAS data reliability using [[techniques/Assess UAS sensor data reliability using a source-count-tiered evaluation framework]], select the category (single-source, multi-UAS-source, or UAS-plus-external-source) matching what data is actually available for the case, and explicitly disclose where reference data is inadequate (particularly for DIY drones) or where the underlying framework itself remains empirically unvalidated against real-world case data.

## Addresses

- [[weaknesses/UAS data reliability assessment lacks reference models and validated methods for DIY drones]]

## How To Apply

Before applying a Category 1 or Category 2 method, confirm adequate reference data or a validated system model actually exists for the specific UAS in question; for a DIY drone, actively search for a documented reference model or comparable published case study before assuming one is available, and if none can be found, document this gap rather than proceeding with an unsupported reference assumption. Prefer Category 3 (similarity analysis against an independent external measurement system) where such external observations exist, since it does not depend on a matched reference model for the UAS itself. In any report presenting a conclusion derived from this framework, disclose that the framework's own real-world validation is limited to a fictitious application example at the time of its publication, and treat resulting reliability conclusions as provisional pending further empirical validation of the framework itself.

## References

- [DFCite-2122] Lohre, Baier, Hardi, and Attenberger, 2025, "Towards reliable data in the scope of unmanned aircraft systems", FSI: Digital Investigation 53, 301914.

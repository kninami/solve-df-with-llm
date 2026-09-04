---
id: LWW-2104
type: weakness
name: UAS data reliability assessment lacks reference models and validated methods for DIY drones
description: Applying likelihood-ratio, signal-quality, sensor-cross-validation, state-estimation, or similarity-analysis methods to assess UAS data reliability requires reference data, reference models, or ground truth with distributional properties matching the actual UAS, but Do-It-Yourself drones -- built from individually varying components with no standardized reference model -- are especially difficult to find or generate suitable reference data for, and the framework proposing these methods has not yet been empirically validated against real-case UAS data at all.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - LWM-2105
source_refs:
  - LWCite-2122
updated_at: 2026-08-16
status: complete
---

# UAS data reliability assessment lacks reference models and validated methods for DIY drones

## Summary

Every category of the UAS reliability-assessment framework depends on some form of reference: Category 1's likelihood-ratio approach needs reference/experimental data with matching distributional properties, Category 2's state-estimation approach needs a system model whose accuracy depends on the chosen model-driven/data-driven/hybrid method actually matching the target system's real behavior, and Category 3's similarity analysis needs an available external measurement system, which is not guaranteed to exist for a given case. For commercial drones from established manufacturers, published specifications and prior case studies can sometimes supply this reference; for DIY drones, whose components and configuration vary individually with no comparable manufacturer specification or published case-study base, generating or locating adequate reference data is substantially harder. The framework's authors additionally state explicitly that the framework itself has only been demonstrated on a fictitious example and has not yet been validated against real-world UAS case data.

## Why It Matters

An investigator applying this reliability-assessment framework to a DIY-drone case may find no adequate reference model or dataset exists to support a Category 1 or Category 2 method with confidence, and even where a method is applied, the framework's own lack of real-world validation means the resulting reliability conclusion's own accuracy has not itself been empirically established. Presenting a reliability assessment derived from this framework without disclosing both the DIY-drone reference-data gap (where applicable) and the framework's current validation status risks overstating the confidence a court or investigator should place in the resulting conclusion.

## Related Mitigations

- [[mitigations/Select the UAS reliability-assessment category matching available data sources and disclose reference-data and validation limitations]]

## Used By

- [[techniques/Assess UAS sensor data reliability using a source-count-tiered evaluation framework]]

## References

- [LWCite-2122] Lohre, Baier, Hardi, and Attenberger, 2025, "Towards reliable data in the scope of unmanned aircraft systems", FSI: Digital Investigation 53, 301914.

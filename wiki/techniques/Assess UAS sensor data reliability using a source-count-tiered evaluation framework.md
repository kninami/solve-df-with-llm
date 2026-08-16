---
id: DFT-2098
type: technique
name: Assess UAS sensor data reliability using a source-count-tiered evaluation framework
description: Assess how much confidence to place in data recovered from an Unmanned Aircraft System (UAS/drone) by selecting a reliability-assessment method matched to how many independent data sources are actually available -- a single-source category using a likelihood ratio or signal quality estimation, a multi-UAS-source category using sensor cross-validation or state estimation, or a UAS-plus-external-source category using similarity analysis against an independent external measurement system -- rather than applying a one-size-fits-all reliability check regardless of what evidence the case actually has available.
objective_ids:
  - DFO-1001
  - DFO-1004
weakness_ids:
  - DFW-2104
aliases:
  - UAS data reliability conceptual framework
source_refs:
  - DFCite-2122
updated_at: 2026-08-16
status: complete
---

# Assess UAS sensor data reliability using a source-count-tiered evaluation framework

## Summary

Unlike classical operating systems and smartphones, Unmanned Aircraft System (UAS) sensor data (position, altitude, velocity, and other flight telemetry from accelerometers, gyroscopes, GNSS, and similar components) lacks a well-understood reliability baseline, particularly for Do-It-Yourself (DIY) drones where reference models and prior case studies are scarce. A three-category conceptual framework matches the reliability-assessment method to the quantity of available data sources: Category 1 (a single data source) uses likelihood-ratio or signal-quality-estimation methods; Category 2 (multiple observations from within the UAS itself) uses sensor cross-validation or state estimation; and Category 3 (UAS observations plus an independent external measurement system) uses similarity analysis, since a higher category's methods are not usable when only fewer data sources are actually available.

## Details

**Category 1 (single source)**: the Likelihood Ratio (LR) approach formulates two competing hypotheses about the information of interest (e.g. the UAV was at altitude A1 versus A2 at time t) and computes the relative probability of the observed evidence under each, using reference/experimental data to model the evidence's probability density under each hypothesis -- directly analogous in structure to [[techniques/Evaluate iPhone Health app distance data using a likelihood ratio]] but applied to UAS telemetry; Signal Quality Estimation (SQE) instead evaluates the measurement signal itself (via filtering/signal-processing analysis or Signal Quality Indices covering statistical, frequency, or entropy-based signal characteristics) to judge whether it is corrupted or degraded, noting that high signal quality does not by itself rule out a sophisticated spoofing attack, which requires a separate Signal Quality Monitoring approach specifically. **Category 2 (multiple UAS-internal sources)**: Sensor Cross-Validation compares redundant sensors measuring the same target variable (e.g. multiple accelerometers or GNSS receivers) directly, or reconstructs the information of interest from a different measuring instrument entirely (e.g. reconstructing altitude via visual odometry from onboard camera footage) to check for consistency with a directly-measured value; State Estimation instead treats the information of interest as an unobservable "hidden state" of a mathematical/physical process and uses a state-estimation method (model-driven, e.g. a Kalman filter family method matched to the system's linearity/noise characteristics; data-driven, e.g. a trained deep-learning model; or hybrid) to predict the expected state and compare it against the actually-observed measurement, treating a significant deviation as an inconsistency reducing reliability. **Category 3 (UAS plus external source)**: Similarity Analysis combines UAS-internal data sources with an External Measurement System's observations (e.g. camera, microphone, radar, or Remote ID receiver recordings from a third party such as a witness or another aircraft) through preprocessing/fusion, temporal synchronization, and a similarity-scoring comparison across the fused sources, with low similarity between the UAS's own account and the external observations taken as an indicator of reduced reliability -- this category is available only when independent external observations of the UAS exist, but represents the framework's strongest evidentiary configuration when they do.

## Examples

- A worked fictitious example (helicopter pilots reporting sighting a UAV that disturbed their rescue mission, versus the identified drone pilot denying the UAV was at the reported altitude) illustrates all three categories against the same underlying dispute: Category 1 assesses only the drone's own barometer-derived altitude log via LR or SQE; Category 2 additionally reconstructs altitude from onboard video via visual odometry and cross-validates it against the flight log; Category 3 further incorporates the helicopters' own black-box collision-avoidance data as an External Measurement System, checking similarity between the drone's account and the helicopters' independent observations.

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/UAS data reliability assessment lacks reference models and validated methods for DIY drones]]

## References

- [DFCite-2122] Lohre, Baier, Hardi, and Attenberger, 2025, "Towards reliable data in the scope of unmanned aircraft systems", FSI: Digital Investigation 53, 301914.

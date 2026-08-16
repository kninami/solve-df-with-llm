---
id: DFT-2076
type: technique
name: Select a source camera identification method using the verification, identification, and exploration problem-class framework
description: Before applying a source camera identification (SCI) method, classify the investigative question into one of three formal problem classes -- Verification (does this specific image come from this specific device?), Identification (which device, among a candidate set, produced this image?), or Exploration (what can be inferred about an unknown device's type/model from this image?) -- and the target into one of four granularity levels (Physical Device, Configured Device, Virtual Model, or Physical Model), then select and evaluate an SCI method against the metrics appropriate to that specific problem class and target rather than assuming a method validated for one combination transfers to another.
objective_ids:
  - DFO-1004
  - DFO-1008
weakness_ids:
  - DFW-2078
aliases:
  - Source Camera Target Model
  - SCTM
source_refs:
  - DFCite-2089
updated_at: 2026-08-16
status: complete
---

# Select a source camera identification method using the verification, identification, and exploration problem-class framework

## Summary

Source camera identification (SCI) research spans a wide range of actual investigative questions and evaluation methodologies, but the field has generally treated sensor pattern noise (SPN)-based methods as a de facto "gold standard" without a shared, formal framework for what target and problem type a given method or metric actually addresses. This technique introduces the Source Camera Target Model (SCTM) and a three-class problem taxonomy (Verification, Identification, Exploration) so that an investigator or researcher can match an SCI method to the actual question being asked, and evaluate it using metrics appropriate to that specific combination.

## Details

The SCTM defines four levels of target granularity, from most specific to most general: a **Physical Device** (the literal, individual camera unit that captured an image); a **Configured Device** (a physical device in a specific hardware/firmware/settings configuration, since the same physical device can behave differently across configurations); a **Virtual Model** (all devices sharing a given make/model, independent of any specific physical unit); and a **Physical Model** (a manufactured product line, encompassing hardware/firmware revisions across a model's production run). Independently, the technique defines three problem classes: **Verification** asks whether a specific image was captured by a specific target (a 1:1 comparison, the class SPN-based methods were originally designed and validated for, typically against the Physical Device level); **Identification** asks which device, among a closed or open set of candidates, produced a given image (a 1:N comparison, relevant when a suspect's device set is known but which specific device captured a given image is not); and **Exploration** asks what can be inferred about an image's unknown source device without any candidate set at all (e.g. inferring model or brand from an image alone, relevant in open-source intelligence or when no physical device has been recovered). Because a method's precision, recall, and error-rate characteristics measured for one problem-class/target-granularity combination do not necessarily hold for another, the framework recommends explicitly stating which combination a given SCI method or evaluation targets before applying its published performance figures to a new investigative question.

## Examples

- A survey of the SCI literature found the substantial majority of published SPN-based work validated against the Verification problem class at the Physical Device target level, using datasets and camera hardware that are now outdated relative to contemporary smartphone camera pipelines, leaving the Identification and Exploration problem classes, and the Virtual Model/Physical Model target levels, comparatively under-validated.
- The framework highlights that an investigator applying SPN verification metrics (e.g. a false-acceptance/false-rejection-rate pair validated for 1:1 Physical Device verification) to an Identification-class question (which of N candidate devices produced this image) or an Exploration-class question (what model camera produced this image, with no candidate device at all) is applying performance figures outside the context in which they were established.

## Related Objectives

- `DFO-1004` Conduct research
- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Sensor-pattern-noise source camera identification is validated almost exclusively for the verification problem class on outdated hardware]]

## References

- [DFCite-2089] Klier and Baier, 2024, "Source Camera Identification - Do we have a gold standard?", FSI: Digital Investigation 52, 301858.

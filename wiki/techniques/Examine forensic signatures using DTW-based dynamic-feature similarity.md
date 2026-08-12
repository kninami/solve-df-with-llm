---
id: DFT-1071
type: technique
name: Examine forensic signatures using DTW-based dynamic-feature similarity
description: Support a forensic handwriting examiner's determination of whether a digitally-captured signature (including a disguised signature) is genuine or imitated by computing Dynamic Time Warping (DTW) alignment distances between the questioned signature's easy-to-derive dynamic features (velocity, acceleration, pressure, displacement over time) and a set of comparative genuine specimens, producing a reproducible, explainable numerical similarity score rather than relying on a black-box biometric classifier.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1076
aliases:
  - DTW-based dynamic-feature similarity decision support for forensic signature examination
source_refs:
  - DFCite-1066
updated_at: 2026-08-10
status: complete
---

# Examine forensic signatures using DTW-based dynamic-feature similarity

## Summary

Advanced biometric signature-verification systems are often accurate but function as unexplainable black boxes, which forensic handwriting examiners are reluctant to rely on for casework. Using Dynamic Time Warping — a simple, well-understood time-series alignment technique — on a small set of intuitively meaningful dynamic features gives examiners an objective, reproducible, and easy-to-explain decision support signal, intended to complement rather than replace their traditional qualitative evaluation.

## Details

For each dynamic feature (velocity, acceleration, pressure), DTW computes an alignment distance between the questioned signature and each comparative genuine specimen; per-feature distances are combined via a majority-voting strategy to reach an overall genuine/imitated classification, and the method was also evaluated on disguised (self-distorted) signatures, an especially subtle case for both traditional and automated evaluation. Feature importance analysis found acceleration and pressure the most discriminating features for correctly recognizing genuine signatures, while velocity and acceleration were most discriminating for correctly flagging imitations (pressure became "confusing" for imitation detection). A blind qualitative evaluation by independent forensic handwriting examiners found the tool useful as an additional support signal in ambiguous cases, without being intended to override an examiner's own traditional evaluation.

## Examples

- Across the test dataset, the method achieved a 78.5% true negative rate (correctly flagging imitations) and an 87.7% true positive rate (correctly recognizing genuine signatures) using the majority-voting combination of all three dynamic features.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/DTW-based signature verification misclassifies roughly one in five imitated signatures as genuine]]

## References

- [DFCite-1066] Mazzolini et al., 2021, "An easy-to-explain decision support framework for forensic analysis of dynamic signatures", FSI: Digital Investigation 38.

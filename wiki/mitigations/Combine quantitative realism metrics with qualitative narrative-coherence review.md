---
id: LWM-1041
type: mitigation
name: Combine quantitative realism metrics with qualitative narrative-coherence review
source_refs:
  - LWCite-1031
updated_at: 2026-08-09
status: complete
---

# Combine quantitative realism metrics with qualitative narrative-coherence review

## Summary

Treat quantitative disk-image realism metrics as a necessary but not sufficient check; pair them with a qualitative review of the scenario's narrative coherence before relying on a synthetic dataset as fully realistic.

## Addresses

- [[weaknesses/Quantitative disk-image realism metrics cannot detect narrative incoherence in synthetic scenario data]]

## How To Apply

After a synthetic disk image passes quantitative realism benchmarking (comparing configuration, longevity, activity, and volume metrics against real-world reference distributions), have a domain-knowledgeable reviewer separately assess whether the underlying investigative scenario and its artifacts are internally consistent and plausible — for example, whether the "storyboarding" and construction stages described in prior scenario-design work were followed, and whether an examiner could form a coherent hypothesis from the artifacts without encountering contradictions. Document both the quantitative and qualitative assessment results together when publishing or reusing a synthetic dataset for research or training.

## References

- [LWCite-1031] Voigt et al., 2025, "A metrics-based look at disk images: Insights and applications", FSI: Digital Investigation 52.

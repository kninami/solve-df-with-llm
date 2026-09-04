---
id: LWW-1309
type: weakness
name: Feature-based tampering recognition does not weight how strongly a feature indicates tampering versus non-tampering
description: The inductive feature-analysis algorithm treats every characterized feature of a tampering action as an equally significant indicator, rather than weighting features by how strongly each one actually indicates tampering versus non-tampering, so a case whose evidence weakly matches several features could be treated the same as one that strongly matches them.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1311
source_refs:
  - LWCite-1349
updated_at: 2026-08-15
status: complete
---

# Feature-based tampering recognition does not weight how strongly a feature indicates tampering versus non-tampering

## Summary

The authors explicitly acknowledge that, at its current early stage of development, the approach "does not account for various factors, such as whether a feature strongly, or weakly indicates tampering (or non-tampering)," noting this could be addressed in future work by introducing weighting on the features rather than treating every characterized feature as an equally reliable, binary indicator.

## Why It Matters

An investigator applying the unweighted feature-analysis algorithm risks over-interpreting a case where the evidence weakly or ambiguously matches several tampering-indicative features as equivalent to a case with strong, unambiguous matches, since the algorithm's output does not currently distinguish between these situations. Because the technique's own stated goal is to produce probabilistic, defensible theories (not deductively proven conclusions), presenting an unweighted match result without qualifying its relative strength risks the finding being given more evidentiary weight than the underlying feature evidence actually supports.

## Related Mitigations

- [[mitigations/Manually assess feature-match strength before treating tampering-recognition output as a confident finding]]

## Used By

- [[techniques/Recognize artefact tampering using inductive reasoning over temporal-logic system-state features]]

## References

- [LWCite-1349] Neale, Kennedy, and Nuseibeh, 2026, "Reasoning about artefact tampering", FSI: Digital Investigation 58, 302147.

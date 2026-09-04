---
id: LWW-2118
type: weakness
name: File and folder naming heuristics for CSAM detection cannot recognize deliberately disguised or novel naming conventions
description: File and folder naming/structuring heuristics for prioritizing CSAM detection depend on the specific naming conventions observed in known prior cases, so a distributor who adopts deliberately misleading, innocuous-looking, or otherwise novel naming and folder-organization conventions -- specifically to evade this kind of pattern-based prioritization -- is not recognized by the heuristics, and content in files/folders that do not match a known pattern is scanned at the same lower priority as genuinely benign content.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2119
source_refs:
  - LWCite-2138
updated_at: 2026-08-16
status: complete
---

# File and folder naming heuristics for CSAM detection cannot recognize deliberately disguised or novel naming conventions

## Summary

The naming/structuring pattern library this prioritization technique relies on is necessarily built from previously observed CSAM-distribution conventions, so it inherently lags behind the introduction of any new or deliberately disguised naming/organization scheme a distributor adopts. A distributor with even a moderate incentive to evade automated detection can adopt innocuous-sounding file and folder names specifically to avoid matching any known pattern, causing the technique to assign that content the same low scanning priority as genuinely unrelated files.

## Why It Matters

Because this technique's entire purpose is prioritization under a limited computational budget, content that evades the naming-pattern check is not scanned later or with lower confidence -- it is simply queued behind other content and may never reach content-level analysis within the available budget, especially on a large site. An investigator or automated system relying on this prioritization to allocate scarce computational resources should not assume low-priority-scored content has been ruled out; it has only not yet been checked, and a sophisticated distributor has a direct incentive to ensure their content is never scored as high-priority in the first place.

## Related Mitigations

- [[mitigations/Periodically update CSAM naming-pattern libraries and apply baseline content-level scanning even to low-priority-scored files]]

## Used By

- [[techniques/Prioritize dark web CSAM detection using file and folder naming and structuring pattern heuristics]]

## References

- [LWCite-2138] "Using file and folder naming and structuring to improve automated detection of child sexual abuse images on the Dark Web", FSI: Digital Investigation 48, 2024.

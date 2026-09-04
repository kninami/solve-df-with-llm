---
id: LWW-1114
type: weakness
name: Static single-location cell-site surveys are susceptible to false negatives that exclude legitimately serving cells
description: A survey taken from a single fixed point with a single unit tends to detect only the cell with the strongest signal or a subset of legitimately serving cells at that instant, systematically missing other cells that genuinely serve the location and that a real device could have selected at a different moment or under different network conditions.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1114
source_refs:
  - LWCite-1108
updated_at: 2026-08-12
status: complete
---

# Static single-location cell-site surveys are susceptible to false negatives that exclude legitimately serving cells

## Summary

The paper states directly: "static survey methods (where measurements are gathered from a single point) have been used in court and yet are demonstrated to be particularly susceptible to false negatives." A device only reports one cell as its "best server" at a given time (though it may report other detected cells with relevant data), and which cell is selected can vary with local RF conditions, time, and network configuration in ways a single static measurement cannot capture; a documented case example of a failure of this method is cited directly in the source paper.

## Why It Matters

An investigator who uses a minimal static survey to conclude that a call data record's recorded cell is inconsistent with (and therefore excludes) a proposed device location risks drawing an unsafe, potentially misleading conclusion, since the absence of a cell in a limited static survey does not reliably establish that the cell could not have served the location — a false negative that could wrongly exclude a legitimate suspect location or fail to identify a legitimate one.

## Related Mitigations

- [[mitigations/Combine multiple survey equipment types, modes, and movement patterns to reduce false negatives in cell site surveys]]

## Used By

- [[techniques/Conduct a cell site survey to validate call data record cell service claims]]

## References

- [LWCite-1108] Tart et al., 2021, "Cell site analysis: use and reliability of survey methods", FSI: Digital Investigation 38.

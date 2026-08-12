---
id: DFW-1100
type: weakness
name: Hyper timelines cannot be automatically flattened into a single global order without sufficient synchronization points
description: Reducing a hyper timeline's partial order back into a single "flat" super timeline respecting a global chronological order requires observing sufficiently many Coincidence relations between the separate time domains to fully resolve their relative ordering; without enough such synchronization points, automatic alignment into a total order is not possible, and implicit timing information generally cannot be easily merged with a classical timeline at all.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1100
source_refs:
  - DFCite-1094
updated_at: 2026-08-10
status: complete
---

# Hyper timelines cannot be automatically flattened into a single global order without sufficient synchronization points

## Summary

The authors state this directly: "we would need the observation of sufficiently many Coincidence relations between the time domains such that the partial order is reduced to a total order. Without a sufficient number of synchronization points, such automatic alignment will also be hard using hyper timelines. Similarly, implicit timing information also cannot be easily merged with classical timelines."

## Why It Matters

An investigator hoping to present a single, fully-ordered timeline covering all evidence sources (rather than the richer but more complex hyper timeline representation) may not be able to do so automatically if the evidence does not happen to contain enough cross-domain relations connecting the various time sources — in that case, the technique's own fallback (visualizing implicit timing information as intervals spread over a classical timeline, bounding the earliest/latest possible time an event occurred) provides a weaker, interval-based result rather than a precise ordering.

## Related Mitigations

- [[mitigations/Identify and preserve cross-time-domain synchronization points before relying on automatic hyper timeline flattening]]

## Used By

- [[techniques/Construct a hyper timeline from implicit and explicit timing information]]

## References

- [DFCite-1094] Dreier et al., 2024, "Beyond timestamps: Integrating implicit timing information into digital forensic timelines", FSI: Digital Investigation 49.

---
id: DFM-1100
type: mitigation
name: Identify and preserve cross-time-domain synchronization points before relying on automatic hyper timeline flattening
source_refs:
  - DFCite-1094
updated_at: 2026-08-10
status: complete
---

# Identify and preserve cross-time-domain synchronization points before relying on automatic hyper timeline flattening

## Summary

Before relying on an automatically flattened, single global ordering derived from a hyper timeline, confirm that enough Coincidence relations (synchronization points) between the relevant time domains have actually been observed in the evidence; where they have not, present findings as a partial order or as interval-bounded placements on a classical timeline instead.

## Addresses

- [[weaknesses/Hyper timelines cannot be automatically flattened into a single global order without sufficient synchronization points]]

## How To Apply

When constructing a hyper timeline from multiple time domains, actively look for and document Coincidence relations connecting them (e.g. an event referenced in both a database sequence and a log file). Where too few such relations exist to fully resolve a total order, avoid presenting a forced flat ordering; instead report the partial order directly, or bound implicit-timing events as intervals over the classical timeline using their earliest/latest possible placement.

## References

- [DFCite-1094] Dreier et al., 2024, "Beyond timestamps: Integrating implicit timing information into digital forensic timelines", FSI: Digital Investigation 49.

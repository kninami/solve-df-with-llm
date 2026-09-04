---
id: LWT-1094
type: technique
name: Construct a hyper timeline from implicit and explicit timing information
description: Extend a classical "flat" digital forensic timeline (events sorted by timestamp) into a richer partial order — a "hyper timeline" — by separating each source of timing information (explicit timestamps, but also implicit ordering signals such as database sequence numbers or log-file line numbers) into its own distinct time domain with its own timeline, then connecting those timelines using observed relations ("Coincidence" relations) between events across domains, enabling ordering of events that have no timestamp at all and supporting detection of timestamp inconsistencies such as tampering.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1100
aliases:
  - Hyper timeline construction from implicit and explicit timing information across time domains
  - Hyper timeline
source_refs:
  - LWCite-1094
updated_at: 2026-08-10
status: complete
---

# Construct a hyper timeline from implicit and explicit timing information

## Summary

Timestamps are not the only source of timing information in digital evidence: sequence numbers embedded in databases, or positional information such as line numbers in log files, often encode the relative order of events without directly referencing a timestamp at all. Modeling each such source as its own time domain, and explicitly connecting domains only where a relation between them is actually observed in the evidence, avoids forcing potentially unrelated timing sources into a single flat ordering that may misrepresent what is actually known.

## Details

The method was implemented and queried using TypeQL/TypeDB, allowing an examiner to query for global ordering relations between entries in different time domains and visualize the resulting partial-order graph. Because the hyper timeline preserves genuine uncertainty (an entry can be shown as both potentially earlier and later than another, when the evidence does not resolve their order), it also exposes timestamp inconsistencies directly, including cycles in the precedence relation — a signature of tampering, such as a suspect altering a local clock to antedate a video session to construct an alibi.

## Examples

- Querying for the relation between two time domain entries revealed both an "earlier than" and a "later than" relationship existing simultaneously — a cycle in the precedence relation identified as evidence that a suspect had manipulated the local system clock to backdate a recording session as part of an alibi.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Hyper timelines cannot be automatically flattened into a single global order without sufficient synchronization points]]

## References

- [LWCite-1094] Dreier et al., 2024, "Beyond timestamps: Integrating implicit timing information into digital forensic timelines", FSI: Digital Investigation 49.

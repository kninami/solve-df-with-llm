---
id: DFW-2075
type: weakness
name: Heuristic-based Bitcoin address clustering has a high inherent misattribution error rate
description: The multi-input and one-time-change heuristics widely used to cluster Bitcoin addresses believed to belong to the same real-world user each carry substantial, previously-unquantified error rates, so a clustering result presented as identifying "an address belonging to a user" may in fact group unrelated addresses together or split a single user's addresses across clusters.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-2076
source_refs:
  - DFCite-2081
updated_at: 2026-08-16
status: complete
---

# Heuristic-based Bitcoin address clustering has a high inherent misattribution error rate

## Summary

Measured against a validated blockchain simulation model with known ground truth, the one-time-change heuristic showed an average error rate of roughly 90%, the multi-input heuristic roughly 46%, and their combination roughly 41% — meaning that even the best-performing combination of these two widely used clustering heuristics misattributes a substantial minority of addresses to the wrong real-world-user cluster. Both heuristics assume specific patterns in how a real user's wallet software constructs transactions (that all input addresses of a multi-input transaction share a private key holder, and that a newly generated one-time change address belongs to the sender), assumptions that mixing services and diverse wallet behaviors can violate.

## Why It Matters

Address clustering results are used in criminal investigations to link seized or suspect-controlled addresses to other addresses believed to belong to the same individual, but without a quantified error rate, a court or investigator has no principled basis for how much weight the clustering result should be given. Presenting a heuristic-derived cluster as if it definitively identifies a single real-world entity, without disclosing that even the best-performing heuristic combination is wrong for roughly two out of every five addresses on average, risks misattributing transactions to an innocent party or overstating the strength of the link between a suspect and blockchain activity.

## Related Mitigations

- [[mitigations/Validate a heuristic-based address-clustering algorithm's error rate against a simulation model before presenting its results as evidence]]

## Used By

- [[techniques/Measure heuristic-based Bitcoin address-clustering error rates using a validated blockchain simulation model]]

## References

- [DFCite-2081] Gong, Chow, Yiu, and Ting, 2022, "Sensitivity analysis for a Bitcoin simulation model", FSI: Digital Investigation 43, 301449.

---
id: LWT-1079
type: technique
name: Identify Bitcoin peeling chains using self-change-address analysis
description: Identify Bitcoin "peeling chains" — a technique used by mixing/laundering services to repeatedly peel off small amounts from a starting address to obscure the flow of illicit funds — by first isolating candidate chains built from self-change addresses (where the input address and the change-receiving address are controlled by the same entity), then further filtering by verifying chain-internal transaction details (version, address type, sequence-number category, SegWit flag, locktime, and block/time-interval constraints consistent with automated peeling) to distinguish genuine mixer-generated peeling chains from coincidentally similar transaction patterns.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1085
aliases:
  - Self-change-address-based peeling chain identification on the Bitcoin blockchain
source_refs:
  - LWCite-1075
updated_at: 2026-08-10
status: complete
---

# Identify Bitcoin peeling chains using self-change-address analysis

## Summary

Prior peeling-chain research relied on heuristic change-address-identification algorithms without ground truth to confirm accuracy. Restricting analysis to self-change addresses (a stronger, narrower signal that the same entity controls both the spending and change-receiving side of a transaction) and then cross-verifying each candidate chain's internal transaction parameters for consistency with automated, mixer-generated peeling behavior improves confidence in which extracted chains are genuine peeling chains, to a degree, without requiring unavailable ground-truth address-ownership data.

## Details

The method parses each transaction's version number, `lock_time` field, sequence number, address type, and SegWit flag across a candidate chain, on the reasoning that an auto-program-generated peeling chain will hold several of these fields constant or classifiably consistent across all its transactions. Time and block-interval constraints (e.g. bounding the maximum block interval for a chain to twice its transaction-round count) further filter out chains whose timing is inconsistent with automated peeling. Applying this combined filtering to an initial candidate set reduced it by nearly 60%, yielding 624,573 chains (9,813,092 total transaction volume) assessed to more precisely represent genuine peeling-chain behavior, whose resulting behavioral patterns (transaction round distribution, time interval distribution, peeling-amount distribution) were then studied.

## Examples

- Peeling chains were used to launder a portion of the funds stolen in the Bitfinex hack, illustrating the real-world investigative relevance of accurately identifying this laundering pattern.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Self-change-address peeling chain identification cannot certainly confirm true address ownership]]

## References

- [LWCite-1075] Gong et al., 2023, "Analyzing the peeling chain patterns on the Bitcoin blockchain", FSI: Digital Investigation 46.

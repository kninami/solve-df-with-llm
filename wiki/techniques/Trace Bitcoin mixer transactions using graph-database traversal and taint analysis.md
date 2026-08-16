---
id: DFT-2107
type: technique
name: Trace Bitcoin mixer transactions using graph-database traversal and taint analysis
description: Import Bitcoin blockchain data (blocks, transactions, and addresses) into a graph database and use graph-query traversal to identify a mixing service's operational patterns -- peeling chains, multi-transaction/multi-address hubs, input/output linkage attempts, and transaction-value-range analysis -- combined with third-party taint-analysis services to narrow down candidate addresses and characterize a specific mixer's structural fingerprint from controlled test transactions.
objective_ids:
  - DFO-1008
  - DFO-1001
weakness_ids:
  - DFW-2113
aliases:
  - Neo4j-based Bitcoin mixer transaction pattern analysis
source_refs:
  - DFCite-2133
updated_at: 2026-08-16
status: complete
---

# Trace Bitcoin mixer transactions using graph-database traversal and taint analysis

## Summary

Custodial Bitcoin mixing services obscure the link between deposited and withdrawn funds by pooling and internally reshuffling customer deposits, but conducting controlled test transactions through a mixer and importing the resulting blockchain data into a graph database (Neo4j) makes the mixer's specific internal patterns queryable: peeling chains, addresses receiving from or sending to many other addresses (multi-transaction/multi-address hubs), and whether a direct graph path exists linking a known input address to a known output address.

## Details

Blockchain data is extracted and formatted for import using an ETL tool (btc-csv), producing a graph schema of Block, Transaction, and Address nodes connected by IS_BEFORE, BELONGS_TO, RECEIVES, and SENDS relationships; Cypher (Neo4j's query language) queries then traverse this graph to identify specific patterns. A shortest-path query between a known input and known output address directly tests whether the mixer's internal transactions leave any traceable graph-level connection during the "period of mixing," and its absence (as found for both mixers tested) demonstrates that the mixer successfully prevents this most direct form of linkage. Multi-transaction address analysis identifies addresses receiving from or sending to an unusually large number of other addresses, a pattern consistent with (though not conclusive proof of) an address being operated directly by the mixing service rather than by an individual customer. Peeling-chain analysis (see [[techniques/Identify Bitcoin peeling chains using self-change-address analysis]] for a self-change-address-based approach to the same underlying pattern) traces the sequence of small-amount transactions leading to or from the payout address, measuring the timing distribution (minimum/maximum/average delay in blocks) between successive peeling transactions to check for signs of a mixing service's characteristic default timing values. Transaction-value-range analysis exploits the fact that mixers typically deduct a fee before paying out, so searching for transactions within the plausible range of possible output values (given the range of fees a mixer might charge) can identify or narrow down the specific transaction(s) representing a payout, even where more than one output address is used to obscure a single-output pattern. Third-party anti-money-laundering taint-analysis services (e.g. CrystalBlockchain, AMLBot) are run alongside the graph analysis to independently assess and cross-verify the risk/taint level and any identified real-world ownership of addresses along the traced path.

## Examples

- Testing Mixer 1 (which only allowed a single output address) found no direct graph-path link between the input and output address even months later, and found only one input-related address correctly identified by name (a cryptocurrency exchange) via taint analysis, with all other addresses in the trace unidentified and showing consistently low (around 10%) taint scores.
- Testing Mixer 2 (which offered up to two output addresses) similarly found no direct input/output graph-path link during the mixing period, but revealed a chain of intermediate pooling transactions with as many as 95 other input addresses and, via taint analysis, correctly identified one connected address as belonging to a specific cryptocurrency exchange (HTX), which the analysis inferred was likely making payouts to its own customers through the mixer rather than being directly operated by the mixer itself.
- A review of three real U.S. legal cases involving mixer operator identification (ChipMixer, Helix, Bitcoin Fog) found that in all three, blockchain transaction analysis alone did not directly lead to identifying the operator; successful identification instead relied on external, off-chain information such as tracing infrastructure hosting payments, cloud-service subpoenas, or operational-security mistakes by the operator.

## Related Objectives

- `DFO-1008` Establish identities
- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Blockchain graph analysis alone cannot identify a Bitcoin mixer's operator without external off-chain information]]

## References

- [DFCite-2133] Tippe and Deckers, 2025, "Unmixing the mix: Patterns and challenges in Bitcoin mixer investigations", FSI: Digital Investigation 52, 301876.

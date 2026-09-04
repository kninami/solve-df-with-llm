---
id: LWT-1135
type: technique
name: Profile a cryptomarket's transaction timing patterns using blockchain escrow-heuristic transaction identification
description: Identify a darknet cryptomarket's escrow-related Bitcoin transactions using address-clustering and escrow-flow heuristics applied to the public blockchain, then aggregate the resulting transaction timestamps by hour of day and day of week to reconstruct when the marketplace's users are actually most active, without relying on web-scraped listing data.
objective_ids:
  - DFO-1001
weakness_ids:
  - LWW-1138
aliases:
  - Bitcoin-transaction-based measurement of cryptomarket activity timing
source_refs:
  - LWCite-1136
updated_at: 2026-08-12
status: complete
---

# Profile a cryptomarket's transaction timing patterns using blockchain escrow-heuristic transaction identification

## Summary

Because a cryptomarket's own Bitcoin address activity is fully recorded on the public blockchain with exact transaction timestamps, applying three complementary heuristics — a common-input-ownership heuristic, and two heuristics based on how cryptomarkets route buyer payments into and out of escrow addresses — lets an investigator or researcher identify which on-chain transactions represent marketplace escrow activity, then aggregate those timestamps to reveal statistically significant hour-of-day and day-of-week activity patterns for the marketplace as a whole.

## Details

The method starts from a small set of publicly known marketplace-owned addresses (surfaced when a marketplace voluntarily reveals its escrow Bitcoin addresses, or via services such as WalletExplorer) and expands the known-address set using: Heuristic 1 (if more than two addresses are inputs to the same transaction, they are owned by the same user — the standard co-spend clustering heuristic); Heuristic 2 (an unknown address that sends to, or receives from, a known marketplace address in a small fixed-value "linking" transaction, e.g. exactly 0.01 BTC, is itself a marketplace-owned address, since marketplaces use these small transactions to anonymize and secure user funds internally); and Heuristic 3 (a transaction where an address not owned by the marketplace is an input, and a marketplace-owned address is the output, is identified as a buyer's escrow payment — i.e., a purchase). Applying these heuristics across the full operating lifetime of six major cryptomarkets (Silk Road, Silk Road 2.0, Agora, Evolution, Nucleus, Abraxas) identified between 130,000 and 630,000 purchase transactions per marketplace, and aggregating the resulting timestamps by hour and day of week (using a likelihood-ratio test to confirm the observed patterns are statistically significant, not due to chance) showed markedly more transactions on Mondays through Wednesdays than on weekends, and transaction peaks at night in European time zones, consistent with retail (personal-use) rather than wholesale drug purchasing behavior. The same method was also used to measure the before/after impact of a coordinated international policing operation (Operation Onymous) on transaction timing patterns, finding that the operation displaced users to other marketplaces without measurably altering the underlying timing behavior. Unlike [[techniques/Correlate darknet marketplace purchases to blockchain transactions using price and timing]], which attributes one specific detected purchase to one specific transaction, this technique measures aggregate marketplace-wide activity timing rather than individual buyer/vendor attribution.

## Examples

- Aggregating roughly 320,000 Heuristic-3-identified Silk Road 2.0 purchase transactions by hour of day produced two clear daily peaks (UTC 0-2 and UTC 18-22) consistent with evening/night purchasing in European and US time zones, and a likelihood-ratio test confirmed the hour-of-day and day-of-week differences were statistically significant (p < 0.001) rather than random variation.

## Related Objectives

- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Escrow-transaction timestamps can misrepresent the actual purchase or consumption time on a cryptomarket]]

## References

- [LWCite-1136] Tsuchiya and Hiramoto, 2021, "Dark web in the dark: Investigating when transactions take place on cryptomarkets", FSI: Digital Investigation 36.

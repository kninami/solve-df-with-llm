---
id: DFW-1138
type: weakness
name: Escrow-transaction timestamps can misrepresent the actual purchase or consumption time on a cryptomarket
description: A blockchain escrow transaction only records when a buyer funded escrow, not when they actually decided to buy, when the vendor shipped, or when the product was consumed, so treating the escrow timestamp as equivalent to "the purchase" can misstate the timing of the underlying real-world event it is meant to represent.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1138
source_refs:
  - DFCite-1136
updated_at: 2026-08-12
status: complete
---

# Escrow-transaction timestamps can misrepresent the actual purchase or consumption time on a cryptomarket

## Summary

Cryptomarket escrow-based blockchain transaction timestamps record precisely when a buyer's funds were placed into (or released from) escrow, and this study's own analysis relies on the assumption that most buyers escrow funds shortly before purchasing. In principle, though, a buyer could fund escrow and complete a purchase at any later time, so the observed transaction timestamp is a proxy for, not a guarantee of, the actual purchase decision, order placement, or product-consumption time.

## Why It Matters

An investigator using escrow transaction timing to infer a specific buyer's behavior (for example, to argue a purchase and subsequent drug use both occurred within a narrow time window) risks over-interpreting a timestamp that, at the level of an individual transaction, may not correspond tightly to the real-world event of interest. The risk is smaller for aggregate, population-level statistical patterns (as used in this study to characterize a marketplace's overall activity rhythm) than for attributing a precise timeline to any single buyer's specific transaction.

## Related Mitigations

- [[mitigations/Corroborate escrow-transaction timestamps with independent evidence before treating them as the exact purchase or consumption time]]

## Used By

- [[techniques/Profile a cryptomarket's transaction timing patterns using blockchain escrow-heuristic transaction identification]]

## References

- [DFCite-1136] Tsuchiya and Hiramoto, 2021, "Dark web in the dark: Investigating when transactions take place on cryptomarkets", FSI: Digital Investigation 36.

---
id: LWT-1101
type: technique
name: Correlate darknet marketplace purchases to blockchain transactions using price and timing
description: Attribute a darknet marketplace purchase (detected via a sales-counter increment or product review) to a specific on-chain transaction by converting the product's price into its cryptocurrency equivalent and searching the blocks mined within the detection window for an output matching that value, yielding candidate buyer and vendor/operator addresses.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1107
aliases:
  - Cryptocurrency transaction correlation for darknet marketplace purchases
  - Blockchain identification of vendor and buyer
source_refs:
  - LWCite-1101
updated_at: 2026-08-12
status: complete
---

# Correlate darknet marketplace purchases to blockchain transactions using price and timing

## Summary

Once a marketplace purchase has been detected (e.g. via a sales-counter increment) and its price and approximate time window are known, that price can be converted into the fiat-to-cryptocurrency equivalent used at the time of listing and used to search the blockchain for a matching transaction output. Input addresses to a matching transaction may belong to the buyer, and output addresses to the vendor (for a direct deal) or the marketplace operator (where escrow was used).

## Details

The technique depends on marketplaces that use a wallet-less, direct-deal payment model rather than an internal marketplace-operated wallet, since only direct deals produce an on-chain transaction that is directly attributable without an intervening operator-controlled pooled address. Accuracy depends on two factors: the uniqueness of the purchase price relative to other simultaneous blockchain activity, and the width of the block-search window (a longer window between scrapes yields more blocks and more candidate transactions, increasing the false-positive rate). The technique was demonstrated on Monopoly Market, which supported both Bitcoin and Monero direct-deal payments with no marketplace-operated escrow wallet required.

## Examples

- A detected cocaine purchase (2g, 171 USD, paid in the Bitcoin equivalent 0.00290497 BTC) within a 15-minute scraping window was searched against two Bitcoin blocks for any output matching that value, yielding three candidate transactions with an average deviation of 0.0000000042 BTC from the target price; one candidate included the presumed buyer's address as an input and the presumed vendor's address as an output.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/DNM purchase-to-blockchain correlation yields multiple candidate transactions when purchase price and timing are not unique]]

## References

- [LWCite-1101] Dolejška et al., 2023, "Busting up Monopoly: Methods for modern darknet marketplace forensics", FSI: Digital Investigation 46.

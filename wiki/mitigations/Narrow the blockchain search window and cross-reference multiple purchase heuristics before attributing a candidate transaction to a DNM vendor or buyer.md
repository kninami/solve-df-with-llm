---
id: DFM-1107
type: mitigation
name: Narrow the blockchain search window and cross-reference multiple purchase heuristics before attributing a candidate transaction to a DNM vendor or buyer
source_refs:
  - DFCite-1101
updated_at: 2026-08-12
status: complete
---

# Narrow the blockchain search window and cross-reference multiple purchase heuristics before attributing a candidate transaction to a DNM vendor or buyer

## Summary

Treat a price-matched blockchain transaction as one candidate among potentially several, not a confirmed attribution, and reduce false positives by scraping at high frequency to keep the block-search window as narrow as possible and by cross-checking each candidate against other known or presumed buyer/vendor addresses.

## Addresses

- [[weaknesses/DNM purchase-to-blockchain correlation yields multiple candidate transactions when purchase price and timing are not unique]]

## How To Apply

Keep the scraping interval that defines the purchase detection window as short as practical, since a narrower window directly reduces the number of blocks — and therefore candidate transactions — that must be searched. Where multiple candidates remain, cross-reference each candidate transaction's input and output addresses against other already-identified buyer, vendor, or operator addresses from the same investigation, and report an attribution only when independent evidence narrows the candidate set to one, rather than defaulting to the closest price match.

## References

- [DFCite-1101] Dolejška et al., 2023, "Busting up Monopoly: Methods for modern darknet marketplace forensics", FSI: Digital Investigation 46.

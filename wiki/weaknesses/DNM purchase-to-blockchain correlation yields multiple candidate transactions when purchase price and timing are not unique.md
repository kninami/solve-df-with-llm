---
id: LWW-1107
type: weakness
name: DNM purchase-to-blockchain correlation yields multiple candidate transactions when purchase price and timing are not unique
description: Searching a block-search window for a transaction output matching a detected purchase's estimated cryptocurrency value is a heuristic that can return several equally plausible candidate transactions, of which all but one are false positives, with accuracy degrading as the price becomes less unique or the search window widens.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-1107
source_refs:
  - LWCite-1101
updated_at: 2026-08-12
status: complete
---

# DNM purchase-to-blockchain correlation yields multiple candidate transactions when purchase price and timing are not unique

## Summary

The paper is explicit that this correlation is heuristic, not deterministic: "the list of transaction candidates can have numerous items, where all except one are false positives." In the paper's own worked example, a single detected purchase yielded three candidate transactions within the search window, and the correct one had to be distinguished by additionally checking whether the buyer's and vendor's presumed addresses appeared among the transaction's inputs and outputs.

## Why It Matters

An investigator who treats the first or only plausible price-matching transaction as confirmed proof of a specific purchase risks misattributing an unrelated transaction that coincidentally matches the target price within the search window, particularly for common price points or wider search windows where more blocks (and more candidate transactions) must be considered.

## Related Mitigations

- [[mitigations/Narrow the blockchain search window and cross-reference multiple purchase heuristics before attributing a candidate transaction to a DNM vendor or buyer]]

## Used By

- [[techniques/Correlate darknet marketplace purchases to blockchain transactions using price and timing]]

## References

- [LWCite-1101] Dolejška et al., 2023, "Busting up Monopoly: Methods for modern darknet marketplace forensics", FSI: Digital Investigation 46.

---
id: DFT-1129
type: technique
name: Track stolen Bitcoin using context-aware taint analysis with address and transaction profiling
description: Trace stolen or illicitly-obtained Bitcoins through the blockchain using a taint analysis strategy that incorporates external address-ownership profiles and transaction-pattern profiles, stopping tracking once tainted funds reach an identified cryptocurrency service or mixer address rather than continuing indefinitely.
objective_ids:
  - DFO-1008
weakness_ids:
  - DFW-1133
aliases:
  - Context-based Bitcoin tracking
  - Dirty-First taint analysis strategy
  - TIHO (Taint-In, Highest-Out) taint analysis strategy
source_refs:
  - DFCite-1129
updated_at: 2026-08-12
status: complete
---

# Track stolen Bitcoin using context-aware taint analysis with address and transaction profiling

## Summary

Standard Bitcoin taint analysis strategies (Poison, Haircut, FIFO, LIFO) distribute "tainted" status across transaction outputs using a fixed rule that ignores who actually controls the receiving address, producing large volumes of unrelated ("unessential") tracked transactions once stolen coins reach an exchange, gambling site, or other service and are no longer in the targeted illicit user's possession. Incorporating address-ownership and transaction-pattern context into the tracking process substantially reduces this unrelated tracking.

## Details

The methodology gathers address-profile data — identifying known cryptocurrency-service and mixer addresses via web scraping, prior research datasets, and multi-input address-clustering heuristics — and transaction-profile data recognizing patterns of known Privacy-Enhancing Technologies (PETs) such as CoinJoin, ChipMixer, Wasabi/Samourai CoinJoin, and the Lightning Network. Two new context-based taint strategies are introduced alongside the established Poison/Haircut/FIFO/LIFO strategies: Dirty-First, which behaves like a depth-first search and stops tracking a specific Bitcoin output as soon as it is combined with any clean (non-tainted) Bitcoin — minimizing false-positive unrelated transactions at the risk of missing genuinely illicit downstream activity if a thief deliberately mixes in their own clean funds — and TIHO (Taint-In, Highest-Out), which prioritizes tracking the highest-value output of a transaction, based on the assumption that a thief is more likely to preserve stolen value in the largest output. Tracking with any of these strategies is designed to stop once tainted Bitcoins reach an identified service or mixer address, since continuing past that point only tracks the service's or other unrelated users' subsequent activity rather than the targeted individual's.

## Examples

- Applied to 26 historical Bitcoin theft/ransomware cases (2012-2021) with matched control-group transactions, incorporating address profiling reduced the number of tracked transactions substantially for most sample cases under the FIFO, LIFO, and TIHO strategies (e.g. one case's FIFO result dropped from an average of 175.1 to 24.3 transactions per day), while the Dirty-First strategy already showed the smallest change since it inherently halts at the first clean-Bitcoin mixing event.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Naive Bitcoin taint analysis continues tracking past service and mixer exit points, producing unrelated transactions]]

## References

- [DFCite-1129] Tironsakkul et al., 2022, "Context matters: Methods for Bitcoin tracking", FSI: Digital Investigation 42-43, 301475.

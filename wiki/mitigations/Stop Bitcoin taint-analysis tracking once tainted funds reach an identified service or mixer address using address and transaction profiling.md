---
id: LWM-1133
type: mitigation
name: Stop Bitcoin taint-analysis tracking once tainted funds reach an identified service or mixer address using address and transaction profiling
source_refs:
  - LWCite-1129
updated_at: 2026-08-12
status: complete
---

# Stop Bitcoin taint-analysis tracking once tainted funds reach an identified service or mixer address using address and transaction profiling

## Summary

Incorporate address-ownership profiles (known cryptocurrency-service and mixer addresses) and transaction-pattern profiles (known PET usage such as CoinJoin or Lightning Network) into the taint-analysis process, and halt tracking once tainted Bitcoins reach an identified service or mixer address, since the funds are no longer traceable to the targeted individual beyond that point.

## Addresses

- [[weaknesses/Naive Bitcoin taint analysis continues tracking past service and mixer exit points, producing unrelated transactions]]

## How To Apply

Before running taint analysis on a case, build or obtain an address-profile dataset identifying cryptocurrency exchange, gambling, payment, darknet-market, wallet, and mixer service addresses (via published research datasets, web-scraped service-tagging sources with manual verification, and multi-input address-clustering heuristics on deposited-address data), plus a transaction-profile classifier for known PET patterns (CoinJoin variants, ChipMixer, Lightning Network funding/closing transactions). Configure the taint-analysis strategy (FIFO, LIFO, TIHO, or Dirty-First) to stop propagating tainted status once a transaction output reaches an address matched in the service/mixer profile, and review the resulting reduction in tracked transaction volume as a sign the tracking scope is now more tightly bound to the targeted individual's actual activity rather than downstream service or third-party behavior.

## References

- [LWCite-1129] Tironsakkul et al., 2022, "Context matters: Methods for Bitcoin tracking", FSI: Digital Investigation 42-43, 301475.

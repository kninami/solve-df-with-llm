---
id: DFM-1290
type: mitigation
name: Grade DeFi scammer-association heuristics by strength and corroborate weaker heuristics before attributing an address to a scammer
source_refs:
  - DFCite-1320
updated_at: 2026-08-15
status: complete
---

# Grade DeFi scammer-association heuristics by strength and corroborate weaker heuristics before attributing an address to a scammer

## Summary

Explicitly rank scammer-association heuristics by evidentiary strength — treating contract-creator and initial-liquidity-provider/receiver addresses as strongly associated, and peak-price-exchange or post-scam-inactive addresses as only weakly, non-conclusively associated — and require independent corroboration before naming a weakly-associated address as a scammer in an investigative report or court filing.

## Addresses

- [[weaknesses/Address-association heuristics used to identify DeFi rug-pull scammers cannot conclusively distinguish scammers from legitimate high-risk traders]]

## How To Apply

When applying [[techniques/Investigate an Ethereum DeFi rug-pull scheme and trace its laundering proceeds using open-source blockchain tools]], record which specific heuristic(s) flagged each candidate address and grade them: contract-creator and initial-liquidity addresses as strong; peak-price-exchange or post-scam-inactivity addresses as weak. For weakly-flagged addresses, seek independent corroboration (off-chain OSINT, exchange KYC records obtained via legal process, or a pattern of coordinated behavior with a strongly-flagged address) before including the address as an identified scammer rather than a possible participant in the investigative report.

## References

- [DFCite-1320] Trozze, Davies, and Kleinberg, 2023, "Of degens and defrauders: Using open-source investigative tools to investigate decentralized finance frauds and money laundering", FSI: Digital Investigation 46, 301575.

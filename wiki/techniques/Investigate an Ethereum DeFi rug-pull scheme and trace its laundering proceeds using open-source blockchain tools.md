---
id: DFT-1279
type: technique
name: Investigate an Ethereum DeFi rug-pull scheme and trace its laundering proceeds using open-source blockchain tools
description: Extract court-usable, transaction-based evidence of an Ethereum decentralized-finance (DeFi) rug-pull or pump-and-dump scam by manually examining a suspect ERC-20 token's on-chain transaction history and smart-contract code with open-source tools, then trace where the scammer's proceeds were subsequently laundered using scammer-association heuristics and blockchain flow-visualization.
objective_ids:
  - DFO-1001
  - DFO-1008
weakness_ids:
  - DFW-1289
aliases:
  - Open-source DeFi fraud and money-laundering investigation
source_refs:
  - DFCite-1320
updated_at: 2026-08-15
status: complete
---

# Investigate an Ethereum DeFi rug-pull scheme and trace its laundering proceeds using open-source blockchain tools

## Summary

Despite billions of dollars reported lost annually to DeFi scams, prosecutions remain rare, partly because most published DeFi-fraud research operates only at an aggregate, statistical level rather than producing case-level, court-usable evidence. Manually and systematically examining a specific suspect token's transaction-level history via a blockchain explorer, its smart-contract code via a static-analysis tool, and the subsequent movement of laundered proceeds via an open blockchain-visualization tool together produce granular, individually-citable transaction evidence suitable for prosecution — using only free, openly available tools whose methodology (unlike subscription blockchain-analytics platforms) can be fully disclosed in court.

## Details

**Fraud investigation**: starting from Etherscan (a free blockchain explorer with both web and API access), every ERC-20 token-transfer transaction involving a suspect token is manually examined — token events (liquidity additions, transfers, ETH exchanges) and price fluctuations are traced in detail to reconstruct the scheme's mechanics, and potential victims are identified as addresses left holding the worthless token unable to exchange it before the scam concluded. The token's Solidity smart-contract source code is separately analyzed with Slither (a static-analysis framework, used here to run its full battery of vulnerability/informational/optimization detectors) to identify "smart contract trapdoor" mechanisms — code deliberately embedded to trap or exploit token holders, such as functions that charge investors on token swaps or prohibit them from selling. **Money-laundering investigation ("following the money")**: proceeds converted back to ETH are traced using a set of scammer-association heuristics — the token's contract creator (and any wallet that funded that creator's address) is treated as scammer-associated, as is the address that supplied the token's initial trading liquidity and the address to which liquidity was ultimately withdrawn, since only the scam's perpetrator or a collaborator could plausibly control these positions; addresses that happened to sell the scam token at its peak price are treated as more weakly associated (they could be the coordinator, or simply lucky participants). Breadcrumbs, an open-source blockchain flow-visualization tool, then maps the flow of funds — amounts, originating and destination addresses, and balances — from these scammer-associated addresses onward, with particular attention paid to short windows of high activity immediately following the scam period (since laundering activity typically clusters there) and to the expectation that genuinely criminal addresses go inactive once laundering is complete.

## Examples

- Manual investigation of five ERC-20 tokens, each requiring inspection of hundreds to thousands of individual transactions and their associated addresses, produced granular evidence identifying each scheme's rug-pull mechanics and subsequent fund movement — the authors note that a comparable full-scale securities-fraud investigation by a professional team typically takes months to years, underscoring the manual effort involved even at this smaller scale.
- Using Slither to statically analyze the five tokens' smart-contract code identified potential trapdoor mechanisms consistent with prior literature's typology of "simple," "sell," and smart-contract-trapdoor rug pulls.

## Related Objectives

- `DFO-1001` Reconstruct events
- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Address-association heuristics used to identify DeFi rug-pull scammers cannot conclusively distinguish scammers from legitimate high-risk traders]]

## References

- [DFCite-1320] Trozze, Davies, and Kleinberg, 2023, "Of degens and defrauders: Using open-source investigative tools to investigate decentralized finance frauds and money laundering", FSI: Digital Investigation 46, 301575.

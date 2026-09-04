---
id: LWW-1289
type: weakness
name: Address-association heuristics used to identify DeFi rug-pull scammers cannot conclusively distinguish scammers from legitimate high-risk traders
description: Heuristics that flag an Ethereum address as scammer-associated based on its trading behavior around a rug-pull event — exchanging the scam token for another cryptocurrency, or remaining inactive afterward — cannot rule out that the address instead belongs to a legitimate but high-risk participant (a "degen") who is engaging in ordinary wash trading or who simply stopped trading for unrelated reasons.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - LWM-1290
source_refs:
  - LWCite-1320
updated_at: 2026-08-15
status: complete
---

# Address-association heuristics used to identify DeFi rug-pull scammers cannot conclusively distinguish scammers from legitimate high-risk traders

## Summary

Only two categories of address in the researchers' own heuristic set are described as "undoubtedly" scammer-associated: the token's contract creator, and the address(es) that supplied and later withdrew the token's initial trading liquidity. Every other heuristic — addresses that exchanged the scam token near its peak price, or addresses that went inactive after the scam — is explicitly acknowledged as ambiguous: such addresses could be the scam's coordinator, an uninvolved participant engaging in wash trading, or simply an unlucky or lucky ordinary trader ("degen").

## Why It Matters

An investigator who treats every heuristically-flagged address as a confirmed scammer risks misattributing legitimate trading activity to a criminal actor, particularly for addresses flagged only by the weaker heuristics (peak-price exchange, post-scam inactivity). Since this misattribution could form the basis of an accusation or asset-tracing action against an innocent party, the strength of each heuristic must be explicitly disclosed and only the strongest (contract creator, initial-liquidity provider/receiver) heuristics should be treated as reliable on their own.

## Related Mitigations

- [[mitigations/Grade DeFi scammer-association heuristics by strength and corroborate weaker heuristics before attributing an address to a scammer]]

## Used By

- [[techniques/Investigate an Ethereum DeFi rug-pull scheme and trace its laundering proceeds using open-source blockchain tools]]

## References

- [LWCite-1320] Trozze, Davies, and Kleinberg, 2023, "Of degens and defrauders: Using open-source investigative tools to investigate decentralized finance frauds and money laundering", FSI: Digital Investigation 46, 301575.

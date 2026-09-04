---
id: LWW-1085
type: weakness
name: Self-change-address peeling chain identification cannot certainly confirm true address ownership
description: Even after filtering candidate chains using self-change addresses and cross-verifying internal transaction parameters, it is not possible to be absolutely certain that a given extracted chain is genuinely a mixer-generated peeling chain, because the actual real-world owner of a given Bitcoin address cannot currently be verified from on-chain data alone, and mixing services do not publicly disclose their address data.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1085
source_refs:
  - LWCite-1075
updated_at: 2026-08-10
status: complete
---

# Self-change-address peeling chain identification cannot certainly confirm true address ownership

## Summary

The authors state this plainly: "the inability to know the actual owner of each address is currently a limitation of Bitcoin blockchain research. It is unsolvable now." Their combined self-change-address and internal-transaction-parameter filtering "ensures the accuracy of the extracted peeling chains to some extent" — an explicit acknowledgment that the method produces a probabilistic best estimate, not a ground-truth-verified result.

## Why It Matters

An investigator relying on peeling-chain identification results to support an attribution or fund-tracing conclusion should treat the output as a strong heuristic indicator rather than definitive proof that a given chain of transactions represents illicit mixing activity by a specific entity, since the underlying address-ownership assumption cannot be independently verified from blockchain data alone and could, without corroboration, misattribute coincidental transaction patterns as a genuine peeling chain.

## Related Mitigations

- [[mitigations/Treat peeling-chain identification as heuristic evidence requiring off-chain corroboration, not definitive address-ownership proof]]

## Used By

- [[techniques/Identify Bitcoin peeling chains using self-change-address analysis]]

## References

- [LWCite-1075] Gong et al., 2023, "Analyzing the peeling chain patterns on the Bitcoin blockchain", FSI: Digital Investigation 46.

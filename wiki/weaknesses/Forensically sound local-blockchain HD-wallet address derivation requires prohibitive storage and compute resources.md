---
id: LWW-1104
type: weakness
name: Forensically sound local-blockchain HD-wallet address derivation requires prohibitive storage and compute resources
description: Running a fully confidential, forensically sound cryptocurrency query platform requires holding a complete local copy of the target blockchain (approximately 350 GB for Bitcoin, approaching a terabyte for Ethereum at time of writing) and, for exhaustive HD-wallet address derivation, significant parallel computing power to search up to 2^31 possible addresses per extended key — resources a local law enforcement agency with limited budget may not have.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1104
source_refs:
  - LWCite-1099
updated_at: 2026-08-10
status: complete
---

# Forensically sound local-blockchain HD-wallet address derivation requires prohibitive storage and compute resources

## Summary

The authors state this directly: "Running a robust forensically sound cryptocurrency query platform requires a significant amount of resources... computing all 2^31 possible addresses for a given extended key would require a machine with significant parallel computing power. A local law enforcement agency with limited resources may find this to be a prohibitive barrier." This is the direct cost of avoiding third-party data providers to preserve investigation confidentiality — the confidentiality guarantee and the resource requirement are directly linked.

## Why It Matters

A smaller or under-resourced investigative unit cannot simply adopt this confidentiality-preserving approach without either accepting the resource cost or compromising the very confidentiality guarantee the local-blockchain design is meant to provide, since the practical alternative (a third-party blockchain data provider) reintroduces the information-disclosure risk the tool was built to avoid.

## Related Mitigations

- [[mitigations/Have trusted larger entities host confidential local-blockchain HD-wallet query services for resource-constrained agencies]]

## Used By

- [[techniques/Derive cryptocurrency addresses using an HD-wallet-aware local blockchain query]]

## References

- [LWCite-1099] Thomas et al., 2022, "BlockQuery: Toward forensically sound cryptocurrency investigation", FSI: Digital Investigation 40.

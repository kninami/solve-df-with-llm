---
id: LWM-1062
type: mitigation
name: Independently security-test and benchmark a blockchain-based IoT evidence framework before adoption
source_refs:
  - LWCite-1052
updated_at: 2026-08-10
status: complete
---

# Independently security-test and benchmark a blockchain-based IoT evidence framework before adoption

## Summary

Before adopting a published blockchain-based IoT forensic framework, independently security-test it (identity/replay/Sybil attack scenarios, and the off-chain evidence-storage attack surface where raw evidence is typically kept) and benchmark its performance using the specific platform version and consensus algorithm intended for deployment, rather than relying on the framework's own reported metrics.

## Addresses

- [[weaknesses/Blockchain-based IoT forensic frameworks lack rigorous security testing and standardized performance benchmarking]]

## How To Apply

Run a standardized performance benchmark (e.g. Hyperledger Caliper, or an equivalent for the chosen platform) against the exact blockchain platform version and consensus algorithm planned for deployment, since published results are inconsistent across studies and often omit these details. Separately evaluate the security of any off-chain evidence storage layer the framework relies on, since the blockchain's tamper-evidence guarantees do not extend to off-chain data.

## References

- [LWCite-1052] Akinbi et al., 2022, "A systematic literature review of blockchain-based Internet of Things (IoT) forensic investigation process models", FSI: Digital Investigation 42-43.

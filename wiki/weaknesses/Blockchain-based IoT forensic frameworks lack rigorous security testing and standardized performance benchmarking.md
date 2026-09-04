---
id: LWW-1062
type: weakness
name: Blockchain-based IoT forensic frameworks lack rigorous security testing and standardized performance benchmarking
description: A systematic review of 16 blockchain-based IoT forensic investigation process models found that almost none had undergone rigorous security testing or evaluation against attacks (e.g. identity/replay/Sybil attacks, or attacks against off-chain evidence storage), and that reported performance evaluations across the reviewed models used inconsistent metrics, undocumented consensus algorithms or platform versions, and rarely tested scalability, making cross-model comparison and pre-deployment risk assessment unreliable.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1062
source_refs:
  - LWCite-1052
  - LWCite-2036
updated_at: 2026-08-14
status: complete
---

# Blockchain-based IoT forensic frameworks lack rigorous security testing and standardized performance benchmarking

## Summary

Only 11 of the 16 reviewed primary studies reported any performance evaluation results at all, and those that did varied in which metrics they measured (latency, throughput, energy consumption, computational cost, scalability), frequently omitted the specific blockchain platform version or consensus algorithm used, and only a handful tested scalability effects as node count or evidence volume grew. The review also found that most frameworks store raw evidence off-chain for cost reasons while only the evidence hash and metadata go on-chain, leaving the off-chain storage layer's own security largely unevaluated in the surveyed literature.

## Why It Matters

An organization comparing published blockchain-based IoT forensic frameworks to select one for deployment cannot reliably use the frameworks' own reported metrics to judge relative security or performance, since the metrics measured, platform versions, and consensus algorithms are inconsistent or missing across studies, and off-chain evidence storage — a common architectural choice — is rarely itself security-evaluated even though it remains vulnerable to attack independent of the blockchain layer's tamper-evidence guarantees.

## Related Mitigations

- [[mitigations/Independently security-test and benchmark a blockchain-based IoT evidence framework before adoption]]

## Used By

- [[techniques/Anchor digital evidence integrity and chain of custody on a blockchain]]

## References

- [LWCite-1052] Akinbi et al., 2022, "A systematic literature review of blockchain-based Internet of Things (IoT) forensic investigation process models", FSI: Digital Investigation 42-43.
- [LWCite-2036] Alashjaee and Alqahtani, 2024, "Improving digital forensic security: A secure storage model with authentication and optimal key generation based encryption", IEEE Access 12 — a concrete illustration of this weakness: its own narrative claims of reduced response/evidence-insertion/evidence-verification times directly contradict its own comparative results table, which shows its proposed system recording the highest (slowest) values of every compared metric.

---
id: DFT-2073
type: technique
name: Measure heuristic-based Bitcoin address-clustering error rates using a validated blockchain simulation model
description: Because no ground truth exists for real-world Bitcoin address ownership, quantify the error rate of heuristic-based address-clustering algorithms (e.g. the multi-input and one-time-change heuristics) by running them against a simulation model of the Bitcoin network whose transaction structure and behavior have been validated to match the real blockchain, using sensitivity analysis to first confirm the simulation model's own stability and credibility.
objective_ids:
  - DFO-1004
  - DFO-1008
weakness_ids:
  - DFW-2075
aliases:
  - Bitcoin simulation model sensitivity analysis
source_refs:
  - DFCite-2081
updated_at: 2026-08-16
status: complete
---

# Measure heuristic-based Bitcoin address-clustering error rates using a validated blockchain simulation model

## Summary

Heuristic-based address clustering — grouping Bitcoin addresses believed to belong to the same real-world user — is central to blockchain de-anonymization investigations, but no heuristic algorithm has a known or provable error rate because no ground truth exists for real Bitcoin address ownership. A simulation model built on known node/transaction behavior and validated by sensitivity analysis provides an internal ground truth against which a heuristic's actual clustering error can be directly measured, addressing an evidentiary gap that otherwise makes it difficult to establish the admissibility of clustering-derived evidence in court.

## Details

The simulation model is built on a Bitcoin network simulator (Simchain), configured with prior knowledge of the real Bitcoin blockchain's transaction distribution (categorized into transfers, multiple payments, consolidation, and complex transaction types) and address-reuse rate (approximately 10%, based on a full parse of the real blockchain from 2009-2021), and integrates a configurable proportion of simulated mixing-service transactions. Sensitivity analysis is then performed in three experimental groups: repeated simulation runs under fixed initial settings (to check output stability), variation of the transaction-type input/output probability distributions by up to ±10% (to check parameter sensitivity), and variation of both the number of simulated network nodes (50-200) and the total number of generated transactions (3,000-10,000) (to check scale sensitivity). A model is judged valid and credible for the purpose of measuring heuristic error rates if its outputs (address reuse rate, transaction-type and input/output-count distributions) remain stable and consistent with the real blockchain's investigated characteristics across these variations. Once validated, the model's internally known address-clustering ground truth is compared against the output of a heuristic algorithm run on the same simulated data to compute per-cluster accuracy (the proportion of correctly clustered addresses) and, from it, an average error rate across all clusters.

## Examples

- Repeated simulation runs (10 runs, ~100 nodes, ~5,000 transactions each) produced stable results: the multi-input heuristic's error rate fluctuated in a narrow band around 46.50% average, the one-time-change heuristic around 90.36% average, and their combination around 41.25% average, none showing significant variation across runs.
- Varying the input/output probability distributions of the three multi-input/output transaction types by up to ±10% across thirteen experimental settings produced only minor fluctuations in the resulting error rates, indicating the model's behavior is not overly sensitive to this parameter.
- Varying the number of simulated nodes (50-200, fixed transaction count) or the total number of generated transactions (3,000-10,000, fixed node count) showed that too many nodes relative to a fixed transaction volume, or too few transactions relative to a fixed node count, each increased the measured error rate, informing recommended parameter ranges for future simulation-model use.

## Related Objectives

- `DFO-1004` Conduct research
- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Heuristic-based Bitcoin address clustering has a high inherent misattribution error rate]]

## References

- [DFCite-2081] Gong, Chow, Yiu, and Ting, 2022, "Sensitivity analysis for a Bitcoin simulation model", FSI: Digital Investigation 43, 301449.

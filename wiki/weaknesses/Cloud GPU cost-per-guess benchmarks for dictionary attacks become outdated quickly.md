---
id: DFW-1028
type: weakness
name: Cloud GPU cost-per-guess benchmarks for dictionary attacks become outdated quickly
description: Published feasibility estimates for cloud-GPU-accelerated password dictionary attacks (guesses achievable per unit cost or time) are tied to hardware performance and cloud rental pricing at the time of measurement, both of which change rapidly, so an estimate cited from prior published research may significantly misstate current real-world feasibility.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1028
source_refs:
  - DFCite-1020
updated_at: 2026-08-09
status: complete
---

# Cloud GPU cost-per-guess benchmarks for dictionary attacks become outdated quickly

## Summary

Prior research on the dollar-cost of password attacks explicitly cautioned that comparing hardware/platform cost-effectiveness (rather than absolute guess counts) is necessary specifically because absolute results "will become outdated very quickly as costs change and hardware performance increases." GPU generations, cloud spot/rental pricing, and even which vendor offers the most cost-effective consumer-grade instance all shift over time frames shorter than typical research publication cycles.

## Why It Matters

An investigator or analyst who cites a published guesses-per-hour or guesses-per-dollar figure to argue that attacking a target's encryption is (or is not) practicable within an operational time or budget window risks relying on stale numbers that no longer reflect current hardware and pricing, potentially over- or under-estimating what is actually achievable at the time of the current investigation.

## Related Mitigations

- [[mitigations/Re-benchmark the key derivation function on current cloud GPU pricing before relying on a feasibility estimate]]

## Used By

- [[techniques/Recover passwords using a dictionary attack with generated mangling rules on cloud GPUs]]

## References

- [DFCite-1020] Holmes and Buchanan, 2023, "A framework for live host-based Bitcoin wallet forensics and triage", FSI: Digital Investigation 44.

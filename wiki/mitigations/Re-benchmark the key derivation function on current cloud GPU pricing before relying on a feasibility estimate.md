---
id: LWM-1028
type: mitigation
name: Re-benchmark the key derivation function on current cloud GPU pricing before relying on a feasibility estimate
source_refs:
  - LWCite-1020
updated_at: 2026-08-09
status: complete
---

# Re-benchmark the key derivation function on current cloud GPU pricing before relying on a feasibility estimate

## Summary

Before deciding whether a dictionary attack against a target's key derivation function is practicable within an operational time or budget window, run a small-scale current benchmark on presently available cloud GPU pricing and hardware rather than relying on previously published guess-rate or cost figures.

## Addresses

- [[weaknesses/Cloud GPU cost-per-guess benchmarks for dictionary attacks become outdated quickly]]

## How To Apply

Identify the specific key derivation scheme protecting the recovered credential (algorithm, iteration count, any custom application-specific construction) and, using [[techniques/Recover passwords using a dictionary attack with generated mangling rules on cloud GPUs]], run a short timed benchmark against currently available consumer-grade cloud GPU instances at current rental pricing to compute an up-to-date guesses-per-second and guesses-per-cost figure, rather than citing a historical benchmark from prior published research or an older investigation.

## References

- [LWCite-1020] Holmes and Buchanan, 2023, "A framework for live host-based Bitcoin wallet forensics and triage", FSI: Digital Investigation 44.

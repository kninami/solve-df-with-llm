---
id: DFW-1040
type: weakness
name: Game-theoretic anti-forensic tool prioritization requires new tools to be manually profiled first
description: Both the attacker's and investigator's payoff matrices are derived from prior empirical profiling of specific, named anti-forensic and counter-anti-forensic tools; a genuinely new tool not yet included in that profiling dataset has no payoff data and therefore cannot be incorporated into the game-theoretic model's equilibrium analysis until it is separately profiled and added.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1040
source_refs:
  - DFCite-1030
updated_at: 2026-08-09
status: complete
---

# Game-theoretic anti-forensic tool prioritization requires new tools to be manually profiled first

## Summary

The model's memory mechanism reduces the computational cost of re-simulating the game as tools are added to either player's action space, but it does not eliminate the prior step of empirically profiling how a new tool performs against every existing tool on the other side to populate the payoff matrix. Newly released anti-forensic tools, or ones not previously studied, therefore have no representation in the model until this profiling work is separately completed.

## Why It Matters

An investigator relying on this framework's equilibrium-derived recommendations to prioritize counter-anti-forensic tool acquisition or development could be operating on stale coverage if a new or rapidly evolving anti-forensic technique has appeared since the payoff data was last updated, without any signal from the model itself that its recommendations no longer reflect the current threat landscape. The framework's usefulness is thus bounded by the currency and completeness of its underlying profiling dataset, not by the game-theoretic algorithm's own capability.

## Related Mitigations

- [[mitigations/Maintain and regularly update the anti-forensic tool payoff-matrix profiling dataset]]

## Used By

- [[techniques/Prioritize counter-anti-forensic tools using a memory-augmented game-theoretic model]]

## References

- [DFCite-1030] Shafiee Hasanabadi et al., 2021, "A memory-based game-theoretic defensive approach for digital forensic investigators", FSI: Digital Investigation 38.

---
id: DFM-1040
type: mitigation
name: Maintain and regularly update the anti-forensic tool payoff-matrix profiling dataset
source_refs:
  - DFCite-1030
updated_at: 2026-08-09
status: complete
---

# Maintain and regularly update the anti-forensic tool payoff-matrix profiling dataset

## Summary

Treat the game-theoretic model's payoff matrices as a living dataset requiring ongoing maintenance, not a one-time input; schedule regular profiling of newly released anti-forensic and counter-anti-forensic tools, and flag any tool without profiled payoff data as outside the current model's coverage.

## Addresses

- [[weaknesses/Game-theoretic anti-forensic tool prioritization requires new tools to be manually profiled first]]

## How To Apply

Establish a recurring process to identify newly released or newly relevant anti-forensic and counter-anti-forensic tools and empirically profile their effectiveness against the existing tool set, feeding the results into the payoff matrices before relying on the model's equilibrium output for prioritization decisions. When presenting the model's recommendations, explicitly note the profiling dataset's currency (which tools and as of when) so decision-makers understand that any tool released after that point is not yet reflected in the analysis.

## References

- [DFCite-1030] Shafiee Hasanabadi et al., 2021, "A memory-based game-theoretic defensive approach for digital forensic investigators", FSI: Digital Investigation 38.

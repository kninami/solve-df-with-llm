---
id: LWT-1039
type: technique
name: Prioritize counter-anti-forensic tools using a memory-augmented game-theoretic model
description: Model the repeated interaction between a digital forensic investigator (choosing counter-anti-forensic tools, e.g., anti-rootkits) and an attacker (choosing anti-forensic tools, e.g., rootkits) as a non-cooperative, non-zero-sum game, and use a memory mechanism that reuses a previously computed Nash equilibrium as the starting point when either side's tool set expands, so the investigator can identify which counter-anti-forensic tools are most effective against known anti-forensic tools without re-simulating the game from scratch each time a new tool appears.
objective_ids:
  - DFO-1004
weakness_ids:
  - LWW-1040
aliases:
  - Memory-augmented game-theoretic counter-anti-forensic tool prioritization
source_refs:
  - LWCite-1030
updated_at: 2026-08-09
status: complete
---

# Prioritize counter-anti-forensic tools using a memory-augmented game-theoretic model

## Summary

Existing game-theoretic security models generally assume the players' action spaces (the attacker's available anti-forensic tools, the investigator's available counter-anti-forensic tools) are fixed and must fully re-simulate the game from the start whenever a new tool is introduced into either side's toolkit. The proposed memory mechanism instead initializes the empirical-frequency beliefs of an expanded game using the previously examined Nash equilibrium of the prior (smaller) game, letting fictitious play or gradient play algorithms reach the new steady state in substantially fewer iterations.

## Details

Each player's payoff matrix is built from empirical profiling data characterizing how effectively each specific counter-anti-forensic tool (e.g., a named anti-rootkit product) performs against each specific anti-forensic tool (e.g., a named rootkit). As new tools are added to either player's action space, the memory mechanism carries forward the prior game's Nash equilibrium as the starting empirical frequency rather than initializing from a random strategy, and the resulting equilibrium's strategy weights reveal which counter-anti-forensic tools the investigator should prioritize as most broadly effective, and which anti-forensic tools most consistently favor the attacker.

## Examples

- Across 12 sequential experiments expanding from 4 to 15 total tool actions (5 attacker rootkits, 10 investigator anti-rootkits), applying the memory mechanism reduced the investigator's average required iterations to reach the steady state by 170.58 (fictitious play) and 54.91 (gradient play), and reduced the attacker's average required iterations by 179.5 (fictitious play) and 64.33 (gradient play), compared to re-simulating from scratch.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Game-theoretic anti-forensic tool prioritization requires new tools to be manually profiled first]]

## References

- [LWCite-1030] Shafiee Hasanabadi et al., 2021, "A memory-based game-theoretic defensive approach for digital forensic investigators", FSI: Digital Investigation 38.

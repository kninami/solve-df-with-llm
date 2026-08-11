---
id: DFT-1029
type: technique
name: Dictionary attack password recovery via mangling-rule generation and cloud GPU execution
description: Recover a password protecting an encrypted credential (a wallet file, extended private key, seed phrase, or other recovered encrypted artifact) using a dictionary-based offline guessing attack, combining two complementary improvements — automatically generating high-hit-ratio password-mangling rules by clustering real-world leaked-password corpora, and executing the resulting expanded dictionary attack cost-effectively at scale on rented, consumer-grade cloud GPU instances split in parallel — rather than relying on a hand-crafted ruleset or a single machine's guess rate.
objective_ids:
  - DFO-1016
weakness_ids:
  - DFW-1028
  - DFW-1099
aliases:
  - RuleForge
source_refs:
  - DFCite-1020
  - DFCite-1093
updated_at: 2026-08-10
status: complete
---

# Dictionary attack password recovery via mangling-rule generation and cloud GPU execution

## Summary

A dictionary attack's effectiveness depends on both the quality of its ruleset (how well it expands a base wordlist to cover real human password-modification habits) and the raw guessing throughput available within a fixed time and cost budget. Automatically deriving mangling rules from clustered real-world leaked-password data improves the former; renting parallel consumer-grade cloud GPU instances improves the latter, and the two combine directly since a better ruleset simply means more high-value guesses to run through the same GPU-accelerated pipeline.

## Details

**Mangling-rule generation (RuleForge)**: clusters a corpus of real-world leaked passwords together with their base dictionary words, using cluster representatives to derive transformation rules (character substitution, insertion, deletion, capitalization, word rotation, reversal, and overwrite commands — 19 in total, with configurable priorities) — rather than relying on hand-crafted or purely heuristic rulesets. Evaluating four clustering techniques (Affinity Propagation, Hierarchical Agglomerative Clustering, DBSCAN, and an improved MDBSCAN variant paired with SymSpell), the MDBSCAN-based configuration achieved up to an 11.67 percentage-point higher hit ratio than the original clustering-based method it extends, outperforming existing automated rule-generation tools and popular hand-crafted rulesets in most tested scenarios.

**Cloud GPU execution**: the specific encryption/key-derivation scheme protecting the target credential determines the achievable guess rate — a fast, weakly-iterated derivation is orders of magnitude faster to attack than a properly key-stretched one. Existing GPU-accelerated password-recovery tools' cryptographic primitives can be reused when developing a custom attack against a reverse-engineered, non-standard encryption scheme. Renting consumer-grade GPU instances from a commercial cloud platform is markedly more cost-effective per guess than commercial-grade GPUs, and splitting a fixed dictionary across many rented instances in parallel linearly reduces wall-clock time for a fixed cost, with total cost for a given attack window estimated as (guesses-per-second-per-instance × instances × time) ÷ hourly rental cost.

## Examples

- Recovering an Electrum wallet's encrypted extended private key (protected by only 2 fast SHA-256 operations and one AES-256 block decrypt) achieved 16.6 billion guesses/hour for ~£25 on a single rented NVIDIA RTX 3090 instance; recovering a Ledger BIP39 seed phrase password (PBKDF2-HMAC-SHA512, 2048 iterations) achieved 2.4 trillion guesses/hour for ~£25 by splitting the dictionary across 40 rented instances in parallel.
- RuleForge's MDBSCAN Combo configuration, trained and attacking against the RockYou960 leaked-password dataset, achieved a significantly higher hit rate than PACK and classic Levenshtein-based rule generation methods across most tested guess-count budgets.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Cloud GPU cost-per-guess benchmarks for dictionary attacks become outdated quickly]]
- [[weaknesses/RuleForge-generated mangling rules' cracking success depends heavily on training-wordlist similarity to the target]]

## References

- [DFCite-1020] Holmes and Buchanan, 2023, "A framework for live host-based Bitcoin wallet forensics and triage", FSI: Digital Investigation 44.
- [DFCite-1093] Hranický et al., 2025, "Beyond the dictionary attack: Enhancing password cracking efficiency through machine learning-induced mangling rules", FSI: Digital Investigation 52.

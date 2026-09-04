---
id: LWW-1099
type: weakness
name: RuleForge-generated mangling rules' cracking success depends heavily on training-wordlist similarity to the target
description: The hit ratio achieved by clustering-derived password-mangling rules depends heavily on how closely the training wordlist (used to derive the rules) and attack wordlist match the actual password-creation habits and language/cultural context of the target, meaning rules trained on a generic or mismatched leaked-password corpus can substantially underperform their benchmarked hit ratio against a specific real-world target.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1099
source_refs:
  - LWCite-1093
updated_at: 2026-08-10
status: complete
---

# RuleForge-generated mangling rules' cracking success depends heavily on training-wordlist similarity to the target

## Summary

The authors state this directly: "The attack's success depends on the training and attack wordlists. Using dictionaries similar to the nature of the target is likely to yield the best results." Benchmarked hit ratios (including the reported 11.67 percentage-point improvement) reflect performance on datasets where training and attack wordlists are drawn from similar, well-studied leaked-password corpora (e.g. RockYou960), which will not necessarily hold for a target population with different language, cultural password conventions, or password policy constraints.

## Why It Matters

A digital forensic lab that adopts a generic, published RuleForge ruleset without adapting the training data to the target's likely password-creation context (organizational policy, language, common local naming conventions, etc.) risks substantially lower real-world cracking success than the published benchmarks suggest, potentially wasting significant compute time on an underperforming ruleset instead of building or selecting a more context-appropriate one.

## Related Mitigations

- [[mitigations/Train RuleForge-style mangling rules on wordlists matched to the target's context before relying on published benchmark hit ratios]]

## Used By

- [[techniques/Recover passwords using a dictionary attack with generated mangling rules on cloud GPUs]]

## References

- [LWCite-1093] Hranický et al., 2025, "Beyond the dictionary attack: Enhancing password cracking efficiency through machine learning-induced mangling rules", FSI: Digital Investigation 52.

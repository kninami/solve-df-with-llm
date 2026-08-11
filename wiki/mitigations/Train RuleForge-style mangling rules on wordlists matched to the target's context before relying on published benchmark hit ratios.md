---
id: DFM-1099
type: mitigation
name: Train RuleForge-style mangling rules on wordlists matched to the target's context before relying on published benchmark hit ratios
source_refs:
  - DFCite-1093
updated_at: 2026-08-10
status: complete
---

# Train RuleForge-style mangling rules on wordlists matched to the target's context before relying on published benchmark hit ratios

## Summary

Before relying on published RuleForge (or similar clustering-derived) hit-ratio benchmarks for a real cracking attempt, train the mangling rules on a wordlist matched as closely as possible to the target's likely language, cultural context, and organizational password conventions, rather than assuming a generic benchmark ruleset will transfer directly.

## Addresses

- [[weaknesses/RuleForge-generated mangling rules' cracking success depends heavily on training-wordlist similarity to the target]]

## How To Apply

Gather or construct a training wordlist reflecting the target's context (organization-specific terms, target-population language, known prior leaked-credential corpora relevant to the case) before generating a ruleset, rather than defaulting to a generic published training set. Where target context is unknown, budget for lower-than-benchmark hit ratios and consider running multiple rulesets trained on different candidate contexts in parallel.

## References

- [DFCite-1093] Hranický et al., 2025, "Beyond the dictionary attack: Enhancing password cracking efficiency through machine learning-induced mangling rules", FSI: Digital Investigation 52.

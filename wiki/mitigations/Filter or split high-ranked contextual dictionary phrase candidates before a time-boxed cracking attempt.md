---
id: DFM-1246
type: mitigation
name: Filter or split high-ranked contextual dictionary phrase candidates before a time-boxed cracking attempt
source_refs:
  - DFCite-1260
updated_at: 2026-08-13
status: complete
---

# Filter or split high-ranked contextual dictionary phrase candidates before a time-boxed cracking attempt

## Summary

Before running a time- or guess-limited attack against a contextual, knowledge-graph-derived password dictionary, review and either split multi-word phrase entries into their component words or otherwise deprioritize implausible phrase-level candidates, so the limited attack budget is spent on more structurally realistic password guesses first.

## Addresses

- [[weaknesses/Contextual dictionary similarity ranking surfaces high-similarity phrase candidates that are unlikely real passwords]]

## How To Apply

Post-process a ranked contextual dictionary before an attack: split multi-word phrase candidates into individual constituent words (which can then be combined with mangling rules per [[techniques/Recover passwords using a dictionary attack with generated mangling rules on cloud GPUs]]), and consider re-ranking or interleaving single-word candidates ahead of longer phrase entries when the time budget is tight. Where compute budget allows, run the phrase-level and word-level candidate sets as separate passes so a time-boxed attack can be terminated after the higher-probability word-level pass without losing coverage of the phrase-level candidates entirely.

## References

- [DFCite-1260] Kanta, Coisel, and Scanlon, 2023, "Harder, better, faster, stronger: Optimising the performance of context-based password cracking dictionaries", FSI: Digital Investigation 44, 301507.

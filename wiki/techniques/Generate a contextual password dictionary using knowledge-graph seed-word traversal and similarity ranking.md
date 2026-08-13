---
id: DFT-1227
type: technique
name: Generate a contextual password dictionary using knowledge-graph seed-word traversal and similarity ranking
description: Build a targeted password-candidate dictionary for a specific suspect or account by traversing a knowledge graph (e.g., DBPedia) outward from a seed word describing the target's known interests, then ranking the resulting candidate terms by semantic similarity to the seed using pre-trained word embeddings (e.g., Wikipedia2Vec), so a dictionary attack can try the most contextually plausible candidates first.
objective_ids:
  - DFO-1016
weakness_ids:
  - DFW-1245
aliases:
  - Context-based password cracking dictionary optimization
source_refs:
  - DFCite-1260
updated_at: 2026-08-13
status: complete
---

# Generate a contextual password dictionary using knowledge-graph seed-word traversal and similarity ranking

## Summary

A password is often an extension of its creator, drawing on a person's known interests, hobbies, or affiliations; generic dictionaries do not exploit this. Starting from one or more seed words that describe a target's known context (from OSINT, case background, or prior interviews), traversing a structured knowledge graph outward from those seeds and ranking the resulting terms by embedding-based semantic similarity produces a compact, prioritized wordlist far more likely to contain the actual password early, within a limited investigative time budget.

## Details

The methodology composes a contextual wordlist in stages: (1) a seed word or phrase describing the target's known interest is chosen (e.g., a hobby, media franchise, or affiliation identified through the investigation); (2) DBPedia (a structured, queryable knowledge graph derived from Wikipedia) is traversed outward from the seed's corresponding entity, following related-entity links to collect a pool of thematically connected candidate terms; (3) each candidate is scored for semantic proximity to the seed using Wikipedia2Vec pre-trained word embeddings, and the pool is ranked by this similarity score, from most to least contextually relevant; and (4) the ranked list is used directly as a dictionary, or combined with mangling rules (see [[techniques/Recover passwords using a dictionary attack with generated mangling rules on cloud GPUs]]) for an expanded attack. Because ranking surfaces the most probable candidates first, a time-boxed cracking attempt can be terminated early with a higher expected hit rate than working through an unranked or generic dictionary of the same size. This approach is directly motivated by empirical findings that overall password guessability improves substantially once population-level statistics are exhausted and target-specific context is incorporated (see [[techniques/Estimate password-cracking feasibility using large-scale breach-corpus guessability analysis]]), and it operationalizes the general recommendation to train or select cracking dictionaries matched to a target's context (see [[weaknesses/RuleForge-generated mangling rules' cracking success depends heavily on training-wordlist similarity to the target]]).

## Examples

- Seeding the traversal with a media franchise or hobby known to be of interest to a target produces a ranked dictionary front-loaded with franchise- or hobby-specific terms and named entities, several ranks of which are themselves multi-word phrases (e.g., a media series title) rather than single dictionary words.
- Experimental results comparing dictionaries generated with and without the DBPedia-traversal-plus-Wikipedia2Vec-ranking step demonstrate a faster, higher-success-rate recovery of passwords known to be thematically linked to the seed context, compared to an equivalently-sized generic or unranked contextual dictionary.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Contextual dictionary similarity ranking surfaces high-similarity phrase candidates that are unlikely real passwords]]

## References

- [DFCite-1260] Kanta, Coisel, and Scanlon, 2023, "Harder, better, faster, stronger: Optimising the performance of context-based password cracking dictionaries", FSI: Digital Investigation 44, 301507.

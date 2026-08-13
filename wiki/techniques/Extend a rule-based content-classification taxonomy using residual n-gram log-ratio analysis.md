---
id: DFT-1188
type: technique
name: Extend a rule-based content-classification taxonomy using residual n-gram log-ratio analysis
description: Apply an initial deterministic, rule-based taxonomy to classify forum or forensic text content, then statistically mine the residual unclassifiable cases for n-grams disproportionately associated with ambiguity, using a smoothed log-ratio score, to surface candidate new taxonomy categories and iteratively re-classify the corpus until residual ambiguity is minimized.
objective_ids:
  - DFO-1003
weakness_ids:
  - DFW-1195
aliases:
  - Iterative taxonomy extension methodology
  - P2P crypto forum taxonomy classification
source_refs:
  - DFCite-1204
updated_at: 2026-08-13
status: complete
---

# Extend a rule-based content-classification taxonomy using residual n-gram log-ratio analysis

## Summary

For domains with high semantic homogeneity — such as peer-to-peer cryptocurrency trading forums, where posts are terse and formulaic rather than discursive — a deterministic, regex/lexicon-based classifier can achieve high, auditable coverage on well-represented predicates while leaving a large residual of cases it cannot classify. Rather than treating that residual as noise, comparing its n-gram vocabulary against the vocabulary of successfully classified cases identifies terms statistically over-represented in the ambiguous set, which serve as evidence-based candidates for new taxonomy categories.

## Details

Classification proceeds in an auditable, rule-first pipeline: a deterministic Phase 1 classifier applies explicit regular expressions and lexicons (a lexicon of unambiguous canonical tokens, and a longest-match-ordered list of names/aliases) to assign values for each predicate (e.g., transactional intent, traded asset, payment mechanism, risk indicator); an LLM is used only as a secondary verifier for cases the deterministic rules leave unresolved (labeled "other"/"unclear"), and is explicitly constrained to confirming or rejecting one of the already-permitted taxonomy values rather than introducing new categories, preserving traceability of every assignment back to an explicit rule. To identify candidate taxonomy extensions, a composite text field is built per post, normalized and tokenized into unigrams/bigrams/trigrams separately for the "clear" (classified) and "unclear" (residual) subsets; for each n-gram, a log-ratio score `log(p_unclear / p_clear)` is computed with additive (Laplace) smoothing to avoid undefined ratios for terms absent from one subset, and terms already used by other predicates (to avoid semantic collisions) are excluded. High-scoring n-grams are manually reviewed and, where they represent a genuine unmodeled functional subclass, promoted to new taxonomy categories; the corpus is then re-classified under the extended taxonomy, and the process (classify → diagnose residual ambiguity → extract candidates → consolidate) can repeat. A random-sample manual validation of assigned labels (as distinct from a check of raw coverage, which only measures how much of the corpus received a non-residual label, not whether that label was correct) should accompany each iteration. The same pipeline supports a downstream co-occurrence/lexical-clustering network analysis of the classified corpus to reveal functional communities within the domain.

## Examples

- Applied to a corpus of 23,642 posts from P2P cryptocurrency dark web forums, the initial deterministic classifier achieved 83.84% coverage for transactional intent and 98.87% for the primary traded asset, but only 0.5% and 1.48% coverage for payment mechanism and risk indicator respectively, leaving those two predicates almost entirely "unclear."
- Log-ratio analysis of the unclear residual surfaced platform-name and forum-discussion n-grams (e.g., an exchange-platform brand name, and generic forum/wiki-question phrasing) as strongly associated with ambiguity; incorporating "exchange-platform" and "forum" as new categories raised payment-mechanism coverage to 76% and eliminated the "other" intent category entirely (100% intent coverage), while a manual-validation sample confirmed 96-100% correctness across the revised predicates.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Iteratively-extended forum classification taxonomies are corpus-specific and unvalidated on other forums]]

## References

- [DFCite-1204] Medina-Merodio et al., 2026, "Extending taxonomies for P2P crypto forum classification in the dark web: An iterative methodological approach", FSI: Digital Investigation 57.

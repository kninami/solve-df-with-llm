---
id: LWT-1231
type: technique
name: Estimate password-cracking feasibility using large-scale breach-corpus guessability analysis
description: Decide whether attempting to crack a specific password-protected artifact is a worthwhile use of investigative time by classifying the target's likely password strength (e.g., with the zxcvbn metric) and cross-referencing published guess-count, hardware, and hash-function-speed benchmarks derived from statistical analysis of billions of real-world breached passwords, rather than committing to an open-ended brute-force or dictionary attack without an evidence-based time estimate.
objective_ids:
  - DFO-1016
weakness_ids:
  - LWW-1249
aliases:
  - Óðinn password fragment analysis
source_refs:
  - LWCite-1264
updated_at: 2026-08-13
status: complete
---

# Estimate password-cracking feasibility using large-scale breach-corpus guessability analysis

## Summary

Digital forensic labs routinely face password-protected evidence but have limited time and compute budget to spend on any one cracking attempt with no guarantee of success. Analyzing the largest available real-world password corpus (over 3.9 billion accounts from the Have I Been Pwned dataset) — decomposing passwords into semantically classified fragments and scoring their strength — provides actionable, evidence-based guidance on how many guesses, how much hardware, and how much time a given class of password realistically requires, letting an investigator decide up front whether cracking a specific target is worth attempting.

## Details

The Óðinn framework fragments each password into its constituent letter, number, and special-character components (e.g., splitting `ilovemom` into `i`, `love`, `mom`) using a spelling-correction algorithm (SymSpell) trained on a large corpus of informal text, then classifies each fragment semantically (as a name, year, city, animal, keyboard-walk pattern, etc.) using WordNet, custom dictionaries, and GloVe embeddings for fragments not found verbatim. Separately, the zxcvbn password-strength metric assigns each password an integer score from 0 (weakest) to 4 (strongest) based on estimated guess count; cross-referencing each score class against measured guess rates for both fast (MD5) and slow, purpose-built (BCRYPT) hash functions on consumer GPU hardware yields concrete crack-time estimates per class. Combining the two analyses further refines feasibility estimates: score-4 ("strongest") passwords average 4.4 fragments versus 2.1 for the full dataset, meaning that even nominally strong passwords remain vulnerable to fragment-informed targeted attacks once some context about the specific person is known, in a way a pure entropy-based strength score does not capture.

## Examples

- Considering a fast hash function (MD5) on a single consumer GPU (NVIDIA 2080 Ti), zxcvbn score-3-and-below passwords (representing roughly 80% of the analyzed dataset) were recoverable via exhaustive search within a few days, while a specific score-4 password with a common construction pattern (15 digits) was fully exhaustible within a day even under a slow hash function (BCRYPT); a comparable 12-lowercase-character score-4 password took approximately 22 days under MD5 but 120,961 days under BCRYPT, illustrating how heavily feasibility depends on the target's hash function rather than password strength alone.
- A preliminary case study on a themed website's breach (a manga-fan forum) found that 37.6% of its top 100 most-frequent passwords, and 63.8% of its top 100 base words, were manga-related — supporting the use of thematic, context-derived candidate generation (see [[techniques/Generate a contextual password dictionary using knowledge-graph seed-word traversal and similarity ranking]]) once generic, non-contextual approaches are exhausted.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Breach-corpus password guessability analysis systematically underrepresents genuinely strong, unrecovered passwords]]

## References

- [LWCite-1264] Kanta, Coray, Coisel, and Scanlon, 2021, "How viable is password cracking in digital forensic investigation? Analyzing the guessability of over 3.9 billion real-world accounts", FSI: Digital Investigation 37, 301186.

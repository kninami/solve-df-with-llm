---
id: DFW-1249
type: weakness
name: Breach-corpus password guessability analysis systematically underrepresents genuinely strong, unrecovered passwords
description: A statistical guessability analysis built from a breach corpus of previously-cracked plaintext passwords is structurally biased toward weaker passwords, because the strongest passwords in the source breach — if stored securely and never successfully recovered by the community that reverse-engineered the corpus's plaintext values — are absent from the dataset entirely.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1250
source_refs:
  - DFCite-1264
updated_at: 2026-08-13
status: complete
---

# Breach-corpus password guessability analysis systematically underrepresents genuinely strong, unrecovered passwords

## Summary

The Have I Been Pwned dataset used for large-scale guessability analysis is composed of passwords that a community reverse-engineering effort (achieving a claimed 99.9999% recovery ratio) successfully recovered from hashed breach data, plus passwords obtained where the original source stored them in cleartext. Both composition sources bias the corpus toward weaker passwords: a password protected by a hash the community failed to crack is missing from the dataset by definition, and a password recovered because it was stored in cleartext implies the responsible service was not following basic password-storage security recommendations to begin with — a further correlate of weaker overall password hygiene at that service.

## Why It Matters

An investigator or researcher using population-level guessability statistics drawn from this kind of corpus to judge how "typical" a given password's strength is risks underestimating how many genuinely strong, well-protected passwords exist in the real world, since those are structurally excluded from the analysis. This does not undermine the validity of guessability conclusions for the overwhelming proportion of accounts the corpus does represent, but it does mean the corpus should not be treated as an unbiased sample of all real-world passwords, particularly when assessing a specific well-secured target.

## Related Mitigations

- [[mitigations/Account for breach-corpus strong-password underrepresentation when setting guessability-based investigative expectations]]

## Used By

- [[techniques/Estimate password-cracking feasibility using large-scale breach-corpus guessability analysis]]

## References

- [DFCite-1264] Kanta, Coray, Coisel, and Scanlon, 2021, "How viable is password cracking in digital forensic investigation? Analyzing the guessability of over 3.9 billion real-world accounts", FSI: Digital Investigation 37, 301186.

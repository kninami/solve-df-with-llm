---
id: LWM-1250
type: mitigation
name: Account for breach-corpus strong-password underrepresentation when setting guessability-based investigative expectations
source_refs:
  - LWCite-1264
updated_at: 2026-08-13
status: complete
---

# Account for breach-corpus strong-password underrepresentation when setting guessability-based investigative expectations

## Summary

Treat breach-corpus-derived guessability statistics as a lower bound on real-world password strength rather than a comprehensive picture, since the strongest, best-protected passwords are structurally excluded from any corpus built from successfully-recovered plaintext, and supplement population-level statistics with a target-specific hardware/hash-function feasibility estimate before committing investigative resources.

## Addresses

- [[weaknesses/Breach-corpus password guessability analysis systematically underrepresents genuinely strong, unrecovered passwords]]

## How To Apply

When citing breach-corpus statistics (e.g., "80% of passwords fall in a weak strength class") to justify a cracking attempt, note explicitly that the underlying corpus is biased toward recoverable — and therefore comparatively weaker or poorly-stored — passwords, and do not assume the same proportion holds for the specific target account, especially if it is known to be protected by a security-conscious service. Before committing to an attack, run the target-specific feasibility estimate described in [[techniques/Estimate password-cracking feasibility using large-scale breach-corpus guessability analysis]] against the actual hash function and available hardware, rather than relying on the corpus-wide weak-password proportion alone.

## References

- [LWCite-1264] Kanta, Coray, Coisel, and Scanlon, 2021, "How viable is password cracking in digital forensic investigation? Analyzing the guessability of over 3.9 billion real-world accounts", FSI: Digital Investigation 37, 301186.

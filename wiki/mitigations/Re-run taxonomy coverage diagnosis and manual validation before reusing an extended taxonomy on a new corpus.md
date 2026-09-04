---
id: LWM-1195
type: mitigation
name: Re-run taxonomy coverage diagnosis and manual validation before reusing an extended taxonomy on a new corpus
source_refs:
  - LWCite-1204
updated_at: 2026-08-13
status: complete
---

# Re-run taxonomy coverage diagnosis and manual validation before reusing an extended taxonomy on a new corpus

## Summary

Before applying a taxonomy and rule set extended for one forum or corpus to a new one, re-run the initial deterministic classification pass to measure coverage per predicate on the new corpus, and treat low coverage as a signal that the taxonomy needs its own extension cycle rather than assuming it transfers.

## Addresses

- [[weaknesses/Iteratively-extended forum classification taxonomies are corpus-specific and unvalidated on other forums]]

## How To Apply

Apply the existing deterministic rules to a sample of the new corpus and record per-predicate coverage; where coverage for a predicate falls well short of the levels achieved on the original corpus, extract and score residual n-grams from the new corpus's own "unclear" cases rather than reusing candidate categories mined from the original forum. Independently manually validate a random sample of assigned labels on the new corpus, since coverage alone measures rule applicability, not classification correctness, and both must be checked before results are relied upon operationally.

## References

- [LWCite-1204] Medina-Merodio et al., 2026, "Extending taxonomies for P2P crypto forum classification in the dark web: An iterative methodological approach", FSI: Digital Investigation 57.

---
id: DFW-1195
type: weakness
name: Iteratively-extended forum classification taxonomies are corpus-specific and unvalidated on other forums
description: A taxonomy extended through residual n-gram analysis of one corpus captures the statistical and morphological patterns specific to that single forum's vocabulary, language mix, and platform conventions, and has not been calibrated or validated against a different forum, a different cryptoasset community, or a different language mix.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1195
source_refs:
  - DFCite-1204
updated_at: 2026-08-13
status: complete
---

# Iteratively-extended forum classification taxonomies are corpus-specific and unvalidated on other forums

## Summary

The extended taxonomy's new categories (e.g., an exchange-platform predicate value derived from a specific brand name repeatedly mentioned in one forum) emerged from log-ratio analysis of that forum's own residual vocabulary. The paper's own stated limitations note the taxonomy has neither been calibrated across multiple forums nor validated in different linguistic or platform contexts, and that automatic translation and the low lexical dispersion of the source corpus are themselves methodological constraints specific to the studied dataset.

## Why It Matters

Applying a taxonomy (and its deterministic rule set) extended for one forum directly to a different P2P crypto forum, a different illicit-goods domain, or content in a different primary language risks reproducing the same high-residual-ambiguity problem the extension process was designed to solve, since the new categories and their supporting lexicons reflect one community's specific vocabulary rather than a general property of the domain. An investigator who assumes coverage gains transfer without re-running the diagnosis-and-extension cycle on the new corpus may under-classify a large fraction of new content without realizing it.

## Related Mitigations

- [[mitigations/Re-run taxonomy coverage diagnosis and manual validation before reusing an extended taxonomy on a new corpus]]

## Used By

- [[techniques/Extend a rule-based content-classification taxonomy using residual n-gram log-ratio analysis]]

## References

- [DFCite-1204] Medina-Merodio et al., 2026, "Extending taxonomies for P2P crypto forum classification in the dark web: An iterative methodological approach", FSI: Digital Investigation 57.

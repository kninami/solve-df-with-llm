---
id: DFM-2002
type: mitigation
name: Re-weight or filter feature-scoring toolkit rankings by the specific case's required features before selecting a tool
source_refs:
  - DFCite-2002
updated_at: 2026-08-14
status: partial
---

# Re-weight or filter feature-scoring toolkit rankings by the specific case's required features before selecting a tool

## Summary

Before adopting a feature-scoring model's top-ranked toolkit, identify the specific features the current case requires (e.g. RAID reconstruction, a particular browser, a particular memory dump format) and either filter candidate toolkits to only those supporting the required features, or apply case-specific weights instead of the model's default equal weighting.

## Addresses

- [[weaknesses/A feature-scoring toolkit ranking that weights all features equally can misrank the best tool for a case's actual priorities]]

## How To Apply

Treat the domain-wide FSM percentage as a shortlisting aid, not a final decision. Cross-check the case's known evidence types and constraints (source OS, image format, suspected artifact types) against the underlying per-feature comparison tables before finalizing toolkit selection, and prefer a lower-overall-score toolkit if it uniquely covers a feature the case specifically requires.

## References

- [DFCite-2002] Javed et al., 2022 — the survey's own per-feature comparison tables (e.g. Table 6-15) provide the granular data needed to check case-specific feature coverage behind the aggregate FSM score.

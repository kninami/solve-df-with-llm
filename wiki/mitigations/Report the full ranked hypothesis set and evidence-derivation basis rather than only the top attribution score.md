---
id: DFM-1047
type: mitigation
name: Report the full ranked hypothesis set and evidence-derivation basis rather than only the top attribution score
source_refs:
  - DFCite-1037
updated_at: 2026-08-09
status: complete
---

# Report the full ranked hypothesis set and evidence-derivation basis rather than only the top attribution score

## Summary

When presenting an ontology-based attribution reasoner's output, report the full set of ranked hypotheses and their scores, not just the top candidate, and distinguish which parts of each hypothesis's derivation come from case-specific evidence versus general background-knowledge rules.

## Addresses

- [[weaknesses/Ontology-based attribution reasoning can produce weakly-differentiated attribution hypotheses]]

## How To Apply

When reviewing attribution output from a reasoning-based tool, examine the derivation/argumentation tree behind each hypothesis to identify how many of the applied rules are grounded in case-specific evidence (technical indicators, observed data specific to this attack) versus general background knowledge (industry patterns, historical actor behavior not specific to this case). Present the top hypothesis alongside its closest-scoring alternatives and the score margin between them, so a reader can judge whether the evidence meaningfully discriminates the leading hypothesis from its competitors rather than treating the highest score as a definitive conclusion.

## References

- [DFCite-1037] Kaur Gill and Karafili, 2026, "A novel ontology for cyber-attack attribution and investigation", FSI: Digital Investigation 57.

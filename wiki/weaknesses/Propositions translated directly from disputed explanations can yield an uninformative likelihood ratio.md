---
id: LWW-1233
type: weakness
name: Propositions translated directly from disputed explanations can yield an uninformative likelihood ratio
description: Translating a party's alternative explanation into a proposition without checking that it captures the actually-disputed aspect of the case (the actor, the activity, or the presence of intent) can produce a proposition pair under which the observed evidence is equally probable, yielding a likelihood ratio of 1.0 that provides no evidential weight despite appearing to be a completed evaluation.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1233
source_refs:
  - LWCite-1246
updated_at: 2026-08-13
status: complete
---

# Propositions translated directly from disputed explanations can yield an uninformative likelihood ratio

## Summary

The paper demonstrates this directly with a fictive example: if two explanations ("the suspect left the traces" vs. "another person with physical access left the traces") are translated straight into propositions H1 and H2 without further refinement, the probability of finding the observed traces is 1 under both scenarios, so the resulting LR is 1.0 — an outcome that looks like a completed, balanced evaluation but in fact conveys no information about which proposition the evidence favors.

## Why It Matters

A likelihood ratio of exactly 1.0 is easy to mistake for a genuinely neutral finding rather than a symptom of poorly formulated propositions, especially since the LR framework's structure (two competing propositions, a computed ratio) gives the output an appearance of rigor regardless of whether the propositions were well-formed. An expert or court that accepts an uninformative LR at face value, rather than recognizing it as a signal to revisit the proposition formulation, risks either wrongly concluding the evidence is neutral or wasting the evaluative exercise entirely — undermining the balanced, transparent reasoning the LR framework is meant to provide.

## Related Mitigations

- [[mitigations/Formulate mutually exclusive propositions around the specific disputed actor, activity, or intent before deriving a likelihood ratio]]

## Used By

- [[techniques/Formulate competing propositions for likelihood-ratio evaluation of Trojan horse defense claims]]

## References

- [LWCite-1246] Vink et al., 2025, "Formulating propositions in Trojan horse defense cases", FSI: Digital Investigation 53, 301915.

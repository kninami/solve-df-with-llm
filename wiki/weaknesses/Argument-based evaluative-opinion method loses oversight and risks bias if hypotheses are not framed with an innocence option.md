---
id: DFW-1065
type: weakness
name: Argument-based evaluative-opinion method loses oversight and risks bias if hypotheses are not framed with an innocence option
description: The argument-based method for evaluating digital evidence becomes difficult to keep track of as the number of evidence pieces, grounds, and inferential leaps considered under a single hypothesis grows, and produces a misleading result if both compared hypotheses are framed as guilt hypotheses rather than including a genuine innocence-oriented hypothesis, since the resulting probative-value comparison would then only rank one guilt theory against another rather than testing guilt against innocence.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1065
source_refs:
  - DFCite-1055
updated_at: 2026-08-10
status: complete
---

# Argument-based evaluative-opinion method loses oversight and risks bias if hypotheses are not framed with an innocence option

## Summary

The method's authors identify two related limitations from applying it. First, complexity: when many pieces of evidence and grounds, each with its own inferential leaps and supporting tests, must be considered under one hypothesis, the practitioner can lose oversight of the full argument structure. Second, and more consequential, fairness depends on how the two compared hypotheses are framed — if both are variants of a guilt theory (e.g. comparing which of two guilt routes is more probable) rather than one guilt hypothesis against a genuine innocence hypothesis, the method's output answers a different question than "is the suspect guilty," undermining the presumption of innocence the method is otherwise designed to support.

## Why It Matters

Because the method is explicitly intended to produce transparent, auditable reasoning for legal decision-makers, a practitioner who fails to include an innocence-oriented hypothesis produces an opinion that looks methodologically rigorous while actually comparing the wrong pair of hypotheses, a flaw that is not visible from the Argument Matrix output alone unless a reviewer checks how the hypotheses were originally framed. Similarly, an analysis that has grown too complex to visually track risks components being overlooked or double-counted without a reviewer noticing.

## Related Mitigations

- [[mitigations/Frame at least one hypothesis as an innocence hypothesis and visualize argument structure when applying an argument-based evaluative-opinion method]]

## Used By

- [[techniques/Evaluate digital evidence probative value using structured argumentation]]

## References

- [DFCite-1055] Sunde and Franqueira, 2023, "Adding transparency to uncertainty: An argument-based method for evaluative opinions", FSI: Digital Investigation 47.

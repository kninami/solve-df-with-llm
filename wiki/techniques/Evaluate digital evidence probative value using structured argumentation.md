---
id: LWT-1060
type: technique
name: Evaluate digital evidence probative value using structured argumentation
description: Produce a documented, non-numerical evaluative opinion on digital evidence by explicitly constructing arguments for two opposing hypotheses (with at least one framed as an innocence hypothesis), decomposing each argument into scored grounds/warrants/backing components, systematically identifying and scoring "attacks" (counter-considerations) against each component, and combining the results in an Argument Matrix to determine the evidence's relative probative value under each hypothesis.
objective_ids:
  - DFO-1003
weakness_ids:
  - LWW-1065
aliases:
  - Argument-based structured evaluation of digital evidence probative value
  - Argument-Based Method for Evaluative Opinions
source_refs:
  - LWCite-1055
updated_at: 2026-08-10
status: complete
---

# Evaluate digital evidence probative value using structured argumentation

## Summary

Digital evidence evaluation is often characterized by high subjectivity, with no fixed reference database comparable to other forensic disciplines. This method draws on argumentation theory (Toulmin-style argument components) combined with probabilistic and narrative/scenario concepts to force an examiner to make their reasoning about evidence credibility and relevance explicit and auditable, rather than relying on an intuitive, unstructured judgment.

## Details

The practitioner identifies two opposing hypotheses (one of which should be an innocence hypothesis, to avoid a fairness-undermining comparison of two guilt theories against each other), then for each hypothesis builds an argument from grounds (the evidence and inferential steps supporting it). Each ground and inferential leap is scored on a defined Argument Evaluation Scale for credibility and relevance, and possible "attacks" — considerations that weaken a component's credibility or relevance — are systematically identified and scored against it. The results are combined in an Argument Matrix to arrive at a holistic determination of the evidence's probative value under each hypothesis. The method can be used stand-alone or alongside quantitative/statistical approaches, and is presented as complementary to (not a replacement for) Analysis of Competing Hypotheses (ACH), since ACH assesses each piece of evidence atomically against each hypothesis and does not capture dependencies between grounds — for example, one ground's credibility being conditioned on another ground's assessment.

## Examples

- A case study evaluating a suspect's claimed travel route based on step-count and CCTV timing evidence: applying the method's dialectic (attack-based) process reduced the credibility of both competing route hypotheses from "weak" to "very weak" once evidential gaps were surfaced, without changing their relative probative value.
- A case study where a police officer claimed to recognize a suspect in poor-quality CCTV footage: systematically evaluating the digital evidence underlying the identification revealed that the footage's poor quality diminished its probative value despite the officer's strong subjective conviction.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Argument-based evaluative-opinion method loses oversight and risks bias if hypotheses are not framed with an innocence option]]

## References

- [LWCite-1055] Sunde and Franqueira, 2023, "Adding transparency to uncertainty: An argument-based method for evaluative opinions", FSI: Digital Investigation 47.

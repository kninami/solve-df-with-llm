---
id: DFW-1193
type: weakness
name: Fine-tuned LLM author profiling misclassifies authors whose writing deviates from gender-stereotyped norms
description: A fine-tuned LLM's age/gender predictions are learned from correlations in its training corpus rather than causal linguistic markers, so male authors with emotional or expressive writing styles and female authors with assertive or analytical styles are disproportionately misclassified, and adjacent age groups are frequently confused.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1193
source_refs:
  - DFCite-1201
updated_at: 2026-08-13
status: complete
---

# Fine-tuned LLM author profiling misclassifies authors whose writing deviates from gender-stereotyped norms

## Summary

Error analysis of a fine-tuned Polyglot model's gender predictions found a substantially lower F1-score for the male class (0.59) than the female class (0.91), driven specifically by authors whose writing style did not match the training data's stereotypical associations — male authors writing in an emotional or expressive register were misclassified as female, and female authors writing in an assertive or analytical register were misclassified as male. Age-group predictions showed a related but distinct failure mode: the model struggled most with linguistically similar adjacent age groups, and overall age accuracy (around 61%) was markedly lower than gender accuracy (up to 87%), reflecting subtler and less consistently marked linguistic differences across age.

## Why It Matters

An investigator using LLM-predicted demographic characteristics to narrow a suspect pool risks wrongly excluding or including candidates if the prediction is treated as a reliable identity signal rather than a probabilistic, bias-prone lead — particularly for authors whose writing does not conform to the demographic stereotypes latent in the model's training data. Because the underlying LLM's decision-making process is largely opaque, an investigator cannot easily tell, for a specific prediction, whether it reflects a genuine stylistic pattern or a stereotype-driven misclassification.

## Related Mitigations

- [[mitigations/Corroborate LLM author-profiling predictions with independent evidence before treating them as identifying]]

## Used By

- [[techniques/Predict an author's age and gender using a fine-tuned LLM]]

## References

- [DFCite-1201] Cho et al., 2024, "Exploring the potential of large language models for author profiling tasks in digital text forensics", FSI: Digital Investigation 50.

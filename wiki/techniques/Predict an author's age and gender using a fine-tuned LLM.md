---
id: LWT-1186
type: technique
name: Predict an author's age and gender using a fine-tuned LLM
description: Fine-tune a large language model, using full fine-tuning or a parameter-efficient method such as LoRA/QLoRA, on labeled writing samples to predict an anonymous or pseudonymous author's demographic characteristics — such as age group and gender — from their writing style, narrowing a suspect pool in text-based investigations.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-1193
aliases:
  - LLM-based author profiling
  - Author profiling for digital text forensics
source_refs:
  - LWCite-1201
updated_at: 2026-08-13
status: complete
---

# Predict an author's age and gender using a fine-tuned LLM

## Summary

Author profiling — inferring demographic traits such as age and gender from writing style rather than confirming a specific individual's identity — narrows the pool of possible authors in cybercrime, online harassment, fraud, and other investigations involving anonymous or pseudonymous text. Fine-tuning a pre-trained LLM on labeled dialogue/writing data can substantially outperform traditional feature-engineered classifiers (e.g. SVMs) at this task, particularly for gender prediction.

## Details

Three multilingual/low-resource LLMs (Polyglot, EEVE, Bllossom) were fine-tuned using three strategies — full fine-tuning, Low-Rank Adaptation (LoRA), and Quantized LoRA (QLoRA) — on the NIKL Korean Dialogue Corpus (27,970 preprocessed dialogue utterances labeled with speaker age and gender). LoRA and QLoRA constrain parameter updates to small low-rank adapter matrices (and further quantize to 4-bit precision for QLoRA), substantially reducing training/inference compute and memory versus full fine-tuning while achieving comparable accuracy — a practical advantage for resource-constrained forensic labs and field-deployable analysis. Gender prediction reached up to 87% accuracy (Polyglot-3.8B); age-group prediction was markedly less accurate (around 61% for Polyglot-1.3B), reflecting the greater difficulty of capturing age-related linguistic variation than gender-related variation. Notably, the smaller Polyglot-1.3B model performed comparably to or better than larger variants on some metrics, suggesting effective author-profiling systems do not necessarily require the largest available LLM.

## Examples

- Polyglot-1.3B fine-tuned with LoRA achieved 0.85 overall accuracy on gender prediction, with an F1-score of 0.91 for the female class versus 0.59 for the male class, on a held-out set of 1,931 dialogues.
- Age prediction error analysis showed the model struggled most to distinguish between adjacent, linguistically similar age groups rather than between clearly distant ones.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Fine-tuned LLM author profiling misclassifies authors whose writing deviates from gender-stereotyped norms]]

## References

- [LWCite-1201] Cho et al., 2024, "Exploring the potential of large language models for author profiling tasks in digital text forensics", FSI: Digital Investigation 50.

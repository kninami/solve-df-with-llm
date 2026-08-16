---
id: DFT-1287
type: technique
name: Rank extracted text strings by password likelihood using fine-tuned language models
description: Search an already-unlocked device's text data (chats, notes, log files) for a cleartext password to a separate, still-locked "secure phone" by extracting every candidate text string and ranking it by likelihood of being a human-generated password using a fine-tuned deep-learning model, so an investigator can try the most promising candidates first instead of attempting an infeasibly large list of strings in an arbitrary order.
objective_ids:
  - DFO-1016
weakness_ids:
  - DFW-1297
aliases:
  - PaSSw0rdVib3s
  - AI-assisted password recognition
source_refs:
  - DFCite-1330
updated_at: 2026-08-15
status: complete
---

# Rank extracted text strings by password likelihood using fine-tuned language models

## Summary

"Secure phones" with hardened software and hardware make traditional brute-force and dictionary password-recovery attacks infeasible, but users still sometimes leave the device's password recorded in cleartext elsewhere — in a text message, a note, or a system log file on another, already-unlocked device. Because the number of candidate text strings extractable from a typical device is far too large to try against the secure phone one by one, framing "is this string a password?" as a machine-learning classification/ranking problem — distinguishing human-generated passwords from all other text — lets an investigator attempt only the most likely candidates first.

## Details

Several model architectures were fine-tuned and compared: three deep-learning models (PassGPT, CodeBERT, DistilBERT) and two traditional machine-learning models (a hand-engineered-feature-based XGBoost and a TF/IDF-based XGBoost), benchmarked against the existing state of the art, a probabilistic-context-free-grammar (PCFG) based password-recognition model. Two research questions drove the design: which mix of training data produces the best results, and which model architecture performs best on both machine-learning metrics and computational throughput (evaluations per second, since a ranking step must run against a large volume of extracted device text within realistic casework time budgets). Training-data composition proved critical: models trained only on dictionary words and leaked-credential lists underperform, and a wide variety of non-password text (data scraped from chats and general websites, in addition to dictionaries and leaks) is needed so the model can correctly distinguish passwords from the full variety of ordinary text actually found on devices, rather than only from the narrower distribution of a leaked-password corpus.

## Examples

- The fine-tuned PassGPT model outperformed the other four candidate models (CodeBERT, DistilBERT, feature-based XGBoost, TF/IDF-based XGBoost) and the PCFG state-of-the-art baseline on the password-ranking task.
- Evaluation was conducted not only on the publicly available RockYou and MyHeritage password-leak datasets but also on a dataset derived from real casework, and on hardware realistic for an investigator's own workstation (rather than a research cluster), demonstrating the approach's practicality for actual forensic deployment despite modern deep-learning models being slower per-string than traditional approaches.

## Related Objectives

- `DFO-1016` Overcome protection mechanisms

## Related Weaknesses

- [[weaknesses/Password-recognition ranking models underrank passwords unlike the specific mix of data they were trained on]]

## References

- [DFCite-1330] van Dijk, van de Wetering, Argentini, Gorka, van Luenen, Minnema, Rijgersberg, Ugen, Mann, and Geradts, 2025, "PaSSw0rdVib3s!: AI-assisted password recognition for digital forensic investigations", FSI: Digital Investigation 52, 301870.

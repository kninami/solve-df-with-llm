---
id: DFT-1216
type: technique
name: Query digital forensic literature and artifacts using a retrieval-augmented fine-tuned local LLM
description: Answer an investigator's natural-language questions about forensic tools, artifacts, and procedures using a small, locally-run LLM fine-tuned on digital forensics research papers and curated artifact data via Retrieval Augmented Fine-Tuning (RAFT), so responses cite their peer-reviewed source and no case data or query content leaves the local environment.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1232
aliases:
  - ForensicLLM
  - RAFT for digital forensics
source_refs:
  - DFCite-1243
updated_at: 2026-08-13
status: complete
---

# Query digital forensic literature and artifacts using a retrieval-augmented fine-tuned local LLM

## Summary

General-purpose cloud LLMs lack domain-specific forensic expertise and cannot be used where internet access or case-data confidentiality is restricted, while a plain local LLM without fine-tuning underperforms on forensic terminology and rarely cites sources. Combining LoRA/QLoRA fine-tuning with retrieval-augmented generation (RAFT) on a purpose-built Q&A dataset extracted from forensic research literature and a curated artifact repository produces a small (8B-parameter, 4-bit quantized) local model that runs on a single consumer GPU while outperforming both the un-tuned base model and a RAG-only baseline on correctness, relevance, and source-citation accuracy.

## Details

The training pipeline extracts text from digital forensics research papers (here, 1,082 papers from *Forensic Science International: Digital Investigation* and its predecessor) and from a curated forensic-artifact repository (the Artifact Genome Project), chunks it, embeds it into a vector store, and prompts a larger general-purpose LLM (GPT-4 Turbo) to generate roughly 10,000 question/answer pairs with mandatory source-citation formatting, filtering out pairs containing meta-referential phrasing ("in the above study"). Each training example combines the question with its top-10 most similar retrieved chunks (the RAFT step), and the base model (LLaMA-3.1-8B) is then fine-tuned via 4-bit-quantized QLoRA on this retrieval-augmented dataset. At inference time, the same embedding model retrieves relevant context for a new user question before the fine-tuned model generates its answer, so the model both reasons over retrieved context (like plain RAG) and has internalized domain terminology and citation behavior (unlike plain RAG on an un-tuned base model).

## Examples

- On a 2,244-question held-out test set, the fine-tuned model scored 0.9232 BERTScore F1 and 2.7544 G-Eval, ahead of the base model (0.8872 / 2.3787) and a RAG-augmented base model (0.8923 / 2.6329), and correctly attributed a source (matching either title or author) in 86.6% of responses.
- In a 32-participant user study with two hypothetical case scenarios (a bank robbery and a missing-person investigation), the fine-tuned model scored highest on "correctness" and "relevance" among the three configurations tested, while the RAG-only model was preferred for response verbosity/"improved understanding" and participants with more forensic experience rated all models' responses more harshly than novice participants.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Retrieval-augmented forensic LLM responses cite sources that do not match the retrieved context or propagate errors from it]]

## References

- [DFCite-1243] Sharma et al., 2025, "ForensicLLM: A local large language model for digital forensics", FSI: Digital Investigation 52, 301872.

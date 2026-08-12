---
id: DFT-1063
type: technique
name: Generate SQLite forensic queries using a fine-tuned text-to-SQL LLM
description: Assist a digital forensic investigator in querying heterogeneous, application-specific SQLite databases recovered from mobile devices by using a small, domain-fine-tuned large language model to translate a natural-language question and the target database's schema into an executable SQL query, avoiding the need for the investigator to have deep SQL and per-application schema expertise, and enabling fully local (non-cloud) inference for chain-of-custody and privacy reasons.
objective_ids:
  - DFO-1018
weakness_ids:
  - DFW-1068
aliases:
  - Fine-tuned LLM text-to-SQL query generation for SQLite forensic analysis
  - ForSQLiteLM
source_refs:
  - DFCite-1058
updated_at: 2026-08-10
status: complete
---

# Generate SQLite forensic queries using a fine-tuned text-to-SQL LLM

## Summary

Mobile applications frequently use SQLite for storage, but their schemas vary widely and formulating correct SQL to retrieve forensically relevant evidence requires expertise many investigators lack. A small (~3B parameter) LLM fine-tuned on a purpose-built forensic text-to-SQL dataset (ForSQLiteLM) can generate accurate, executable SQL queries against real forensic database schemas, running locally on commodity hardware so that evidence and schemas never need to be transmitted to a cloud API.

## Details

The base LLaMA 3.2 3B model was fine-tuned on a novel dataset of natural-language-question/SQL-query pairs built from real SQLite schemas extracted from forensic tools and controlled device acquisitions, spanning categories including messaging/social apps, Android artifacts, iOS CoreData-normalized schemas, and finance/crypto apps. Benchmarked by execution accuracy (does the generated query, when run, return the correct result) against the untuned base model (35%), CodeLLaMA 7B, and GPT-4o, the fine-tuned model reached 93% overall accuracy — statistically indistinguishable from GPT-4o's 95% (p ≈ 0.39) — despite being roughly 500x smaller, while offering offline, zero-marginal-cost, locally deployable inference that avoids transmitting forensic evidence or schemas to a third-party cloud service.

## Examples

- On a 100-query benchmark, the fine-tuned model achieved 100% execution accuracy on Messaging & Social (28/28) and Android artifact (18/18) query categories, and 92% on iOS CoreData-normalized schemas, matching or exceeding GPT-4o on the same categories.

## Related Objectives

- `DFO-1018` Read data from digital evidence storage formats

## Related Weaknesses

- [[weaknesses/LLM-generated forensic SQL queries can hallucinate schema columns or return wrong results while still executing successfully]]

## References

- [DFCite-1058] Pawlaszczyk et al., 2026, "AI-based automated SQL query generation for SQLite databases in Mobile forensics", FSI: Digital Investigation 57.

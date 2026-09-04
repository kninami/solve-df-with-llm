---
id: LWW-1068
type: weakness
name: LLM-generated forensic SQL queries can hallucinate schema columns or return wrong results while still executing successfully
description: Even a domain-fine-tuned LLM text-to-SQL model achieved only a 93% overall execution-accuracy on a forensic SQLite benchmark, with its residual failures including hallucinated column names not present in the real schema, queries that combine hallucinated columns with incorrect aggregation logic, and syntactically valid queries that execute without error but return the wrong result set, none of which are flagged as errors by the query's successful execution alone.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-1068
source_refs:
  - LWCite-1058
updated_at: 2026-08-10
status: complete
---

# LLM-generated forensic SQL queries can hallucinate schema columns or return wrong results while still executing successfully

## Summary

The paper's own failure analysis of the fine-tuned model's 7 residual errors (out of 100 benchmark queries) found cases where the model fabricated schema-absent columns (e.g. `duration_minutes`, `average_heart_rate` on a Fitbit schema) and returned raw rows instead of the required weekly aggregation, and a case where a syntactically correct, schema-valid query executed successfully but returned a five-column result set against a two-column reference answer — a "wrong result" failure that would not be caught by checking only whether the query runs without a database error.

## Why It Matters

An investigator who treats a generated query's successful execution as sufficient evidence of correctness may unknowingly rely on results built on a fabricated column (silently returning NULL or an execution error only sometimes) or on a result set that is subtly wrong (extra, missing, or misaggregated data) — errors most concentrated in deeply normalized, multi-table schemas (e.g. iOS CoreData) where the correct answer requires joining across several tables rather than reading one flat table.

## Related Mitigations

- [[mitigations/Independently verify LLM-generated forensic SQL query results against the evidence schema before relying on them]]

## Used By

- [[techniques/Generate SQLite forensic queries using a fine-tuned text-to-SQL LLM]]

## References

- [LWCite-1058] Pawlaszczyk et al., 2026, "AI-based automated SQL query generation for SQLite databases in Mobile forensics", FSI: Digital Investigation 57.

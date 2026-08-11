---
id: DFM-1068
type: mitigation
name: Independently verify LLM-generated forensic SQL query results against the evidence schema before relying on them
source_refs:
  - DFCite-1058
updated_at: 2026-08-10
status: complete
---

# Independently verify LLM-generated forensic SQL query results against the evidence schema before relying on them

## Summary

Treat an LLM-generated SQL query's successful execution as necessary but not sufficient evidence of correctness: independently verify that every referenced column exists in the actual evidence database schema and that the result set matches the investigative question, especially for deeply normalized, multi-table schemas.

## Addresses

- [[weaknesses/LLM-generated forensic SQL queries can hallucinate schema columns or return wrong results while still executing successfully]]

## How To Apply

Before relying on a generated query's output as evidence, cross-check the query's referenced tables and columns against the actual database schema (not just confirm the query executes), and manually spot-check a sample of the returned rows against the investigative question, with particular attention to queries against multi-table or deeply normalized schemas (e.g. iOS CoreData) where join- and aggregation-logic errors are most likely.

## References

- [DFCite-1058] Pawlaszczyk et al., 2026, "AI-based automated SQL query generation for SQLite databases in Mobile forensics", FSI: Digital Investigation 57.

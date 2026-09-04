---
id: LWM-2133
type: mitigation
name: Cross-validate a merged causal log graph for structural gaps and non-isomorphic anomalies before trusting it
source_refs:
  - LWCite-2154
updated_at: 2026-08-17
status: complete
---

# Cross-validate a merged causal log graph for structural gaps and non-isomorphic anomalies before trusting it

## Summary

Before relying on a merged causal event graph reconstructed from multiple applications' logs, check it structurally for the two signatures of tampering it can still expose: a broken predecessor chain (a referenced event missing from the log that should contain it) and a non-isomorphic graph shape where two branches that should mirror each other structurally do not, analogous to a double-entry bookkeeping imbalance between credit and debit records.

## Addresses

- [[weaknesses/A compromised application can fabricate or omit its own causal log claims undetected]]

## How To Apply

When merging per-application logs into the combined causal graph, flag every predecessor reference that does not resolve to an actual event in the referenced application's log as a gap requiring explanation, and compare the graph shape produced by repeated or similar operations for structural asymmetries that would indicate a fabricated or substituted causal link. Treat any single application's claimed causal predecessor as unverified until corroborated by the receiving or sending counterpart's own independently generated log, particularly for applications known or suspected to have been compromised in the incident under investigation.

## References

- [LWCite-2154] Olegård, Axelsson, and Li, 2025, "When is logging sufficient? — Tracking event causality for improved forensic analysis and correlation", FSI: Digital Investigation 52.

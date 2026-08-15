---
id: DFM-1294
type: mitigation
name: Supplement SSCA behavior-query detection with broader anomalous-behavior review for binaries outside the characterized attack set
source_refs:
  - DFCite-1325
updated_at: 2026-08-15
status: complete
---

# Supplement SSCA behavior-query detection with broader anomalous-behavior review for binaries outside the characterized attack set

## Summary

Do not treat a "no known SSCA behavior matched" result as proof a binary is uncompromised; supplement semantic-graph-query detection with general-purpose anomalous-behavior review (unexpected network calls, unusual privilege use, unexplained persistence mechanisms) that does not depend on a pre-characterized attack signature, and keep the query set updated as new SSCAs are documented.

## Addresses

- [[weaknesses/Software supply chain attack behavior detection depends on previously characterized queries and cannot detect a not-yet-catalogued attack behavior]]

## How To Apply

When using [[techniques/Detect software supply chain attack behaviors in binaries using semantic-graph queries and Bayesian malicious-intent scoring]] to screen a binary, disclose that a clean result reflects only the absence of the specific characterized behaviors in the current query set, not a general absence of compromise. For binaries from vendors or software ecosystems not represented among the attacks the query set was derived from, or in high-stakes investigations, supplement the query-based screen with broader dynamic or static anomaly analysis (unexpected network beaconing, unusual API import combinations, unexplained persistence mechanisms) that does not depend on matching a pre-characterized signature. Periodically update the query set as new SSCAs are publicly documented so the framework's coverage keeps pace with the evolving threat landscape.

## References

- [DFCite-1325] Andreoli, Lounis, Debbabi, and Hanna, 2023, "On the prevalence of software supply chain attacks: Empirical study and investigative framework", FSI: Digital Investigation 44, 301508.

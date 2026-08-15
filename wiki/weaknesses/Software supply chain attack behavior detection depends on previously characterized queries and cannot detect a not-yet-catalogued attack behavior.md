---
id: DFW-1293
type: weakness
name: Software supply chain attack behavior detection depends on previously characterized queries and cannot detect a not-yet-catalogued attack behavior
description: Because semantic-graph-query-based SSCA detection can only flag a binary for behaviors that have already been manually reverse-engineered and encoded as a query from prior known attacks, a supply chain attack using a genuinely novel technique with no characterized-behavior overlap will not be matched by any existing query and will pass through undetected by this method alone.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1294
source_refs:
  - DFCite-1325
updated_at: 2026-08-15
status: complete
---

# Software supply chain attack behavior detection depends on previously characterized queries and cannot detect a not-yet-catalogued attack behavior

## Summary

The investigative framework's query set was built by manually dissecting seven specific, already-discovered SSCAs. Its own temporal analysis found that the characteristic behaviors used by these attacks had existed in software for 13-21 years before being weaponized — implying the technique is fundamentally retrospective, detecting known-bad patterns after they have been characterized from a prior attack, rather than proactively identifying a genuinely new attack technique with no query-set overlap.

## Why It Matters

An investigator who relies on this detection framework as a complete SSCA screening solution risks missing a supply chain attack that uses a technique outside the seven characterized attacks' behavior set, since the framework has no mechanism for flagging behaviors it has not been given a query for. This is a general limitation of any signature- or pattern-based detection approach and should be disclosed alongside any negative ("no SSCA behavior detected") finding, particularly for binaries from vendors or ecosystems not represented in the seven attacks the query set was derived from.

## Related Mitigations

- [[mitigations/Supplement SSCA behavior-query detection with broader anomalous-behavior review for binaries outside the characterized attack set]]

## Used By

- [[techniques/Detect software supply chain attack behaviors in binaries using semantic-graph queries and Bayesian malicious-intent scoring]]

## References

- [DFCite-1325] Andreoli, Lounis, Debbabi, and Hanna, 2023, "On the prevalence of software supply chain attacks: Empirical study and investigative framework", FSI: Digital Investigation 44, 301508.

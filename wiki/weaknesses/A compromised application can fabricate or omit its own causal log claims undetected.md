---
id: LWW-2132
type: weakness
name: A compromised application can fabricate or omit its own causal log claims undetected
description: A cross-application causal event ID recorded by an application is only as trustworthy as that application, so an attacker who gains code execution in the application can tamper with, omit, or fabricate its own causal references before an investigator ever merges logs into the combined causal graph.
categories:
  - ASTM_INAC_ALT
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-2133
source_refs:
  - LWCite-2154
updated_at: 2026-08-17
status: complete
---

# A compromised application can fabricate or omit its own causal log claims undetected

## Summary

Because each application independently generates and records its own causal event identifiers, an attacker with remote code execution in one component can tamper with that component's own log (e.g., deleting the record of a received message) or fabricate a plausible-looking but false causal predecessor reference when sending an outbound message, without directly needing access to any other application in the system. A deleted local event does leave a detectable gap once logs are merged, but a fabricated predecessor reference for an event the attacker never actually received is harder to distinguish from a genuine one without independent corroboration.

## Why It Matters

An investigator merging per-application logs into a combined causal graph must treat every application's own claim about its causal predecessor as an assertion to be scrutinized, not as ground truth, since the same compromise that lets an attacker act maliciously on a system can also let them manipulate how that action is causally attributed in the resulting evidence. Presenting a merged causal graph as an authoritative reconstruction without accounting for this risks either following a fabricated causal trail away from the actual attacker, or drawing an unwarranted conclusion of tampering from an ordinary logging gap.

## Related Mitigations

- [[mitigations/Cross-validate a merged causal log graph for structural gaps and non-isomorphic anomalies before trusting it]]

## Used By

- [[techniques/Embed cross-application causal event IDs in logs for forensic readiness]]

## References

- [LWCite-2154] Olegård, Axelsson, and Li, 2025, "When is logging sufficient? — Tracking event causality for improved forensic analysis and correlation", FSI: Digital Investigation 52.

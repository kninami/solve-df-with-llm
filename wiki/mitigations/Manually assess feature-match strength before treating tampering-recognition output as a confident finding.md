---
id: DFM-1311
type: mitigation
name: Manually assess feature-match strength before treating tampering-recognition output as a confident finding
source_refs:
  - DFCite-1349
updated_at: 2026-08-15
status: complete
---

# Manually assess feature-match strength before treating tampering-recognition output as a confident finding

## Summary

Before reporting a tampering-recognition result as a confident finding, manually review how strongly each individual matched feature actually supports the tampering conclusion in the specific case, since the underlying algorithm does not itself distinguish strong from weak feature matches.

## Addresses

- [[weaknesses/Feature-based tampering recognition does not weight how strongly a feature indicates tampering versus non-tampering]]

## How To Apply

After applying [[techniques/Recognize artefact tampering using inductive reasoning over temporal-logic system-state features]] and obtaining a set of matched features indicating possible tampering, manually review the case-specific evidence supporting each matched feature and assess whether the match is strong (clear, unambiguous evidence) or weak (marginal or ambiguous evidence) before drawing conclusions. Report the tampering finding together with an explicit statement of feature-match strength and any weakly-supported features, rather than presenting the algorithm's binary match/no-match output alone as if all features contributed equally reliable evidence.

## References

- [DFCite-1349] Neale, Kennedy, and Nuseibeh, 2026, "Reasoning about artefact tampering", FSI: Digital Investigation 58, 302147.

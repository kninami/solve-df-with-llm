---
id: LWM-2009
type: mitigation
name: Cross-reference artifacts spanning multiple DBB phases in each relevant phase's chain of artifacts
source_refs:
  - LWCite-2009
updated_at: 2026-08-14
status: partial
---

# Cross-reference artifacts spanning multiple DBB phases in each relevant phase's chain of artifacts

## Summary

When an artifact discovered during data breach investigation is used by the attacker across more than one Data Breach Breakdown phase (e.g. a persistence mechanism created during propagation and later invoked during exfiltration), record and link it in the Chain of Artifacts for every phase it genuinely supports, rather than assigning it to only its first or most obvious phase.

## Addresses

- [[weaknesses/Forcing each data-breach artifact into a single DBB phase can misrepresent artifacts that span multiple attack phases]]

## How To Apply

During content analysis, before finalizing an artifact's DBB-phase assignment, explicitly check whether the artifact's timestamp, process relationships, or attack-flow role indicate reuse in a later phase, and add a correlation link (or duplicate cross-reference entry) into that phase's portion of the Chain of Artifacts so the attack-flow analysis captures the artifact's full role in the incident.

## References

- [LWCite-2009] Hakim et al., 2023 — the paper's own Chain of Artifacts design already supports correlation links between phases (via shared timestamps, IPs, and processes), which this mitigation extends to explicitly cover artifacts genuinely relevant to multiple DBB phases.

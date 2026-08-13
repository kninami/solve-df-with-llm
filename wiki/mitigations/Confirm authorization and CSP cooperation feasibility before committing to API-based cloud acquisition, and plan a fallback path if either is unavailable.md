---
id: DFM-1122
type: mitigation
name: Confirm authorization and CSP cooperation feasibility before committing to API-based cloud acquisition, and plan a fallback path if either is unavailable
source_refs:
  - DFCite-1116
updated_at: 2026-08-12
status: complete
---

# Confirm authorization and CSP cooperation feasibility before committing to API-based cloud acquisition, and plan a fallback path if either is unavailable

## Summary

Before planning an API-based multi-CSP acquisition and emulation workflow, confirm that either the target owner will cooperate in providing login access or that the CSP will cooperate with a lawful request, and identify an alternative acquisition path in advance for the scenario where neither holds.

## Addresses

- [[weaknesses/API-based cloud host acquisition depends on cooperative authorization from the target owner or CSP]]

## How To Apply

Early in case planning, determine which of the two cooperative scenarios applies (victim/target-owner-initiated request, or law-enforcement acquisition from a suspect who has disclosed access) and confirm the relevant CSP will honor API access requests in a reasonable timeframe. Where neither condition can be met — an uncooperative account holder, or a CSP that is unresponsive, outside legal jurisdiction, or itself implicated — do not rely on API-based acquisition; instead pursue credential-capture, memory-resident secret recovery, or legal-process routes such as [[techniques/Access a cloud account using captured credentials]] as an alternative or complementary acquisition path, and document the authorization basis relied upon for any evidence obtained via the API-based route.

## References

- [DFCite-1116] Wu et al., 2022, "Cloud Evidence Tracing System: An integrated forensics investigation system for large-scale public cloud platform", FSI: Digital Investigation 41.

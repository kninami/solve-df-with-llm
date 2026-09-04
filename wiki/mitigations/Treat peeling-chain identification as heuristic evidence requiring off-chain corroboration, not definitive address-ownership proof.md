---
id: LWM-1085
type: mitigation
name: Treat peeling-chain identification as heuristic evidence requiring off-chain corroboration, not definitive address-ownership proof
source_refs:
  - LWCite-1075
updated_at: 2026-08-10
status: complete
---

# Treat peeling-chain identification as heuristic evidence requiring off-chain corroboration, not definitive address-ownership proof

## Summary

Report self-change-address-based peeling chain identification results as strong heuristic indicators of likely mixer activity, not as certain proof of address ownership or entity attribution, and seek independent off-chain corroboration before relying on a peeling-chain finding as a standalone basis for attribution.

## Addresses

- [[weaknesses/Self-change-address peeling chain identification cannot certainly confirm true address ownership]]

## How To Apply

When presenting peeling-chain identification results (e.g. in an investigative report or as evidence), explicitly characterize them as heuristic-derived rather than verified from ground truth, and pursue independent corroboration where available (exchange KYC records obtained via legal process, known wallet clustering from other investigations, or admissions/other evidence) before treating the identified chain as proof of who controlled the addresses involved.

## References

- [LWCite-1075] Gong et al., 2023, "Analyzing the peeling chain patterns on the Bitcoin blockchain", FSI: Digital Investigation 46.

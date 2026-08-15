---
id: DFM-1284
type: mitigation
name: Cross-reference multiple independent frequency indicators and item-specific context before treating a marketplace trade pattern as suspicious
source_refs:
  - DFCite-1311
updated_at: 2026-08-15
status: complete
---

# Cross-reference multiple independent frequency indicators and item-specific context before treating a marketplace trade pattern as suspicious

## Summary

Require an account or item to appear as a statistical outlier across more than one independent frequency measure (frequent item, frequent seller, frequent buyer, duplicated trade) before escalating it for further investigation, and supplement the frequency data with independent context about the traded item (its function, typical acquisition method, and general market desirability) rather than relying on frequency in isolation.

## Addresses

- [[weaknesses/High-frequency marketplace trading alone cannot distinguish money laundering from legitimately popular high-volume items]]

## How To Apply

When applying [[techniques/Detect potential money laundering using frequency-based marketplace transaction indicators]], record which of the four frequency measures (frequent item, frequent seller, frequent buyer, duplicated trade) each outlier account or item satisfies, and prioritize review of accounts that recur across two or more measures over any single-measure outlier. Where feasible, obtain independent information about a flagged item's typical price, availability, and function within the platform's economy to rule out genuine popularity as the explanation before escalating the account for deeper investigation.

## References

- [DFCite-1311] Cooke and Marshall, 2024, "Money laundering through video games, a criminals' playground", FSI: Digital Investigation 50, 301802.

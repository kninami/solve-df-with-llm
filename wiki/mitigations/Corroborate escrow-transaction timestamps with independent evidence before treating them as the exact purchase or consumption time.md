---
id: DFM-1138
type: mitigation
name: Corroborate escrow-transaction timestamps with independent evidence before treating them as the exact purchase or consumption time
source_refs:
  - DFCite-1136
updated_at: 2026-08-12
status: complete
---

# Corroborate escrow-transaction timestamps with independent evidence before treating them as the exact purchase or consumption time

## Summary

Treat a cryptomarket escrow transaction's blockchain timestamp as the time funds were committed to escrow, not as a proven timestamp for the buyer's purchase decision, order placement, or product consumption, and seek independent corroboration before relying on it for case-specific timeline claims.

## Addresses

- [[weaknesses/Escrow-transaction timestamps can misrepresent the actual purchase or consumption time on a cryptomarket]]

## How To Apply

When timing evidence is used only to characterize aggregate marketplace-wide behavior (e.g. peak activity hours across thousands of transactions), the escrow-timestamp proxy is adequate on its own. When timing evidence is used to support a claim about a specific individual's actions, corroborate the escrow transaction's timestamp with independent evidence — postal/shipping records, communications between buyer and vendor, device-level browsing history, or other timestamped artifacts — before treating the on-chain escrow time as the actual moment of purchase, delivery, or consumption.

## References

- [DFCite-1136] Tsuchiya and Hiramoto, 2021, "Dark web in the dark: Investigating when transactions take place on cryptomarkets", FSI: Digital Investigation 36.

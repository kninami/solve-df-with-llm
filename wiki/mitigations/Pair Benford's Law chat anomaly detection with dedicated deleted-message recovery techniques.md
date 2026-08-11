---
id: DFM-1097
type: mitigation
name: Pair Benford's Law chat anomaly detection with dedicated deleted-message recovery techniques
source_refs:
  - DFCite-1090
updated_at: 2026-08-10
status: complete
---

# Pair Benford's Law chat anomaly detection with dedicated deleted-message recovery techniques

## Summary

Do not treat a Benford's-Law-conforming leading-digit distribution as evidence that a chat conversation is complete and unaltered; separately apply dedicated deleted-record recovery techniques (e.g. app-specific SQLite deleted-record recovery) to check for message deletion, since the two questions (statistical anomaly vs. deletion) are independent.

## Addresses

- [[weaknesses/Benford's Law chat anomaly detection cannot detect deleted chat records]]

## How To Apply

When a chat's authenticity or completeness is at issue, run Benford's-Law-based anomaly triage alongside (not instead of) an app-appropriate deleted-record recovery technique against the underlying message-store database, and report the two results separately rather than treating a clean Benford result as covering the deletion question.

## References

- [DFCite-1090] Mahindra and Karabiyik, 2026, "Benford's Law as a Forensic Tool for Identifying Anomalous Chat Behavior in Instant Messaging", IEEE SmartNets 2026.

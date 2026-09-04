---
id: LWM-2052
type: mitigation
name: Vet participant honesty and add protocol-level safeguards before relying on combined private indexing across multiple parties
source_refs:
  - LWCite-2053
updated_at: 2026-08-14
status: partial
---

# Vet participant honesty and add protocol-level safeguards before relying on combined private indexing across multiple parties

## Summary

Before relying on combined Soundex/CLK private indexing to link investigative records across multiple organizations, vet and formally agree the trust assumptions with every participating party, and layer in additional protective safeguards (audit logging, cryptographic commitments, or a trusted coordinating authority) beyond the base protocol's semi-honest assumption.

## Addresses

- [[weaknesses/Combined private indexing assumes all participating parties are genuine, risking privacy compromise by a dishonest party]]

## How To Apply

Establish formal data-sharing agreements and legal accountability for every organization participating in a private-indexing-based record-linkage exercise, since the technical protocol alone cannot guarantee good-faith behavior. Where the stakes justify it, add protocol-level safeguards such as commitment schemes, audit trails of query and result exchanges, or routing the linkage process through a mutually trusted coordinating third party, rather than relying on the base indexing protocol's privacy guarantees alone in a genuinely adversarial multi-party setting.

## References

- [LWCite-2053] Desai and Shelake, 2022 — the paper's own future-work discussion identifies the need for "more protective safety measures and communication" to address this exact limitation, motivating additional protocol-level or organizational safeguards.

---
id: LWM-1249
type: mitigation
name: Timestamp digital evidence immediately upon acquisition and disclose the limits of a Horodocs-style timestamp
source_refs:
  - LWCite-1263
updated_at: 2026-08-13
status: complete
---

# Timestamp digital evidence immediately upon acquisition and disclose the limits of a Horodocs-style timestamp

## Summary

Submit a digital evidence item's hash values to a blockchain-anchored timestamping system as early as possible after acquisition, to minimize the unprotected window before submission, and clearly document to any downstream verifier (a judge, prosecutor, or defense) exactly what the resulting timestamp does and does not prove.

## Addresses

- [[weaknesses/Horodocs timestamp verification provides no integrity guarantee for file modifications occurring before submission]]

## How To Apply

Build hash-submission into the evidence-acquisition workflow itself, rather than as a later administrative step, so the gap between acquisition and timestamping is minimized. When presenting a valid timestamp verification as part of a case, explicitly state that it establishes integrity only from the recorded submission time forward, and separately document (through standard chain-of-custody procedures) how the evidence's authenticity and integrity were established for the period before submission.

## References

- [LWCite-1263] Jaquet-Chiffelle, Pfeiffer, Brocard, Benoist, and Foukia, 2025, "Horodocs: A scalable, sustainable, robust and privacy compliant system to securely timestamp digital evidence and documents", FSI: Digital Investigation 53, 301913.

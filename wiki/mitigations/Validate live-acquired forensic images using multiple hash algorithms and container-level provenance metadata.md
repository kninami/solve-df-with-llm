---
id: LWM-2075
type: mitigation
name: Validate live-acquired forensic images using multiple hash algorithms and container-level provenance metadata
source_refs:
  - LWCite-2080
updated_at: 2026-08-16
status: complete
---

# Validate live-acquired forensic images using multiple hash algorithms and container-level provenance metadata

## Summary

When acquisition software must run on a live target system, add a dedicated validation stage that independently re-checks the acquired data's integrity — using multiple hash algorithms computed at acquisition time and re-verified afterward, plus artifact/metadata-consistency checks — rather than trusting the acquisition step's own output as sufficient.

## Addresses

- [[weaknesses/Autonomous system processes and forensic tool vulnerabilities inadvertently alter or destroy evidence during acquisition or examination]]

## How To Apply

Compute more than one hash (e.g. MD5, SHA1, and a collision-resistant algorithm such as SHA256) for each acquired artifact immediately upon acquisition, store them alongside the artifact's other metadata inside a self-describing container format (e.g. AFF4) rather than a bare file copy, and re-verify all hash values in a separate validation pass before the acquisition is considered complete. Treat any hash mismatch, or any artifact missing expected metadata, as a possible sign of interference or corruption during the live acquisition, and document the discrepancy rather than silently discarding it. Keep a backup archive of acquired artifacts as a further redundancy in case the primary output is later found to be corrupted.

## References

- [LWCite-2080] Faust, Thierry, Müller, and Freiling, 2021, "Selective Imaging of File System Data on Live Systems", FSI: Digital Investigation 36, 301115.

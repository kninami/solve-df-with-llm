---
id: DFW-1248
type: weakness
name: Horodocs timestamp verification provides no integrity guarantee for file modifications occurring before submission
description: A valid Horodocs timestamp only proves that a specific hash value existed at or before the recorded time and has not changed since; it says nothing about whether the underlying file was already altered, backdated in content, or fabricated before it was ever submitted for timestamping, a limitation a verifier could easily misread as a stronger guarantee than the system actually provides.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1249
source_refs:
  - DFCite-1263
updated_at: 2026-08-13
status: complete
---

# Horodocs timestamp verification provides no integrity guarantee for file modifications occurring before submission

## Summary

Horodocs is designed to make backdating infeasible from the moment of submission forward — an attacker cannot later claim an earlier timestamp than the one actually recorded, nor alter the file without the hash mismatch being detectable. However, the system has no visibility into, and makes no claim about, the state or history of a file before its hash values were first submitted; if the file was already tampered with, fabricated, or captured at a later point than the incident it purports to document, a Horodocs timestamp will not reveal this.

## Why It Matters

A judge, prosecutor, or defense counsel unfamiliar with exactly what a timestamping receipt does and does not prove risks treating a valid Horodocs verification as evidence that a piece of digital evidence is authentic and untampered throughout its entire history, when it in fact only establishes integrity from the submission time onward. This gap is most consequential when there is a meaningful delay between an evidence item's creation or seizure and the point at which an investigator actually submits its hash values to the timestamping system, since that entire window remains unprotected.

## Related Mitigations

- [[mitigations/Timestamp digital evidence immediately upon acquisition and disclose the limits of a Horodocs-style timestamp]]

## Used By

- [[techniques/Timestamp digital evidence hashes using a privacy-preserving blockchain-anchored Merkle tree]]

## References

- [DFCite-1263] Jaquet-Chiffelle, Pfeiffer, Brocard, Benoist, and Foukia, 2025, "Horodocs: A scalable, sustainable, robust and privacy compliant system to securely timestamp digital evidence and documents", FSI: Digital Investigation 53, 301913.

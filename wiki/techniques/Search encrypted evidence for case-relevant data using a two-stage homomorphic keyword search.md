---
id: DFT-2018
type: technique
name: Search encrypted evidence for case-relevant data using a two-stage homomorphic keyword search
description: The process of narrowing a large volume of seized digital evidence down to case-pertinent data while limiting exposure of irrelevant private third-party information, by encrypting the acquired dataset with a public key, running a broad disjunctive first-keyword search over the ciphertext, then a narrower conjunctive second-keyword search over the encrypted results, and only decrypting the final analysis output.
objective_ids:
  - DFO-1007
weakness_ids:
  - DFW-2018
aliases:
  - Privacy-Preserving Digital Forensics (PPDF) model
  - Homomorphic-encryption-based keyword search for digital forensics
source_refs:
  - DFCite-2018
updated_at: 2026-08-14
status: partial
---

# Search encrypted evidence for case-relevant data using a two-stage homomorphic keyword search

## Summary

Because a full-scale extraction of a device's contents inevitably captures private information belonging to suspects, victims, third parties, and secondary users that may be entirely irrelevant to the investigation, an investigator can instead encrypt acquired data with a public key immediately after collection, run keyword searches directly over the ciphertext using homomorphic encryption's compute-without-decrypting property, and only decrypt the small, case-pertinent result set that survives two successive filtering passes - never the full original dataset.

## Details

DFCite-2018's four-stage PPDF model works as follows: (1) Preparation/Key Generation - an asymmetric key pair is generated, either by a cooperating user (to give them some control over their own data's privacy) or by the investigating law enforcement agent, with the public key shared with the service provider and/or investigator and the private key held in a secured storage system; (2) Preservation/Encryption - acquired data is encrypted, and a first, deliberately broad set of case-related keywords (a disjunctive search, i.e. matching any of several keywords) is run to maximize independent, non-interrelated data retrieval, with the results encrypted using the shared public key; (3) Extraction/Computation - a second, narrower set of case-relevant keywords (a conjunctive search, i.e. requiring multiple keyword matches together) is run directly on the still-encrypted case-related data to compute case-pertinent evidence (supporting pattern-recognition analyses like metadata, network-traffic, file-structure, and correlation analysis, all performed on ciphertext) without decrypting the intervening dataset; (4) Presentation/Decryption - only the final analyzed, case-relevant result is decrypted with the private key for the investigator's review and hypothesis validation. Of the five cryptographic technique families surveyed (homomorphic encryption, commutative encryption, secret sharing, searchable encryption, identity-based encryption), only homomorphic and searchable encryption directly support the model's requirement of computing on already-encrypted data without a trusted third party.

## Examples

- DFCite-2018's worked scenario: a smartphone seized in an online-fraud case is imaged, first-keyword-searched (text messages, emails, call logs, browsing history) and encrypted, then second-keyword-searched (fraud-specific terms) on the encrypted first-pass results to extract encrypted case-pertinent data for pattern/metadata/network-traffic analysis, decrypted only at the final presentation stage.

## Related Objectives

- `DFO-1007` Reduce data under consideration

## Related Weaknesses

- [[weaknesses/Homomorphic keyword search lacks a way to verify submitted keywords are actually case-relevant]]

## References

- [DFCite-2018] Ogunseyi and Adedayo, "Cryptographic techniques for data privacy in digital forensics", IEEE Access, 2023 — source of the PPDF conceptual model, its four-stage process, and its cryptographic-technique comparison summarized above.

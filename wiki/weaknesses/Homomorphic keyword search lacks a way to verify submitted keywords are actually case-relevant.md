---
id: LWW-2018
type: weakness
name: Homomorphic keyword search lacks a way to verify submitted keywords are actually case-relevant
description: Privacy-preserving keyword-search models for encrypted digital forensic data generally have no built-in mechanism to confirm that an investigator's submitted keywords are genuinely tied to the case, so overly broad or poorly chosen keywords (especially in the deliberately wide first-pass disjunctive search) can still cause substantial irrelevant private data to be retrieved and eventually processed or exposed.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-2018
source_refs:
  - LWCite-2018
updated_at: 2026-08-14
status: partial
---

# Homomorphic keyword search lacks a way to verify submitted keywords are actually case-relevant

## Summary

The source paper's own "Drawbacks of Deploying Cryptographic Techniques" discussion identifies as a key limitation that "some of the cryptography-based schemes lack a verification method to ascertain whether the keyword searches are case-relevant or not," and separately notes that "the resulting size of ciphertext from encrypted evidential information is too large" when broad, unverified keyword sets are used. Because the model's first-stage keyword search is deliberately disjunctive (matching any of several broad keywords, to maximize data retrieval), an investigator who selects poorly targeted or overly broad first-pass keywords can pull a large volume of non-relevant, private third-party data into the encrypted working set, even though the encryption itself still protects it from being read in plaintext until decryption.

## Why It Matters

Even though the encryption layer prevents casual exposure, the underlying privacy-protection goal - limiting how much non-relevant private data about suspects, victims, or third parties is captured and processed at all during an investigation - is undermined if keyword selection is not itself scrutinized for case relevance, since a broad, unverified keyword set determines how much data enters the pipeline for later computation and eventual decryption of matched results.

## Related Mitigations

- [[mitigations/Require collaborative case-relevance verification of search keywords before running privacy-preserving keyword searches]]

## Used By

- [[techniques/Search encrypted evidence for case-relevant data using a two-stage homomorphic keyword search]]

## References

- [LWCite-2018] Ogunseyi and Adedayo, 2023 — Section III.F explicitly lists the lack of a keyword case-relevance verification method as a drawback of existing cryptography-based privacy-preserving digital forensics schemes.

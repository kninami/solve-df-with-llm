---
id: DFW-1105
type: weakness
name: Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification
description: Common similarity digest (fuzzy hashing / approximate matching) algorithms — including ssdeep, sdhash, TLSH, SimHash, LZJD, and mvHash-B — are each vulnerable to at least one of two general attack classes given an adversary who understands the algorithm's internal design: reducing the similarity score between two inputs that should match (evading blacklist-style detection), or emulating a high similarity score between two inputs that should not match (spoofing an allowlist or planting false corroboration), each achievable with a small, bounded number of modified bytes.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-1105
source_refs:
  - DFCite-1100
  - DFCite-2013
  - DFCite-2037
updated_at: 2026-08-14
status: complete
---

# Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification

## Summary

The study demonstrates concrete, low-cost attacks against specific widely-used algorithms: for ssdeep, an adversary who knows which features will be extracted needs to modify only about 9 bytes to drop the similarity score to zero (since ssdeep's minimum-commonality comparison requirement is no fewer than 7 consecutive common features out of a maximum 64). For algorithms using a hash function as their mapping function, changing roughly 1 bit in each (or the majority) of the extracted features suffices, due to the avalanche effect of cryptographic hashing. Conversely, sdhash tolerates up to 20% of an input's content being modified without changing its generated digest at all — a robustness property that can be turned into an emulation attack, letting an adversary insert or alter content within that budget without disturbing a target similarity match. SimHash and LZJD have their own analogous emulation weaknesses tied to how they select and process input features.

## Why It Matters

An investigator relying on a similarity digest match (or non-match) as evidence — for example, that a file is/is not related to a known blacklisted or allow-listed artifact, or that a blockchain-recorded evidence block's fuzzy hash still matches its original (per DFCite-2013's SSDEEP-based Merkle-tree tamper check) — is relying on a comparison that a knowledgeable adversary can manipulate in either direction with a small, often practical number of byte-level changes, without needing to break any cryptographic primitive. Because the specific vulnerability depends on the target algorithm's internal design (feature length, mapping function, storing structure, coverage), the same investigator's confidence in a match should vary by which specific similarity digest algorithm produced it. In particular, an SSDEEP-based evidence-integrity check that treats similarity at or above a fixed threshold (e.g. 90%) as proof of authenticity is exposed to ssdeep's known emulation-attack surface, where an adversary could in principle craft a tampered evidence block that still scores above the threshold.

## Related Mitigations

- [[mitigations/Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface]]

## Used By

- [[techniques/Similarity-based Android malware family detection]]
- [[techniques/Blockchain-anchored digital evidence integrity and chain-of-custody management]]

## References

- [DFCite-1100] Martín-Pérez et al., 2021, "Bringing order to approximate matching: Classification and attacks on similarity digest algorithms", FSI: Digital Investigation 36.
- [DFCite-2013] Mahrous et al., 2021, "An enhanced blockchain-based IoT digital forensics architecture using fuzzy hash", IEEE Access 9 — uses SSDEEP similarity above a fixed threshold as its blockchain evidence-block tamper check, which is exposed to this same attack surface.
- [DFCite-2037] Elgohary et al., 2022, "Improving uncertainty in chain of custody for image forensics investigation applications", IEEE Access 10 — its own "Security Analysis" section independently confirms this same attack surface for MRSH-v2-style fuzzy hashing, describing how an active adversary can defeat blacklist/whitelist fuzzy-hash matching by manipulating as little as one bit per hash-triggering building block.

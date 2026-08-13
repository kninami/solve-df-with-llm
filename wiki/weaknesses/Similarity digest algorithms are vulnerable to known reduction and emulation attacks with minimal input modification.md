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
  - DFCite-1249
updated_at: 2026-08-13
status: complete
---

# Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification

## Summary

The study demonstrates concrete, low-cost attacks against specific widely-used algorithms: for ssdeep, an adversary who knows which features will be extracted needs to modify only about 9 bytes to drop the similarity score to zero (since ssdeep's minimum-commonality comparison requirement is no fewer than 7 consecutive common features out of a maximum 64). For algorithms using a hash function as their mapping function, changing roughly 1 bit in each (or the majority) of the extracted features suffices, due to the avalanche effect of cryptographic hashing. Conversely, sdhash tolerates up to 20% of an input's content being modified without changing its generated digest at all — a robustness property that can be turned into an emulation attack, letting an adversary insert or alter content within that budget without disturbing a target similarity match. SimHash and LZJD have their own analogous emulation weaknesses tied to how they select and process input features.

A related but distinct attack surface, empirically measured by [[techniques/Benchmark approximate matching algorithms using an automated test framework]] (FRASHER), is **digest generation impediment**: crafting input that an algorithm cannot hash at all, letting it slip past any filter built on that algorithm entirely. sdhash requires a minimum input size of 512 bytes and at least 8 unique characters within any 750-byte window before it can reliably hash and match; MRSH-v2 requires at least 2900 bytes with more than 3 unique characters. Any file an adversary crafts below these size/diversity thresholds is invisible to a filter built on either algorithm. TLSH (minimum 50 bytes, 2 unique characters) and FbHash (a variance of at least 3 characters) have looser but still exploitable minimums; ssdeep and mrsh-cf could hash and match starting from the smallest tested input size of 10 bytes. A second, related surface is **digest comparison impediment**: repeatedly duplicating a file's content (rather than genuinely modifying it) lowered the similarity score reported by ssdeep, TLSH, and mrsh-cf — ssdeep's score reached 0 after four concatenated copies of the same 5 KB block — while MRSH-v2, sdhash, and FbHash correctly continued to report near-100% similarity regardless of duplication factor.

## Why It Matters

An investigator relying on a similarity digest match (or non-match) as evidence — for example, that a file is/is not related to a known blacklisted or allow-listed artifact — is relying on a comparison that a knowledgeable adversary can manipulate in either direction with a small, often practical number of byte-level changes, without needing to break any cryptographic primitive. Because the specific vulnerability depends on the target algorithm's internal design (feature length, mapping function, storing structure, coverage), the same investigator's confidence in a match should vary by which specific similarity digest algorithm produced it.

## Related Mitigations

- [[mitigations/Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface]]

## Used By

- [[techniques/Detect Android malware families using similarity scoring]]
- [[techniques/Benchmark approximate matching algorithms using an automated test framework]]

## References

- [DFCite-1100] Martín-Pérez et al., 2021, "Bringing order to approximate matching: Classification and attacks on similarity digest algorithms", FSI: Digital Investigation 36.
- [DFCite-1249] Göbel et al., 2022, "FRASHER -- A framework for automated evaluation of similarity hashing", FSI: Digital Investigation 42, 301407.

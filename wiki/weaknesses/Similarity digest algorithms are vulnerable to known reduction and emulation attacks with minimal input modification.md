---
id: LWW-1105
type: weakness
name: Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification
description: Common similarity digest (fuzzy hashing / approximate matching) algorithms — including ssdeep, sdhash, TLSH, SimHash, LZJD, and mvHash-B — are each vulnerable to at least one of two general attack classes given an adversary who understands the algorithm's internal design: reducing the similarity score between two inputs that should match (evading blacklist-style detection), or emulating a high similarity score between two inputs that should not match (spoofing an allowlist or planting false corroboration), each achievable with a small, bounded number of modified bytes.
categories:
  - ASTM_INAC_EX
  - ASTM_INAC_COR
mitigation_ids:
  - LWM-1105
source_refs:
  - LWCite-1100
  - LWCite-1249
  - LWCite-2013
  - LWCite-2037
  - LWCite-2092
  - LWCite-2131
updated_at: 2026-08-16
status: complete
---

# Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification

## Summary

The study demonstrates concrete, low-cost attacks against specific widely-used algorithms: for ssdeep, an adversary who knows which features will be extracted needs to modify only about 9 bytes to drop the similarity score to zero (since ssdeep's minimum-commonality comparison requirement is no fewer than 7 consecutive common features out of a maximum 64). For algorithms using a hash function as their mapping function, changing roughly 1 bit in each (or the majority) of the extracted features suffices, due to the avalanche effect of cryptographic hashing. Conversely, sdhash tolerates up to 20% of an input's content being modified without changing its generated digest at all — a robustness property that can be turned into an emulation attack, letting an adversary insert or alter content within that budget without disturbing a target similarity match. SimHash and LZJD have their own analogous emulation weaknesses tied to how they select and process input features.

A related but distinct attack surface, empirically measured by [[techniques/Benchmark approximate matching algorithms using an automated test framework]] (FRASHER), is **digest generation impediment**: crafting input that an algorithm cannot hash at all, letting it slip past any filter built on that algorithm entirely. sdhash requires a minimum input size of 512 bytes and at least 8 unique characters within any 750-byte window before it can reliably hash and match; MRSH-v2 requires at least 2900 bytes with more than 3 unique characters. Any file an adversary crafts below these size/diversity thresholds is invisible to a filter built on either algorithm. TLSH (minimum 50 bytes, 2 unique characters) and FbHash (a variance of at least 3 characters) have looser but still exploitable minimums; ssdeep and mrsh-cf could hash and match starting from the smallest tested input size of 10 bytes. A second, related surface is **digest comparison impediment**: repeatedly duplicating a file's content (rather than genuinely modifying it) lowered the similarity score reported by ssdeep, TLSH, and mrsh-cf — ssdeep's score reached 0 after four concatenated copies of the same 5 KB block — while MRSH-v2, sdhash, and FbHash correctly continued to report near-100% similarity regardless of duplication factor.

Beyond deliberate adversarial attacks, ssdeep's own reference implementation carries independent, non-adversarial reliability defects that further erode confidence in its similarity output. A "last segment bug" causes the final segment of an input file to be silently dropped from the similarity hash whenever the last byte happens to trigger a new segment boundary, discarding information about the file's ending without any indication to the user that this occurred. Separately, ssdeep's second (larger block-size) signature is truncated to a hard 32-character limit inherited from a legacy 64-character total-signature-length constraint, discarding otherwise-computable hash information for larger inputs purely to preserve a compact representation. An evaluation study documenting these and related inconsistencies found the two corresponding fixes (removing the last-segment bug, removing the 32-character limit) measurably increased runtime throughput (~14% for the second-signature fix) without changing the algorithm's core design, and further found ssdeep's similarity score degrades toward zero after only four concatenated copies of an unmodified 5 KB block -- a "digest comparison impediment" distinct from either the adversarial attacks or the implementation bugs above, where alternative algorithms (MRSH-v2, sdhash, FbHash) correctly continued reporting near-100% similarity regardless of duplication factor.

A related, non-adversarial reliability concern is threshold sensitivity: using similarity hashing to increase AV malware-detection coverage or to cluster samples into malware families produces materially different conclusions depending purely on the similarity threshold chosen, with no standard, universally appropriate threshold value established in the literature. A threshold requiring 100% compatibility is the most conservative but still increases coverage measurably; progressively lower thresholds increase coverage further but correspondingly raise the risk of false positives, and different individual tools/AV engines respond to threshold changes to very different degrees. Separately, malware packing (even with a single common open-source packer, UPX) significantly reduces the similarity score between a packed sample and its own unpacked original, though it does not eliminate the ability to cluster same-packer variants together via the commonality the packer itself introduces.

## Why It Matters

An investigator relying on a similarity digest match (or non-match) as evidence — for example, that a file is/is not related to a known blacklisted or allow-listed artifact, or that a blockchain-recorded evidence block's fuzzy hash still matches its original (per LWCite-2013's SSDEEP-based Merkle-tree tamper check) — is relying on a comparison that a knowledgeable adversary can manipulate in either direction with a small, often practical number of byte-level changes, without needing to break any cryptographic primitive. Because the specific vulnerability depends on the target algorithm's internal design (feature length, mapping function, storing structure, coverage), the same investigator's confidence in a match should vary by which specific similarity digest algorithm produced it. In particular, an SSDEEP-based evidence-integrity check that treats similarity at or above a fixed threshold (e.g. 90%) as proof of authenticity is exposed to ssdeep's known emulation-attack surface, where an adversary could in principle craft a tampered evidence block that still scores above the threshold.

## Related Mitigations

- [[mitigations/Select and configure similarity digest algorithms with awareness of their known reduction and emulation attack surface]]

## Used By

- [[techniques/Detect Android malware families using similarity scoring]]
- [[techniques/Benchmark approximate matching algorithms using an automated test framework]]
- [[techniques/Anchor digital evidence integrity and chain of custody on a blockchain]]
- [[techniques/Increase antivirus malware detection coverage by clustering samples using similarity hashing]]

## References

- [LWCite-1100] Martín-Pérez et al., 2021, "Bringing order to approximate matching: Classification and attacks on similarity digest algorithms", FSI: Digital Investigation 36.
- [LWCite-1249] Göbel et al., 2022, "FRASHER -- A framework for automated evaluation of similarity hashing", FSI: Digital Investigation 42, 301407.
- [LWCite-2013] Mahrous et al., 2021, "An enhanced blockchain-based IoT digital forensics architecture using fuzzy hash", IEEE Access 9 — uses SSDEEP similarity above a fixed threshold as its blockchain evidence-block tamper check, which is exposed to this same attack surface.
- [LWCite-2037] Elgohary et al., 2022, "Improving uncertainty in chain of custody for image forensics investigation applications", IEEE Access 10 — its own "Security Analysis" section independently confirms this same attack surface for MRSH-v2-style fuzzy hashing, describing how an active adversary can defeat blacklist/whitelist fuzzy-hash matching by manipulating as little as one bit per hash-triggering building block.
- [LWCite-2092] Jakobs, Lambertz, and Hilgert, 2022, "ssdeeper: Evaluating and improving ssdeep", FSI: Digital Investigation 42, 301402. Documents non-adversarial ssdeep implementation defects (the last-segment bug, the 32-character second-signature limitation) and the digest-comparison-impediment effect of file duplication, independent of the deliberate adversarial attacks above.
- [LWCite-2131] Botacin, Galhardo Moia, and Ceschin, 2021, "Understanding uses and misuses of similarity hashing functions for malware detection and family clustering in actual scenarios", FSI: Digital Investigation 38, 301220. Documents similarity-threshold-selection sensitivity and malware-packing's effect on similarity-hashing-based clustering, both non-adversarial reliability concerns independent of the deliberate attacks above.

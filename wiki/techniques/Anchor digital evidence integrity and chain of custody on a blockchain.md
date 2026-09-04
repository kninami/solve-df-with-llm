---
id: LWT-1042
type: technique
name: Anchor digital evidence integrity and chain of custody on a blockchain
description: Record digital evidence integrity information — a per-frame fingerprint at capture time, an evidence hash at collection time, or a custody-transfer event — as an immutable blockchain transaction, so that later tampering with the evidence itself, or a break in its chain of custody, can be detected by comparing the evidence against its blockchain record rather than relying solely on a centralized, alterable log.
objective_ids:
  - DFO-1010
weakness_ids:
  - LWW-1043
  - LWW-1060
  - LWW-1062
  - LWW-1105
aliases:
  - Blockchain-anchored digital evidence integrity and chain-of-custody management
  - Fuzzy hash-based blockchain of IoT evidence management
  - DFA-AOKGE (cloud evidence storage architecture)
  - MRSH-v2 fuzzy hash Hyperledger chain of custody
source_refs:
  - LWCite-1033
  - LWCite-1050
  - LWCite-1052
  - LWCite-2013
  - LWCite-2036
  - LWCite-2037
updated_at: 2026-08-14
status: complete
---

# Anchor digital evidence integrity and chain of custody on a blockchain

## Summary

A centralized evidence-management log is a single point of failure for both availability and trust: if it is compromised or altered, there may be no independent way to detect it. Recording evidence integrity information on a blockchain — whether a per-frame capture-time fingerprint (for video) or an evidence hash and custody-transfer event (for general digital evidence, common in reviewed IoT forensic frameworks) — provides a decentralized, tamper-evident record that does not depend on trusting a single custodian's log.

## Details

**Capture-time fingerprinting** (video-specific instance): on the capture device itself, a lightweight per-frame fingerprint (e.g., a DCT DC-coefficient sequence) is computed and submitted in real time to a permissioned blockchain, chained via cryptographic hashes to the previous block; later identification and tamper verification correlate a clip's recomputed fingerprint against the stored blockchain record, without needing the original file for comparison. **Chain-of-custody transaction logging** (general IoT/digital evidence instance): each time evidence is collected, transferred between custodians, or accessed, that event (along with an evidence hash) is recorded as a blockchain transaction, using a private/consortium/permissioned blockchain (evaluated in IoT forensic frameworks such as B-CoC and Block-DEF) to provide decentralized storage, authenticity, transparency, and non-repudiation of the custody record. Reviewed frameworks vary in which architecture layer they anchor to blockchain (device, network, or cloud level) and in whether they store the evidence itself off-chain (more common, for storage-cost reasons) versus only its hash and metadata on-chain. A second systematic literature review of 16 primary studies (LWCite-1052) categorized these frameworks as public (untainted, transparent, but weaker privacy/scalability — e.g. custom distributed ledgers, Ethereum) versus permissioned (identity-known, more scalable, and the majority choice), and found chain-of-custody support (32%) and data integrity (29%) to be the most common themes addressed, ahead of data provenance (24%) and privacy/identity anonymity (15%).

**Fuzzy-hash Merkle tree validation** (a third variant): rather than encoding the Merkle tree with a conventional cryptographic hash alone (which flags any single-bit input change as a completely different, unrelated output), one reviewed IoT architecture (LWCite-2013) also encodes the Merkle root using an SSDEEP fuzzy hash (context-triggered piecewise hashing) after conventional SHA256 fingerprinting of each evidence record. An investigator validating a block computes its fuzzy hash similarity against other nodes' copies via SSDEEP; a similarity score at or above a set threshold (90-95% in the reviewed implementation) is treated as confirming the block is unaltered "original evidence," which lets the scheme tolerate small, permissible/benign IoT-sensor-driven variation between near-identical evidence versions (e.g. minor differences from IoT device jitter) without requiring byte-exact matches, while still flagging blocks below the threshold as potentially tampered.

**Encrypted cloud evidence storage with authenticated peer distribution** (a fourth variant): rather than anchoring only a hash/custody-transaction on-chain, LWCite-2036's DFA-AOKGE architecture uses SDN and blockchain together to distribute cloud (IaaS) evidence across multiple storage peers, gates evidence access behind a circle-equation-based two-factor Secure Block Verification Mechanism, generates cryptographic keys via a metaheuristic (Enhanced Equilibrium Optimizer) search rather than a fixed algorithm, and encrypts stored evidence with multikey homomorphic encryption so authorized parties can jointly compute over it without full decryption.

**MRSH-v2 fuzzy-hash Hyperledger chain of custody** (a fifth variant): LWCite-2037 stores each image evidence block's validity in a permissioned Hyperledger Fabric/Composer blockchain using MRSH-v2 (a Bloom-filter-based Multi-Resolution Similarity Hashing fuzzy hash) instead of SHA-256, with blocks compared via a >95% similarity threshold rather than exact-match comparison, so that permissible/benign alteration between two versions of the same evidence image (e.g. re-compression, minor edits by the examining lab) is tolerated without breaking the custody chain's integrity guarantee, while still flagging genuinely different images as non-matching.

## Examples

- Tested against the VIRAT CCTV dataset (8800 enrolled blocks), object removal was detected as a clear, localized dip in frame correlation exactly at the tampered blocks in all tested samples, and object insertion was detected via a correlation drop below 0.99 combined with object-detection (YOLO) confirmation in three of four test clips.
- Block-DEF: a blockchain-based IoT forensic framework separating block-header storage (distributed across nodes) from evidence-content storage (a trusted off-chain platform) to reduce storage pressure while still providing tamper-resistant custody tracking via multi-signature evidence submission.
- LWCite-2013's fuzzy-hash Merkle tree architecture: simulated on both a laptop and a Raspberry Pi 3B (512MB RAM, 700MHz) IoT node, reducing block response time by an average of 2% versus a conventional-hash-only Merkle tree while remaining feasible for low-power/low-memory IoT devices (13s/12mW average per new block on the Raspberry Pi vs. 3s/4mW on a laptop).

## Related Objectives

- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/Static or low-movement surveillance footage produces colliding on-camera DCT fingerprints]]
- [[weaknesses/Blockchain-based IoT evidence management frameworks largely neglect legal and management readiness]]
- [[weaknesses/Blockchain-based IoT forensic frameworks lack rigorous security testing and standardized performance benchmarking]]
- [[weaknesses/Similarity digest algorithms are vulnerable to known reduction and emulation attacks with minimal input modification]]

## References

- [LWCite-1033] Kerr et al., 2023, "A non-invasive method for the cataloguing and authentication of surveillance video using on-camera blockchain participation, machine learning and signal analysis", FSI: Digital Investigation 46.
- [LWCite-1050] Khanji et al., 2022, "A systematic analysis on the readiness of Blockchain integration in IoT forensics", FSI: Digital Investigation 42-43.
- [LWCite-2013] Mahrous et al., 2021, "An enhanced blockchain-based IoT digital forensics architecture using fuzzy hash", IEEE Access 9 — source of the fuzzy-hash Merkle tree variant and its Raspberry Pi feasibility evaluation described above.
- [LWCite-2036] Alashjaee and Alqahtani, 2024, "Improving digital forensic security: A secure storage model with authentication and optimal key generation based encryption", IEEE Access 12 — source of the DFA-AOKGE encrypted, authenticated, blockchain-distributed cloud evidence storage variant described above; note the paper's own comparative timing claims are internally inconsistent with its results tables (see wiki/log.md and LWCite-2036's reference note for detail), so its specific performance figures should not be treated as verified.
- [LWCite-2037] Elgohary et al., 2022, "Improving uncertainty in chain of custody for image forensics investigation applications", IEEE Access 10 — source of the MRSH-v2 fuzzy-hash Hyperledger chain-of-custody variant described above.

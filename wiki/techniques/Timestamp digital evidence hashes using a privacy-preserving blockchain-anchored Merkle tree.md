---
id: LWT-1230
type: technique
name: Timestamp digital evidence hashes using a privacy-preserving blockchain-anchored Merkle tree
description: Obtain an independently verifiable, backdating-resistant proof of when a digital evidence file's hash values were submitted, by batching many submitters' file hashes into a short-lived local Merkle tree and anchoring only the tree's root — never the underlying files or their hashes individually — to a public blockchain, giving each submitter a minimal-disclosure receipt sufficient to reconstruct and verify that root independently.
objective_ids:
  - DFO-1010
weakness_ids:
  - LWW-1248
aliases:
  - Horodocs
source_refs:
  - LWCite-1263
updated_at: 2026-08-13
status: complete
---

# Timestamp digital evidence hashes using a privacy-preserving blockchain-anchored Merkle tree

## Summary

A cryptographic hash proves a file's integrity but says nothing about when the hash was computed, and nothing prevents a dishonest party from re-hashing an altered file later. Horodocs addresses this by having a submitter (typically an investigator) send only their file's MD5 and SHA256 hash values — never the file itself — to a timestamping server, which clusters many submitters' hash values from a short interval into a local, temporary Merkle tree and anchors only the resulting root (as a derived record identifier and an encrypted control value) to a public Ethereum blockchain, keeping per-transaction blockchain costs low and bounded regardless of submission volume.

## Details

On receiving a timestamp request, the server adds a new leaf to the current Merkle tree, computed as `SHA256(salt || unix_timestamp || md5 || sha256)` using a freshly generated random 128-bit salt (sourced from a physical quantum random number generator) — making the leaf value itself non-sensitive, since without the salt an attacker cannot feasibly determine which file (or even which hash pair) produced it. At the end of the tree's short lifespan (on the order of minutes), the server computes the tree's SHA256 root, splits it into a public record identifier and a secret control value, XORs the control value with an independently random value to form a `cipher`, and writes the record identifier plus `cipher` to the Ethereum blockchain via a smart contract; the temporary tree itself, and all per-submitter information, is then discarded from the server. Each submitter instead receives a PDF receipt containing only the minimum information needed to reconstruct the tree's root value from their own leaf's perspective — the salt and Unix time used for their leaf, and one extra 256-bit vertex value per depth level along the leaf-to-root path (n = log2(tree size) values total, so the receipt stays small — under 1 KB — even for a tree of a billion leaves). A verifier (e.g., a judge or the defense) uses the receipt to recompute the root independently, locates the matching record on the Ethereum blockchain via the derived record identifier, and recovers the encrypted control value to confirm the timestamp's date and time — all without needing the Horodocs server to be available, and without the server ever having retained persistent information linking a submitter to their submitted file. The scheme is designed against backdating even by a resourceful adversary (including, potentially, the Horodocs operators themselves) by relying on a widely-used, highly decentralized public blockchain (Ethereum) rather than a private or permissioned ledger, which distinguishes its threat model from evidence-management systems built on private/consortium blockchains (see [[techniques/Anchor digital evidence integrity and chain of custody on a blockchain]]) and from local, non-blockchain-anchored integrity structures (see [[techniques/Preserve digital evidence integrity using a Merkle-tree-based elastic evidence container]]).

## Examples

- For a Horodocs tree containing 1 billion timestamp requests, only 30 extra 256-bit vertex values (log2 of 1 billion, rounded up) are needed on a receipt to reconstruct the root — keeping the receipt small enough to encode as a QR code regardless of how many other submitters shared the same short-lived tree.
- The QR code printed on each Horodocs PDF receipt links to the system's own online verification tool, letting a verifier confirm a timestamp's validity and integrity from any smartphone without needing to run the reconstruction algorithm manually.

## Related Objectives

- `DFO-1010` Preserve digital evidence

## Related Weaknesses

- [[weaknesses/Horodocs timestamp verification provides no integrity guarantee for file modifications occurring before submission]]

## References

- [LWCite-1263] Jaquet-Chiffelle, Pfeiffer, Brocard, Benoist, and Foukia, 2025, "Horodocs: A scalable, sustainable, robust and privacy compliant system to securely timestamp digital evidence and documents", FSI: Digital Investigation 53, 301913.

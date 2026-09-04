---
id: LWT-2052
type: technique
name: Link records across databases using combined phonetic-encoding and multibit-tree private indexing
description: The process of identifying which records held by two or more separately controlled databases (e.g. different investigating agencies or organizations) likely refer to the same real-world individual, by encoding each party's identifying attributes first with phonetic (Soundex) codes and then with a Cryptographic Long-term Key (a bloom-filter-based encoding), and comparing the resulting encoded keys via a multibit-tree similarity search, without any party exposing its underlying raw identifying data to the other.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-2052
aliases:
  - Combined PPRL indexing (Soundex + CLK/multibit tree)
source_refs:
  - LWCite-2053
updated_at: 2026-08-14
status: partial
---

# Link records across databases using combined phonetic-encoding and multibit-tree private indexing

## Summary

When an investigation requires linking records about the same individual held separately by multiple organizations (e.g. two law-enforcement agencies, or an agency and a private-sector data holder), sensitive identifiers like names or dates of birth cannot simply be shared in the clear for comparison. An investigator or data custodian instead has each party encode its own records - first standardizing and phonetically encoding text fields (Soundex) to tolerate spelling/transliteration variation, then further encoding the phonetic codes into a Cryptographic Long-term Key (CLK), a bloom-filter-style bit vector that supports approximate similarity comparison without revealing the original values - and compares the resulting encoded keys across parties using a multibit-tree search to efficiently find likely-matching record pairs.

## Details

LWCite-2053's combined method layers two established PPRL techniques rather than using either alone: standard Soundex-based blocking groups records by a coarse phonetic code (e.g. mapping "Robert" and "Rupert" to the same block "R163"), while the CLK/multibit-tree stage encodes each record's q-grams into a fixed-length bit vector via k independent hash functions, then organizes records of similar bit-vector size into a balanced binary tree structure (splitting recursively on informative bit positions) to efficiently search for records whose Tanimoto/Dice similarity exceeds a threshold without needing to compare every record pair exhaustively. Applying CLK encoding on top of the already-phonetically-encoded data (rather than encoding raw values directly into CLKs, as prior multibit-tree-only approaches did) both improves security (an additional encoding layer) and reduces the multibit tree's tendency toward false-positive matches when used alone.

## Examples

- LWCite-2053's evaluation on two real bibliographic (publication-record) datasets: the combined approach reached a 0.9996 reduction ratio, 0.84 pairs completeness, 0.9129 F-score, and 4.9463-second running time, each outperforming the multibit-tree-only baseline (0.9953, 0.7514, 0.8563, 6.9535 seconds respectively).

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Combined private indexing assumes all participating parties are genuine, risking privacy compromise by a dishonest party]]

## References

- [LWCite-2053] Desai and Shelake, "A combined approach for private indexing mechanism", Journal of Digital Forensics, Security and Law, 2022 — source of the combined Soundex-plus-CLK/multibit-tree indexing method and its evaluation results described above.

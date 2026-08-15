---
id: DFW-1272
type: weakness
name: Automated dark web identifier extraction misses obfuscated, image-embedded, or non-standard-format identification forms
description: Automated text-pattern-based extraction of dark web identification forms (email addresses, Telegram usernames, wallet addresses) cannot recognize identifiers that are embedded as images rather than text, encoded in non-standard formats, or deliberately obfuscated using known techniques such as two-layered ID encoding, causing a systematic undercount of an onion service's true set of external communication channels.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1273
source_refs:
  - DFCite-1300
updated_at: 2026-08-14
status: complete
---

# Automated dark web identifier extraction misses obfuscated, image-embedded, or non-standard-format identification forms

## Summary

The underlying study's authors explicitly acknowledge that its automated ID-extraction approach "may have missed certain IDs (e.g., those embedded in images or non-standard formats), introducing potential bias in the bipartite graph's construction," and separately note that "two-layered obfuscated ID forms are known to exist on the dark web but are difficult to extract using automated methods." Because the resulting network graph is built entirely from the IDs the automated scraper successfully recognized, any identifier hidden from that recognition step is simply absent from the graph rather than flagged as an unknown or low-confidence node.

## Why It Matters

An investigator relying on a network-analysis-derived hub ranking or connectivity picture to prioritize which service or identifier to target risks underestimating a specific actor's or channel's true reach if their preferred identifiers happen to be image-embedded, obfuscated, or otherwise outside the extraction method's recognized formats — a deliberately obfuscation-savvy operator's centrality in the real ecosystem could be systematically understated relative to less careful operators, inverting the intended prioritization value of the analysis for exactly the targets most worth pursuing.

## Related Mitigations

- [[mitigations/Supplement automated dark web ID extraction with OCR and manual review for obfuscated or image-embedded identifiers]]

## Used By

- [[techniques/Map a Tor darkmarket ecosystem using bipartite network analysis of onion services and identification forms]]

## References

- [DFCite-1300] de-Marcos, Domínguez-Díaz and Stapic, 2026, "Mapping the Tor darkmarket ecosystem: A network analysis of topics, communication channels, and languages", FSI: Digital Investigation 56, 302032.

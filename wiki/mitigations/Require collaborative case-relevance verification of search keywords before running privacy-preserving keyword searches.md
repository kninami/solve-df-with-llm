---
id: DFM-2018
type: mitigation
name: Require collaborative case-relevance verification of search keywords before running privacy-preserving keyword searches
source_refs:
  - DFCite-2018
updated_at: 2026-08-14
status: partial
---

# Require collaborative case-relevance verification of search keywords before running privacy-preserving keyword searches

## Summary

Before running a first- or second-stage keyword search over encrypted evidential data, have the case-related and case-relevant keyword sets reviewed collaboratively by relevant stakeholders (e.g. the investigator together with a supervising officer, legal counsel, or a service provider) to check that each keyword is genuinely justified by the investigation's scope, rather than allowing an unverified keyword list to determine how much private data is drawn into the pipeline.

## Addresses

- [[weaknesses/Homomorphic keyword search lacks a way to verify submitted keywords are actually case-relevant]]

## How To Apply

Integrate a keyword-relevance-verification step into the privacy-preserving digital forensics workflow, documenting for each keyword why it is tied to the investigation's scope (consistent with the "who, what, when, where, why, how" review recommended when scoping evidence sources), and prefer the narrower, justified keyword set over maximally broad disjunctive searches where the added retrieval does not meaningfully advance the investigation.

## References

- [DFCite-2018] Ogunseyi and Adedayo, 2023 — Section III.F's proposed solution recommends integrating keyword verification techniques and careful, collaborative keyword selection between investigators and other stakeholders to reduce the risk of over-broad, non-relevant data collection.

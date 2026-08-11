---
id: DFT-1027
type: technique
name: Formal Concept Analysis of antivirus identifier equivalence and hierarchy
description: Model a set of scanned files and the malware identifiers assigned to them by many different antivirus engines as a Formal Concept Analysis (FCA) formal context, then use context clarification and the resulting concept lattice to automatically detect which differently-named identifiers from different vendors refer to the same malware, and to derive a generalization-specialization hierarchy between malware categories.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1027
aliases: []
source_refs:
  - DFCite-1019
updated_at: 2026-08-09
status: complete
---

# Formal Concept Analysis of antivirus identifier equivalence and hierarchy

## Summary

Given a table of files (objects) and the malware identifiers each of many antivirus engines assigned to them (attributes, via one-hot/nominal scaling), FCA's context-clarification step automatically flags two vendor-specific identifiers as equivalent whenever they are always assigned to exactly the same set of files — meaning both vendors always agree, even if their naming schemes are unrelated. Reading the resulting concept lattice's vertical structure further reveals which identifiers are strict generalizations, specializations, or intersections of others, without requiring any natural-language processing of the identifier strings themselves.

## Details

A formal context K = (G, M, I) is built with G = scanned files, M = ⟨antivirus, identifier⟩ attribute pairs, and I = which files each identifier was assigned to. Clarification merges attributes with identical object-sets (equivalent identifiers) and objects with identical attribute-sets, without changing the resulting concept lattice's structure. The lattice's generalization-specialization order can then be read directly: a concept that is a coatom (only the universal top concept above it) represents a generic malware category; a concept with exactly one upper neighbor is a proper subcategory of that neighbor; and a concept with multiple upper neighbors corresponds exactly to the intersection of those neighboring categories (via Birkhoff's representation theorem). This gives a mathematically grounded hierarchy without manual curation, distinct from prior approaches based on natural-language similarity of identifier strings or unsupervised clustering.

## Examples

- Applied to 183 Android threat files scanned by 6 antivirus engines (a reduced subset of VirusTotal's 66), clarification reduced 491 attributes to 194 and found 84 sets of equivalent cross-vendor identifiers (e.g., McAfee's `!03eaa0113ccf` ≡ ESET-NOD32's `spy.androrat.ak` ≡ Kaspersky's, Avast-Mobile's, and Avira's respective identifiers for the same threat). The resulting 265-concept lattice further identified 39 malware sets expressible as the exact intersection of other categories and 123 categories strictly contained within such intersections.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Inconsistent antivirus naming prevents straightforward cross-vendor correlation of malware reports]]

## References

- [DFCite-1019] Ojeda-Hernández et al., 2024, "A Formal Concept Analysis approach to hierarchical description of malware threats", FSI: Digital Investigation 50.

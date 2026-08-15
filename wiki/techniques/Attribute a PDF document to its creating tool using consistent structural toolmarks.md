---
id: DFT-1281
type: technique
name: Attribute a PDF document to its creating tool using consistent structural toolmarks
description: Determine which software tool created a questioned PDF document by identifying structural choices the PDF standard leaves unspecified (line-termination style, whitespace usage, object ordering, and other low-level formatting decisions) that a given tool's implementation makes consistently across every document it produces, then comparing a questioned document's feature vector of these "toolmarks" against a reference set built from documents of known origin.
objective_ids:
  - DFO-1002
  - DFO-1008
weakness_ids:
  - DFW-1291
aliases:
  - PDF toolmark classification
  - Programmed execution principle applied to PDF attribution
source_refs:
  - DFCite-1322
updated_at: 2026-08-15
status: complete
---

# Attribute a PDF document to its creating tool using consistent structural toolmarks

## Summary

Because the PDF standard leaves many low-level structural details unspecified (for example, how a "line" within the file is terminated, even though PDF documents are in practice split into lines far more often than the standard strictly requires), each software tool's implementation must independently choose how to handle these details — and, per the "programmed execution principle," a piece of software executing deterministically will make the same choice every time it runs, leaving a structural mark ("toolmark") in every document it produces that can be compared across documents to attribute a questioned document to its creating tool, analogous to attributing a bullet to the firearm that fired it or handwriting to a suspect's typewriter.

## Details

The approach proceeds in three stages, mirroring classification as defined by Inman and Rudin (determining whether two artefacts share a common origin): (1) identify structural aspects of PDF representation that are not fully standardised and could plausibly serve as toolmarks; (2) verify that a given candidate toolmark occurs *consistently* across a large number of documents independently known to have been created by the same tool, since a mark that varies unpredictably even within one tool's output cannot serve as a reliable toolmark; (3) combine a set of verified, sufficiently varied toolmarks into a feature vector and use it to classify a large mixed-origin dataset of documents into per-tool classes, measuring how successfully the resulting classes correspond to genuine common origin. Verification and classification were performed against the 1000 .gov PDF dataset provided by the US Library of Congress. The paper is explicit that no single toolmark by itself needs to be provably unique to one tool — variety and combination across several toolmarks is what gives the feature vector its discriminatory power, and the paper notes this power was "quite surprising," exceeding what was initially anticipated when the study set out merely to demonstrate that toolmark variety exists at all.

## Examples

- A trivial but representative toolmark: since the PDF standard does not prescribe line termination, a tool's choice among carriage return, line feed, or a CR+LF combination — made consistently every time that tool executes — is itself a usable toolmark component.
- Metadata fields embedded by a creation tool are comparatively easy for a document's producer to modify or strip, making metadata alone an unreliable basis for tool attribution; structural toolmarks, being a side effect of the tool's own deterministic code rather than an explicit, user-editable field, are harder to falsify without specialized knowledge of the target tool's internal formatting choices.

## Related Objectives

- `DFO-1002` Extract data from specific formats
- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/PDF toolmark-based tool attribution can misclassify documents from the same tool under different configurations]]

## References

- [DFCite-1322] Olivier, 2026, "On the classification of questioned PDF documents — Attributing PDF documents to the tools that created them", FSI: Digital Investigation 57, 302104.

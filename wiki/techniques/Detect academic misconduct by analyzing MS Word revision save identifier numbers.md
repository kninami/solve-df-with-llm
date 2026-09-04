---
id: LWT-1183
type: technique
name: Detect academic misconduct by analyzing MS Word revision save identifier numbers
description: Examine the revision save identifier (rsid) tags embedded in a single submitted MS Word document's XML structure — which record each editing session and text-insertion event — to test whether a student's or author's asserted document-generation process (self-written, iteratively edited, pasted from another source, AI-generated) is consistent with the document's actual editing history.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1190
aliases:
  - Rsid forensic analysis
  - Revision save identifier document forensics
source_refs:
  - LWCite-1195
updated_at: 2026-08-13
status: complete
---

# Detect academic misconduct by analyzing MS Word revision save identifier numbers

## Summary

MS Word assigns a unique document identifier (rootrsid) at file creation and a further unique identifier to every editing session that ends in a save, and tags text insertions, paragraph creation, and character-formatting changes (`insrsid`, `charrsid`, `pararsid`, `rsidRPr`, `rsidR`, `rsidRDefault`) with the rsid of the session in which they occurred. Because these tags are collectively listed in an ascending-order summary table (`rsidtbl`) in the document's `settings.xml`, and because the probability of two independently generated files sharing a given rsid combination by chance is astronomically small, comparing the rsid tags actually present in a single submitted document against the pattern a genuinely iterative writing process would produce can reveal whether text was typed in place, pasted from an external source, or carried over from an unrelated file — evidence directly relevant to contract-cheating and AI-generated-text allegations.

## Details

The technique works from a single available document, extracted either by unpacking the `.docx` archive's XML or by exporting to rich text format. A short editing time and low revision count in the document properties (`docProps/core.xml`) can indicate either genuinely minimal editing or that an older file's text was blanked and reused (carrying over its legacy rsid). Text pasted from a different MS Word file is enclosed by both an `insrsid` (denoting the current paste session) and a `charrsid` (denoting the pasted text's original edit history); if that `charrsid` value is absent from the document's own `rsidtbl`, the enclosed text did not originate in this document. Text lacking both tags entirely ("rsid-less" or "washed" text) is characteristic of content pasted from a webpage/PDF, a paraphrasing tool, or a generative AI system's output, since none of these preserve MS Word's internal edit-tracking tags. A genuinely iterative single-author manuscript shows numerous, temporally nested `insrsid`/`charrsid` codes tracking its writing and editing progress; a document assembled by copying a whole external essay in one paste action shows a small number of uniform rsid values covering large text blocks instead. The method's premises — MS Word's own non-adherence to the ECMA Office Open XML rsid-ordering specification and the absence of the `track changes` review feature in most student submissions — must be understood before drawing conclusions, since some plausible academic-integrity officer intuitions about rsid ordering (e.g. that later rsid numbers are always chronologically later) do not reliably hold.

## Examples

- A submitted document whose editing time and revision count were both implausibly low, but whose rsidtbl contained thousands of legacy rsid entries inconsistent with a freshly created file, indicated that an old document had been blanked and reused rather than genuinely written from scratch.
- A chunk of plagiarized text enclosed by a single uniform `insrsid`/`charrsid` pair, with a spurious citation inserted via a distinct later-session rsid, matched the expected signature of a whole external document pasted in and then given a fabricated reference in a subsequent edit session.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Failure to retain rsid tags in washed or plain-text-pasted content prevents source attribution]]

## References

- [LWCite-1195] Spennemann, Spennemann and Singh, 2024, "Examining and detecting academic misconduct in written documents using revision save identifier numbers in MS Word as exemplified by multiple scenarios", FSI: Digital Investigation 51, 301821.

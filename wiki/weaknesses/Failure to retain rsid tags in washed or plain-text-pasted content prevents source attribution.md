---
id: DFW-1190
type: weakness
name: Failure to retain rsid tags in washed or plain-text-pasted content prevents source attribution
description: Text that has been copied through a plain-text intermediary (a text editor, a webpage, a PDF, a paraphrasing tool, or a generative AI system's output) arrives in an MS Word document with no insrsid or charrsid tags at all, so while rsid analysis can show that such a block of text was inserted as a single unit rather than typed, it cannot by itself determine where that text actually originated.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1190
source_refs:
  - DFCite-1195
updated_at: 2026-08-13
status: complete
---

# Failure to retain rsid tags in washed or plain-text-pasted content prevents source attribution

## Summary

Any text-copying route that strips MS Word's internal XML formatting before the text reaches the document under examination — a paraphrasing tool, a plain-text editor, a PDF or webpage, or the raw output of a generative AI model — produces rsid-less ("washed") text indistinguishable, from the rsid data alone, between these different possible sources. The rsid evidence can establish the extent and structural pattern of the insertion (e.g. confined to one paragraph in one session versus scattered across the document across multiple sessions) but not which of several plausible external sources actually produced it.

## Why It Matters

An investigator who over-relies on rsid analysis alone for a single document risks either over-attributing washed text to a specific source without corroboration, or dismissing a genuinely suspicious insertion because rsid data alone cannot confirm its origin, when in either case the missing information is a structural limitation of the file format rather than a flaw in the analysis itself. Because innocuous explanations for rsid-less text exist (e.g. legitimately typing in a plain-text editor before pasting into Word), treating the absence of rsid tags as conclusive proof of misconduct on its own would risk an unsupported finding.

## Related Mitigations

- [[mitigations/Cross-correlate rsid-based document forensic findings with a structured perpetrator interview]]

## Used By

- [[techniques/Detect academic misconduct by analyzing MS Word revision save identifier numbers]]

## References

- [DFCite-1195] Spennemann, Spennemann and Singh, 2024, "Examining and detecting academic misconduct in written documents using revision save identifier numbers in MS Word as exemplified by multiple scenarios", FSI: Digital Investigation 51, 301821.

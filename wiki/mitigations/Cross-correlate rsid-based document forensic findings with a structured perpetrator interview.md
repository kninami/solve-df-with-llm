---
id: DFM-1190
type: mitigation
name: Cross-correlate rsid-based document forensic findings with a structured perpetrator interview
source_refs:
  - DFCite-1195
updated_at: 2026-08-13
status: complete
---

# Cross-correlate rsid-based document forensic findings with a structured perpetrator interview

## Summary

Pair a document's rsid-based editing-history findings with a structured interview of the alleged perpetrator about their claimed document-generation and editing process, so the rsid observations can be tested for congruence (an innocuous explanation) or dissonance (a misconduct indicator) against what the author actually asserts happened, rather than relying on rsid data alone to determine intent or source.

## Addresses

- [[weaknesses/Failure to retain rsid tags in washed or plain-text-pasted content prevents source attribution]]

## How To Apply

Before or alongside the rsid examination, gather as much detail as possible about the author's asserted document-generation and editing process — a structured set of interview prompts covering how and where the document was drafted, whether any text was copied or pasted from another source, what tools were used, and over what timeframe — since this establishes a testable scenario. Convert the interview responses into concrete, checkable predictions about the rsid pattern a genuine account should produce (e.g. a claimed multi-day iterative drafting process should show a correspondingly rich rsidtbl with rsid distributed across multiple save sessions), then examine whether the actual rsid data is congruent or dissonant with that account. Where rsid-less text is found, do not treat its mere presence as conclusive; instead use the interview to establish which of the innocuous or non-innocuous explanations (own prior plain-text drafting, a permitted paraphrasing tool, a prohibited external source, or AI generation) is most consistent with the author's own account, and note where their account is inconsistent with the observed structural pattern (a single-session single-tag insertion versus multiple scattered rsid-less segments).

## References

- [DFCite-1195] Spennemann, Spennemann and Singh, 2024, "Examining and detecting academic misconduct in written documents using revision save identifier numbers in MS Word as exemplified by multiple scenarios", FSI: Digital Investigation 51, 301821.

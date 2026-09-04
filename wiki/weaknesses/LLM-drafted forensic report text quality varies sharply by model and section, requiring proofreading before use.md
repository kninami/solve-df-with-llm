---
id: LWW-1119
type: weakness
name: LLM-drafted forensic report text quality varies sharply by model and section, requiring proofreading before use
description: LLM-generated forensic report text is inconsistently accurate and complete — quality drops substantially for locally-run models compared to cloud-based ones, and for report sections whose input data is less structured or less available — so unreviewed LLM output can introduce inaccuracies, unsupported claims, or omissions directly into a document intended for court.
categories:
  - ASTM_INAC_EX
  - ASTM_MISINT
mitigation_ids:
  - LWM-1119
source_refs:
  - LWCite-1111
updated_at: 2026-08-12
status: complete
---

# LLM-drafted forensic report text quality varies sharply by model and section, requiring proofreading before use

## Summary

Across all tested report sections, the locally-run model (Llama-2-13B) underperformed the cloud-based model (ChatGPT-3.5), at times producing text containing claims not supported by, or contradicting, the source case data — for example, inventing a detail (a phone being "stolen by Italian police") that was not present in the mandate. Even the stronger cloud model's output quality varied within and across sections: results-section summaries "had a wide range of quality with varying levels of accuracy and completeness," and the discussion and conclusion sections were assessed as too dependent on inaccessible examiner judgment and experience to be reliably automated at all.

## Why It Matters

A forensic report is a document submitted to a court, so unreviewed inaccuracies or fabricated details inserted by an LLM draft carry direct legal risk, not just a stylistic cost. Because quality is not uniform — varying by model choice, by report section, and even between repeated generations of the same section — an investigator cannot assume a given LLM-assisted workflow is reliable based on one successful output and must treat every generated section as a draft requiring independent verification against the source case data before inclusion.

## Related Mitigations

- [[mitigations/Require expert proofreading of every LLM-drafted report section against its source case data before inclusion]]

## Used By

- [[techniques/Draft forensic report sections using a large language model]]

## References

- [LWCite-1111] Michelet and Breitinger, 2024, "ChatGPT, Llama, can you write my report? An experiment on assisted digital forensics reports written using (local) large language models", FSI: Digital Investigation 48.

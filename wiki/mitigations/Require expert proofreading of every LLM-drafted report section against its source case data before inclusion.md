---
id: LWM-1119
type: mitigation
name: Require expert proofreading of every LLM-drafted report section against its source case data before inclusion
source_refs:
  - LWCite-1111
updated_at: 2026-08-12
status: complete
---

# Require expert proofreading of every LLM-drafted report section against its source case data before inclusion

## Summary

Treat every LLM-generated report section as an unverified draft: have the investigator who wrote the lab log and knows the case facts proofread and correct the generated text against the mandate, lab log, and tool report before it is included in the final submitted report, and restrict LLM assistance to sections with high LLM-potential (introduction, items received, methodology) rather than sections dependent on examiner judgment (discussion, conclusion).

## Addresses

- [[weaknesses/LLM-drafted forensic report text quality varies sharply by model and section, requiring proofreading before use]]

## How To Apply

Limit LLM-assisted drafting to report sections shown to have high or medium LLM-potential based on data availability and structural consistency (introduction, items received, methodology, and narrow results sub-elements), and always compare the generated text sentence-by-sentence against its source input (mandate, lab log, or tool-report excerpt) before use, watching in particular for claims not traceable to any input source. Where a local model is used for confidentiality reasons instead of a cloud service, budget for materially more correction effort than with a cloud-based model, since local-model output was consistently less accurate and complete across every tested section.

## References

- [LWCite-1111] Michelet and Breitinger, 2024, "ChatGPT, Llama, can you write my report? An experiment on assisted digital forensics reports written using (local) large language models", FSI: Digital Investigation 48.

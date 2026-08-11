---
id: DFW-1033
type: weakness
name: LLM-assisted forensic text triage hallucinates entities not present in the source evidence
description: When a large language model is used to extract or summarize forensically relevant entities (names, locations, device identifiers, phone numbers) from clustered forensic text data, it generates a measurable proportion of plausible-sounding entities that do not actually exist anywhere in the source corpus, alongside its genuine extractions.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - DFM-1033
source_refs:
  - DFCite-1023
updated_at: 2026-08-09
status: complete
---

# LLM-assisted forensic text triage hallucinates entities not present in the source evidence

## Summary

Across the evaluated prompts and models, hallucination rates ranged from 0.02 to 0.07 for the best-performing model (GPT-4) on the primary dataset, and were markedly worse for some other models on specific tasks (e.g., a geographical-locations prompt where one model hallucinated countries such as "Japan" and "Korea" that were not present in the source data in any form or language). Because hallucinations count as false positives in the paper's own precision calculation, they are already reflected in reduced precision scores, but a plausible-sounding hallucinated entity is not otherwise distinguishable from a genuine extraction without independent verification.

## Why It Matters

A hallucinated entity presented alongside genuinely extracted forensic data risks being mistaken for evidence that was actually present on the device, since the language model's output for both is stylistically identical and equally confident-sounding. In an investigative context, this could lead to pursuing a lead (a name, location, or device) that was never actually part of the original evidence, or citing a fabricated data point in a report — a direct injection of extra, non-original data into the forensic record if not caught.

## Related Mitigations

- [[mitigations/Cross-reference LLM-identified entities against the source corpus before accepting them as evidence]]

## Used By

- [[techniques/Clustering-assisted LLM triage of unstructured forensic string-search output]]

## References

- [DFCite-1023] Fayyaz et al., 2024, "A hybrid artificial intelligence framework for enhancing digital forensic investigations of infotainment systems", FSI: Digital Investigation 49.

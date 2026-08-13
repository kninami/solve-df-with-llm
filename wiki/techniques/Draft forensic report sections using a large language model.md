---
id: DFT-1114
type: technique
name: Draft forensic report sections using a large language model
description: Prompt a large language model — a cloud-based service such as ChatGPT, or a locally-run model such as Llama — with case data (mandate, lab log, or tool report excerpts) to generate a first-draft version of a structured forensic report section, such as the introduction, items-received description, methodology summary, or an artefact/results summary, for the investigator to review and correct rather than write from scratch.
objective_ids:
  - DFO-1020
weakness_ids:
  - DFW-1119
aliases:
  - LLM-assisted forensic report writing
  - ChatGPT/Llama assisted digital forensics report generation
source_refs:
  - DFCite-1111
updated_at: 2026-08-12
status: complete
---

# Draft forensic report sections using a large language model

## Summary

Forensic report writing is a time-consuming, mostly unautomated step of an investigation, distinct from the technical tool-report summaries produced by software like Autopsy or Cellebrite. Analysis of forensic reports found a consistent underlying structure — introduction, items received, methodology, results, discussion, conclusion — with each section drawing on a specific combination of input sources (the prosecutor's mandate, the examiner's lab log, and tool-report output); prompting an LLM with the relevant input source for a given section can produce a usable first draft for sections with high input-data availability and low structural variability.

## Details

Assessed across six report sections, LLM-potential correlated directly with data availability and structural consistency: the introduction, items-received, and methodology sections (mandate- and lab-log-derived, with a fairly fixed structure) were rated high-potential; the results section (combining tool-report and lab-log data, but with highly variable per-case organization) was rated medium; and the discussion and conclusion sections (dependent on the examiner's own experience, judgment, and opinion, largely absent from any written input source) were rated low and excluded from the generation experiment. In a case-study experiment generating text with both a cloud LLM (ChatGPT-3.5) and a local LLM (Llama-2-13B, 4-bit quantized) across 36 prompts per model, ChatGPT consistently produced accurate, complete text usable in a report after only minor adjustment for the introduction, items-received, and methodology sections, and added correct auxiliary domain detail (e.g. describing standard mobile-forensic methodology steps) beyond what was explicitly supplied in the input. For the results section, generation was limited to two artefact types (conversation summaries and GPS-location summaries); output quality varied and was not affected by which of three input formats (raw tool-report excerpt, lab-log table, or a filtered/reformatted CSV) was supplied. The local model (Llama) underperformed the cloud model across every tested section, frequently producing text lacking sufficient accuracy or completeness to be usable without extensive correction, though it still produced at least one report element of sufficient quality per section tested.

## Examples

- Prompted with a structured copy of the case mandate and a request to "summarize the previous text and write the intro of a forensic report," ChatGPT produced accurate, complete introductions requiring only minor adjustment, while Llama's output on the same prompt included a materially incorrect claim (that a suspect's phone had been "stolen by Italian police," which was not part of the case facts).
- Generating the methodology section from the lab log's list of investigative steps and tools, ChatGPT produced accurate, complete first drafts and added correct supplementary detail about standard mobile-forensic methodology, plausibly reflecting methodology descriptions present in its training data.

## Related Objectives

- `DFO-1020` Document digital forensic activities

## Related Weaknesses

- [[weaknesses/LLM-drafted forensic report text quality varies sharply by model and section, requiring proofreading before use]]

## References

- [DFCite-1111] Michelet and Breitinger, 2024, "ChatGPT, Llama, can you write my report? An experiment on assisted digital forensics reports written using (local) large language models", FSI: Digital Investigation 48.

---
id: DFT-1031
type: technique
name: Contextual case-information-guided review of digital evidence
description: A digital forensic examiner reviews an evidence file (e.g., a disk image or set of digital traces) while informed by contextual case information provided at commissioning, forming observations, interpretations of those observations, and an overall conclusion about the matter under investigation.
objective_ids:
  - DFO-1003
weakness_ids:
  - DFW-1031
  - DFW-1032
aliases: []
source_refs:
  - DFCite-1022
updated_at: 2026-08-09
status: complete
---

# Contextual case-information-guided review of digital evidence

## Summary

Digital forensic casework is normally commissioned with some accompanying contextual information about the suspected incident, and examiners are expected to use their normal workstation, tools of choice, and professional judgement to observe traces in the evidence, interpret what those observations mean, and reach a conclusion that is reported to the requesting party. This is the default, everyday mode of digital forensic examination, distinct from fully blinded or algorithmically-constrained review.

## Details

The process operates at three distinct levels that can each be evaluated separately: observation (what traces are noticed and reported as found/not found), interpretation (what a given observed trace is understood to mean, e.g., which of several possible explanations fits), and conclusion (an overall judgement, e.g., whether the evidence indicates guilt, innocence, or is ambiguous). Because examiners are given latitude in which tools to use and how to explain their findings, and because case files typically contain large amounts of both task-relevant and task-irrelevant information, the review process is inherently more variable between examiners than would be expected of a purely mechanical procedure.

## Examples

- A simulated confidential-information-leakage case file (an Excel spreadsheet leak from a company's internal network) was analyzed by 53 digital forensic examiners across four contextual-information groups (Control, Strong Guilt, Weak Guilt, Innocence), each reporting observed traces, interpretations, and a conclusion about a named suspect's involvement.

## Related Objectives

- `DFO-1003` Review content for relevance

## Related Weaknesses

- [[weaknesses/Task-irrelevant contextual information biases DF examiner observations and conclusions]]
- [[weaknesses/Independent DF examiners reach low-reliability conclusions analyzing the same evidence file]]

## References

- [DFCite-1022] Sunde and Dror, 2021, "A hierarchy of expert performance (HEP) applied to digital forensics: Reliability and biasability in digital forensics decision making", FSI: Digital Investigation 37.

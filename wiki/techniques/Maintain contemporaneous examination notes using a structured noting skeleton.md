---
id: DFT-1128
type: technique
name: Maintain contemporaneous examination notes using a structured noting skeleton
description: Record a digital forensic examination's actions, decisions, and findings at the time they occur, or as soon as possible after, using a structured content skeleton covering exhibit handling, case information, and each stage of the investigative workflow, to support later review, reporting, and disclosure.
objective_ids:
  - DFO-1020
weakness_ids:
  - DFW-1131
aliases:
  - Contemporaneous notes (CNs)
  - DF examination noting skeleton
source_refs:
  - DFCite-1128
updated_at: 2026-08-12
status: complete
---

# Maintain contemporaneous examination notes using a structured noting skeleton

## Summary

Contemporaneous notes (CNs) — created at or near the time of the event they describe, as opposed to retrospectively recollected notes — support a practitioner throughout an examination and through to report production, and may also be subject to disclosure requirements. A structured "noting skeleton of content," mapped to the standard investigative stages, gives practitioners a concrete checklist of what to record.

## Details

CNs are considered a "gold standard" over retrospective notes because practitioners cannot reliably recall fine examination detail months or years later when a case reaches court, and examinations are often multi-staged and lengthy, with work potentially revisited at later intervals. The noting skeleton covers exhibit information (make/model, serial numbers, visible condition and marks, a photographic/video record, component inventory for devices with multiple storage media, and any configuration changes caused by handling), case information (investigators involved, instructions received, and communications with other parties that could affect the examination scope), and entries mapped to the generic investigative stages — exhibit handling, data acquisition, data examination, analysis and interpretation, and reporting — with "critical decisions" that change the course of an examination specifically flagged and their basis recorded. Notes should be detailed enough that an independent third party could reconstruct the practitioner's process, interpretations, and the inferences drawn from the work without needing to consult the original examiner.

## Examples

- A UKAS surveillance review of 29 ISO 17025-accredited digital forensic units in England and Wales (September 2018-April 2019) found recurring concerns about "inaccurate or insufficient information being recorded in notes or supporting quality records," motivating the structured noting skeleton proposed here.

## Related Objectives

- `DFO-1020` Document digital forensic activities

## Related Weaknesses

- [[weaknesses/Contemporaneous note-taking platforms without write-once integrity protections allow undetected retrospective editing]]

## References

- [DFCite-1128] Horsman, 2021, "Contemporaneous notes for digital forensic examinations", FSI: Digital Investigation 37, 301173.

---
id: LWT-1147
type: technique
name: Score digital device seizure priority using a structured scoresheet
description: Support a first responder's at-scene decision about whether to seize a digital device, and how urgently to examine it, by completing the Device Evaluation and Prioritisation Scoresheet (DEPS) — a structured set of questions about a device's likely investigative value and volatility — rather than relying on ad hoc judgment or a default "seize everything" approach.
objective_ids:
  - DFO-1005
weakness_ids:
  - LWW-1150
aliases:
  - Device Evaluation and Prioritisation Scoresheet
  - DEPS methodology
source_refs:
  - LWCite-1147
updated_at: 2026-08-12
status: complete
---

# Score digital device seizure priority using a structured scoresheet

## Summary

First responders often lack the confidence, training, or time at scene to reliably judge which of potentially many digital devices are relevant to an inquiry, leading either to indiscriminate seizure of everything present or inconsistent, undocumented judgment calls. The DEPS methodology addresses this by providing a structured, transparent scoresheet that captures a first responder's device-prioritisation reasoning at the point of decision, producing a documented, reviewable record of both the identification/seizure decision and the assumed investigative priority assigned to each device.

## Details

DEPS is completed by the first responder for each identified device at scene, working through a defined set of questions about the device's apparent relevance, ownership/association with a person of interest, likely data volatility (e.g., whether powered on, whether encryption is in use), and evidential potential given the nature of the inquiry. The resulting score both supports the immediate seizure decision and gives a documented priority ranking that downstream forensic examiners can use to triage a backlog of seized devices, rather than examining devices in seizure order or by default assumption. Because the scoresheet is completed and retained as a record, it also creates an auditable trail explaining why a particular device was or was not seized, and why it was assigned a given priority, addressing a documented gap in current practice where such decisions are made informally and are difficult to review or challenge after the fact.

## Examples

- A first responder completing a DEPS scoresheet at scene for each of several personal devices found, seizing only those scoring above a relevance threshold and recording the score sheet as justification for both decisions.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/First responders can inflate device-prioritisation scoresheet answers to increase seizure priority]]

## References

- [LWCite-1147] Horsman, 2021, "Decision support for first responders and digital device prioritisation", FSI: Digital Investigation 38.

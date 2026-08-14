---
id: DFW-2039
type: weakness
name: Infrared diagnostic imaging of a damaged SD card risks creating or worsening the fault it is meant to locate
description: Infrared thermal diagnostic analysis of a damaged SD card requires powering the card on, which risks accentuating an existing defect or creating a new one not previously present, and the forensic expert cannot always tell in advance whether a rising temperature will stabilize (a usable diagnostic result) or continue climbing toward chip-damaging levels (requiring the test to be aborted before a conclusive location is found).
categories:
  - ASTM_INAC_ALT
mitigation_ids:
  - DFM-2039
source_refs:
  - DFCite-2039
updated_at: 2026-08-14
status: partial
---

# Infrared diagnostic imaging of a damaged SD card risks creating or worsening the fault it is meant to locate

## Summary

The source paper's own discussion states plainly: "this paper, to the best of our knowledge, has introduced for the first time the possibility of using an infrared camera as a diagnostic method in forensic protocols for digital devices. However, this method must be classified as an invasive method since the infrared diagnosis requires the SD card to be powered on, which increases the risk of accentuating or creating a fault not previously diagnosed." During the technique's own worked example, the authors note two possible outcomes when temperature is observed rising: either it reaches a threshold "dangerous for the integrity of the chip materials," forcing the expert to stop the process before establishing a final, stabilized diagnostic state, or it stabilizes, allowing a precise fault location without further risk - and the expert cannot know in advance which outcome will occur.

## Why It Matters

An investigator applying infrared thermal diagnosis to a damaged card containing irreplaceable evidence is trading diagnostic information for a real risk of causing additional, potentially unrecoverable damage; a card that could have been partially readable before the test may become less so if the observed defect worsens during the powered-on imaging process, and because this method is classified as invasive, using it without appropriate judicial authorization in a legal investigation risks compromising the evidence's admissibility as well as its physical integrity.

## Related Mitigations

- [[mitigations/Apply infrared thermal diagnosis only after non-invasive steps are exhausted and be ready to abort immediately on unbounded temperature rise]]

## Used By

- [[techniques/Diagnose damaged SD card failure modes using a non-invasive-to-invasive decision protocol]]

## References

- [DFCite-2039] Thomas-Brans et al., 2022 — Section V "Discussion" explicitly classifies infrared analysis as invasive due to the power-on requirement, and Section III.B.2 details the two possible (safe-stabilizing vs. damage-risking) temperature-rise outcomes observed during infrared diagnosis.

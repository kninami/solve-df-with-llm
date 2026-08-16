---
id: DFW-1296
type: weakness
name: End-of-investigation-only peer review lets an early undetected error propagate through the rest of the investigation
description: When peer review is performed only once, after all investigative work is complete, an error introduced early (such as an incomplete or errored data acquisition) is not caught until the practitioner has already built and reported further analysis on top of it, forcing costly rework and increasing the risk that the error is never identified at all.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1298
source_refs:
  - DFCite-1329
updated_at: 2026-08-15
status: complete
---

# End-of-investigation-only peer review lets an early undetected error propagate through the rest of the investigation

## Summary

A traditional, single end-of-case peer review evaluates the entirety of a practitioner's completed work at once. Because it occurs only after all investigative work has concluded, it is inherently reactive: an early-stage problem — for example, an acquisition method that produced only a partial data set due to incomplete sectors or a verification issue — is not surfaced until the practitioner has already spent further time examining, interpreting, and reporting on that incomplete data.

## Why It Matters

Discovering a foundational error only at final review forces the practitioner to restart affected work, effectively duplicating effort and doubling the resources spent on the case, and increases the risk of a "cascading" or "snowball" effect where the initial error's consequences have already influenced downstream findings, conclusions, or even other cases before it is caught. In the worst case, a subtle early error that is not obviously wrong to a reviewer examining only the final report may never be caught at all, since the specific point in the workflow where it was introduced is no longer directly visible in the final artifact.

## Related Mitigations

- [[mitigations/Distribute peer review across investigation phase checkpoints rather than performing it only at case close]]

## Used By

- [[techniques/Apply a phase-oriented multi-stage peer review structure to a digital forensic investigation]]

## References

- [DFCite-1329] Sunde and Horsman, 2021, "Part 2: The Phase-oriented Advice and Review Structure (PARS) for digital forensic investigations", FSI: Digital Investigation 36, 301074.

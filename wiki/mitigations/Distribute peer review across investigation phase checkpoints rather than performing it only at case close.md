---
id: DFM-1298
type: mitigation
name: Distribute peer review across investigation phase checkpoints rather than performing it only at case close
source_refs:
  - DFCite-1329
updated_at: 2026-08-15
status: complete
---

# Distribute peer review across investigation phase checkpoints rather than performing it only at case close

## Summary

Restructure an organization's peer review process into checkpoints positioned at critical milestones throughout an investigation, rather than a single review conducted only once all investigative work is complete, so foundational errors (such as an incomplete acquisition) are caught and corrected before further work is built on top of them.

## Addresses

- [[weaknesses/End-of-investigation-only peer review lets an early undetected error propagate through the rest of the investigation]]

## How To Apply

Adopt [[techniques/Apply a phase-oriented multi-stage peer review structure to a digital forensic investigation]] (PARS) or an equivalent phased structure: identify the critical milestones in the organization's typical casework (e.g. after acquisition, after initial triage, after core analysis, before report drafting), assign an Advisor to review work at each milestone as it is reached, and reserve a final independent Review for the completed case. Use separate individuals for the Advisor and Reviewer roles to reduce workload concentration and cognitive bias, and formally define a dispute-resolution procedure so disagreements between the practitioner and Reviewer can be resolved without stalling the case.

## References

- [DFCite-1329] Sunde and Horsman, 2021, "Part 2: The Phase-oriented Advice and Review Structure (PARS) for digital forensic investigations", FSI: Digital Investigation 36, 301074.

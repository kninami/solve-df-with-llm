---
id: LWM-1307
type: mitigation
name: Precisely scope a tampering task's boundaries and pilot-test the description before running the full experiment
source_refs:
  - LWCite-1342
updated_at: 2026-08-15
status: complete
---

# Precisely scope a tampering task's boundaries and pilot-test the description before running the full experiment

## Summary

Before running a full tampering experiment, explicitly define what counts as satisfying the task and what does not (including edge cases such as wholesale deletion versus surgical alteration), and pilot-test the task description with a small number of participants to surface unanticipated interpretations before committing the full participant pool to the study.

## Addresses

- [[weaknesses/Ambiguous tampering-task descriptions in evidence-tampering experiments produce inconsistent participant interpretations]]

## How To Apply

When designing a study using [[techniques/Apply prudent design principles when conducting digital-evidence-tampering experiments]], write the task description to explicitly address boundary cases (e.g., for a "removal" task: does wholesale deletion of the relevant data category count, or is a narrower, more surgical alteration required?) rather than assuming a description that worked for a structurally different task (e.g. "addition") will translate without modification. Pilot-test the finalized description with a small number of participants — ideally drawn from the same pool as the intended full study — and review their interpretations and questions before running the full experiment, revising the description if pilot participants diverge in their understanding of the task's scope.

## References

- [LWCite-1342] Schneider, Düsel, Lorch, Drafz, and Freiling, 2022, "Prudent design principles for digital tampering experiments", FSI: Digital Investigation 40, 301334.

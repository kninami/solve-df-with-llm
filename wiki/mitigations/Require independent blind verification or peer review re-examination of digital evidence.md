---
id: LWM-1032
type: mitigation
name: Require independent blind verification or peer review re-examination of digital evidence
source_refs:
  - LWCite-1022
updated_at: 2026-08-09
status: complete
---

# Require independent blind verification or peer review re-examination of digital evidence

## Summary

Because consistency between examiners is not proof of validity and reliability between independent examiners analyzing the same evidence is otherwise low, build a formal verification step into casework where a second examiner independently re-examines the same evidence file (ideally without knowing the first examiner's conclusion) before a finding is finalized.

## Addresses

- [[weaknesses/Independent DF examiners reach low-reliability conclusions analyzing the same evidence file]]

## How To Apply

Implement quality-control measures such as verification reviews and re-examination of evidence by a second, independent examiner as a standard step for consequential findings, rather than treating a single examiner's conclusion as final. Where feasible, structure this as blind proficiency testing (e.g., using known test cases with a verified ground truth) to separately assess whether consistent results among examiners actually reflect accuracy, since consistent examiners can still be consistently wrong for the same underlying reason (e.g., a shared bias).

## References

- [LWCite-1022] Sunde and Dror, 2021, "A hierarchy of expert performance (HEP) applied to digital forensics: Reliability and biasability in digital forensics decision making", FSI: Digital Investigation 37.

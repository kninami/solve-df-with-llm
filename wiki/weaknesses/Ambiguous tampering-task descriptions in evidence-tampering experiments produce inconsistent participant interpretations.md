---
id: DFW-1305
type: weakness
name: Ambiguous tampering-task descriptions in evidence-tampering experiments produce inconsistent participant interpretations
description: A tampering-experiment task description that has not been precisely scoped is subject to varying subjective interpretation by different participants, and this ambiguity is easy to underestimate in advance, since a task description that reads as clear can turn out to admit dramatically different valid interpretations once participants actually attempt it.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1307
source_refs:
  - DFCite-1342
updated_at: 2026-08-15
status: complete
---

# Ambiguous tampering-task descriptions in evidence-tampering experiments produce inconsistent participant interpretations

## Summary

In the documented SFD1 experiment, changing a tampering task's framing from "add evidence of website accesses" to "remove evidence of website accesses" proved surprisingly ambiguous once formulated for real participants: does removing an entire browser history satisfy the task, or does a wiped hard disk, or does the task require a more surgical, harder-to-detect manipulation? The ambiguity was severe enough to force a mid-experiment change to the background story, after which participants held inconsistent understandings of what the task actually required.

## Why It Matters

A researcher whose tampering-experiment task description admits multiple valid interpretations risks collecting data that cannot be meaningfully compared across participants, since different participants effectively performed different tasks while believing they performed the same one. This directly threatens the study's internal validity and can force costly rework (re-running or modifying an experiment mid-course, as happened in SFD1), or worse, go unnoticed and produce misleading conclusions about tampering difficulty or detectability that do not actually reflect a single well-defined task.

## Related Mitigations

- [[mitigations/Precisely scope a tampering task's boundaries and pilot-test the description before running the full experiment]]

## Used By

- [[techniques/Apply prudent design principles when conducting digital-evidence-tampering experiments]]

## References

- [DFCite-1342] Schneider, Düsel, Lorch, Drafz, and Freiling, 2022, "Prudent design principles for digital tampering experiments", FSI: Digital Investigation 40, 301334.

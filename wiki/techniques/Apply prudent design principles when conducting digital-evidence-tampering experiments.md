---
id: DFT-1295
type: technique
name: Apply prudent design principles when conducting digital-evidence-tampering experiments
description: Design a controlled experiment that studies whether and how digital evidence can be successfully tampered with (and subsequently detected) by applying three lessons learned from evaluating past tampering studies and the researchers' own repeated attempts — accepting inherently small specialist-participant numbers rather than substituting unqualified participants at scale, formulating the tampering task with enough precision to eliminate subjective reinterpretation, and designing data collection so participant reasoning and reported factors can be systematically interpreted afterward.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1305
aliases:
  - Digital tampering experiment design lessons learned
source_refs:
  - DFCite-1342
updated_at: 2026-08-15
status: complete
---

# Apply prudent design principles when conducting digital-evidence-tampering experiments

## Summary

Empirically studying digital evidence tampering — whether forgeries can be successfully created and whether they can be detected — requires participants with specialized forensic knowledge, a well-defined tampering task, and data collected in a form that supports meaningful interpretation afterward. Reviewing several past tampering studies (including the researchers' own repeated attempts across multiple iterations) surfaced three recurring, avoidable design failures, each of which independently degraded or entirely prevented meaningful conclusions from being drawn.

## Details

**Lesson 1 — accept small numbers**: because tampering experiments require participants with specialized forensic skill, the pool of qualified professional participants is inherently small, and substituting students (a common past workaround) introduces its own problems — varying prior knowledge/experience/motivation that adds noise, and in several past studies, zero successful forgeries were produced at all, making quantitative success-rate analysis impossible. Attempting to scale up participant numbers via a Capture-the-Flag-style competitive "rodeo" format introduced new confounds (parallel/team-based work, guessing under time pressure, inconsistent effort-time measurement) that made results incomparable across studies; the paper concludes CTF-style contests are not a reliable route to more participants and recommends designing around small-N from the outset, e.g. by giving each participant multiple items to analyze and having each item examined by more than one participant to reduce noise. **Lesson 2 — account for the relativity of task definition**: a tampering task's description is inherently subject to participant interpretation, and this problem is easy to underestimate — changing a task from "add evidence of X" to "remove evidence of X" proved surprisingly ambiguous (does removing an entire browser history count, or does the manipulation need to be more surgical?), forcing a mid-experiment change to the task's background story and producing inconsistent participant knowledge levels that complicated data analysis; the lesson is to define precisely and unambiguously what the tampering task does and does not entail before the experiment begins, and not to assume a task description that worked for a different (e.g. "addition") task will translate cleanly to a superficially similar but structurally different (e.g. "removal") task. **Lesson 3 — data interpretation**: how and what data is collected during the experiment (timestamps, confidence levels, effort measures) must be designed with the intended analysis in mind from the start, since ad hoc or inconsistently-recorded measures (as encountered when trying to compare individual-participant effort values against team-based rodeo effort values) cannot be reconciled after the fact.

## Examples

- Reusing an existing tampering task description from a prior study, rather than carefully redesigning the description for a new (structurally different) task, directly caused the SFD1 experiment's task ambiguity problem — a cautionary example for future researchers tempted to reuse task descriptions across meaningfully different tampering tasks.
- Introducing a confidence-level field intended purely as a measure of participant decision certainty in SFD3 was found to have an unintended secondary effect (participants used it to maximize a competitive point multiplier rather than to honestly express uncertainty), illustrating how a data-collection design choice can distort the very data it was meant to capture.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Ambiguous tampering-task descriptions in evidence-tampering experiments produce inconsistent participant interpretations]]

## References

- [DFCite-1342] Schneider, Düsel, Lorch, Drafz, and Freiling, 2022, "Prudent design principles for digital tampering experiments", FSI: Digital Investigation 40, 301334.

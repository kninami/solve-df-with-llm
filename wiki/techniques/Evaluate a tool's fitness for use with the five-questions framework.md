---
id: LWT-1121
type: technique
name: Evaluate a tool's fitness for use with the five-questions framework
description: Systematically assess whether a digital forensic tool is appropriate to deploy in an examination by answering five linked questions covering its stated capability, required usage, underlying operation, tested reliability, and legal/ethical authorization, before relying on its output.
objective_ids:
  - DFO-1004
weakness_ids:
  - LWW-1126
aliases:
  - Five-questions tool-fitness framework
  - "'Can I use that tool?' decision framework"
source_refs:
  - LWCite-1120
updated_at: 2026-08-12
status: complete
---

# Evaluate a tool's fitness for use with the five-questions framework

## Summary

Deciding whether a given tool can be used for an examination task is often treated as trivial, but it actually requires unpacking hidden complexity around what the tool does, how it is used, why it produces the results it does, whether those results can be trusted, and whether its use is permitted. This technique formalizes that decision into five linked questions a practitioner should explicitly answer and document before deploying an unfamiliar or newly-encountered tool.

## Details

The five questions are: (1) "what does that tool do?"; (2) "how do I use that tool?"; (3) "how does the tool do it?"; (4) "does the tool do it properly?"; and (5) "should I use the tool?". Each carries named risks a practitioner must consciously address: subjective misinterpretation of a tool's stated capability; vague or missing vendor instructions; "Concept Compound Complexity" — where a tool's claimed functionality (e.g. "file carving") is itself a complex, multi-layered concept that must be fully unpacked (does it handle fragmented files? compressed structures?) rather than taken at face value; simply misunderstanding a tool due to gaps in the practitioner's own knowledge; an unfounded assumption that a tool can be used correctly without consulting its instructions; no, incomplete, or ineffective testing of the tool before relying on its output; and misunderstanding applicable legal, ethical, or organizational authorization requirements for the tool's use. The work distinguishes tool evaluation (assessing a tool's raw technical performance) from tool selection suitability (a wider appraisal of the tool, the practitioner's competence, and the investigative circumstances) — a tool can function correctly while still being unsuitable for a given case. Practitioners are encouraged to document their answers to all five questions so that the resulting decision to use (or not use) a tool is evidenced and defensible, not solely a matter of the tool "working" or being deployed "straight from its box."

## Examples

- A practitioner encountering a tool that claims to be able to "carve specific files" should determine exactly what that covers — whether it handles non-contiguous fragments, compressed structures, and which attributes are included in its output — rather than assume the vendor's high-level description matches the practitioner's actual investigative requirement.
- Before using a tool's results in casework, a practitioner checks whether the tool has undergone sufficiently comprehensive testing/validation (Question 4) and whether their organization's authorization or accreditation requirements permit its use for this task (Question 5), rather than proceeding on the assumption that "it works, so it must be fine."

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/Tool documentation gaps and insufficient testing lead practitioners to misunderstand or misapply a forensic tool's capability]]

## References

- [LWCite-1120] Horsman, 2024, "Commentary:- Can I use that tool?", FSI: Digital Investigation 51, 301843.

---
id: LWW-1031
type: weakness
name: Task-irrelevant contextual information biases DF examiner observations and conclusions
description: When digital forensic examiners are given contextual case information suggesting a suspect's likely guilt or innocence before analyzing an evidence file, the number and interpretation of traces they observe and report is measurably skewed toward confirming that suggested narrative, including for information that is task-irrelevant to the technical question at hand.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-1031
source_refs:
  - LWCite-1022
updated_at: 2026-08-09
status: complete
---

# Task-irrelevant contextual information biases DF examiner observations and conclusions

## Summary

In a controlled experiment, examiners given a "Guilt" context (Strong or Weak) observed more traces overall than those given an "Innocence" context, and the pattern of which traces were reported (found/not found) and how ambiguous traces were interpreted shifted measurably toward the suggested narrative — described in the study as "guilt framing" and "innocence framing" of the same underlying evidence file. A statistically significant effect of contextual information was found at the observation level (Kruskal-Wallis H(3) = 15.16, p < .05), though not at the interpretation or conclusion level in this particular dataset.

## Why It Matters

This means the same evidence file, examined by different examiners who received different (even task-irrelevant) case narratives beforehand, can yield reports that appear to confirm whatever narrative was already suggested — a serious threat to the objectivity that digital evidence examination is generally assumed to have. An examiner who believes a suspect is likely innocent may observe fewer traces and describe overlooked information as irrelevant, while one who believes the suspect is likely guilty may observe more traces and interpret ambiguous ones as incriminating, independent of what a neutral examination of the same file would find.

## Related Mitigations

- [[mitigations/Withhold task-irrelevant contextual information from DF examiners and manage context exposure]]

## Used By

- [[techniques/Review digital evidence guided by contextual case information]]

## References

- [LWCite-1022] Sunde and Dror, 2021, "A hierarchy of expert performance (HEP) applied to digital forensics: Reliability and biasability in digital forensics decision making", FSI: Digital Investigation 37.

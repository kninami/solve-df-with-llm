---
id: LWW-2125
type: weakness
name: LLM process-triage decision rules omit legitimate processes commonly abused by ransomware
description: A prompt-based process-triage decision ruleset that judges suspiciousness mainly from process naming and spawn relationships fails to flag legitimate Windows utilities (vssadmin.exe, vssvc.exe, cmd.exe) that ransomware invokes to delete shadow copies or run encryption batch scripts, because the ruleset contains no rule tied to that malicious usage pattern.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-2126
source_refs:
  - LWCite-2147
updated_at: 2026-08-16
status: complete
---

# LLM process-triage decision rules omit legitimate processes commonly abused by ransomware

## Summary

WannaCry and TeslaCrypt both invoke vssvc.exe (and TeslaCrypt additionally vssadmin.exe) to delete Volume Shadow Copies and prevent file recovery, and Vipasana invokes cmd.exe to run encryption batch scripts. In the reported evaluation, an LLM-based triage tool prompted with a decision rule set covering process naming, VAD permissions, and code-injection indicators consistently missed all of these processes as false negatives because none of its rules captured "legitimate process spawned by ransomware to perform a destructive action."

## Why It Matters

A false negative in ransomware process triage means the process responsible for destroying recovery options is never surfaced to the investigator for review, even though it was directly spawned by an already-identified malicious parent. Because the underlying model relies on the explanations and background knowledge supplied in the prompt rather than independent domain reasoning, any gap in the decision ruleset produces a systematic blind spot across every case that uses the same abused utility, rather than an isolated one-off miss.

## Related Mitigations

- [[mitigations/Expand LLM triage prompts with rules for legitimate utilities commonly abused by ransomware]]

## Used By

- [[techniques/Triage suspicious memory-resident processes using LLM decision-rule prompting]]

## References

- [LWCite-2147] Oh et al., 2024, "volGPT: Evaluation on triaging ransomware process in memory forensics with Large Language Model", FSI: Digital Investigation 49.

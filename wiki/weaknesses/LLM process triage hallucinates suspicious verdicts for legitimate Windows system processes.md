---
id: LWW-2124
type: weakness
name: LLM process triage hallucinates suspicious verdicts for legitimate Windows system processes
description: A large language model used for memory-forensic process triage sometimes flags a legitimate Windows system process (e.g. svchost.exe) as suspicious in violation of its own prompt instructions, and this fabricated verdict then cascades to every process spawned from the mislabeled parent.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-2125
source_refs:
  - LWCite-2147
updated_at: 2026-08-16
status: complete
---

# LLM process triage hallucinates suspicious verdicts for legitimate Windows system processes

## Summary

Despite explicit prompt instructions to treat known Windows system processes such as svchost.exe or explorer.exe as normal, the model occasionally hallucinates a suspicious verdict for one of them anyway. Because the tool's own decision rules treat "spawned from a suspicious process" as grounds for flagging a child process, one hallucinated parent verdict propagates suspicious labels to every legitimate child process spawned from it.

## Why It Matters

An investigator relying on the tool's triage list to prioritize manual review would be misdirected toward reviewing an entire subtree of legitimate processes while the confident, well-formatted natural-language explanation gives no indication that the root verdict was fabricated rather than rule-derived. The same underlying model behavior also produces false suspicious verdicts for processes whose 14-character-truncated or otherwise incomplete names resemble known-benign processes (e.g. "googlecrashhan", "trustedinstall") and for unknown processes with insufficient context (e.g. "defrag.exe", "wmpnetwk.exe"), inflating the reviewed set and eroding trust in the tool's output.

## Related Mitigations

- [[mitigations/Apply post-hoc allow-list verification to LLM-flagged suspicious processes]]

## Used By

- [[techniques/Triage suspicious memory-resident processes using LLM decision-rule prompting]]

## References

- [LWCite-2147] Oh et al., 2024, "volGPT: Evaluation on triaging ransomware process in memory forensics with Large Language Model", FSI: Digital Investigation 49.

---
id: LWT-2118
type: technique
name: Triage suspicious memory-resident processes using LLM decision-rule prompting
description: Extract process-list, VAD, and code-injection data from a memory dump via memory-forensics framework plugins, structure it as JSON, and prompt a large language model with domain-specific decision rules to flag suspicious processes and explain the reasoning in natural language.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-2124
  - LWW-2125
aliases:
  - volGPT
  - LLM-based ransomware process triage
source_refs:
  - LWCite-2147
updated_at: 2026-08-16
status: complete
---

# Triage suspicious memory-resident processes using LLM decision-rule prompting

## Summary

A memory-forensics plugin extracts process-list (PID, PPID, name), VAD-region permission, and code-injection indicator data from a memory dump, serializes it as JSON, and sends it to a large language model together with a persona ("you are a cyber investigator"), an explanation of the JSON schema, and a small decision ruleset (unusual process names, abnormal parent-child spawn relationships, executable-and-writable VAD regions, "MZ"/shellcode strings). The model returns, per process, a suspicious/not-suspicious verdict and a natural-language explanation of its reasoning.

## Details

The prompt is assembled from five components applied in sequence: a persona pattern, JSON-structured input with an explicit schema explanation, a written decision ruleset, and a fixed output template (process name, PID, reason). Because the underlying model's output is stochastic even at temperature 0, the tool executes the same prompt three times and takes the majority-vote result. The reported evaluation covered five ransomware families (WannaCry, TeslaCrypt, Cerber, Vipasana, HiddenTear) totaling 16,436 processes across 418 memory dumps, using ground-truth labels derived by intersecting the process list observed live during ransomware execution with the process list later recovered from the corresponding memory dump. This reduced the set of processes an investigator must manually review to roughly 10% of the total while reaching 94.1% overall triage accuracy, and — unlike purely classifier-based memory-triage approaches such as [[techniques/Classify malware features extracted from memory dumps]] that only label an entire memory dump as malicious/benign — it identifies which individual processes are suspicious and supplies a rationale for each verdict.

## Examples

- volGPT: GPT-3.5-turbo prompted with pslist/vadinfo/malfind output from Volatility 3, achieving 87-99% accuracy per ransomware family and correctly explaining VAD-region PAGE_EXECUTE_READWRITE and embedded "MZ"/API-name findings for the Cerber sample.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/LLM process triage hallucinates suspicious verdicts for legitimate Windows system processes]]
- [[weaknesses/LLM process-triage decision rules omit legitimate processes commonly abused by ransomware]]

## References

- [LWCite-2147] Oh et al., 2024, "volGPT: Evaluation on triaging ransomware process in memory forensics with Large Language Model", FSI: Digital Investigation 49.

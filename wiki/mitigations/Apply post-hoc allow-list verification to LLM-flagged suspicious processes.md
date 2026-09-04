---
id: LWM-2125
type: mitigation
name: Apply post-hoc allow-list verification to LLM-flagged suspicious processes
source_refs:
  - LWCite-2147
updated_at: 2026-08-16
status: complete
---

# Apply post-hoc allow-list verification to LLM-flagged suspicious processes

## Summary

After an LLM-based triage pass flags a process as suspicious, cross-check the flagged process name (and its normalized/de-truncated form) against a maintained allow-list of known-legitimate Windows system processes before including it in the reviewed set, and re-evaluate any child process whose only basis for suspicion is a flagged parent.

## Addresses

- [[weaknesses/LLM process triage hallucinates suspicious verdicts for legitimate Windows system processes]]

## How To Apply

Maintain a reference list of legitimate Windows process names (including their common 14-character EPROCESS-truncated forms) and run it against every LLM-flagged verdict before presenting results to the investigator; treat "flagged only because its parent was flagged" as a lower-confidence tier requiring separate confirmation (e.g. independent VAD or code-injection evidence) rather than accepting the cascading verdict at face value. Tightening the prompt's own conditions for what counts as an anomalous system process (stricter phrasing, explicit examples) can reduce the hallucination rate but does not eliminate the need for independent verification.

## References

- [LWCite-2147] Oh et al., 2024, "volGPT: Evaluation on triaging ransomware process in memory forensics with Large Language Model", FSI: Digital Investigation 49.

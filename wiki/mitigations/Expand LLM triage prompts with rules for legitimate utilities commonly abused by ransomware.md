---
id: DFM-2126
type: mitigation
name: Expand LLM triage prompts with rules for legitimate utilities commonly abused by ransomware
source_refs:
  - DFCite-2147
updated_at: 2026-08-16
status: complete
---

# Expand LLM triage prompts with rules for legitimate utilities commonly abused by ransomware

## Summary

Add explicit decision-rule entries and background knowledge to an LLM process-triage prompt for legitimate Windows utilities known to be abused by ransomware for destructive purposes (e.g. vssadmin.exe and vssvc.exe for shadow-copy deletion, cmd.exe for running encryption batch scripts), so that "spawned by a flagged parent to perform a known-destructive action" becomes an explicit rule rather than relying on the model's unguided inference.

## Addresses

- [[weaknesses/LLM process-triage decision rules omit legitimate processes commonly abused by ransomware]]

## How To Apply

Curate and periodically update a list of legitimate-but-frequently-abused utilities and the malicious usage patterns associated with them (specific command-line arguments, parent-process context) and encode them as additional rows in the triage ruleset supplied to the model; validate rule coverage against a labelled ransomware-family dataset before relying on the expanded ruleset operationally, since gaps in the ruleset produce systematic rather than isolated false negatives.

## References

- [DFCite-2147] Oh et al., 2024, "volGPT: Evaluation on triaging ransomware process in memory forensics with Large Language Model", FSI: Digital Investigation 49.

---
id: DFT-1112
type: technique
name: Generate forensic analysis scripts using a general-purpose LLM
description: Prompt a general-purpose large language model (e.g. GPT-4) to write a working script for a specific digital forensic task — such as file carving, RAID disk acquisition, password-protected archive cracking, or memory-dump encryption-key search — to provide an investigator with a functional starting point instead of building the tool from scratch.
objective_ids:
  - DFO-1004
weakness_ids:
  - DFW-1117
aliases:
  - LLM-assisted forensic script generation
  - ChatGPT/GPT-4 code generation for digital forensics
source_refs:
  - DFCite-1110
updated_at: 2026-08-12
status: complete
---

# Generate forensic analysis scripts using a general-purpose LLM

## Summary

Digital forensic investigations often require a bespoke script for a task not covered by existing tooling, or for a resource-limited live scenario. Prompting a general-purpose LLM to generate the script, then iteratively refining the prompt and correcting the model's own output, can produce a well-commented, functional first draft far faster than writing it unassisted, though the investigator must already have enough domain and scripting knowledge to validate the result.

## Details

Across four tested scenarios, GPT-4 produced progressively refined scripts through iterative prompting: a file-carving script that initially used a filesystem-walking library (missing the point of carving unallocated space) was corrected, on request for a "more pragmatic" approach, into a byte-sequence PDF-header/EOF-signature scanner; a RAID disk-acquisition script determined the RAID level from the first of several mounted, write-blocked SSDs and used it to assemble and image the array; a password-cracking script for an encrypted zip file initially refused as "unethical" but, after the request was broken into smaller sub-steps, produced a dictionary-attack script iterating candidate password lists; and a memory-dump analysis script searched for byte sequences of a target entropy to locate AES/RSA/BitLocker encryption keys, refined on request to target a specific tool's (Volatility) profile-based key-extraction approach. In each case the model provided commented, syntactically correct code and could explain its own design choices when asked, but consistently required a domain-knowledgeable user to catch unstated or unreasonable assumptions in the generated logic.

## Examples

- A GPT-4-generated RAID acquisition script determined the array's RAID level from only the first of four mounted disk images and applied that level to all four without independently verifying disk-count consistency or validating the level against the other three disks.

## Related Objectives

- `DFO-1004` Conduct research

## Related Weaknesses

- [[weaknesses/LLM-generated forensic scripts can embed unvalidated technical assumptions that silently produce incorrect results]]

## References

- [DFCite-1110] Scanlon et al., 2023, "ChatGPT for digital forensic investigation: The good, the bad, and the unknown", FSI: Digital Investigation 46.

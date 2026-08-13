---
id: DFM-1117
type: mitigation
name: Independently verify LLM-generated forensic script assumptions against corroborating evidence before relying on results
source_refs:
  - DFCite-1110
updated_at: 2026-08-12
status: complete
---

# Independently verify LLM-generated forensic script assumptions against corroborating evidence before relying on results

## Summary

Before relying on an LLM-generated forensic script's output, read through the generated logic to identify every technical assumption it makes, and independently verify each one against the actual evidence rather than trusting that the script's successful execution implies its assumptions were correct.

## Addresses

- [[weaknesses/LLM-generated forensic scripts can embed unvalidated technical assumptions that silently produce incorrect results]]

## How To Apply

Review a generated script line by line for any point where it infers a configuration parameter, file format, or data structure from a subset of the available evidence and then applies that inference more broadly (e.g. a RAID level determined from one disk applied to an entire array). For each such assumption, independently verify it against the full evidence set before trusting the script's output, and only proceed with an investigator who has sufficient domain and scripting knowledge to recognize when a generated approach is technically unreasonable for the specific case at hand.

## References

- [DFCite-1110] Scanlon et al., 2023, "ChatGPT for digital forensic investigation: The good, the bad, and the unknown", FSI: Digital Investigation 46.

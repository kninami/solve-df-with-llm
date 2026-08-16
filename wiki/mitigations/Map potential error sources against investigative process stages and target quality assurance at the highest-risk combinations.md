---
id: DFM-2080
type: mitigation
name: Map potential error sources against investigative process stages and target quality assurance at the highest-risk combinations
source_refs:
  - DFCite-2090
updated_at: 2026-08-16
status: complete
---

# Map potential error sources against investigative process stages and target quality assurance at the highest-risk combinations

## Summary

Build and maintain an explicit map of which of the six error sources (client, wider investigative team, practitioner, tools/instruments, methods, trace) can plausibly introduce an error at each stage of an organization's digital forensic investigative process, and prioritize quality-assurance and error-mitigation measures at the stage/source combinations judged highest-risk, rather than focusing quality assurance on tool validation alone.

## Addresses

- [[weaknesses/Errors from client, team, practitioner, tool, method, and trace sources are not systematically tracked across investigative process stages]]

## How To Apply

Walk through an organization's own investigative process stages (from initial client request through to giving evidence) and, for each stage, explicitly consider all six error sources rather than only tools/instruments: could the client's brief be incomplete or misleading at this stage; could the wider investigative team have mishandled the exhibit before this stage; could the practitioner's own manual interpretation introduce error here; could a tool bug affect this stage; could the chosen method be inappropriate for the question being asked at this stage; and could the trace itself be inherently ambiguous or already corrupted going into this stage. Use [[techniques/Decompose forensic analysis tool internals into abstraction-layer stages to identify errors]] for the tools/instruments source specifically, and layer targeted procedural controls (e.g. brief-verification checklists, exhibit-handling audits, peer review, method-selection justification) onto whichever stage/source combinations the mapping identifies as highest-risk for the organization's typical casework.

## References

- [DFCite-2090] Horsman, 2024, "Sources of error in digital forensics", FSI: Digital Investigation 48, 301693.

---
id: DFM-2119
type: mitigation
name: Periodically update CSAM naming-pattern libraries and apply baseline content-level scanning even to low-priority-scored files
source_refs:
  - DFCite-2138
updated_at: 2026-08-16
status: complete
---

# Periodically update CSAM naming-pattern libraries and apply baseline content-level scanning even to low-priority-scored files

## Summary

Maintain and periodically update the naming/structuring pattern library used for CSAM detection prioritization with newly identified conventions from ongoing casework, and ensure files/folders that do not match any known pattern still receive some baseline level of content-level scanning rather than being effectively deprioritized out of the computational budget entirely.

## Addresses

- [[weaknesses/File and folder naming heuristics for CSAM detection cannot recognize deliberately disguised or novel naming conventions]]

## How To Apply

Establish a feedback process for adding newly observed CSAM-distribution naming and structuring conventions to the pattern library as they are identified in ongoing investigations, so the prioritization heuristic's coverage improves over time rather than remaining static. Ensure the prioritization scheme still allocates some non-zero scanning budget to files and folders that do not match any known pattern -- for example, via periodic random sampling of low-priority-scored content -- rather than treating a non-match as equivalent to a confirmed-benign determination. Treat the naming/structuring heuristic strictly as a resource-allocation aid that speeds up finding known-pattern content faster, not as a filter that reduces the scope of what ultimately needs review.

## References

- [DFCite-2138] "Using file and folder naming and structuring to improve automated detection of child sexual abuse images on the Dark Web", FSI: Digital Investigation 48, 2024.

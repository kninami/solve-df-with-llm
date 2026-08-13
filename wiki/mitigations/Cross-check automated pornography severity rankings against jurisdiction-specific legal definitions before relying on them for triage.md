---
id: DFM-1153
type: mitigation
name: Cross-check automated pornography severity rankings against jurisdiction-specific legal definitions before relying on them for triage
source_refs:
  - DFCite-1156
updated_at: 2026-08-12
status: complete
---

# Cross-check automated pornography severity rankings against jurisdiction-specific legal definitions before relying on them for triage

## Summary

Treat an automated severity ranking as a relative sorting aid for building a review queue, not as a validated harmfulness classification, and confirm how the applicable jurisdiction or agency legally or operationally defines pornographic-content severity before using the ranking to make prioritization or charging-relevant decisions.

## Addresses

- [[weaknesses/Pornographic content severity ranking relies on a non-standardized, unvalidated severity scale]]

## How To Apply

Use the ranked worklist to decide review order among flagged content, but have a human reviewer confirm the actual severity/legal classification of any item before it informs a charging or prioritization decision, rather than accepting the automated severity label directly. Where an agency has its own severity or grading framework, map the tool's object-category-based severity levels to that framework explicitly (and document the mapping) rather than assuming the tool's four-level scale is equivalent.

## References

- [DFCite-1156] Borg et al., 2022, "Detecting and ranking pornographic content in videos", FSI: Digital Investigation 42-43.

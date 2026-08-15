---
id: DFM-2003
type: mitigation
name: Corroborate unusual-traffic detector triggers with the unexpected-behavior state detector before full DFIR acquisition
source_refs:
  - DFCite-2003
updated_at: 2026-08-14
status: partial
---

# Corroborate unusual-traffic detector triggers with the unexpected-behavior state detector before full DFIR acquisition

## Summary

Do not let a single AI traffic classification alone initiate full, resource-intensive DFIR evidence acquisition; require corroboration from the independent, multi-source, consensus-based unexpected-behavior state detector (or additional network health statistics) before escalating a flagged event to full forensic processing.

## Addresses

- [[weaknesses/An SDN unusual-traffic detector's imperfect recall on usual traffic triggers unnecessary forensic evidence acquisition]]

## How To Apply

Configure the filtering, acquisition, and treatment engine to treat an unusual-traffic classification as a provisional flag rather than an automatic full-scale trigger, and use the incident response engine's own filter-effectiveness evaluation (statistical traffic values, response-engine activation frequency, network health statistics before/after incidents) to periodically retrain or threshold-tune the classifier for better usual-class recall.

## References

- [DFCite-2003] Jiménez et al., 2024 — the architecture's own Event Correlation Module and Incident Response Engine already evaluate and forward "filter revisions" based on observed filter effectiveness, providing the feedback mechanism this mitigation relies on.

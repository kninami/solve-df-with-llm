---
id: LWW-2003
type: weakness
name: An SDN unusual-traffic detector's imperfect recall on usual traffic triggers unnecessary forensic evidence acquisition
description: An AI-based unusual-traffic detector used to trigger SDN forensic evidence gathering can misclassify a meaningful share of genuinely benign ("usual") traffic as unusual, causing the DFIR pipeline to acquire and preserve evidence for events that are not actually security incidents.
categories:
  - ASTM_INAC_EX
mitigation_ids:
  - LWM-2003
source_refs:
  - LWCite-2003
updated_at: 2026-08-14
status: partial
---

# An SDN unusual-traffic detector's imperfect recall on usual traffic triggers unnecessary forensic evidence acquisition

## Summary

The source paper's own evaluation shows the usual-traffic class achieving only 77% recall on average (76.2% of all instances correctly classified for the usual class across folds), which the authors explicitly flag as an area with "room for improvement." Since a positive (unusual) classification is what triggers DFIR evidence acquisition and stakeholder notification, misclassified usual traffic results in evidence being gathered, timestamped, and forwarded to the forensic processing engine for events that were never actually security incidents.

## Why It Matters

Repeated false-positive triggers dilute the forensic record with non-relevant data, undermining the filtering model's core purpose of reducing storage and analysis burden, and can desensitize incident responders to detector alerts over time (alert fatigue), risking slower response to genuine incidents. Because the ephemeral event registry retains data only until verified and consolidated, frequent false triggers also increase system load on the SDN controller and forensic pipeline components.

## Related Mitigations

- [[mitigations/Corroborate unusual-traffic detector triggers with the unexpected-behavior state detector before full DFIR acquisition]]

## Used By

- [[techniques/Trigger SDN forensic evidence collection using unusual-traffic and unexpected-behavior detectors]]

## References

- [LWCite-2003] Jiménez et al., 2024 — Table 4 reports 76.2% average accuracy and 77% average recall for the usual-traffic class, with the authors' own conclusion noting room for recall improvement.

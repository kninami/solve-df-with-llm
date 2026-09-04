---
id: LWW-2002
type: weakness
name: A feature-scoring toolkit ranking that weights all features equally can misrank the best tool for a case's actual priorities
description: A feature-scoring model that gives every supported feature the same point value produces a single overall ranking that does not reflect that a specific feature may be essential in one case and irrelevant in another, potentially recommending a toolkit that is not actually best suited to the case at hand.
categories:
  - ASTM_MISINT
mitigation_ids:
  - LWM-2002
source_refs:
  - LWCite-2002
updated_at: 2026-08-14
status: partial
---

# A feature-scoring toolkit ranking that weights all features equally can misrank the best tool for a case's actual priorities

## Summary

The source survey's own Feature Scoring Model explicitly assigns each domain feature 2 points if supported and 0 if not, with equal weighting across all features, acknowledging that "one feature may be necessary in one case while another may not be important" but treating all features equally regardless. A toolkit that excels at case-critical features (e.g. RAID reconstruction in a multi-disk case) but lacks a few unimportant ones can therefore be outranked by a toolkit that broadly supports many low-priority features.

## Why It Matters

An investigator who selects a toolkit purely from an equal-weighted overall FSM percentage, without checking whether the case's specific evidentiary needs are among the weighted-down or missing features, risks choosing a toolkit that cannot perform a task the case actually requires (e.g. picking a toolkit that scores well overall for file-system forensics but lacks RAID reconstruction for a case involving a striped array). This is a misinterpretation risk: the aggregate score is read as "best overall" when it does not represent "best for this case."

## Related Mitigations

- [[mitigations/Re-weight or filter feature-scoring toolkit rankings by the specific case's required features before selecting a tool]]

## Used By

- [[techniques/Select a forensic toolkit using a domain-specific feature-scoring model]]

## References

- [LWCite-2002] Javed et al., 2022 — states the FSM's equal-weighting design choice and its acknowledged case-dependent-importance limitation directly in Section IV.

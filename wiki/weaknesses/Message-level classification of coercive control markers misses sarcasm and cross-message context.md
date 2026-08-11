---
id: DFW-1034
type: weakness
name: Message-level classification of coercive control markers misses sarcasm and cross-message context
description: A classifier that evaluates each chat message independently, without broader conversational context, both misclassifies sarcastic literal-sounding messages as genuine markers of abuse (false positives) and fails to flag messages whose abusive character only becomes apparent when combined with information from an earlier, non-adjacent message (false negatives).
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1034
source_refs:
  - DFCite-1024
updated_at: 2026-08-09
status: complete
---

# Message-level classification of coercive control markers misses sarcasm and cross-message context

## Summary

A manual review of the model's test-set failures identified two primary error categories, both rooted in the same single-message-analysis limitation. False positives from sarcasm: a message like "Wow, another brilliant idea from the genius over here" was flagged as Grandiosity (T1) because the classifier mistook sarcastic praise for a literal statement. False negatives from context-shifting: a message such as "I'm with James from the firm now" was missed as Arrogance (T9), even though it contextually amplified an arrogant remark from several messages earlier ("I'm not coming, you're ruining the mood"), because the connection between the two messages was not evaluated.

## Why It Matters

Coercive control is specifically defined as a cumulative, longitudinal pattern rather than a single incident, so a classifier's inability to track meaning across message boundaries directly undermines the pipeline's core purpose. False positives from sarcasm risk misdirecting limited investigator review time toward benign exchanges, while false negatives from context-shifting risk omitting genuinely relevant messages from the triage report, understating the true frequency of a linguistic pattern relevant to establishing coercive control. The paper explicitly frames this as reinforcing "the absolute necessity of a Human-in-the-Loop (HITL) to manually verify all flagged messages."

## Related Mitigations

- [[mitigations/Present flagged messages with surrounding conversational context for human-in-the-loop review]]

## Used By

- [[techniques/Hybrid regex-BERT longitudinal linguistic-marker triage of chat evidence]]

## References

- [DFCite-1024] Patel et al., 2026, "A hybrid neural-symbolic approach for the longitudinal profiling of coercive control in digital investigations", FSI: Digital Investigation 56.

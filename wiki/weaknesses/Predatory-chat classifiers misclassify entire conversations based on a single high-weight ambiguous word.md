---
id: DFW-1169
type: weakness
name: Predatory-chat classifiers misclassify entire conversations based on a single high-weight ambiguous word
description: A supervised text classifier trained to detect sexual predatory conversation can flip an entire conversation's label because of a single word or short phrase carrying a high feature weight, producing both false positives (an innocuous conversation flagged as predatory) and false negatives (a genuinely predatory conversation missed) without any visible indication that the decision hinged on one ambiguous token.
categories:
  - ASTM_INCOMP
  - ASTM_MISINT
mitigation_ids:
  - DFM-1169
source_refs:
  - DFCite-1174
updated_at: 2026-08-12
status: complete
---

# Predatory-chat classifiers misclassify entire conversations based on a single high-weight ambiguous word

## Summary

Because a word or phrase can carry a high classification weight for one class while appearing legitimately in conversations of the other class, a single ambiguous token can dominate a model's prediction for an entire conversation, causing the model to state a confident but wrong verdict.

## Why It Matters

A non-predatory conversation containing the word "May" (the sender's name in one documented example) was misclassified as predatory with 0.594 probability, while a genuinely predatory conversation containing the informal contraction "u're" was missed with only 0.41 probability. Without inspecting which tokens actually drove a given prediction, an investigator using the model's bare output risks flagging innocent conversations for further scrutiny or, more seriously, overlooking genuinely predatory conversations that the model happened to score just below threshold because of one misleading word.

## Related Mitigations

- [[mitigations/Trace individual token contribution to an ML predatory-chat classification before treating it as confirmed evidence]]

## Used By

- [[techniques/Classify chat conversations as sexual predatory using supervised machine learning within a digital forensic process model]]

## References

- [DFCite-1174] Ngejane et al., 2021, "Digital forensics supported by machine learning for the detection of online sexual predatory chats", FSI: Digital Investigation 36, 301109.

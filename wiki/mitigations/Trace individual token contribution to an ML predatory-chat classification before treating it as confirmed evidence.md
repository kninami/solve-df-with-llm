---
id: LWM-1169
type: mitigation
name: Trace individual token contribution to an ML predatory-chat classification before treating it as confirmed evidence
source_refs:
  - LWCite-1174
updated_at: 2026-08-12
status: complete
---

# Trace individual token contribution to an ML predatory-chat classification before treating it as confirmed evidence

## Summary

Before an investigator relies on an ML predatory-chat classifier's verdict for a conversation, use a per-word perturbation-analysis tool to identify which specific word or phrase drove the prediction probability, and confirm the classification still holds once ambiguous high-weight tokens are accounted for.

## Addresses

- [[weaknesses/Predatory-chat classifiers misclassify entire conversations based on a single high-weight ambiguous word]]

## How To Apply

Run each word or n-gram in a flagged (or borderline) conversation individually through the model and record its prediction probability, using a tool such as Google's What-If Tool to visualize and manipulate data points interactively. Where removing or altering a single ambiguous token flips the conversation's label, treat the original classification as unconfirmed and route the conversation for manual review rather than accepting the model's output at face value.

## References

- [LWCite-1174] Ngejane et al., 2021, "Digital forensics supported by machine learning for the detection of online sexual predatory chats", FSI: Digital Investigation 36, 301109.

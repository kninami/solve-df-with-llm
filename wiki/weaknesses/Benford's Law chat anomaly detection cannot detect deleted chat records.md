---
id: LWW-1097
type: weakness
name: Benford's Law chat anomaly detection cannot detect deleted chat records
description: Because the technique analyzes the leading-digit distribution of timestamps and message lengths present in an exported chat, it has no mechanism for detecting messages that have been deleted from the conversation entirely, since a deleted record leaves no leading digit in the dataset at all to deviate from the expected distribution.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1097
source_refs:
  - LWCite-1090
updated_at: 2026-08-10
status: complete
---

# Benford's Law chat anomaly detection cannot detect deleted chat records

## Summary

The paper states this limitation directly in its own summary of findings: "Record deletion is not detectable using this method." The technique's anomaly signal depends entirely on the statistical distribution of values that are present in the exported chat data; a record that no longer exists in that export contributes nothing to the distribution and therefore cannot trigger a deviation.

## Why It Matters

An investigator relying on this technique to identify tampering or fraud risk should not interpret a "clean" (Benford-conforming) result as evidence that no messages were deleted from the conversation — the two are unrelated questions, and a chat that has had incriminating messages selectively deleted could still show a perfectly normal leading-digit distribution for the messages that remain.

## Related Mitigations

- [[mitigations/Pair Benford's Law chat anomaly detection with dedicated deleted-message recovery techniques]]

## Used By

- [[techniques/Detect chat message anomalies using Benford's Law leading-digit analysis]]

## References

- [LWCite-1090] Mahindra and Karabiyik, 2026, "Benford's Law as a Forensic Tool for Identifying Anomalous Chat Behavior in Instant Messaging", IEEE SmartNets 2026.

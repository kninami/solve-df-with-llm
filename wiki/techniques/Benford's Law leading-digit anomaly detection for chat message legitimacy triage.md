---
id: DFT-1091
type: technique
name: Benford's Law leading-digit anomaly detection for chat message legitimacy triage
description: Triage a large collection of instant-messaging chat conversations for spam, AI-chatbot-generated, or otherwise artificial content by extracting the leading digit of each message's timestamp and character-length values, comparing the resulting frequency distribution against the expected Benford's Law distribution (where "1" is the most common leading digit, with decreasing frequency thereafter) using a chi-squared significance test, and flagging chats whose distribution deviates substantially for further manual investigation.
objective_ids:
  - DFO-1019
weakness_ids:
  - DFW-1097
aliases: []
source_refs:
  - DFCite-1090
updated_at: 2026-08-10
status: complete
---

# Benford's Law leading-digit anomaly detection for chat message legitimacy triage

## Summary

With an ever-increasing number of instant messaging apps and no established method to categorize suspicious conversations at scale, applying Benford's Law — previously used in forensic accounting, election-fraud detection, and cryptocurrency-ledger analysis — to the leading digits of chat timestamps and message character lengths gives a lightweight, largely automatable first-pass signal for which chats warrant closer manual review.

## Details

Three chat types were evaluated: a legitimate two-party conversation, a spam-message chat, and an AI SMS-chatbot session, each exported via Magnet AXIOM. Legitimate chat message-length data followed the Benford distribution closely (with an interpretable exception attributable to common short-sentence lengths), while spam-chat message lengths showed significant deviation attributable to either long advertisement text or very brief alert-style messages, and bot-chat message lengths lacked the expected high frequency of leading digit "1" — a distinguishing signature the authors suggest may be specific to bot-generated content. Two indicators flag a deviation for investigation: absence of "1" as the most common leading digit, and a visible spike rather than the expected smoothly decreasing frequency curve; a chi-squared test assesses whether an observed deviation is statistically significant.

## Examples

- The bot chat's message-length leading-digit distribution lacked the high frequency of "1" characteristic of both the legitimate and spam chats, distinguishing it as a candidate signature for identifying AI-chatbot-generated conversations specifically, separate from generic spam detection.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Benford's Law chat anomaly detection cannot detect deleted chat records]]

## References

- [DFCite-1090] Mahindra and Karabiyik, 2026, "Benford's Law as a Forensic Tool for Identifying Anomalous Chat Behavior in Instant Messaging", IEEE SmartNets 2026.

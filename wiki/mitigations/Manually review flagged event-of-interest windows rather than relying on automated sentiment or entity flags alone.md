---
id: DFM-2077
type: mitigation
name: Manually review flagged event-of-interest windows rather than relying on automated sentiment or entity flags alone
source_refs:
  - DFCite-2082
updated_at: 2026-08-16
status: complete
---

# Manually review flagged event-of-interest windows rather than relying on automated sentiment or entity flags alone

## Summary

Treat automated sentiment-, volume-, and lexical-diversity-based "event of interest" flags in a messaging-conversation review tool as a triage aid that narrows down which time windows to read, not as a substitute for an investigator directly reading the flagged messages before drawing a conclusion.

## Addresses

- [[weaknesses/Sentiment and named-entity models trained for general text misjudge short, informal messaging text]]

## How To Apply

When a time-series-based conversation-review tool flags a period as an event of interest (via sentiment extremes, volume spikes, or lexical-diversity shifts), read the underlying messages in and around that window directly rather than accepting the automated label at face value, giving particular scrutiny to messages the sentiment model would classify as neutral, since this is typically the least reliably classified class. Periodically spot-check a sample of unflagged periods as well, to gauge how often the classifier is missing genuinely relevant periods (false negatives) in addition to over-flagging irrelevant ones.

## References

- [DFCite-2082] Harris, Jacobson, and Provetti, 2024, "Sentiment and time-series analysis of direct-message conversations", FSI: Digital Investigation 49, 301753.

---
id: LWM-1216
type: mitigation
name: Correlate conversational AI records across platforms using content and timestamps in addition to conversation ID
source_refs:
  - LWCite-1226
updated_at: 2026-08-13
status: complete
---

# Correlate conversational AI records across platforms using content and timestamps in addition to conversation ID

## Summary

When reconciling a user's conversational AI activity across Android, iOS, and cloud-export copies, cross-check candidate matches using message content, timestamps, and model/metadata rather than relying on the conversation GUID alone as the sole join key.

## Addresses

- [[weaknesses/Conversation identifiers for the same conversational AI exchange can diverge across a user's client platforms and cloud export]]

## How To Apply

Join conversation records across sources primarily by conversation ID, but flag conversations that appear on one platform with no ID match elsewhere as candidates for manual review rather than concluding they are unique to that platform. For flagged candidates, compare message timestamps, prompt/response text, and any voice-chat-specific metadata to determine whether an apparently ID-mismatched conversation on a different platform is in fact the same underlying exchange, giving particular attention to voice-chat sessions, where the source study found this divergence occurred most often. Document any content-based (rather than ID-based) correlations explicitly in the examination notes, since they rely on interpretive judgment rather than a direct identifier match.

## References

- [LWCite-1226] Dragonas et al., 2024, "Forensic analysis of OpenAI's ChatGPT mobile application", FSI: Digital Investigation 50, 301801.

---
id: DFW-1216
type: weakness
name: Conversation identifiers for the same conversational AI exchange can diverge across a user's client platforms and cloud export
description: The GUID-format identifier assigned to a single conversational AI conversation is usually consistent across a user's Android app, iOS app, and cloud export copies of that conversation, but for some conversations (most often voice-chat sessions) the same underlying conversation is recorded under a different ID on one platform than on the others, for reasons the source study could not determine.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-1216
source_refs:
  - DFCite-1226
updated_at: 2026-08-13
status: complete
---

# Conversation identifiers for the same conversational AI exchange can diverge across a user's client platforms and cloud export

## Summary

Across the study's three-month testing period, most of a user's conversations retained the same GUID-format conversation ID whether examined via the Android app's SQLite database, the iOS app's JSON conversation files, or the account's cloud data export, but a subset of conversations — occurring mostly with voice chat — had the same content recorded under a different ID on iOS than on Android and in the cloud export, with the underlying cause left unresolved.

## Why It Matters

An investigator who correlates a suspect's conversational AI activity across devices and cloud data by matching on conversation ID alone risks either failing to link related evidence (treating what is actually the same conversation, recorded under two different IDs, as two unrelated conversations) or, conversely, risks a wrong linkage if IDs happen to collide for an unrelated reason. Because the divergence is not fully understood and its scope is limited to a subset of cases (predominantly voice chat) in the underlying study, a naive ID-based join cannot be assumed reliable for a complete cross-platform reconstruction.

## Related Mitigations

- [[mitigations/Correlate conversational AI records across platforms using content and timestamps in addition to conversation ID]]

## Used By

- [[techniques/Collect conversational AI artifacts across cloud export, desktop cache, browser cache, and mobile app storage]]

## References

- [DFCite-1226] Dragonas et al., 2024, "Forensic analysis of OpenAI's ChatGPT mobile application", FSI: Digital Investigation 50, 301801.

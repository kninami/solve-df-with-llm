---
id: LWW-1214
type: weakness
name: VoIP call activity within a messaging app is not recorded in the app's local chat database
description: A messaging app that offers VoIP audio/video calling as a feature may not log call events (initiation, duration, participants, missed/received status) anywhere in its local chat database or elsewhere on the device file system, leaving no forensic record that a call occurred even though the app's own user interface displays no call history either.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1214
source_refs:
  - LWCite-1225
updated_at: 2026-08-13
status: complete
---

# VoIP call activity within a messaging app is not recorded in the app's local chat database

## Summary

Both audio and video VoIP calls were initiated between the local user and contacts using Siskin IM during testing, but no corresponding record appeared in the `siskinim_main.db` database, in any other identified user-data location on the iOS file system, or in the app's own chat-window call history — confirmed further by a file-system extraction using the checkm8 exploit chain, which still returned no call-log data.

## Why It Matters

An investigator examining an app's database for evidence of VoIP call activity between a suspect and a contact may conclude no calls occurred, when in fact the absence of a database record simply reflects the app's failure to log calls at all rather than an absence of communication. This creates a specific gap for apps offering VoIP functionality: chat message evidence may be complete while an entire communication modality (voice/video calls) is invisible to database-level analysis.

## Related Mitigations

- [[mitigations/Corroborate suspected in-app VoIP call activity using network or OS-level artifacts]]

## Used By

- [[techniques/Extract OMEMO-encrypted XMPP chat artifacts from iOS multi-client SQLite databases]]

## References

- [LWCite-1225] Akinbi and Ojie, 2021, "Forensic analysis of open-source XMPP multi-client social networking apps on iOS devices", FSI: Digital Investigation 36.

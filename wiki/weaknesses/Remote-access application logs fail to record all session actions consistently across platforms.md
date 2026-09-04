---
id: LWW-1151
type: weakness
name: Remote-access application logs fail to record all session actions consistently across platforms
description: A remote-access application's log files record only a subset of the actions performed during a session, omitting others (such as issued commands, exchanged credentials, or thumbnail/wallpaper data) and recording a different subset on each platform, so relying on log files alone understates the true extent of session activity.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1151
source_refs:
  - LWCite-1148
updated_at: 2026-08-12
status: complete
---

# Remote-access application logs fail to record all session actions consistently across platforms

## Summary

A study of TeamViewer across Windows and Android found that although several distinct commands and interactions were exercised during a session — nudges, screenshot requests, uninstallation commands, clipboard interactions, and chat conversations — only the nudge command appeared consistently in the session log file (`TeamViewer15_Logfile.log`/`TVLog.html`); email addresses, email passwords, dynamic session passwords, and installed-application information were also conspicuously absent from the logs despite being present elsewhere (registry, memory, or clipboard artifacts). The set of actions and detail recorded also differed between the Windows and Android sides of the same session.

## Why It Matters

An investigator who treats a remote-access application's own log file as a complete record of what happened during a session risks materially understating the session's actual scope — for example, concluding that no file transfer, credential exchange, or uninstall command occurred simply because the log is silent on it, when the log file's own documented behavior is to omit exactly those categories of action. Because the omitted categories differ from what the same application logs on its other supported platform, an examiner working from only one side's log risks an even more incomplete picture than either side alone would suggest.

## Related Mitigations

- [[mitigations/Corroborate remote-access session activity using memory and cross-device artifacts beyond log files]]

## Used By

- [[techniques/Correlate remote-access session identifiers across devices]]

## References

- [LWCite-1148] Soni, Kaur and Aziz, 2024, "Decoding digital interactions: An extensive study of TeamViewer's Forensic Artifacts across Windows and android platforms", FSI: Digital Investigation 51.

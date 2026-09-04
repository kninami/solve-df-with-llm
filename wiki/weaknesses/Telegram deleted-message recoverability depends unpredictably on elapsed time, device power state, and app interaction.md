---
id: LWW-1314
type: weakness
name: Telegram deleted-message recoverability depends unpredictably on elapsed time, device power state, and app interaction
description: Even though Telegram's default configuration leaves deleted records theoretically recoverable in the main database (Auto Vacuum and Secure Delete disabled) and briefly in the WAL file, actual recovery success in a realistic multi-user scenario varied substantially with the elapsed time before acquisition, the device's power/connectivity state, and how the app was subsequently used, and different forensic tools examining the identical dataset produced diverging results in accuracy and completeness.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - LWM-1316
source_refs:
  - LWCite-1354
updated_at: 2026-08-15
status: complete
---

# Telegram deleted-message recoverability depends unpredictably on elapsed time, device power state, and app interaction

## Summary

The study tested Telegram deleted-record persistence under three variable/condition categories — elapsed time until forensic acquisition, device status (powered on/off, airplane mode), and interaction with the app itself (creating, reading, or deleting further messages) — across a realistic four-user scenario involving thousands of exchanged text messages and media files. Results varied across these conditions, and cross-checking several well-known, up-to-date forensic tools against the identical underlying dataset found their accuracy and completeness diverged from one another, meaning tool choice itself materially affects what an investigator recovers from the same evidence.

## Why It Matters

An investigator cannot assume a fixed, predictable recovery outcome for Telegram deleted content based on the app's default configuration alone (WAL enabled, Auto Vacuum and Secure Delete disabled); the actual recoverable content at the time of acquisition depends on case-specific timing and device-handling factors largely outside the investigator's control once the relevant events have already occurred, and depends further on which specific tool is used to perform the recovery. Reporting a negative recovery result without accounting for these variables risks understating what could plausibly have been recovered under different acquisition timing or with a different tool, while reporting a positive result without noting tool-dependence risks appearing to overstate confidence if a different tool would have found less.

## Related Mitigations

- [[mitigations/Acquire a Telegram-relevant device as promptly as possible and cross-validate deleted-record recovery across multiple tools]]

## Used By

- [[techniques/Recover deleted SQLite records]]

## References

- [LWCite-1354] Vasilaras, Dosis, Kotsis, and Rizomiliotis, 2022, "Retrieving deleted records from Telegram", FSI: Digital Investigation 43, 301447.

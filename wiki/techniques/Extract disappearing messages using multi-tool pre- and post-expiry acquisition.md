---
id: DFT-1197
type: technique
name: Extract disappearing messages using multi-tool pre- and post-expiry acquisition
description: Acquire an ephemeral/disappearing-messaging app both before and immediately after a message's expiry timer elapses, using more than one mobile forensic tool (e.g. Cellebrite UFED and MSAB XRY) plus manual database/hex review, since no single app, platform, or tool combination reliably recovers all disappearing-message content once it has "disappeared."
objective_ids:
  - DFO-1006
weakness_ids:
  - DFW-1206
aliases:
  - Comparative multi-tool extraction of WhatsApp/Snapchat/Telegram disappearing messages
source_refs:
  - DFCite-1218
updated_at: 2026-08-13
status: complete
---

# Extract disappearing messages using multi-tool pre- and post-expiry acquisition

## Summary

Ephemeral/disappearing-message features are inconsistently implemented across apps, mobile platforms, and even between logical and physical extraction methods, so relying on a single tool or a single extraction pass materially under-recovers content. Acquiring the device both before and after the expiry point, comparing logical, advanced-logical, and physical extractions from at least two forensic tools, and manually reviewing the underlying SQLite databases and cache files maximizes recoverable disappearing-message content.

## Details

A structured comparison of WhatsApp, Snapchat, and Telegram disappearing-message features on Android (Samsung, physical extraction available) and iOS (iPhone, logical/advanced-logical only) found no consistent winner: Cellebrite UFED outperformed XRY on iOS both pre- and post-expiry, but the two tools performed comparably on Android; Cellebrite's physical extraction on Android surprisingly retrieved no more data than its logical/advanced-logical extraction in the WhatsApp test, contrary to the general expectation that physical extraction recovers more deleted data. Where a forensic tool's built-in parser failed to surface expired content (e.g. Telegram's `Cache4.db` on Android), manually opening the database in a hex editor and converting raw timestamp/text fragments recovered otherwise-inaccessible message content and image file paths. Cloud extraction (via account credentials/tokens) and paired-desktop-application acquisition were both evaluated as secondary techniques and found far less effective than direct device acquisition, useful mainly as a last resort or to capture images cached in RAM while the desktop app remains open.

## Examples

- Comparing pre- and post-expiry Cellebrite/XRY extractions of WhatsApp on a Samsung S6 and an iPhone 6s: Cellebrite recovered 75% of data pre-expiry and 42% post-expiry versus XRY's 50%/0%, but neither tool fully recovered Samsung's post-expiry text messages despite the Samsung device otherwise showing better raw data retention than the iPhone.
- On Telegram Android, standard extraction retrieved no parsed "secret chat" messages, but manually opening `Cache4.db` in a hex editor and converting stored Unix timestamps recovered message metadata and image file paths that the forensic tool's own parser had missed.
- Snapchat data was fully unrecoverable via standard iOS extraction but near-completely recoverable via Android physical extraction of the `arroyo.db` database, showing that platform choice alone can determine whether disappearing-message content survives.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Ephemeral-message recovery completeness varies unpredictably by app, platform, and forensic tool]]

## References

- [DFCite-1218] Heath et al., 2023, "Forensic analysis of ephemeral messaging applications: Disappearing messages or evidential data?", FSI: Digital Investigation 46.

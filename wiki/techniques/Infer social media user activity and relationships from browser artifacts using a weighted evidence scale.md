---
id: LWT-2066
type: technique
name: Infer social media user activity and relationships from browser artifacts using a weighted evidence scale
description: During a live triage, automatically recover and categorize browser artifacts (history, cache, and session-store files) that indicate a user's social media registration, search/view, content-sharing, and association/relationship activity, weighting each artifact by evidential reliability, without needing to recover the actual communication content itself.
objective_ids:
  - DFO-1008
weakness_ids:
  - LWW-2066
aliases:
  - Social Media User Relationship Framework
  - SMURF
source_refs:
  - LWCite-2070
updated_at: 2026-08-15
status: complete
---

# Infer social media user activity and relationships from browser artifacts using a weighted evidence scale

## Summary

Because a social media platform's actual message/post content is often not readily available or accessible on disk during a live triage (it may reside in unallocated space, require file carving, or simply not be locally cached), this technique instead automates recovery of browser artifacts — history, cache, and session-store files — that indicate registration/authentication, search/view, content-sharing, and association/relationship activity, and weights each recovered artifact by how directly it evidences genuine user activity, so an investigator can quickly infer and prioritize leads without waiting for a full forensic examination.

## Details

The technique groups artifacts recovered during a live triage's "Capture" stage (system- and user-generated browser artifacts) through "Identify" (segregating by artifact type and location) and "Process" (pattern-matching to extract features of interest, e.g. via regular expressions against URL/history/cache/session-store data) into a final "Present" stage that generates a human-readable report. Each artifact type is assigned one or more positions on a five-level weighting scale — "Strongly expect to find" (e.g. the account's own email address, username), "May expect to find" (e.g. login/logout activity, other users' usernames), "Corroborates other artifacts" (e.g. search/query parameters), "Needs to be contextualized" (e.g. a profile ID that could mean different things depending on context), and "Requires corroboration" (e.g. communication content, which cannot be validated on its own) — so an investigator can judge how much weight to place on a given recovered artifact when building relationship or activity inferences. The technique targets specific known browser storage locations per browser (e.g. Chrome's `formhistory.sqlite`, `Login Data`, and cache; Firefox's `places.sqlite`, `sessionstore.mozlz4`, and cache) and can incorporate third-party parsers (e.g. `chromagnon` for Chrome History, PECmd for Prefetch, a mozlz4-decoding script for Firefox session data) as modular components feeding a single collated report.

## Examples

- On a simulated Twitter live-triage case study, the technique recovered the account owner's email address (strongly-expect-to-find), login/logout URLs and other users' usernames/profile IDs (may-expect-to-find), and search/query parameters that contextualized a previously-recovered profile ID as the target of a deliberate search rather than an incidental page visit, illustrating relationship attribution (a searched-for user later added as a connection) without recovering any tweet or message content directly.
- Cross-validated against Autopsy 4.15.0's own web-history recovery on the same test VM: Autopsy recovered a comparable set of social-media URL artifacts from the browser data source but its "Communications Visualization" feature did not support visualizing web-browser-sourced social media activity (only email/call-log/mobile-account sources), confirming a gap this technique's purpose-built weighting/reporting approach fills.

## Related Objectives

- `DFO-1008` Establish identities

## Related Weaknesses

- [[weaknesses/Browser-cache and history artifacts inferring social media activity may originate from background processes rather than deliberate user interaction]]

## References

- [LWCite-2070] David, Morris & Appleby-Thomas, 2021, "Social Media User Relationship Framework (SMURF)", JDFSL 16(1). Source of the SMURF live-triage framework, its five-level weighting scale, and the Twitter case study/Autopsy comparison.

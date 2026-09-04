---
id: LWM-2067
type: mitigation
name: Corroborate browser-cache-and-history social media artifacts against multiple sources before attributing them to deliberate user action
source_refs:
  - LWCite-2070
updated_at: 2026-08-15
status: complete
---

# Corroborate browser-cache-and-history social media artifacts against multiple sources before attributing them to deliberate user action

## Summary

Do not treat a single browser-cache or history artifact indicating a social media profile or piece of content as conclusive evidence of deliberate user interaction; instead, weight the artifact by how directly it evidences genuine activity and corroborate lower-confidence artifacts against independent sources (search/query parameters, login/session activity, or other recovered artifacts) before drawing an inference about a user's activity or relationships.

## Addresses

- [[weaknesses/Browser-cache and history artifacts inferring social media activity may originate from background processes rather than deliberate user interaction]]

## How To Apply

Apply a tiered confidence scale to recovered browser artifacts — distinguishing artifacts strongly indicative of the account owner's own activity (e.g. the account's own email/username), artifacts that only may indicate interaction with another user, and artifacts that require independent corroboration before they support any conclusion (e.g. a cached profile with no accompanying search, login, or session-activity evidence) — and document, for any artifact used to support a relationship or activity inference in a report, which corroborating evidence (if any) supports treating it as deliberate user action rather than a background/caching side effect.

## References

- [LWCite-2070] David, Morris & Appleby-Thomas, 2021, "Social Media User Relationship Framework (SMURF)", JDFSL 16(1). Proposes the five-level weighting scale (strongly expect to find / may expect to find / corroborates other artifacts / needs to be contextualized / requires corroboration) as the mechanism for assessing artifact reliability before attribution.

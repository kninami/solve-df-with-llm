---
id: DFW-2066
type: weakness
name: Browser-cache and history artifacts inferring social media activity may originate from background processes rather than deliberate user interaction
description: A browser cache or history entry indicating social media activity (a URL visit, a page load, or cached content) does not by itself prove the user deliberately viewed, shared, or interacted with that content, since the same artifacts can be created by background processes, caching mechanisms, or automatic page prefetching without any conscious user action.
categories:
  - ASTM_INAC_AS
  - ASTM_MISINT
mitigation_ids:
  - DFM-2067
source_refs:
  - DFCite-2070
updated_at: 2026-08-15
status: complete
---

# Browser-cache and history artifacts inferring social media activity may originate from background processes rather than deliberate user interaction

## Summary

The source framework's own authors caution that "artefacts may exist as a result of background processes on the social media platform" and that "a web browser's caching mechanism and/or web storage of content the user has not interacted with" can generate the very artifact types (cached pages, cookies, session data) that the technique otherwise treats as indicators of user activity. A recovered artifact showing a particular profile or piece of content in a user's browser cache is therefore not, on its own, proof that the user actually viewed, searched for, or interacted with it.

## Why It Matters

If an investigator treats a browser-cache artifact indicating the presence of a particular social media profile or piece of content as direct evidence of deliberate user interaction, without corroborating it against other artifacts (e.g. explicit search/query parameters, login-session activity, or communication content), they risk incorrectly attributing an association, viewing, or relationship to a suspect that was in fact generated automatically by the platform or browser rather than by the user's own action — a misattribution that could unfairly implicate a user or wrongly establish a relationship between two accounts.

## Related Mitigations

- [[mitigations/Corroborate browser-cache-and-history social media artifacts against multiple sources before attributing them to deliberate user action]]

## Used By

- [[techniques/Infer social media user activity and relationships from browser artifacts using a weighted evidence scale]]

## References

- [DFCite-2070] David, Morris & Appleby-Thomas, 2021, "Social Media User Relationship Framework (SMURF)", JDFSL 16(1). States explicitly that background processes and browser caching/web storage can create artefacts of content "the user has not interacted with," and that context and corroboration are necessary when assessing relevance and reliability.

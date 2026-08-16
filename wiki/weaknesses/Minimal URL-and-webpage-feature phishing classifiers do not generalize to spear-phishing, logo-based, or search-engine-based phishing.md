---
id: DFW-2065
type: weakness
name: Minimal URL-and-webpage-feature phishing classifiers do not generalize to spear-phishing, logo-based, or search-engine-based phishing
description: A phishing classifier trained on a minimal feature set composed entirely of URL-structure and webpage-markup heuristics (dots, URL length, HTTPS presence, IFrame redirection, and similar) has no basis for detecting phishing attacks that do not rely on those features, such as spear-phishing messages relying on social-engineering text, logo-based visual impersonation, or search-engine-result-based phishing.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2066
source_refs:
  - DFCite-2069
updated_at: 2026-08-15
status: complete
---

# Minimal URL-and-webpage-feature phishing classifiers do not generalize to spear-phishing, logo-based, or search-engine-based phishing

## Summary

The minimal feature set this class of technique selects is composed of 13 URL-structure and webpage-markup features (dot count, URL length, presence of an `@` symbol, absence of HTTPS, domain-in-path, HTTPS-in-hostname, path length, IP-address use, popup windows, submitting to email, missing title, IFrame redirection, and return-URL length). None of these features model the content of a phishing email/message, the visual similarity of a page's branding/logo to a legitimate one, or the manipulation of search-engine results — attack categories that the paper's own literature review identifies as limitations of comparable prior studies (e.g., a prior user-awareness study "does not consider spear email and phishing websites/logo-based phishing attacks which may limit the generalization of the research study," and another study similarly "does not consider all categories of phishing attacks such as search-engine based, logo-based phishing etc.").

## Why It Matters

An investigator or organization that deploys a URL/webpage-feature-only phishing classifier and treats a "not phishing" classification as reassurance risks a false sense of coverage: an attack delivered as a spear-phishing message with no suspicious URL structure, or a visually convincing logo-impersonation page hosted at a structurally unremarkable URL, would not trigger the classifier's discriminative features at all, since those features were never designed to capture that attack vector.

## Related Mitigations

- [[mitigations/Supplement URL-feature phishing classifiers with dedicated spear-phishing and logo-based detection models]]

## Used By

- [[techniques/Select phishing-detection features using frequency-analysis minimal feature selection]]

## References

- [DFCite-2069] Abiodun, Sodiya, Kareem & Oladimeji, 2021, "Performance Assessment of some Phishing predictive models based on Minimal Feature corpus", JDFSL 16(5). The paper's own 13-feature minimal set is entirely URL/webpage-structural, and its literature review explicitly flags the same generalization gap (spear-phishing, logo-based, search-engine-based phishing) as a limitation of comparable prior studies using a similarly URL-centric feature scope.

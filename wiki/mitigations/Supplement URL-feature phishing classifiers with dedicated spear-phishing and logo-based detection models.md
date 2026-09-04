---
id: LWM-2066
type: mitigation
name: Supplement URL-feature phishing classifiers with dedicated spear-phishing and logo-based detection models
source_refs:
  - LWCite-2069
updated_at: 2026-08-15
status: complete
---

# Supplement URL-feature phishing classifiers with dedicated spear-phishing and logo-based detection models

## Summary

Pair a minimal URL/webpage-feature phishing classifier with complementary detectors targeting attack categories its feature set cannot see — a content/text-based classifier for spear-phishing messages and a visual/logo-similarity detector for brand-impersonation pages — rather than relying on the URL-feature classifier's "not phishing" output as a complete authenticity signal.

## Addresses

- [[weaknesses/Minimal URL-and-webpage-feature phishing classifiers do not generalize to spear-phishing, logo-based, or search-engine-based phishing]]

## How To Apply

Where an investigation or defensive deployment needs broad phishing coverage, run the URL/webpage-feature classifier alongside a text-based spear-phishing detector (e.g., analyzing message content and sender-context for social-engineering cues) and a logo/visual-similarity detector (comparing a suspect page's branding elements against known legitimate brand assets); treat a "not phishing" result from the URL-feature classifier alone as coverage only for the URL/webpage-structure attack category it was designed for, and document which attack categories were and were not screened when reporting results.

## References

- [LWCite-2069] Abiodun, Sodiya, Kareem & Oladimeji, 2021, "Performance Assessment of some Phishing predictive models based on Minimal Feature corpus", JDFSL 16(5). The paper's literature review identifies logo-based and text-based (image, frame) integrated feature approaches (e.g., Adebowale et al., 2018) as the kind of complementary detection needed beyond a purely URL-based feature scope.

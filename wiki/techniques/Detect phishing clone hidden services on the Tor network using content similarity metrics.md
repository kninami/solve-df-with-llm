---
id: LWT-1290
type: technique
name: Detect phishing clone hidden services on the Tor network using content similarity metrics
description: Identify phishing clones of Tor hidden services — sites that impersonate a legitimate onion service to steal cryptocurrency payments or confidential information — by crawling a broad set of onion services, then comparing each pair of crawled pages for content similarity (exact-hash equality, compression-based similarity, or perceptual image-hash similarity of rendered screenshots) and comparing onion addresses for prefix similarity, since a phishing clone typically reuses most of the legitimate site's text/layout content while only altering payment and contact details.
objective_ids:
  - DFO-1019
weakness_ids:
  - LWW-1300
aliases:
  - Tor hidden service phishing/site-cloning detection
source_refs:
  - LWCite-1334
updated_at: 2026-08-15
status: complete
---

# Detect phishing clone hidden services on the Tor network using content similarity metrics

## Summary

Phishing is a particularly severe problem on Tor: onion addresses are random-looking strings hard for a human to recognize or remember, SSL certificates are little used (obtaining one from a central authority while remaining anonymous is difficult), and the network's own anonymity lets a single attacker easily stand up multiple impersonating services and create replacements as soon as one is identified. Because irreversible cryptocurrency payments make phishing on Tor especially lucrative (an attacker clones a shop or drop-box service, alters only the payment address or a man-in-the-middle-proxied content stream, then distributes the clone's link through the same channels as the original), automatically detecting content-similar page pairs among a broad crawl of onion services surfaces likely phishing clones for investigative or takedown action.

## Details

Content is compared at several levels: exact equality (cryptographic hash comparison of the raw served HTML/CSS/JS, detecting unmodified clones), compression-based similarity (comparing how well one page's content compresses using a dictionary built from another, which tolerates minor textual differences an attacker introduces when substituting payment details or contact information), and rendered-page perceptual image hashing (screenshotting the rendered page and comparing perceptual hashes, catching visual clones even where the underlying markup has been substantially altered). Onion addresses themselves are also compared for prefix similarity — since generating a Tor v3 onion address with a specific desired prefix requires increasingly prohibitive computational effort as the prefix length grows, two services sharing an unusually long common address prefix (beyond roughly the first half of the typical 16-character comparison window used) is itself a signal worth investigating, though legitimately unrelated addresses will also share a small number of characters by chance and this baseline must be accounted for when setting a similarity threshold. Data collection uses a broad crawl seeded from known darknet link-list portals, parsing HTML for onion links and additionally regex-matching plaintext onion addresses (since link lists and services frequently post them as unlinked text rather than clickable links), routed through a Tor SOCKS proxy so onion addresses can be crawled like regular domains.

## Examples

- A real 2019 incident is cited in which a phishing clone impersonated The Guardian's Tor SecureDrop whistleblower drop-box service, harvesting SecureDrop "codenames" (pseudonyms used for follow-up communication with sources) and advertising malware to visitors — illustrating that Tor phishing targets legitimate, non-criminal anonymity use cases as well as illicit marketplaces.
- A test set was assembled by manually selecting pages from known clone-detection listings together with randomly selected individual crawled services, then comparing every page against every other page at a chosen similarity threshold to evaluate detection accuracy.

## Related Objectives

- `DFO-1019` Detect anti-forensics and other anomalies

## Related Weaknesses

- [[weaknesses/Content-similarity Tor phishing detection misses a clone whose attacker deliberately alters enough content to evade the similarity threshold]]

## References

- [LWCite-1334] Steinebach, Zenglein, and Brandl, 2021, "Phishing detection on tor hidden services", FSI: Digital Investigation 36, 301117.

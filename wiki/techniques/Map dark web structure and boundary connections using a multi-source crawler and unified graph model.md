---
id: DFT-2108
type: technique
name: Map dark web structure and boundary connections using a multi-source crawler and unified graph model
description: Comprehensively map the dark web's structure -- including its connections to and from the surface web, which single-strategy crawlers largely miss -- by combining three complementary crawling strategies (seed-node expansion, dark web search engine querying, and surface web search engine querying for dark web links) into one closed-loop crawler, and representing the resulting data in a single "one-size-fits-all" graph model that simultaneously supports page-level and site-level analysis using multiple node and edge types (hyperlink and redirect, dark-to-dark, dark-to-surface, and surface-to-dark).
objective_ids:
  - DFO-1014
  - DFO-1012
weakness_ids:
  - DFW-2115
aliases:
  - Multi-source multi-channel dark web crawler
source_refs:
  - DFCite-2135
updated_at: 2026-08-16
status: complete
---

# Map dark web structure and boundary connections using a multi-source crawler and unified graph model

## Summary

Prior dark web crawling research typically relies on a single crawling strategy and a single-type graph (usually only dark-web-to-dark-web edges at either the page or site level), which leaves substantial "blind zones" unreachable from any given entry point and fails to capture the structurally important boundary between the dark web and the surface web. Integrating three mutually-reinforcing crawler types -- seed-node-based expansion, dark web search engine querying, and surface web search engine querying specifically for dark web URLs -- into one system, and modeling the combined results in a graph with multiple node types (page, site; each further marked as dark or surface) and multiple edge types (hyperlink, redirect; each further categorized as dark-to-dark, dark-to-surface, or surface-to-dark), supports systematic investigation of the dark web's covertness and any adversarial (anti-monitoring) behavior by its site administrators.

## Details

The extended dark web crawler based on seed nodes starts from a curated root set (dark web directory pages, chosen as an efficient entry point since they concentrate many outbound links) and recursively expands to both dark-web and any linked surface-web URLs it discovers, using a distributed worker pool coordinating through a shared request queue with deduplication and retry-with-backoff for failed requests. The extended dark web crawler based on search engines instead queries dark-web-specific search engines (e.g. Torch) with case-relevant keywords, retrieving and expanding from the resulting dark web pages, which improves efficiency and coverage relative to purely following hyperlinks since search engines index content a pure link-following crawler might not reach through any available path. The dark web crawler based on the surface web search engine performs the complementary operation: an exact-match search on ordinary surface web search engines for known dark web URLs surfaces which surface web pages reference or discuss those URLs, and crawling those surface pages recovers additional links back into the dark web, specifically populating the boundary (dark-to-surface and surface-to-dark) edge types the other two crawler types cannot capture. The resulting one-size-fits-all graph model tags each node (page or site level) as dark or surface and as valid or invalid (based on HTTP status and .onion-address-format validation), and each edge as a hyperlink or redirect, further categorized by which side of the dark/surface boundary it crosses, letting an analyst query the graph from multiple simultaneous perspectives (page-level or site-level; dark web interior structure, or the dark/surface boundary specifically) without needing separate graph constructions for each.

## Examples

- Comparing the combined crawler (S4) against three baseline crawler configurations representative of prior single-strategy research (S1: seed-node only; S2: seed-node plus its own directly-discovered surface links; S3: search-engine only) over an identical 24-hour, six-server run with matched seed nodes and keywords, S4 collected roughly 6.47 million dark web links and reached nearly 30,000 distinct dark web sites, substantially exceeding all three baselines, and was the only configuration of the four able to establish links from the surface web to the dark web at all (over 75,000 such links), since S1-S3 each structurally lack the surface-web-search-engine-based crawler component needed to discover them.
- Applying the resulting graph model to a live 72-hour crawl (9.87 million pages, 35.17 million edges) found the dark web's overall network density (≈3.6×10⁻⁷) and average node degree (7.12) were both markedly lower than typical surface web baselines, and that dark web directory and search-engine pages play an outsized structural role in traffic diversion -- from either a dark web or surface web starting page, expanding six hyperlink-clicks outward reached over 1.8 million pages specifically when the expansion passed through a directory or search-engine node, versus a comparatively flat, limited reach when it did not.

## Related Objectives

- `DFO-1014` Find potential digital evidence sources
- `DFO-1012` Locate potentially relevant content

## Related Weaknesses

- [[weaknesses/Crawler-based dark web mapping cannot discover completely isolated sites with no incoming links from any indexed source]]

## References

- [DFCite-2135] Li, Zhang, Yan, Gao, Yin, and Gu, 2026, "Unveiling the mysteries of the dark web: A comprehensive graph-based multi-view analysis", FSI: Digital Investigation 57, 302105.

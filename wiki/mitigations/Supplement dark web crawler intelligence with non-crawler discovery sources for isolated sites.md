---
id: DFM-2116
type: mitigation
name: Supplement dark web crawler intelligence with non-crawler discovery sources for isolated sites
source_refs:
  - DFCite-2135
updated_at: 2026-08-16
status: complete
---

# Supplement dark web crawler intelligence with non-crawler discovery sources for isolated sites

## Summary

Treat crawler-derived dark web intelligence as necessarily incomplete for sites with no discoverable incoming references, and actively seek non-crawler discovery sources (informant tips, seized-device bookmarks/history, prior case leads, human intelligence) to identify dark web sites a crawl-based approach structurally cannot find.

## Addresses

- [[weaknesses/Crawler-based dark web mapping cannot discover completely isolated sites with no incoming links from any indexed source]]

## How To Apply

Do not treat a crawler's coverage, however extensive, as a complete inventory of dark web sites relevant to an investigation; explicitly seek discovery channels independent of crawling, such as onion addresses recovered from a seized device's browser history or bookmarks, addresses referenced in intercepted communications, informant or undercover-sourced URLs, or addresses surfaced by other agencies' prior investigations. Where a suspected isolated site's existence is known through one of these independent channels, use [[techniques/Map dark web structure and boundary connections using a multi-source crawler and unified graph model]] to characterize that specific site's own structure and any connections it does have outward, even though the crawler could not have discovered the site's existence on its own. Periodically cross-check whether a previously isolated site has since acquired any indexed incoming links, since a site's isolation status can change over time.

## References

- [DFCite-2135] Li, Zhang, Yan, Gao, Yin, and Gu, 2026, "Unveiling the mysteries of the dark web: A comprehensive graph-based multi-view analysis", FSI: Digital Investigation 57, 302105.

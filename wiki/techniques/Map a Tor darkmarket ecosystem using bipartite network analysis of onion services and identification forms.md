---
id: DFT-1260
type: technique
name: Map a Tor darkmarket ecosystem using bipartite network analysis of onion services and identification forms
description: Model a large corpus of scraped Tor darkmarket onion services and their referenced external identification forms (email addresses, Telegram usernames, cryptocurrency wallets, Pastebin/Discord/PGP identifiers) as a bipartite graph, then apply social-network-analysis metrics (connected components, density, average path length, k-core extraction, degree centrality) to identify high-value hub services and identifiers for law enforcement targeting.
objective_ids:
  - DFO-1005
weakness_ids:
  - DFW-1272
aliases:
  - Tor darkmarket ecosystem bipartite network mapping
source_refs:
  - DFCite-1300
updated_at: 2026-08-14
status: complete
---

# Map a Tor darkmarket ecosystem using bipartite network analysis of onion services and identification forms

## Summary

An individual onion service's content review does not reveal how it relates to the broader darkmarket ecosystem, but the external identification forms (IDs) it references — a shared email address, Telegram channel, or cryptocurrency wallet — link otherwise-separate services together; modeling this at scale as a bipartite graph (one partition of onion services, one partition of IDs, with edges wherever a service references an ID) and applying standard network-analysis metrics reveals which services and IDs function as structural hubs, offering law enforcement concrete, high-leverage targets for disruption rather than requiring manual cross-referencing of thousands of services individually.

## Details

Onion services are collected via sustained automated web crawling (with manual Captcha-resolution intervention for services that resist automated bypass), each is topic-categorized against a standardized taxonomy (e.g. the MISP Dark Web taxonomy: hacking, finance-crypto, drugs-narcotics, electronics, search-engine-index, finance, other), and each service's page content is parsed for external identifiers (email, phone, Telegram, Pastebin, Discord, PGP key, and cryptocurrency wallet references) to build the bipartite graph's edges. Several structural metrics are then computed on the overall graph and on topic-specific subnetworks: connected-component count and largest-component size (fragmentation vs. cohesion), density (how promiscuously services and IDs are shared), average path length and diameter (how compact or sprawling the network is), and k-core extraction (the subgraph where every node has at least k connections, surfacing the network's most densely interconnected core). Ranking nodes by degree centrality within this structure identifies both hub onion services (heavily cross-referenced sites) and hub IDs (identifiers, such as a specific Telegram channel or Bitcoin wallet, shared across many otherwise-unrelated services) — the latter being particularly actionable, since removing or compromising a single widely-shared communication channel or wallet can disrupt a disproportionate share of the mapped ecosystem at once.

## Examples

- Analyzing 82,285 onion services and 57,071 extracted IDs collected over a 20-week crawl found hacking the dominant topic (57,233 services) and email the dominant ID type (43,298 instances), with the overall network fragmenting into 1,848 connected components but a single dominant component still containing 76.72% of all nodes.
- Topic-specific subnetworks showed structurally opposite patterns: the hacking subnetwork was large, sprawling, and collaborative (diameter 30, average path length 22.85, low density), while the finance-crypto subnetwork was small, dense, and centralized (diameter 6, average path length 2.00, four key IDs — one Telegram, one email, two Monero wallets — connecting 98.28% of the subnetwork's 17,900 services), indicating finance-crypto activity is structurally far more vulnerable to targeted disruption of just a few shared identifiers than the more decentralized hacking community.
- The single highest-degree ID identified across the entire network was a Telegram channel (degree 48,197) linked predominantly to hacking-related onion services, and the top five onion services by degree centrality were all drawn from just two domains, illustrating that a small number of specific services and IDs account for a disproportionate share of the ecosystem's overall connectivity.

## Related Objectives

- `DFO-1005` Prioritize digital evidence sources

## Related Weaknesses

- [[weaknesses/Automated dark web identifier extraction misses obfuscated, image-embedded, or non-standard-format identification forms]]

## References

- [DFCite-1300] de-Marcos, Domínguez-Díaz and Stapic, 2026, "Mapping the Tor darkmarket ecosystem: A network analysis of topics, communication channels, and languages", FSI: Digital Investigation 56, 302032.

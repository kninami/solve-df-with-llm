---
id: DFM-2131
type: mitigation
name: Corroborate web-scraped drug-report trends against independent wastewater or population-survey data
source_refs:
  - DFCite-2150
updated_at: 2026-08-16
status: complete
---

# Corroborate web-scraped drug-report trends against independent wastewater or population-survey data

## Summary

Cross-check regional distribution and prevalence trends derived from a voluntary drug-checking user-report site against independently collected, population-wide data sources such as wastewater drug monitoring reports or national drug-use household surveys, rather than relying on the self-selected reporting population alone.

## Addresses

- [[weaknesses/Voluntary self-reported drug data samples only a harm-reduction-conscious subset of the user population]]

## How To Apply

Obtain the most recent available wastewater-based drug monitoring data or national/regional drug-use survey statistics covering the same geographic regions and time period as the scraped dataset, and compare the relative regional ranking or temporal trend direction between the two sources; treat concordance as increasing confidence in the OSINT-derived trend and material divergence as a signal that the reporting population's composition may not be representative for that region or period, warranting caution before acting on the OSINT finding alone.

## References

- [DFCite-2150] Maybir and Chapman, 2021, "Web scraping of ecstasy user reports as a novel tool for detecting drug market trends", FSI: Digital Investigation 37.

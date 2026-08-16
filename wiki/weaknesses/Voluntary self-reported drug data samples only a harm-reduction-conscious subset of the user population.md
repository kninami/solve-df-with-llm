---
id: DFW-2130
type: weakness
name: Voluntary self-reported drug data samples only a harm-reduction-conscious subset of the user population
description: A drug-checking user-report website is populated only by the subset of drug users who are harm-reduction-conscious enough to seek out and post on such a site, so trend intelligence derived from it may not represent the broader user population's actual consumption or trafficking patterns.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2131
source_refs:
  - DFCite-2150
updated_at: 2026-08-16
status: complete
---

# Voluntary self-reported drug data samples only a harm-reduction-conscious subset of the user population

## Summary

Prior survey research cited in the paper found that only around 6.25% of a sampled drug-using population reported using harm-reduction pill-report sites, meaning the population that voluntarily generates this open-source data is a self-selected minority rather than a representative cross-section of drug users. Because the underlying reporting is entirely voluntary, free-form, and unverified, there is also no guarantee that any individual report's claimed contents, location, or date are accurate.

## Why It Matters

Intelligence derived from such a source — most-reported logos, regional distribution counts, or apparent trafficking timelines — reflects the reporting behavior of a specific subgroup of users rather than the full illicit drug market, so conclusions about overall market size, prevalence, or precise trafficking timing could be systematically skewed if treated as directly representative. An investigator or policymaker relying on this data without corroboration risks over- or under-estimating the scale of a trend, or drawing conclusions about regions or user groups that are structurally underrepresented in the source data.

## Related Mitigations

- [[mitigations/Corroborate web-scraped drug-report trends against independent wastewater or population-survey data]]

## Used By

- [[techniques/Detect drug trafficking trends using web-scraped user-reported pill characteristics]]

## References

- [DFCite-2150] Maybir and Chapman, 2021, "Web scraping of ecstasy user reports as a novel tool for detecting drug market trends", FSI: Digital Investigation 37.

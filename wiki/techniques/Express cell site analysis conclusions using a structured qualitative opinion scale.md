---
id: DFT-1110
type: technique
name: Express cell site analysis conclusions using a structured qualitative opinion scale
description: Report a cell site analysis finding using a defined five-category verbal scale of technical opinion strength (ranging from strong positive support through to a deductive exclusion), each grounded in an explicit description of the underlying observations, rather than presenting an unsupported quantitative probability for how discriminating the finding is.
objective_ids:
  - DFO-1020
weakness_ids:
  - DFW-1115
aliases:
  - Case Assessment and Interpretation (CAI) model for cell site analysis
  - CAI verbal scale reporting
source_refs:
  - DFCite-1108
updated_at: 2026-08-12
status: complete
---

# Express cell site analysis conclusions using a structured qualitative opinion scale

## Summary

Cell site analysis findings inherently carry uncertainty from network variability, incomplete survey coverage, and unresolved technical assumptions, so presenting a bare "match/no-match" conclusion risks overstating precision. The Case Assessment and Interpretation (CAI) model addresses this by combining individual technical sub-observations about each call event into an overall opinion expressed on a defined, five-category verbal scale rather than a single unsupported number.

## Details

The five categories range from strongest to weakest support: (1) the cell was observed serving the location at the time of the survey with close proximity and clear line of sight; (2) it is reasonable that the cell served the location, without direct survey confirmation but with no evidence against it; (3) the expert cannot determine whether the cell did or did not serve the location, given unresolved uncertainty (e.g. network changes since the events, or nearby but not clearly overlapping survey measurements); (4) the expert would not expect the cell to have served the location but cannot rule it out; and (5) it is not reasonable that the cell served the location — a stronger, potentially deductive conclusion (e.g. a non-extended-range GSM cell cannot serve a location more than approximately 35km from the mast). Each category is explicitly grounded in the specific observations that support it (proximity, line of sight, known cell-selection behavior, or physical range limits) rather than an abstract confidence percentage. The authors note this qualitative scale is used because no validated method for calculating a calibrated likelihood ratio in cell site analysis currently exists, unlike some other forensic disciplines.

## Examples

- A cell detected serving a location during a blind-trial survey, at close range with clear line of sight to the location, was reported under category [One] ("I would expect the cell to serve an area including the location, and I have demonstrable information that suggests it did"), grounded explicitly in the survey observation and proximity/line-of-sight assessment rather than a numeric probability.

## Related Objectives

- `DFO-1020` Document digital forensic activities

## Related Weaknesses

- [[weaknesses/Cell site analysis technical opinions cannot currently be mapped onto calibrated likelihood ratios]]

## References

- [DFCite-1108] Tart et al., 2021, "Cell site analysis: use and reliability of survey methods", FSI: Digital Investigation 38.

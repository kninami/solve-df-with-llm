---
id: LWM-1115
type: mitigation
name: Use the qualitative CAI verbal scale instead of unsupported quantitative likelihood ratios when reporting cell site opinions
source_refs:
  - LWCite-1108
updated_at: 2026-08-12
status: complete
---

# Use the qualitative CAI verbal scale instead of unsupported quantitative likelihood ratios when reporting cell site opinions

## Summary

Report cell site analysis conclusions using the qualitative, observation-grounded five-category CAI verbal scale rather than a numeric likelihood ratio or a verbal scale borrowed from a discipline where LR calibration is validated, since no such calibration currently exists for cell site analysis.

## Addresses

- [[weaknesses/Cell site analysis technical opinions cannot currently be mapped onto calibrated likelihood ratios]]

## How To Apply

When forming and reporting a cell site opinion, select the CAI verbal-scale category (from strong positive support through to deductive exclusion) that is directly supported by the specific technical observations available (survey results, proximity, line of sight, known cell-selection behavior, or physical range limits), and state explicitly which observations ground the chosen category. Avoid presenting a numeric probability or a likelihood-ratio-style verbal scale unless and until a validated method for calibrating cell site analysis uncertainty is established and referenced.

## References

- [LWCite-1108] Tart et al., 2021, "Cell site analysis: use and reliability of survey methods", FSI: Digital Investigation 38.

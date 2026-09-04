---
id: LWM-1187
type: mitigation
name: Document Bayesian network probability sources and subject them to sensitivity analysis and peer review
source_refs:
  - LWCite-1190
updated_at: 2026-08-13
status: complete
---

# Document Bayesian network probability sources and subject them to sensitivity analysis and peer review

## Summary

Record, in the case file, the data or reasoning behind every conditional probability assigned in a Bayesian network evidence evaluation — just as an expert would document the basis for a judgment made without a network — and run a sensitivity analysis to check how much the derived likelihood ratio moves under plausible alternative assignments before relying on or reporting it.

## Addresses

- [[weaknesses/Bayesian network probability assignments rely on subjective judgment outside typical forensic domain expertise]]

## How To Apply

Keep the constructed Bayesian network (node structure, conditional probability tables, and the reasoning or data source behind each assignment) in the laboratory case file, so that if questions arise, the underlying judgments can be inspected, discussed, and revisited with fresh perspective rather than remaining implicit in the expert's head. Use available sensitivity-analysis tooling (e.g. Champod's BN sensitivity analysis tool) to test how much the derived likelihood ratio changes under plausible alternative probability assignments, and report a probability that clearly falls outside the examiner's own domain expertise (e.g. general population priors) as an assumption sourced from elsewhere rather than as an expert finding. Where the network will be used repeatedly across similar cases, have it reviewed by peer forensic examiners before adoption, and communicate to recipients (court, opposing counsel) that the network is a structured aid for transparent reasoning under uncertainty, not a fully objective calculation independent of expert judgment.

## References

- [LWCite-1190] Vink et al., 2025, "Evaluating digital forensic findings in Trojan horse defense cases using Bayesian networks", FSI: Digital Investigation 55, 302023.

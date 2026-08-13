---
id: DFW-1187
type: weakness
name: Bayesian network probability assignments rely on subjective judgment outside typical forensic domain expertise
description: Every node in a Bayesian network evidence-evaluation model requires a conditional probability table populated with numeric values, but assigning those values often calls for judgments (e.g. how likely an unrelated remote party is to exist at all) that fall outside a digital forensic expert's own domain knowledge, and there is no single objectively correct network structure or set of assignments for a given case.
categories:
  - ASTM_MISINT
mitigation_ids:
  - DFM-1187
source_refs:
  - DFCite-1190
updated_at: 2026-08-13
status: complete
---

# Bayesian network probability assignments rely on subjective judgment outside typical forensic domain expertise

## Summary

The source paper's own worked example assigned many conditional probabilities from the authors' expert judgment and experience, and explicitly cautions that these fictitious values should not be reused directly in other casework since every case has a different framework of circumstances. Because a Bayesian network is not based on data-driven structure learning (unlike some AI-fusion alternatives), every dependency and probability in it is a manually specified expert judgment call, and different experts modeling the same case could reasonably produce different networks.

## Why It Matters

A likelihood ratio derived from a Bayesian network can look like a precise, objective numerical output even though its inputs are subjective probability assignments, some of which (e.g. the prior likelihood that an unknown third party had the opportunity and motive to act) may fall outside what a digital forensic examiner is qualified to judge on their own. A court or opposing expert who is not shown how the underlying CPTs were derived risks over-interpreting the resulting LR as more objectively grounded than it is, undermining exactly the balance and transparency the method is meant to provide.

## Related Mitigations

- [[mitigations/Document Bayesian network probability sources and subject them to sensitivity analysis and peer review]]

## Used By

- [[techniques/Model digital evidence evaluation using a Bayesian network]]

## References

- [DFCite-1190] Vink et al., 2025, "Evaluating digital forensic findings in Trojan horse defense cases using Bayesian networks", FSI: Digital Investigation 55, 302023.

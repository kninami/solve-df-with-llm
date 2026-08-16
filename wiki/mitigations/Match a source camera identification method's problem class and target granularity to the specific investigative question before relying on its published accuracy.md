---
id: DFM-2079
type: mitigation
name: Match a source camera identification method's problem class and target granularity to the specific investigative question before relying on its published accuracy
source_refs:
  - DFCite-2089
updated_at: 2026-08-16
status: complete
---

# Match a source camera identification method's problem class and target granularity to the specific investigative question before relying on its published accuracy

## Summary

Before relying on a source camera identification method's published accuracy or error-rate figures, explicitly classify the actual investigative question into its Verification/Identification/Exploration problem class and its Physical Device/Configured Device/Virtual Model/Physical Model target granularity, and confirm the method was validated for that same combination rather than assuming its gold-standard reputation transfers automatically.

## Addresses

- [[weaknesses/Sensor-pattern-noise source camera identification is validated almost exclusively for the verification problem class on outdated hardware]]

## How To Apply

Use [[techniques/Select a source camera identification method using the verification, identification, and exploration problem-class framework]] to classify the investigative question, then check whether the candidate SCI method's published validation actually covers that problem class and target granularity level. Where a method (such as SPN) has only been validated for Verification at the Physical Device level, treat its accuracy figures as inapplicable to an Identification- or Exploration-class question until independently re-validated for that use case, and prefer re-validating against contemporary camera hardware over relying on figures from outdated benchmark datasets.

## References

- [DFCite-2089] Klier and Baier, 2024, "Source Camera Identification - Do we have a gold standard?", FSI: Digital Investigation 52, 301858.

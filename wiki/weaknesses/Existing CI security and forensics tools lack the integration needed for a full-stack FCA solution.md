---
id: DFW-2010
type: weakness
name: Existing CI security and forensics tools lack the integration needed for a full-stack FCA solution
description: Most currently available security, forensics, and compliance-auditing tools for critical infrastructure do not embrace open standards for chain of custody or plug-and-play interoperability, so an organization assembling a converged FCA platform is left with fragmented tools that cannot be readily combined into a complete, coherent evidence pipeline.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-2010
source_refs:
  - DFCite-2010
updated_at: 2026-08-14
status: partial
---

# Existing CI security and forensics tools lack the integration needed for a full-stack FCA solution

## Summary

The survey's own discussion identifies as "probably one of the most important findings" that existing security tools are, in most cases, missing the integration means for a full-stack FCA solution, largely because many tools do not adopt open standards for maintaining an effective chain of custody or for plug-and-play interoperability, increasing the need for collaborative work between tool owners and end-users. It further lists related gaps affecting both SIEMs and forensics tools for CIP: absence of custom connectors/parsers for data-source integration, incomplete data, lack of basic correlation rules, limited data visualization, and reliance on manual operation.

## Why It Matters

An organization that adopts a converged FCA reference architecture but relies on today's fragmented tool ecosystem risks gaps in its evidence pipeline - data from tools that lack open interoperability or standardized chain-of-custody support may not be reliably ingested, correlated, or preserved to evidentiary standard, undermining the completeness of both forensic investigations and compliance audits the architecture is meant to support.

## Related Mitigations

- [[mitigations/Prioritize open interoperability and chain-of-custody standards when selecting components for a converged CI FCA platform]]

## Used By

- [[techniques/Deploy a converged forensics-and-compliance-auditing reference architecture for critical infrastructure]]

## References

- [DFCite-2010] Henriques et al., 2024 — Section VIII.B ("Open Issues") explicitly identifies the lack of full-stack FCA tool integration, open standards adoption, and chain-of-custody interoperability as a key finding of the survey.

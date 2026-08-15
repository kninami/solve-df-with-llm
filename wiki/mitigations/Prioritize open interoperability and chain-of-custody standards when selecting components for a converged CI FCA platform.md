---
id: DFM-2010
type: mitigation
name: Prioritize open interoperability and chain-of-custody standards when selecting components for a converged CI FCA platform
source_refs:
  - DFCite-2010
updated_at: 2026-08-14
status: partial
---

# Prioritize open interoperability and chain-of-custody standards when selecting components for a converged CI FCA platform

## Summary

When assembling the ingestion, data lake, forensic analysis, and audit compliance components of a converged FCA platform for critical infrastructure, prefer tools and data adapters that support open standards for evidence exchange and chain of custody over proprietary formats, and budget for building custom connectors/parsers where standard interoperability is unavailable.

## Addresses

- [[weaknesses/Existing CI security and forensics tools lack the integration needed for a full-stack FCA solution]]

## How To Apply

Evaluate each candidate tool or data source against the platform's Ingesting Module requirements for standardized, timestamp-synchronized, common-format normalization before adoption, and where a tool lacks plug-and-play interoperability or chain-of-custody support, plan for a custom adapter component rather than assuming direct integration; track known gaps (privacy/GDPR compliance, security risk KPIs, data visualization) identified for the CI domain when prioritizing which components to build in-house versus source externally.

## References

- [DFCite-2010] Henriques et al., 2024 — the survey's own open-issues discussion recommends adopting open standards and data abstractions for sharing and exchanging evidence as key to improving FCA tool interoperability.

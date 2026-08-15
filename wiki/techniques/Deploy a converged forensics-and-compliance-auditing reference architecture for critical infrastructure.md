---
id: DFT-2010
type: technique
name: Deploy a converged forensics-and-compliance-auditing reference architecture for critical infrastructure
description: The process of unifying digital forensics and regulatory compliance auditing capabilities for a critical infrastructure/industrial automation and control system (IACS) environment into a single reference architecture, sharing data ingestion, a central data lake, and an analytics layer between post-incident forensic analysis and ongoing audit-compliance checks.
objective_ids:
  - DFO-1015
weakness_ids:
  - DFW-2010
aliases:
  - FCA reference architecture
  - Forensics and Compliance Auditing (FCA) taxonomy for CIP
source_refs:
  - DFCite-2010
updated_at: 2026-08-14
status: partial
---

# Deploy a converged forensics-and-compliance-auditing reference architecture for critical infrastructure

## Summary

Because forensic investigation and regulatory compliance auditing for a critical infrastructure organization draw on largely the same heterogeneous data sources (IDS, AAA, physical access control, logs, third-party interactions), an investigator or infrastructure architect can avoid duplicating collection and correlation effort by deploying a converged FCA (Forensics and Compliance Auditing) platform: a shared ingestion pipeline and data lake feeding both a forensic-analysis module (post-mortem event tracing and root-cause identification) and an audit-compliance module (checking events against business policies, regulatory frameworks, and standards).

## Details

DFCite-2010's reference architecture organizes the platform into an Ingesting Module (probes/adapters normalizing heterogeneous data from IDS, AAA, physical access logs, maintenance activity, and third-party interactions into a common ETL-style format), a Data Lake (the central, often horizontally scaled, persistence layer), an Analytics Module (ML-supported classification/correlation of events and threats, feeding both forensic and compliance consumers), a Forensic Analysis component (post-mortem event tracing and causality/root-cause identification), an Audit Compliance component (checking event conformance against business rules, regulatory, and standardization frameworks), plus Visualization/Dashboards, Monitoring, Real-Time Search, and an Orchestration layer coordinating the whole stack (optionally as cloud-native, containerized microservices for scale-out deployment). The accompanying seven-dimension FCA taxonomy (Critical Infrastructures, Governance, Preparedness, Data Acquisition, Evidence Identification, Reporting, Deployment) gives investigators and architects a structured checklist for scoping which capabilities a given CI's FCA platform needs to cover.

## Examples

- DFCite-2010's Figure 8/9 reference architecture and component-integration view, mapping applicable regulations (NERC-CIP, ISO/IEC 62443, NIST SP 800-82) and auditing models (IIA 2420) onto the architecture's Governance dimension.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation

## Related Weaknesses

- [[weaknesses/Existing CI security and forensics tools lack the integration needed for a full-stack FCA solution]]

## References

- [DFCite-2010] Henriques et al., "A survey on forensics and compliance auditing for critical infrastructure protection", IEEE Access, 2024 — source of the FCA taxonomy and reference architecture described above.

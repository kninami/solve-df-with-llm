---
id: DFT-1025
type: technique
name: Confidence-graded cross-layer evidence correlation for pooled cloud resources
description: Attribute user activity in a pooled or multi-tenant cloud resource (e.g., a shared virtual desktop VM used by several users over time) by correlating user identifiers, resource identifiers, and temporal information across independently-logged architectural layers (user endpoint, access/authentication, resource, and control/management), and explicitly grading the resulting attribution as High, Medium, or Low confidence based on which evidence types were actually obtainable.
objective_ids:
  - DFO-1008
  - DFO-1001
weakness_ids:
  - DFW-1025
aliases: []
source_refs:
  - DFCite-1017
updated_at: 2026-08-09
status: complete
---

# Confidence-graded cross-layer evidence correlation for pooled cloud resources

## Summary

In cloud services where multiple users share the same underlying virtual resource (pooled VM allocation), no single layer of logging is sufficient on its own to attribute a specific activity to a specific user: authentication logs establish who logged in and when, resource-management logs establish which VM was allocated and when, and resource-level artifacts establish what activity occurred, but only combining all three establishes who did what and when. A structured, four-phase investigation process (Identification and Preparation, Collection and Preservation, Examination and Analysis, Response and Containment) applies this correlation systematically and grades the resulting attribution's reliability based on the completeness of the evidence actually obtained.

## Details

Attribution confidence is derived from five evidence conditions: a uniquely-identified user identifier, a specified resource identifier, temporal information consistently established across layers, a VM-internal user activity artifact (a trace of the activity itself, from inside the virtual machine), and/or an externalized artifact (an activity outcome recorded in storage external to the VM), plus optional independent user-layer endpoint evidence. High confidence requires the first four plus a VM-internal artifact; Medium confidence is reached when only an externalized artifact (not a VM-internal one) is available; Low confidence applies when key identifying information itself is missing. Because resource-layer VM-internal artifacts (snapshot/live-forensic disk access) are gated by cloud service provider (CSP) policy and offering, the achievable confidence level for a given case is often determined by the CSP rather than by investigator effort.

## Examples

- Case study on AWS WorkSpaces (non-persistent pool, no VM disk snapshot support): attribution reached only Medium confidence, relying on Access-layer authentication events (AssumeRoleWithSAML), Control-layer VPC Flow Logs/DNS query logs, and S3 persistent-storage externalized artifacts, since Resource-layer VM-internal evidence was unavailable.
- Case study on Microsoft Azure Virtual Desktop (multi-session pool, snapshot-based disk acquisition supported): attribution reached High confidence by additionally combining VHD disk snapshots, FSLogix externalized profile containers, and Windows endpoint artifacts (Prefetch, Amcache) with Access- and Control-layer logs.

## Related Objectives

- `DFO-1008` Establish identities
- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/Cross-layer correlation confidence is capped when resource-layer VM-internal artifacts are inaccessible]]

## References

- [DFCite-1017] Park et al., 2026, "A forensic investigation framework for desktop-as-a-service in cloud environments", FSI: Digital Investigation 58.

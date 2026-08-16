---
id: DFT-2123
type: technique
name: Embed cross-application causal event IDs in logs for forensic readiness
description: Design a system's logging so that every logged event (a sent or received message, function call, or system call) carries a unique event identifier plus references to the identifier(s) of the event(s) that caused it, so that logs collected independently from different applications, protocols, and the OS kernel can be merged into a single causal graph and correlated deterministically, without relying on synchronized timestamps or fuzzy correlation heuristics.
objective_ids:
  - DFO-1015
  - DFO-1001
weakness_ids:
  - DFW-2132
aliases:
  - Gretel numbers
  - Causality tracking for logs
source_refs:
  - DFCite-2154
updated_at: 2026-08-17
status: complete
---

# Embed cross-application causal event IDs in logs for forensic readiness

## Summary

Conventional logs record what happened and when, but rarely record why an event occurred in terms of which other logged event caused it, which forces an investigator to correlate logs from different applications using imprecise heuristics such as timestamp proximity. Assigning each logged event a unique identifier ("gretel number" after the Hansel and Gretel fairy tale) and recording the identifier(s) of its causal predecessor event(s) — including predecessors logged by a different application entirely — lets an investigator reconstruct the complete causal chain of an incident by merging per-application logs into a single graph, following predecessor references directly rather than guessing at correlation.

## Details

The approach models most logged events as SENT or RECEIVED messages: a message is RECEIVED because it was SENT, and it was SENT because of the processing of a prior RECEIVED message, a model that also captures function calls between source modules and system calls from a process to the OS kernel. Context propagation carries a causal predecessor's identifier forward in message metadata (e.g., an HTTP header) across application and even host boundaries, similar to distributed-tracing "context propagation" but extended to protocols (system calls, binary database protocols) that lack native support for it. Because correlation depends only on following predecessor-ID references rather than timestamp proximity, it remains reliable even when clocks across the involved systems are unsynchronized or drifting — directly avoiding the correlation-reliability gap addressed elsewhere by [[techniques/Reconcile cross-layer SDN forensic timestamps using controller-assisted delay estimation]] for timestamp-only correlation.

## Examples

- A proof-of-concept using a customized Nginx web server and an EBPF (Extended Berkeley Packet Filter) Linux kernel module tracked gretel numbers through HTTP requests, Nginx-internal thread handoffs, and system calls/INODE writes across a two-tier Nginx deployment, producing a queryable causal graph (visualized in Gephi) that let an investigator trace an SQL-injection indicator in a database-layer log entry directly back to the originating external IP address logged at the web-server layer.

## Related Objectives

- `DFO-1015` Prepare for a digital investigation
- `DFO-1001` Reconstruct events

## Related Weaknesses

- [[weaknesses/A compromised application can fabricate or omit its own causal log claims undetected]]

## References

- [DFCite-2154] Olegård, Axelsson, and Li, 2025, "When is logging sufficient? — Tracking event causality for improved forensic analysis and correlation", FSI: Digital Investigation 52.

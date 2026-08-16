---
id: DFW-2129
type: weakness
name: Reloading a cached web resource reproduces a stale external timestamp that predates the current access
description: Refreshing a page or reopening a previously visited tab creates a new local access-time record while reusing the external timestamp embedded in the original request, associating an old external time with a new local event and making the pair look like a valid time anchor for the wrong moment.
categories:
  - ASTM_INAC_AS
mitigation_ids:
  - DFM-2130
source_refs:
  - DFCite-2149
updated_at: 2026-08-16
status: complete
---

# Reloading a cached web resource reproduces a stale external timestamp that predates the current access

## Summary

When a browser reloads a page or reopens a tab from history, the resulting cache or history record typically stores a fresh local system-clock timestamp for the new access, but the external timestamp embedded in the record (e.g., a server-issued epoch value in the request URL) can be carried over unchanged from the resource's original retrieval, sometimes hours earlier. Because both a local and an external timestamp are present, the record still qualifies structurally as a time anchor, but the external value no longer corresponds to the local event it is paired with.

## Why It Matters

An examiner comparing the local and external timestamps of such a record without checking whether it represents a reload would either wrongly conclude the clock was skewed (comparing a stale external time against a genuine current local time) or wrongly validate the clock as correct by coincidence, in both cases attributing the external timestamp to the wrong local event. Because reload and reopen actions are common browsing behavior, this is not a rare edge case but a routine source of misleading anchors that must be screened out before an anchor is relied upon.

## Related Mitigations

- [[mitigations/Verify a cached time anchor's external timestamp reflects the current access rather than a prior cached access]]

## Used By

- [[techniques/Validate system clock correctness at event time using paired local-external timestamp anchors]]

## References

- [DFCite-2149] Vanini et al., 2024, "Was the clock correct? Exploring timestamp interpretation through time anchors for digital forensic event reconstruction", FSI: Digital Investigation 49.

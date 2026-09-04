---
id: LWM-1234
type: mitigation
name: Systematically discover and version-track undocumented cloud APIs via automated OpenAPI-schema snapshot comparison
source_refs:
  - LWCite-1245
updated_at: 2026-08-13
status: complete
---

# Systematically discover and version-track undocumented cloud APIs via automated OpenAPI-schema snapshot comparison

## Summary

Rather than only re-validating internal-API mappings manually before each acquisition run, proactively build and maintain a versioned OpenAPI-Specification history for every forensically relevant endpoint used, so a provider-side change is detected automatically as a schema-similarity drop and the specific added/removed/renamed fields are documented rather than discovered as an opaque acquisition failure.

## Addresses

- [[weaknesses/Internal-API-based cloud acquisition breaks when a cloud storage provider changes its website or API implementation]]

## How To Apply

Capture live API traffic through the same sequence of user actions each time an acquisition tool is validated, normalize and decode the request/response records, and generate an OpenAPI Specification snapshot (endpoint path with runtime identifiers abstracted to placeholders, request/response field schemas with observed example values) for every endpoint the acquisition tool depends on. Store each snapshot with a timestamp in a version history database, and before relying on the tool for a live acquisition, compute the Jaccard similarity between the current snapshot and the most recent stored one; treat a similarity drop as a signal that the provider's API has changed, and consult the field-level diff (rather than a generic error code) to determine whether the acquisition tool's parameter mapping needs updating. Because schema-similarity matching can link a functionally equivalent endpoint even when its path has been renamed or refactored, use it in addition to path-string comparison to avoid concluding a data category has disappeared when it has, in fact, simply moved.

## References

- [LWCite-1245] Jeong et al., 2026, "FOREST: Inspecting and tracking RESTful APIs for constructing a cloud forensic knowledge base", FSI: Digital Investigation 56, 302070.

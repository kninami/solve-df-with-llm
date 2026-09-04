---
id: LWM-1113
type: mitigation
name: Re-validate internal-API request parameters and monitor for cloud provider API and website changes before each acquisition run
source_refs:
  - LWCite-1107
updated_at: 2026-08-12
status: complete
---

# Re-validate internal-API request parameters and monitor for cloud provider API and website changes before each acquisition run

## Summary

Before relying on internal-API-based cloud acquisition results, re-verify that the target provider's web client still uses the previously mapped internal API request URLs, parameters, and response formats, and treat unexpectedly sparse or errored results as a possible sign of a provider-side change rather than an empty account.

## Addresses

- [[weaknesses/Internal-API-based cloud acquisition breaks when a cloud storage provider changes its website or API implementation]]

## How To Apply

Periodically re-run internal-API traffic analysis (via a web debugging proxy) against the target provider's current web client and compare the observed request/response format against the acquisition tool's mapped parameters before a live acquisition, updating the mapping if a mismatch is found. Where the tool implements a self-check (comparing API responses against known-good formats and flagging detected changes), enable and monitor it during acquisition, and cross-check any category returning unexpectedly little or no data against the open API's or a commercial tool's results as a sanity check before concluding the account contains no further data.

## References

- [LWCite-1107] Yang et al., 2022, "CATCH: Cloud Data Acquisition through Comprehensive and Hybrid Approaches", FSI: Digital Investigation 43.

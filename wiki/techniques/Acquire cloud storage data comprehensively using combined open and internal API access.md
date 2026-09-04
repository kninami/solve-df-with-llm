---
id: LWT-1108
type: technique
name: Acquire cloud storage data comprehensively using combined open and internal API access
description: Acquire the full contents of a suspect's cloud storage account by combining a provider's official, publicly documented open API with its unofficial internal API (reverse-engineered from the provider's own web client via network traffic analysis), so that resources and categories the open API does not expose — such as a "Personal Vault" or "Recycle Bin" — are still collected.
objective_ids:
  - DFO-1006
weakness_ids:
  - LWW-1113
aliases:
  - CATCH
  - Cloud Data Acquisition through Comprehensive and Hybrid Approaches
  - FOREST
source_refs:
  - LWCite-1107
  - LWCite-1132
  - LWCite-1245
  - LWCite-1262
updated_at: 2026-08-13
status: complete
---

# Acquire cloud storage data comprehensively using combined open and internal API access

## Summary

Commercial digital forensic tools that acquire cloud storage typically rely only on a provider's open (publicly documented) API, which is scoped by the provider and often cannot access certain data categories at all. Reverse-engineering and additionally using the provider's own internal API — the private endpoints its web and desktop clients use internally — closes this gap.

## Details

The CATCH framework structures acquisition into four steps: (1) **Authentication** — obtain access tokens, cookies, or salt values via browser-automation login (handling 2-factor authentication where required) to access resources through either API type; (2) **Exploration** — enumerate file lists, metadata, and thumbnails via both open and internal API calls, normalizing the differing response formats (JSON, HTML, JavaScript) each returns; (3) **Filtering** — narrow the explored resource set by metadata (name, date, extension) or, where supported, content search; and (4) **Collection** — download the filtered resources' full contents via whichever API type supports each category. Internal API endpoints and their required parameters (e.g. authentication cookies, a per-session "canary" token) are identified by intercepting the provider's own web client traffic with a proxy tool during manual browsing. Applied as a case study to Microsoft OneDrive, the internal API alone could access and download files in the 'Personal Vault' category (which the open API can only partially enumerate via metadata, with no working download URL) and the 'Recycle Bin' category (entirely inaccessible via the open API), while two evaluated commercial tools (Magnet AXIOM, Cellebrite UFED Cloud) could not fully collect either category.

**Systematic undocumented-endpoint discovery and longitudinal tracking (FOREST)**: a complementary six-step framework generalizes the internal-API-discovery step beyond cloud storage to any RESTful cloud service, and directly addresses internal-API acquisition's provider-drift problem rather than only working around it. Live API traffic captured through natural user interaction (login, file/message browsing, sending) is preprocessed (decompressing Gzip/chunked payloads into normalized request/response records), then filtered for forensic relevance in three layered stages — target-domain filtering, keyword-based extraction across four semantic categories (user identity, authentication, personal data, service-specific fields), and an LLM prompted with a "forensic analyst persona" to catch content keyword filtering misses. A parameter-dependency module then determines which headers, cookies, query parameters, and body fields are actually required for each endpoint by systematically replaying the request with one component removed at a time and checking whether the response status degrades to an error. The filtered sessions are converted into OpenAPI Specifications (endpoint path, abstracted runtime identifiers, typed request/response schemas with real observed example values) and stored as timestamped snapshots in a versioned API History Database; successive snapshots for the same endpoint are compared via Jaccard similarity over their field-key sets to detect added, removed, or renamed fields — and, by matching on schema overlap rather than path string alone, to link a functionally equivalent endpoint across a renamed or refactored path.

**Driving-insurance telematics (PyShot-style acquisition)**: the same underlying reverse-engineering method applies beyond conventional cloud storage or drone backends to usage-based-insurance ("snapshot") telematics apps. Intercepting a driving-insurance mobile app's own network traffic with a MITM proxy reveals undocumented backend API endpoints (beyond the trip summaries and limited event list the app's own interface displays) that return a driver's complete per-trip telemetry — GPS coordinates, speed, and discrete driving events such as hard braking, acceleration, speeding, and distraction — for use in downstream event reconstruction (see [[techniques/Reconstruct a vehicle incident timeline using driving-insurance-app cloud telematics data]]).

## Examples

- Applied to Microsoft OneDrive, the open API could enumerate but not download files in 'Personal Vault' (empty `name` field, no working content URL) and could not access 'Recycle Bin' at all, while the internal `GetItems` API successfully retrieved full metadata and a working `downloadURL` for files in both categories, outperforming Magnet AXIOM and Cellebrite UFED Cloud on the same test set.
- Applied to DJI's drone-manufacturer cloud backend as a second case study of the same underlying method, reconstructing the mobile app's private API additionally required bypassing SSL/certificate pinning, per-request message authentication codes, anti-replay tokens, and CAPTCHA challenges before account-to-device binding records and cloud-synced flight logs could be retrieved (see [[techniques/Correlate a drone pilot to a drone and remote controller using cloud account-binding and flight-log data]]).
- Applied to Microsoft OneDrive, Microsoft Teams, and Mattermost, FOREST's AI-assisted keyword filtering uncovered undocumented endpoints such as OneDrive's `/v1.0/drive/special/vault` and Teams' call-log message endpoint, exposing names, emails, file structures, and chat/call content with 0.92-0.94 precision and 0.90-0.94 recall against a manually built ground truth; on Mattermost's publicly versioned releases (v3.7.0 to v10.6.1), schema-similarity matching traced six functional endpoint groups (login, team-membership, paginated posts, user listing, team queries, thread access) across renamed or restructured v4 paths that simple path-string comparison would have reported as entirely new, unrelated endpoints.

## Related Objectives

- `DFO-1006` Acquire data

## Related Weaknesses

- [[weaknesses/Internal-API-based cloud acquisition breaks when a cloud storage provider changes its website or API implementation]]

## References

- [LWCite-1107] Yang et al., 2022, "CATCH: Cloud Data Acquisition through Comprehensive and Hybrid Approaches", FSI: Digital Investigation 43.
- [LWCite-1245] Jeong et al., 2026, "FOREST: Inspecting and tracking RESTful APIs for constructing a cloud forensic knowledge base", FSI: Digital Investigation 56, 302070.
- [LWCite-1262] Onik, Spinosa, Asad, and Baggili, 2024, "Hit and run: Forensic vehicle event reconstruction through driver-based cloud data from Progressive's snapshot application", FSI: Digital Investigation 49, 301762.

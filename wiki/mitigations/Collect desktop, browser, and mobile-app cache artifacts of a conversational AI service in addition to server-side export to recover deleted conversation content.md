---
id: DFM-1135
type: mitigation
name: Collect desktop, browser, and mobile-app cache artifacts of a conversational AI service in addition to server-side export to recover deleted conversation content
source_refs:
  - DFCite-1131
updated_at: 2026-08-12
status: complete
---

# Collect desktop, browser, and mobile-app cache artifacts of a conversational AI service in addition to server-side export to recover deleted conversation content

## Summary

Do not treat a conversational AI provider's account-level export or API response as a complete record; also collect and examine the local artifacts left by every client the suspect used to access the service, since deleted-from-account content can still be recoverable from those local caches.

## Addresses

- [[weaknesses/Conversational AI service-side export and API collection cannot recover conversations the user has already deleted]]

## How To Apply

Identify every client the suspect used to access the conversational AI service (desktop application, web browser, mobile app) and image the associated device or profile. Examine the desktop app's local cache and configuration/database files, the browser's cache, local storage, and IndexedDB entries for the service's domain, and the mobile app's local SQLite databases and cache directories, in addition to requesting or extracting the provider's own account-level export or API data. Cross-reference recovered fragments across sources — a partial exchange visible only in a browser cache can sometimes be matched to a timestamp or session identifier still present in the account-level metadata — to reconstruct conversation content that no single source preserves completely.

## References

- [DFCite-1131] Cho et al., 2025, "Conversational AI forensics: A case study on ChatGPT, Gemini, Copilot, and Claude", FSI: Digital Investigation 52.

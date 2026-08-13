---
id: DFT-1059
type: technique
name: Extract application runtime artefacts from process memory using structure signatures
description: Extract forensically relevant runtime artefacts — such as a web server's connection/TLS state, a browser's visited-URL and tab history including private/incognito-mode data, or an instant-messaging app's conversations, contacts, and account information — directly from an application process's memory (a live process dump or a full RAM image) by locating and parsing the application's internal data structures via known object/structure layouts, recovering information no longer available once the process has exited, the application is locked or logged out, or logging/storage files have been deleted, disabled, or never written in the first place.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1064
aliases:
  - Structure-signature-based extraction of web server runtime artefacts from process memory
  - Apache2 web server memory forensics
  - Chracer
  - Object-layout-based Chromium browser memory analysis
  - IM Artifact Finder
  - Telegram Desktop memory artefact extraction
source_refs:
  - DFCite-1054
  - DFCite-1114
  - DFCite-1205
updated_at: 2026-08-13
status: complete
---

# Extract application runtime artefacts from process memory using structure signatures

## Summary

Traditional application forensics relies on log files and stored artefacts, both of which can be absent by design (logging disabled, private/incognito browsing modes that leave no on-disk trace) or deliberately deleted. Because a running application must hold its state — connection data, request/response payloads, visited URLs, tab and window structure — in memory to function, parsing its process memory against known internal structure/object layouts (derived from the application's own C++ class definitions) can recover this information even when it was never persisted to disk.

## Details

**Web server variant (Apache2)**: locates and parses Apache2-specific structures (memory pools, buckets/brigades that hold request/response payload data, `process_rec`/`conn_rec` connection structures, and per-virtual-host TLS configuration including certificate/key file paths and the `SSL_CTX` pointer) within a process memory dump. It was validated against six test scenarios including large POST uploads over TLS, and against three Apache versions (2.2.34, 2.4.43, 2.4.52) spanning over six years to test robustness. The paper positions the extracted structured results as a lower bound: on a full physical memory image, freed-but-not-yet-reused structures could still be recovered, and unstructured pattern search (e.g. for IP addresses and HTTP request lines) found remnants persisting in memory even after the corresponding structures had already been overwritten by further server activity — complementing the structured approach where it reaches its limits.

**Chromium-based browser variant (Chracer)**: identifies the Chromium project's own C++ classes relevant to web browsing activity (`Browser`, `TabStripModel`, `NavigationEntryImpl`, and related tab-group/URL classes) from source code, derives each class's 64-bit object layout (including handling of C++ STL container types `std::string`/`std::u16string`, `std::vector`, and `std::map`), and then scans a process's virtual memory for byte patterns matching those layouts to reconstruct browsing objects. Because private/secret browsing mode is specifically designed to leave no trace on disk, and simple string-search/pattern-matching approaches on memory can recover individual URLs but no context (e.g. whether the browsing occurred in private mode, or which tab group a URL belonged to), the object-layout approach recovers structured, contextualized artefacts — including whether the browser window was in private mode — that neither disk-based nor unstructured memory techniques can provide. A proof-of-concept tool validated the methodology against Google Chrome, Microsoft Edge, and Brave.

**Instant-messaging desktop-app variant (IM Artifact Finder / Telegram Desktop)**: dumps every memory region of a target process (using a purpose-built Windows tool rather than relying on Volatility, which only recovers resident, non-swapped pages) and, for open-source IM applications, derives the internal object model (e.g. `PeerData`, `UserData`, `ChatData`, `HistoryMessage`, `History`) directly from the application's own C++ source code via manual UML analysis. Attributes stored as Qt `QString` objects (phone numbers, message text, usernames) are located by first identifying the fixed byte-level `QString` memory layout (UTF-16 character data starting at a known offset, preceded by a length field), then searching for domain-specific content patterns within that layout (e.g. a general international phone-number digit-group pattern to locate `UserData` objects, or timestamp-string patterns to locate `HistoryMessage` objects). Once an anchor object is found, pointers embedded within it are followed to related objects (sender, parent conversation, owning account) to reconstruct structured, cross-referenced artefacts — conversation content, contacts, and account information — extending the same structure-signature methodology to a case where the artefact of interest is encrypted at rest and the running application may be locked.

## Examples

- Extracted a TLS-enabled virtual host's configuration from memory, including certificate and key file paths and the negotiated cipher suite, even when TLS was in use for the connection itself.
- Recovered a full HTTP response body from a heap bucket structure in all six tested scenarios, including cases using TLS.
- Recovered the list of URLs visited in a Chromium-based browser's private (incognito) mode window directly from process memory, including per-window private-mode status, by carving `Browser`, `TabStripModel`, and `NavigationEntryImpl` objects using their derived 64-bit object layouts.
- Recovered Telegram Desktop conversation content, shared contacts (name and phone number), shared geographic locations, and account/user information directly from a Windows process memory dump by locating `QString`-formatted phone-number and timestamp patterns and following object pointers, with identical results whether the application was unlocked, locked, or logged out — information not otherwise visible through the application's own GUI in the locked/logged-out states.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/In-memory structure layouts change across application versions, breaking structure-signature-based memory forensics]]

## References

- [DFCite-1054] Hilgert et al., 2023, "About the applicability of Apache2 web server memory forensics", FSI: Digital Investigation 46.
- [DFCite-1114] Choi et al., 2023, "Chracer: Memory analysis of Chromium-based browsers", FSI: Digital Investigation 46.
- [DFCite-1205] Fernández-Álvarez and Rodríguez, 2022, "Extraction and analysis of retrievable memory artifacts from Windows Telegram Desktop application", FSI: Digital Investigation 40.

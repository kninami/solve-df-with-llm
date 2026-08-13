---
id: DFT-1131
type: technique
name: Collect conversational AI artifacts across cloud export, desktop cache, browser cache, and mobile app storage
description: Systematically collect forensic artifacts of a suspect's use of a conversational AI service (e.g. ChatGPT, Gemini, Copilot, Claude) from every access surface the service offers — server-side account export/API, desktop application cache, web browser cache and local storage, and mobile app storage — since no single surface preserves the full conversation history.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1135
  - DFW-1202
  - DFW-1216
aliases:
  - Conversational AI forensics artifact collection framework
  - Multi-platform conversational AI (ChatGPT, Gemini, Copilot, Claude) forensic artifact collection
source_refs:
  - DFCite-1131
  - DFCite-1215
  - DFCite-1226
updated_at: 2026-08-13
status: complete
---

# Collect conversational AI artifacts across cloud export, desktop cache, browser cache, and mobile app storage

## Summary

Conversational AI services are typically accessed through several different clients (a web browser, a desktop app, a mobile app) in addition to any account-level export or API the provider offers, and each access surface leaves a different, partially overlapping set of forensic artifacts. Collecting from all available surfaces, rather than relying on a single one, maximizes both the completeness of recovered conversation content and the chance of recovering content the user has already deleted from their account.

## Details

The framework was demonstrated as a case study across four major conversational AI services — ChatGPT, Gemini, Copilot, and Claude — examining artifacts at each access surface: server-side account data (conversation history obtainable via the provider's own export/settings feature or an authenticated API call, when available), desktop application local cache and configuration files, web browser cache/local storage/IndexedDB entries left by the browser-based chat interface, and mobile application local storage (SQLite databases, cache files) on Android and iOS. Different services and different clients retain different levels of detail (e.g. full prompt/response text versus only session metadata), and some artifacts persist locally even after a conversation has been deleted from the user's account, making the offline-client artifacts a critical complement to any server-side or API-based collection. The paper also illustrates the investigative value of this artifact set with a case study of a user prompting Gemini for content that violated the service's own guardrails via a jailbreak-style prompt, showing that the locally cached conversation artifacts preserved the exchange even where the account-level view no longer did.

## Examples

- Recovering a deleted ChatGPT conversation from the Windows desktop app's local cache and SQLite storage after the corresponding conversation had already been removed from the user's account-level chat history.
- Extracting Gemini prompt/response pairs (including a guardrail-bypassing "jailbreak" prompt and its unsafe response) from browser cache artifacts left by the web chat interface.
- Tyagi et al., 2025: on a rooted Android device (Magnet AXIOM-imaged) and a jailbroken/GrayKey-imaged iOS device, ChatGPT and Copilot stored full plaintext conversation content, user account identifiers, and browser-visited-link data locally under each app's own data directory on both platforms; Gemini stored essentially no forensically significant conversation data locally on either platform, instead requiring collection via the account's Google Takeout cloud export, from which prompts, responses, location history, and account profile data (name, gender, email) were recovered.
- Dragonas et al., 2024: a dedicated study of OpenAI's ChatGPT mobile app on Android and iOS found conversation content stored in plaintext JSON files (iOS, under `/Library/Application Support/conversations-account-ID/`) or a SQLite database (Android, `<user-ID>_<account-ID>_conversations.db`, with metadata in the `DBConversation` table and message text in `DBMessage`), plus draft messages, added custom-GPT metadata, and PII (account ID, user ID, device ID, workspace ID, external IP address) scattered across accompanying protobuf/plist/XML preference files; the cloud-native data export (requested in-app and delivered by email as a `.zip` archive) instead surfaces `conversations.json` (full metadata), `chats.html` (content without metadata), `user.json`, `shared_conversations.json`, `message_feedback.json`, and `model_comparisons.json`. At the time of study, none of Cellebrite Physical Analyzer, Oxygen Forensic Detective, ALEAPP, iLEAPP, or RLEAPP could parse the app's data automatically, requiring manual database/JSON review until the authors' own contributed ALEAPP/iLEAPP/RLEAPP parsers were adopted.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Conversational AI service-side export and API collection cannot recover conversations the user has already deleted]]
- [[weaknesses/Location data recovered from an LLM mobile app artifact may reflect IP-based geolocation rather than the device's actual GPS position]]
- [[weaknesses/Conversation identifiers for the same conversational AI exchange can diverge across a user's client platforms and cloud export]]

## References

- [DFCite-1131] Cho et al., 2025, "Conversational AI forensics: A case study on ChatGPT, Gemini, Copilot, and Claude", FSI: Digital Investigation 52.
- [DFCite-1215] Tyagi et al., 2025, "Forensic analysis and privacy implications of LLM mobile apps: A case study of ChatGPT, Copilot, and Gemini", FSI: Digital Investigation 54, 301974.
- [DFCite-1226] Dragonas et al., 2024, "Forensic analysis of OpenAI's ChatGPT mobile application", FSI: Digital Investigation 50, 301801.

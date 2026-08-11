---
id: DFT-1022
type: technique
name: Streaming application cache artifact recovery
description: Recover evidence of a user's engagement with live or replayed streamed video by examining an Android streaming application's own cache directories for still images, video fragments, and metadata files, since streamed content is generally not stored as a single reconstructable media file.
objective_ids:
  - DFO-1011
weakness_ids:
  - DFW-1022
aliases: []
source_refs:
  - DFCite-1015
updated_at: 2026-08-09
status: complete
---

# Streaming application cache artifact recovery

## Summary

Because live-streamed and replayed video is rarely cached as a single playable file, forensic recovery instead targets the application-specific cache/data directory for fragments: still images (thumbnails, profile pictures, category previews), structured preference files (XML/plist-style key-value stores recording watch time, recent searches, last-played timestamps), and — for some platforms — encrypted or chunked media segments that may be partially viewable after format-specific reconstruction.

## Details

Caching behavior is inconsistent across streaming platforms and is not predictable from a platform's desktop/browser behavior: some applications (Instagram Live) cache almost everything regardless of content type, others (Twitch, Reddit) cache only previews and metadata but no reconstructable video, and some (Facebook Live, YouTube Live, Periscope) cache differently depending on whether content is live or a replay. Where reconstructable fragments exist, file-signature carving (e.g., locating JFIF/PNG/RIFF headers within monolithic `.cache` container files) or format-specific decoding (e.g., YouTube's serialized-Java-object `media.pb` chunks, or renaming `.exo` chunks to `.mp4`) can recover viewable content. Structured preference files often retain quantitative usage evidence (e.g., total minutes watched, most recently watched item IDs) independent of whether any video fragment itself survives.

## Examples

- Twitch's `recently_watched.xml` retained a game ID and Unix-timestamp pair for the last time a specific game category was viewed, cross-referenced against Twitch's public game-ID list to identify the exact title watched.
- YouTube Live's `media.pb` file (a serialized Java object) contained the last playback timestamp for a video, recoverable by locating its known Java-serialization file signature within the cache container.

## Related Objectives

- `DFO-1011` Extract artifacts stored by applications

## Related Weaknesses

- [[weaknesses/Android application cache-clear operation purges recoverable streaming video artifacts]]

## References

- [DFCite-1015] García Murias et al., 2023, "A forensic analysis of streaming platforms on Android OS", FSI: Digital Investigation 44.

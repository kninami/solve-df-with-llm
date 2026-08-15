---
id: DFT-1257
type: technique
name: Extract evidentiary data from Android log messages using string and taint analysis
description: Automatically identify which log messages an Android app's logging-system entries contain forensically relevant data (GPS coordinates, timestamps, device IDs, URLs, text input) and extract the specific value, by pre-building a per-app database of "tainted" string-pattern automata that combine static string analysis with taint tracking from known evidentiary source APIs through to the logging-system sink.
objective_ids:
  - DFO-1017
weakness_ids:
  - DFW-1077
aliases:
  - LogExtractor
  - App Log Evidence Database (ALED)
source_refs:
  - DFCite-1297
updated_at: 2026-08-14
status: complete
---

# Extract evidentiary data from Android log messages using string and taint analysis

## Summary

Android's logging system is a rich but easily-missed evidentiary source: apps routinely write GPS coordinates, timestamps, device identifiers, URLs, and user text input into log messages, but a log message's raw string content gives no indication of what type of evidentiary data, if any, it contains, or where within the string the value sits — keyword search is unreliable since apps format the same evidence type inconsistently (e.g. "latitude,longitude" vs. "longitude,latitude" order, with or without labeling keywords). Statically analyzing an app's code offline to build a per-app database of "tainted" finite-state automata — each modeling a specific log message's string pattern together with which segments of that pattern carry which evidence type — lets an investigator later match a suspect device's actual log messages against the database and extract the evidentiary value automatically and reliably.

## Details

The offline phase extends the Java String Analyzer (JSA) with a new "tainted DFA" data structure — a deterministic finite automaton paired with a taint table mapping automaton states to evidence types — and new taint-propagation rules that track evidentiary data from known Android source APIs (e.g. `getLatitude()`) through string concatenation, formatting, and other operations, all the way to the 14 Android logging APIs treated as sinks. Because JSA was built for general Java programs, the analysis is extended with FlowDroid- and IccTA-derived call graphs to model Android-specific lifecycle callbacks and inter-component communication, without which many app data flows would be invisible to the underlying string analyzer. The resulting per-app, per-log-message tainted DFAs are stored in an App Log Evidence Database (ALED), keyed by package name and log level. In the online phase, a log message retrieved from a suspect's device (e.g. via ADB) is matched against the ALED's automata for the app that produced it; a successful match against a DFA whose taint table includes evidentiary data both confirms the message contains evidence and — walking the specific automaton states the message's characters passed through — extracts exactly which substring corresponds to which evidence type, without the investigator needing to manually infer the message's ad hoc format.

## Examples

- Evaluated against 65 DroidBench benchmark apps that write to the Android log, the tool achieved 97.7% precision and 79.2% recall at determining whether a log message contains evidentiary data, and extracted the correct value from 100% of the messages it correctly identified as containing evidence.
- Building an ALED for 12.1 K real-world apps from AndroZoo and PlayDrone found 5,382 apps write log messages containing at least one of latitude, longitude, altitude, mailing address, text input, database information, network information, or calendar information, with 1,688 apps alone writing latitude/longitude coordinates to their logs.
- A manual end-to-end verification against 91 randomly sampled real-world apps (over 90,000 collected log messages, 266 confirmed to contain evidentiary data) found the tool correctly identified 230 of the 266 evidentiary messages, achieving 86.5% precision and 91.3% recall, and correctly extracted the data value from all 230 correctly-identified messages.
- A real-world case study confirmed the technique resolves the ambiguity a manual keyword search cannot: three different apps encoded GPS coordinates as "lat"/"lon"-keyword-labeled fields, unlabeled latitude-then-longitude fields, and unlabeled longitude-then-latitude fields respectively, all of which LogExtractor correctly disambiguated and extracted, while a fourth app's log message encoded a value that was a valid-looking number but was in fact a Unix timestamp, which existing generic log parsers could not identify as time-relevant.

## Related Objectives

- `DFO-1017` Extract artifacts stored by the operating system

## Related Weaknesses

- [[weaknesses/Android's volatile circular log buffers discard older entries and are lost entirely on power loss]]

## References

- [DFCite-1297] Cheng, Shi, Gong and Guan, 2021, "LogExtractor: Extracting digital evidence from android log messages via string and taint analysis", DFRWS 2021 USA; FSI: Digital Investigation 37, 301193.

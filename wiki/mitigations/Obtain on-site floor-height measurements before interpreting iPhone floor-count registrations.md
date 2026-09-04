---
id: LWM-1247
type: mitigation
name: Obtain on-site floor-height measurements before interpreting iPhone floor-count registrations
source_refs:
  - LWCite-1261
updated_at: 2026-08-13
status: complete
---

# Obtain on-site floor-height measurements before interpreting iPhone floor-count registrations

## Summary

Before drawing a conclusion about which or how many physical floors a device's registered floor-ascent or floor-descent count represents, obtain detailed information about the actual height differences between floors at the specific site under investigation, and account for elevator or escalator use rather than assuming the registered count directly equals the number of physical floors traveled.

## Addresses

- [[weaknesses/iPhone floor-count registrations do not correspond one-to-one with physical floors ascended or descended]]

## How To Apply

Where possible, carry out on-site experiments with a comparable iPhone model at the specific location under investigation to establish the actual relationship between the site's floor-to-floor height differences and the resulting registered floor count, since the roughly 3 m-per-floor rule is an approximation validated at only 70-80% accuracy. Check the scene and any available evidence for indications of elevator or escalator use during the relevant time window, since neither reliably registers as ascended or descended floors, and explicitly caveat any floor-placement conclusion drawn from Health app data with the measurement's known accuracy range.

## References

- [LWCite-1261] van Zandwijk, Lensen, and Boztas, 2023, "Have you been upstairs? On the accuracy of registrations of ascended and descended floors in iPhones", FSI: Digital Investigation 47, 301660.

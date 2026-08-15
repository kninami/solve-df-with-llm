---
id: DFW-1280
type: weakness
name: Your Phone deletes a notification record from its local database as soon as it is acknowledged on the phone
description: Once a Your Phone notification alert is acknowledged (dismissed or actioned) on the linked smartphone, its record is deleted from the Windows-side notifications database, so a straightforward live query of the notifications table only ever shows currently pending alerts and silently omits every notification the phone's user has already handled.
categories:
  - ASTM_INCOMP
mitigation_ids:
  - DFM-1281
source_refs:
  - DFCite-1308
updated_at: 2026-08-15
status: complete
---

# Your Phone deletes a notification record from its local database as soon as it is acknowledged on the phone

## Summary

The Windows-side `notifications.db` database's `notifications` table holds an alert's originating-app JSON payload and posted timestamp only for as long as the alert remains unacknowledged at the phone. As soon as the phone's user acknowledges the notification, its row is removed from the live table, so an investigator who only queries the live table sees exclusively the alerts that happened to still be pending at the moment of acquisition.

## Why It Matters

An investigator relying on a live-table read of `notifications.db` will conclude that few or no notifications were received during the monitored period, when in fact the phone's user may have received and dismissed a large number of them — understating the true volume and content of activity relayed through Your Phone and potentially omitting notification content directly relevant to the investigation (e.g. a message-preview notification from an app not otherwise imaged).

## Related Mitigations

- [[mitigations/Apply SQLite deleted-record recovery tools to Your Phone's local databases before relying on live-table content alone]]

## Used By

- [[techniques/Extract cross-device messaging, call, and photo-sync artifacts from Microsoft's Your Phone SQLite databases]]

## References

- [DFCite-1308] Domingues, Andrade, and Frade, 2021, "Microsoft's Your Phone environment from a digital forensic perspective", FSI: Digital Investigation 38, 301177.

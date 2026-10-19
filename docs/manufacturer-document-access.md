# Manufacturer documentation network access

The earlier manufacturer proxy blocker is resolved. On 2026-10-19, both the Microchip product page and Atmel-ICE PDF downloaded successfully through the configured proxy.

## Verified destinations

These exact destinations now work in the running environment:

- `www.microchip.com` — product information and manual links.
- `ww1.microchip.com` — manufacturer PDF downloads.

These are Internet-access settings; no manufacturer credential or secret was needed for the successful requests.

## Retrieved and remaining documents

- **Retrieved and read:** [Atmel-ICE User Guide, Atmel-42330C, October 2016](research/manufacturer/atmel-ice-user-guide-42330c.pdf), directly from Microchip. Its [local provenance record](research/manufacturer/atmel-ice-user-guide-42330c.json) records the source and checksum. [Verified pinout and voltage details](hardware/atmel-ice-pinout.md) are available for TASK-3.
- **Page retrieved; routing document not recovered:** the [ATARD-DBGADPT product page](https://www.microchip.com/en-us/development-tool/atard-dbgadpt) loads, but its public documentation section supplied no shield guide or schematic link. This is now a document-availability gap rather than the previous proxy denial. Shield assembly A09-2340/02 routing remains unverified.

## If a later request is blocked

No further network-setting action is needed for the two verified hosts. If a later document redirects to another host, Codex should identify the exact blocked destination before proposing a network addition. Preserve all existing settings when applying changes, save/publish the configuration, and retry the affected request.

An allowed domain does not prove that an individual manual URL exists or that the manufacturer permits the request. If the saved policy includes the host but the runtime still rejects the connection, use the environment's reconnect option if available and retry; persistent proxy errors require platform support.

If downloading the public manuals works on the owner's phone or MacBook, the original PDFs can alternatively be attached in chat or placed on the Notion inbox page. The photo importer deliberately skips PDFs, so documentation attachments need a separate retrieval step.

## Documents needed for TASK-3

- Atmel-ICE user guide: SAM connector pinout, target-voltage range and voltage-reference behavior, and cable orientation.
- Atmel ATARD-DBGADPT Debug Adapter Shield user guide and schematic: routing for the photographed A09-2340/02 assembly and connector references.

No cable pin mapping is considered verified until the relevant documentation has been read and matched to the equipment photographs.

# Debug equipment and cable evidence

Date: 2026-10-19. Related task: TASK-3. Target: [SB-FB-001](force-band-01.md).

## Received photographs

Three equipment photographs were imported from the Notion inbox. Each is 4032 × 3024 pixels. Downloaded byte sizes, SHA-256 checksums, and full image decoding were verified; source blocks are recorded in the [Notion manifest](photos/notion-manifest.json).

| Photograph | Direct observations |
|---|---|
| [Atmel-ICE and attached cable](photos/notion-dfebf588de7cc1753da37ff4a4061771f3d1ad273d4496f34a826114a46e76a8.jpg) | Atmel-ICE enclosure labeled SAM and AVR; attached ribbon cable with a red edge and multiple connector ends. The user confirms an end can connect to the shield. The angle obscures exact probe-port engagement and connector pin-1 orientation. |
| [Shield underside](photos/notion-023870ecd11f4d0fcab1104ab9cf3a57598872ae4e73efec61935c6305f431be.jpg) | Atmel Corp © 2014; board label `A09-2340/02`; connector references including J106, J107, and J108. Packaging identifies part number `ATARD-DBGADPT`. |
| [Shield component side](photos/notion-1f7df1b642478846d18003fc0c2ea6a052d015087b86970f8ce5f1e36c54b0b8.jpg) | Atmel Debug Adapter Shield, matching packaging part number `ATARD-DBGADPT`; Arduino-style headers labeled POWER, AD, IOH, and IOL; several smaller debug/programming connectors. |

The shield is now physically identified as **Atmel ATARD-DBGADPT**, with assembly label **A09-2340/02**. The label is transcribed as observed; its revision-field interpretation has not been checked against a schematic.

## What the photographs establish

The owner has an Atmel-ICE, the shield, and a cable intended to connect them. Mechanical fit alone does not establish that a particular shield connector exports the Force Band's required SWD signals or that the cable has the assumed pin mapping. The shield's Arduino-style `3V3`, `5V`, and `IOREF` labels are not verified voltage-reference or power connections for this target.

Before connecting the Force Band, document:

1. The Atmel-ICE SAM connector pinout and exact cable-end mapping, including pin 1.
2. The shield schematic/header routing for `ATARD-DBGADPT` and the photographed assembly.
3. The final accessible SWDIO, SWCLK, ground, and voltage-reference connection points.
4. The measured Force Band logic supply and its compatibility with the probe's documented target-interface range.

The probe's [documented SWD pinout](atmel-ice-pinout.md) is now recorded from the manufacturer guide, for both SAM and AVR ports. Shield routing and the physical cable mapping remain unverified, so no board-to-probe wiring is prescribed yet. No debugger-to-Force-Band connection, continuity check, or voltage measurement has been reported.

## Documentation access

The manufacturer-network blocker is resolved: the Microchip product page and Atmel-ICE user-guide PDF now download successfully. The guide has been read, archived, and used to record the [probe pinout, voltage range, and VTG behavior](atmel-ice-pinout.md).

The current ATARD-DBGADPT product page did not yield a public shield schematic/user-guide link. Its connector routing remains unresolved. See [manufacturer-document access](../manufacturer-document-access.md) for retrieval status. No additional domain change is currently required for the two successfully tested hosts.

The [annotated target-pad reference](pad-reference.md) is available independently of the manual retrieval; actual voltages and connections remain unverified.

## Next owner input

Provide the digital multimeter's make/model, or a clear photograph of its front showing the selector and input sockets. The next measurement sheet should identify exact probe points, meter mode, power state, and the reading to report. It should be prepared after the available meter and accessible board contacts are established.

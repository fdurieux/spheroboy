# Sphero Force Band 01

Project identifier: **SB-FB-001** (an internal label, not a manufacturer serial number).  
Record date: 2026-10-19.  
Related task: TASK-1.

## Selected hardware

The project uses the owner's existing **Sphero Force Band**, the wrist-mounted controller supplied with the Sphero BB-8 toy. The owner confirmed that this Force Band will be modified. See the [decision record](../decisions/0002-modify-existing-force-band.md).

The first imported conversation associates the board with the toy's remote-control component; the [packaging photograph](photos/conversation-1-message-129-part-00.jpg) shows the special-edition BB-8 with Force Band set. The earlier Oral-B photographs and the final Philips WiZ bulb photograph are separate hardware discussions.

## Reviewed board photographs

The following three original photographs have been visually reviewed. They show the same component side of the Force Band PCB:

| Photograph | Visible evidence |
|---|---|
| [Board overview](photos/conversation-1-message-116-part-02.jpg) | White PCB in the wrist-band casing, micro-USB socket, button, speaker, antenna wire, major ICs, and board silkscreen `00-001000` / `REV15` |
| [Upper-board close-up](photos/conversation-1-message-116-part-00.jpg) | Micro-USB socket, button, U1, U7, U8, and adjacent components |
| [Lower-board close-up](photos/conversation-1-message-116-part-01.jpg) | U1 marking `N52832`, flash-package markings, speaker, and revision silkscreen |

The new MCU close-up and manufacturer marking tables now confirm **nRF52832-QFAA with 512 KiB internal flash and 64 KiB RAM**. See the [MCU and memory record](mcu-and-memory.md) for photographs, specifications, confidence limits for the external flash, and documentation sources. No electrical measurements or debugger connection have been performed here.

Two additional full-resolution photographs were imported from the Notion inbox and visually reviewed on 2026-10-19:

| Photograph | Visible evidence |
|---|---|
| [Component side, removed from casing](photos/notion-3550f5ded18391aed3ecc2e0ddef4efb5d62957787ae6f40a37d9b964fe30f9a.jpg) | Entire board, U1, flash, speaker, button, antenna wire, attached round motor, and `00-001000` / `REV15` silkscreen |
| [Reverse side](photos/notion-53dd11c2f5456bccee28ca13f87c8e14c34bc024ef9bd5ba674f5568d43f3585.jpg) | Entire reverse side with readable pad labels including `SWDIO`, `SWCLK`, `GND`, `3V3`, `UART TX`, `UART RX`, and SPI labels |

Both PCB sides are now documented clearly enough for TASK-1. The two imported files are 4032 × 3024 pixels; their bytes, hashes, and full image decoding were verified. The visible labels provide evidence for later connection mapping; no pad voltage, continuity, or electrical function has been measured or verified.

The [Notion manifest](photos/notion-manifest.json) records the source page/block IDs and checksums. The [Notion index](photos/notion-index.md) links to the source blocks.

Conversation-photo filenames, source message IDs, and SHA-256 checksums are preserved in the [photo manifest](photos/manifest.json). Notion publication photos have private metadata removed without pixel recompression; their [manifest](photos/notion-manifest.json) distinguishes original and published hashes. The original photo pixels remain unchanged, and the generated annotation is a separate file. See [publication checks](../publication-checks.md).

## Available equipment

Ownership was explicitly confirmed by the user on 2026-10-19:

| Equipment | Recorded model/name | Version or revision |
|---|---|---|
| Logic analyzer | Saleae Logic 8 | Logic software and hardware revision not yet recorded |
| Debug probe | Atmel-ICE | Probe firmware version not yet recorded |
| Adapter | Atmel Debug Adapter Shield, ATARD-DBGADPT | Photographed assembly label A09-2340/02; schematic/revision interpretation pending |

These model names satisfy the initial equipment inventory. Missing versions can be recorded when establishing the local tool setup. The shield is now identified from the new photos; see the [debug-equipment record](debug-equipment.md). Its pinout, cable mapping, and suitability for the Force Band remain to be established before wiring it.

No multimeter or soldering equipment ownership has been confirmed. Assess those needs when planning physical measurements and connections.

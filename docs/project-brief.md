# Project brief

## Goal

Investigate repurposing a Sphero Force Band as a general-purpose programmable wrist computer. The original discussion expresses interest in Lua and asks whether additional RAM would help. A small display and motion-controlled Pong or Breakout are proposed milestones in the second conversation, rather than a finalized hardware specification.

## What is established

- Two shared conversations have been imported into [the research archive](research/conversations/README.md).
- The first discussion explores several devices before discussing a Force Band. Earlier toothbrush observations must not be assigned to the Force Band.
- The user has selected their existing Sphero Force Band for modification, recorded as [SB-FB-001](hardware/force-band-01.md).
- The user owns a Saleae Logic 8, an Atmel-ICE, and an Atmel Debug Adapter Shield. New [equipment photographs](hardware/debug-equipment.md) identify the shield as ATARD-DBGADPT with assembly label A09-2340/02 and show the Atmel-ICE with its cable. Software/firmware versions and electrical cable mapping remain unrecorded; compatibility still requires verification.
- No board measurements, local debugger sessions, or firmware builds have been performed in this workspace.
- The [new MCU close-up and Nordic documentation](hardware/mcu-and-memory.md) confirm **nRF52832-QFAA, 64 MHz Cortex-M4F, 512 KiB internal flash, and 64 KiB RAM**. The rated MCU VDD range is 1.7–3.6 V and the debug interface is SWD; board voltage and access remain unmeasured.
- All 16 user image attachments from the first conversation have been recovered into the [photo archive](hardware/photos/README.md). The second conversation has no user image attachments. Three photographs from message 116 show the same component side of the selected Force Band PCB. Two additional Notion photos now provide readable full-board views of both sides, documented in [SB-FB-001](hardware/force-band-01.md).

## Working hypotheses

Remaining claims and open verifications:

| Claim | Needed evidence |
|---|---|
| External flash is a Winbond W25Q40-family part with 512 KiB storage | `25Q40` marking supports the capacity; exact suffix, manufacturer datasheet for that suffix, voltage, and JEDEC read remain unresolved |
| U7 is a TAS2505 audio device | `TAS / 2505` marking is visible; peripheral specifications and board connections still need documentation |
| A motion sensor can supply game input | Identified sensor, bus capture, and decoded motion data |
| Atmel-ICE can access this target through OpenOCD | Probe firmware details, confirmed wiring, and a non-destructive connection log |
| Lua can fit alongside the desired features | A build for the confirmed MCU and measured memory usage |
| A display can be added | Verified GPIO availability, electrical compatibility, power budget, and enclosure fit |

The MCU capacity is now based on the photographed `QFAAB0` marking: Nordic explicitly maps the `AA` function variant to 512 KiB flash and 64 KiB RAM. Available application RAM and flash will be smaller than the hardware totals and must be measured after a firmware build. External flash does not expand ordinary Lua heap memory.

## Decisions

The accepted [documentation workflow](decisions/0001-project-records.md) uses Notion as a notebook, Git as the technical record, and Backlog.md for tasks. The owner has [chosen to modify the existing Force Band](decisions/0002-modify-existing-force-band.md). No firmware SDK, display, runtime, or programming procedure has been selected.

## Open questions

1. What are the exact external-flash suffix and remaining peripheral identities?
2. What are the measured power rails and verified pad-to-signal connections? Reverse-side silkscreen labels are readable, but electrical functions remain unverified.
3. Is non-destructive debug/read access possible, and can original firmware be backed up?
4. Which display and runtime fit the verified hardware and first application?

## Next work

TASK-1's hardware evidence and TASK-2's MCU identification are complete. Next is TASK-3 in the [backlog](../backlog/README.md): document measured power rails and candidate debug connections. The reverse-side labels provide starting evidence, but measurements are needed before connecting the debugger. Sensor capture and display investigation follow the verified board findings.

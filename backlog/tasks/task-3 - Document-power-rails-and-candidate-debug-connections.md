---
id: TASK-3
title: Document power rails and candidate debug connections
status: In Progress
assignee:
  - '@codex'
created_date: '2026-10-19 18:04'
updated_date: '2026-10-19 20:30'
labels:
  - hardware
dependencies:
  - TASK-2
references:
  - docs/research/conversations/README.md
documentation:
  - docs/project-brief.md
  - docs/hardware/README.md
  - docs/hardware/debug-equipment.md
  - docs/hardware/pad-reference.md
  - docs/manufacturer-document-access.md
  - docs/hardware/atmel-ice-pinout.md
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Probe connections require a board-specific map supported by measurements and documentation. Photos show Force Band test-pad labels, and the supplied equipment photos identify the shield as Atmel ATARD-DBGADPT (assembly label A09-2340/02). Board voltage and cable signal mapping are not yet verified.

## Responsibilities and prerequisites

| Needed | Responsible person | Action and current status |
|---|---|---|
| Digital multimeter with DC-voltage and continuity/resistance modes | Owner | Provide its make/model or a clear front photo showing selector and input sockets. Awaiting input. Fine probe tips and an insulated ground clip help contact small pads. |
| Exact adapter and cable identification | Owner supplies evidence; Codex documents it | Photos of both shield sides and the Atmel-ICE with attached cable received and imported. Shield identified as ATARD-DBGADPT, assembly label A09-2340/02. Exact cable-end orientation and electrical mapping remain to be verified. |
| Board and connector map | Codex | Identify candidate GND, supply, SWDIO, and SWCLK points from PCB photographs; check Nordic, Atmel-ICE, and shield documentation. Nordic MCU specifications are recorded. A separate annotated pad-reference image now identifies P1 GND, P2 3V3, P3 SWCLK, and P4 SWDIO; electrical functions and voltages remain unverified. Manufacturer network access now works. Atmel-ICE User Guide Atmel-42330C has been retrieved and read; SAM and AVR SWD pinouts, cable orientation, and VTG reference behavior are documented. The ATARD-DBGADPT page loads, but no public shield schematic/user-guide link was recovered; shield routing remains unresolved. |
| J1 alternate connector mapping | Owner measures; Codex interprets | Record the four J1 positions as project labels A through D, top to bottom in the upright reverse-side photo (D is square). With USB and battery disconnected, measure resistance from each position to P1–P4. Do not assume SWD pin order from the four-hole count. No readings yet. |
| Ground and signal continuity checks | Owner, following the Codex measurement sheet | With USB and battery disconnected, measure resistance between the exact accessible points specified in the sheet. Awaiting the measurement sheet and physical readings. Never use continuity/resistance mode on a powered board. |
| Supply-voltage measurements | Owner, following the Codex measurement sheet | Power the Force Band normally and measure the specified supply points relative to verified ground in DC-voltage mode. Record readings and the power state. Awaiting physical readings. |
| Evidence and compatibility assessment | Codex | Record supplied readings, annotate the board map, document connector orientation, and check the debugger voltage-reference requirements against the measured target rail. Awaiting measurements and documentation. |

The measurement sheet will name exact probe points, meter mode, power state, and readings to report. A cable fitting the shield does not by itself establish correct SWD routing. TASK-3 records the connection map and evidence; live debugger access belongs to TASK-5.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 An annotated board view identifies ground, measured target supply rails, and candidate debug pads.
- [ ] #2 Each proposed connection records supporting measurements or datasheet tracing and unresolved uncertainty.
- [ ] #3 Instrument connector pinouts and target voltage compatibility are documented before any debugger connection.
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Import and inspect the adapter and Atmel-ICE cable photographs; identify visible connector labels and part numbers. 2. Check available manufacturer or board-vendor pinout documentation and distinguish documented signals from unverified cable mapping. 3. Record the equipment evidence and candidate connection map, then prepare specific measurements once the owner provides a multimeter model. 4. Complete acceptance criteria only after board voltage and connection measurements are recorded.

5. Prepare a separate annotated reference photo for the four silkscreen-labeled GND, 3V3, SWCLK, and SWDIO pads; verify marker placement against the untouched original and retain measurement status as unknown. 6. Save manufacturer-domain additions in the environment draft and document the required apply/publish step.

7. Investigate J1 as a potential alternate connection: record its four physical positions and obtain unpowered resistance readings to the labeled pads before assigning signals.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Imported three new Notion equipment photos; sizes, hashes, and full decoding verified. Visually identified the Atmel Debug Adapter Shield as ATARD-DBGADPT, assembly A09-2340/02. Recorded both shield sides and the Atmel-ICE ribbon-cable view in docs/hardware/debug-equipment.md. User confirms cable can connect to the shield; signal mapping and pin-1 orientation remain unverified. Added an owner/action/status table at the user’s request, marking equipment photos received and multimeter identification outstanding. Microchip documentation retrieval returned HTTP 403. No physical measurements or debugger-to-target connection performed; all acceptance criteria remain unchecked.

Saved docs/hardware/annotations/force-band-reverse-pads.png and docs/hardware/pad-reference.md. Visually checked the four annotated small-pad locations against the untouched source photo; corrected the initial P2 marker before saving. The image is a generated visual aid, and original geometry/trace evidence remains the source photo. Recorded provenance hashes and explicit unknown measurement fields. J1 has three round and one square through-hole pads; added project reference labels J1-A through J1-D and an unpowered resistance matrix against P1–P4. No J1 signal mapping or pin numbering is established. Added www.microchip.com and ww1.microchip.com to the environment network draft, preserving existing domains. Owner must save/publish before retrying manufacturer documents. All TASK-3 criteria remain unchecked because measurements and instrument mapping are outstanding.

Manufacturer retry succeeded for the Microchip product page and Atmel-ICE User Guide PDF. Archived Atmel-42330C (10/2016), SHA-256 e3fc67fea09cc891b3497f337a9f00be08dae591fa91892b13e9ee0605f57cf0. Independently reviewed manual sections 2.6, 3.1, 4.2.4–4.2.5, and 5.4.1; recorded both SAM/AVR SWD mappings and 1.62–5.5 V probe target range in docs/hardware/atmel-ice-pinout.md. VTG is a reference input, not target power; target MCU limits remain 1.7–3.6 V and actual voltage is unmeasured. Photo appears to show AVR selected; this is not automatically wrong because port selection depends on connector routing. Physical mapping still needs confirmation. Official shield product page's public documentation section yielded no guide or schematic; compliance association endpoint returned no documents. No shield routing inferred. Network blocker resolved; target measurements, multimeter model, and shield/cable mapping remain outstanding. All criteria remain unchecked.
<!-- SECTION:NOTES:END -->

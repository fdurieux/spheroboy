# Hardware record

The selected hardware is the owner's existing Sphero Force Band, recorded as [SB-FB-001](force-band-01.md). That record includes reviewed board photographs and the confirmed equipment inventory. Electrical pin mappings remain unverified. Candidate parts are listed in the [project brief](../project-brief.md); see the [research conversations](../research/conversations/README.md) for their origin.

The [MCU and memory identification](mcu-and-memory.md) confirms the nRF52832-QFAA's 512 KiB flash and 64 KiB RAM against Nordic's marking table. The external Winbond flash is consistent with 512 KiB storage; its full suffix and supply voltage remain unresolved.

The [front-side component inventory](front-side-components.md) identifies the main ICs and visible controls/transducers, and records uncertain parts separately. U8's exact sensor identity and the small power/support ICs remain unresolved.

The [debug-equipment record](debug-equipment.md) identifies the Atmel ATARD-DBGADPT shield and records the Atmel-ICE cable photographs, verification gaps, and the next measurement prerequisite.

The [Atmel-ICE pinout](atmel-ice-pinout.md) records both probe ports' manufacturer-documented SWD assignments, cable orientation, target-voltage range, and voltage-reference behavior. Target and shield wiring remain unverified.

The [annotated reverse-side pad reference](pad-reference.md) locates candidate GND, 3V3, SWCLK, and SWDIO pads. It distinguishes visible labels from the measurements and electrical verification still needed.

All 16 user image attachments from the first conversation are now available in the [photo index](photos/README.md), with source references and checksums. Filenames preserve conversation positions; they do not assert which device or component is shown.

## Recording evidence

Keep component identification, pin mapping, power measurements, and instrument setup here. Use a dated Markdown record with:

- Device identifier, board revision if readable, date, and operator.
- Photograph or capture filename and source.
- Direct observation, including units and instrument settings.
- Interpretation and confidence, separately from the observation.
- Relevant manufacturer documentation and exact part variant.
- Linked task and remaining uncertainty.

Store recovered PCB photographs in a `photos/` subdirectory with descriptive filenames. Record measurements against an annotated photograph or clearly defined board orientation; avoid pin names based only on visual guesses.

## Investigation order

Recover photographs and identify the experiment device, confirm component markings, then map power and candidate interfaces. Verify logic voltage and connector pinout before connecting probes. Record the preservation decision before any operation that can erase or replace firmware. The imported OpenOCD command is a research example, not a tested board procedure.

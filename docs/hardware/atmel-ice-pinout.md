# Atmel-ICE documented SWD pinout

Related task: TASK-3. Equipment: [Atmel-ICE and ATARD-DBGADPT photos](debug-equipment.md). Verified against the manufacturer guide on 2026-10-19.

## Source

[Atmel-ICE User Guide, Atmel-42330C, October 2016](../research/manufacturer/atmel-ice-user-guide-42330c.pdf), retrieved directly from [Microchip's PDF server](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42330-Atmel-ICE_UserGuide.pdf). The local [provenance record](../research/manufacturer/atmel-ice-user-guide-42330c.json) includes its source URL, size, and SHA-256 checksum.

The tables below describe the **probe connector**, not the shield's Arduino headers, the shield's small connectors, or the Force Band's J1 footprint. They are not a completed board-to-probe wiring instruction.

## SWD signal assignments

The manufacturer documents SWD mappings for both probe ports. The correct port depends on the target connector's wiring, rather than the MCU brand alone. Table 4-4, page 29, supplies both columns:

| Signal | SAM port pin(s) | AVR port pin(s) | Purpose |
|---|---|---|---|
| VTG | 1 | 4 | Target voltage-reference input |
| SWDIO | 2 | 5 | SWD data |
| SWDCLK | 4 | 1 | SWD clock |
| GND | 3, 5, 9 | 2, 10 | Common ground; the manual specifies connecting all listed grounds |
| SWO | 6 | 3 | Optional trace signal |
| nSRST | 10 | 6 | Target reset; target-specific use still needs establishing |

The standard SAM/Cortex 10-pin layout is shown in Figure 4-4, page 28:

```text
   1 VTG       2 SWDIO
   3 GND       4 SWDCLK
   5 GND       6 SWO
   7 KEY       8 NC
   9 GND      10 nRESET
```

This is a logical pin-number diagram. Physical pin 1 must be matched to the actual socket, cable end, and the manufacturer's orientation figure before wiring.

## Power and voltage reference

- Section 1.2, page 5: documented target-interface operating range **1.62–5.5 V**.
- Section 5.4.1, pages 51–52: **VTG is a reference input only; it does not power the target**. Supply the Force Band through its normal target power arrangement once that arrangement is documented.
- Section 4.2.2.1, page 25: the reference input draws less than 1 mA in modes other than debugWIRE.
- The nRF52832-QFAA's own recommended VDD range remains **1.7–3.6 V**; the probe's wider supported range does not extend the MCU's limits. Actual Force Band rail voltage has not been measured.

The candidate pad labeled `3V3` is not yet verified as MCU VDD or an appropriate VTG connection. See the [target pad reference](pad-reference.md) for pending checks.

## Cable and orientation

Section 2.6, page 10, specifies the red conductor as pin 1, aligned with the triangle on the probe enclosure's blue belt, with the cable exiting upwards. Section 3.1, page 15, Figure 3-2 identifies cable end A as the debugger side and end B as the target side. The three-termination ribbon also has a six-pin AVR tap; mechanical fit to a shield connector does not identify that connector as a Cortex/SWD connection.

In the supplied equipment photo, the SAM socket at left appears empty and the ribbon appears to enter the AVR socket at right. The cable loop partly obscures it, so this is an observation to confirm locally, not a verified electrical connection. The manual documents SWD on either port with different pin assignments. Do not move or select a port solely from the MCU brand: establish the shield routing and cable mapping first.

## What remains unresolved

The [official shield product page](https://www.microchip.com/en-us/development-tool/atard-dbgadpt) now loads, but no public shield schematic or user-guide download was recovered from its documentation section. Its Arduino-shield description does not establish routing for the photographed **A09-2340/02** assembly. Obtain the shield schematic/user guide or establish routing by unpowered continuity checks before assigning its pins.

The manual documents AVR/SAM support. It does not establish host-tool support for an nRF52832. Nordic compatibility remains part of TASK-5. SAM-specific reset/erase instructions must not be treated as instructions for this Force Band.

TASK-3 remains In Progress until target measurements, cable/shield mapping, and voltage compatibility are recorded.

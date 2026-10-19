# Force Band front-side component inventory

Hardware: [SB-FB-001](force-band-01.md). Photo review: 2026-10-19.

The inventory uses the [untouched front-side overview](photos/notion-3550f5ded18391aed3ecc2e0ddef4efb5d62957787ae6f40a37d9b964fe30f9a.jpg), displayed with the USB connector at the left, and the [U7/U8 close-up](photos/notion-cdc6a89ca5c02d1ae4bb1f523fd93005035ef17c29d9ef78b83f164f42328942.jpg). Identifying a physical component does not establish its board wiring or GPIO assignment. No physical measurements were performed.

## Main integrated circuits

| Reference | Identification | Role | Evidence and confidence |
|---|---|---|---|
| U1 | **Nordic nRF52832-QFAA** | Main microcontroller and Bluetooth Low Energy radio; 64 MHz Cortex-M4F, 512 KiB flash, 64 KiB RAM | Confirmed by `N52832 / QFAAB0` photograph and Nordic marking table; see [MCU record](mcu-and-memory.md) |
| U7 | **Texas Instruments TAS2505** | Audio conversion / Class-D speaker amplification | `TAS / 2505` marking is readable. Confident part-family identification; exact ordering suffix and board connections unverified. The attempted TI datasheet download was proxy-blocked, so no additional electrical ratings are adopted here. |
| U9 | **Winbond W25Q40-family serial NOR flash candidate** | External persistent storage, consistent with 4 Mbit / 512 KiB | Winbond logo and `25Q40` prefix readable; complete suffix, operating voltage, and electronic device ID remain unresolved; see [memory record](mcu-and-memory.md) |
| U8 | **Unidentified IC; motion-sensor role plausible** | Candidate inertial sensor / sensor subsystem | Marking appears approximately `134` or `I34`, then `A1529`, then `047` or `D47`. Shape and product function are clues, not an exact identification. No additional RAM is established by this package. |

U8 should not be labeled as a BNO055 from appearance alone. A retrieved Bosch-authored [BNO055 datasheet revision 1.2, section 6.2, page 102](https://github.com/jcorcoran/BNO055_FRC/blob/665e21f40362d02a3eaa1272c349686cca31148c/BST_BNO055_DS000_12.pdf) specifies product marking `701`, which does not match the observed U8 transcription. This comparison did not establish an exact U8 identity. Its package dimensions, pin count, and bus connections have not been measured.

## Connectors, controls, indicators, and transducers

| Reference / location | Identification | Confidence and remaining limits |
|---|---|---|
| J2, left edge | Micro-USB connector | Clearly visible. Power/charging/data connections require tracing; no USB programming path has been established. |
| S1, centre-left | Momentary tactile pushbutton | Physical type clear; MCU signal unknown. |
| D1, D4, D5, around S1 | Three six-terminal LED packages, likely RGB | Appearance and nearby groups of resistors support RGB interpretation; channel assignment and exact LED part unknown. |
| ANT1, wire running along lower edge | Likely wire antenna | Single insulated wire and ANT1 label support RF role. Exact radio-net connection and tuning remain unverified. |
| X1, metal-can part near U1/U9 | Crystal/resonator | Package and reference designator support this classification. Frequency marking is not readable; no frequency is assigned from the photo alone. |
| Large rectangular black assembly beside U1/U7 | Likely loudspeaker | Mechanical appearance and nearby audio amplifier support this. Model, impedance, and wiring are unverified. |
| J4 and round component on red/blue wires | Likely coin vibration motor and its two-wire connection | The wires visibly connect to J4. Physical form supports a motor identification; no model or drive circuit verified. |

## Small support components

| Reference | What can be established | Still unknown |
|---|---|---|
| U6, near USB | Small five-terminal IC | Readable exact marking, part number, and circuit role; a power-related role is only a hypothesis |
| U10, below-left of S1 near D5 | Small five-terminal IC | Exact marking, part number, and circuit role |
| Q4, Q5, near J4 | Three-terminal transistor/MOSFET-class devices, based on Q designators and package | Exact device types and whether they drive the motor or switch power |
| D3, adjacent to USB | Two-terminal diode package with polarity band; marking appears `A7` | Exact diode part number and function; the short marking is not unique |
| D2 | Smaller diode component | Exact type and role |
| R*, C*, L* parts | Resistors, capacitors, and inductive/RF components as indicated by designators | Values and circuit roles require markings, a schematic, or measurements |

## Evidence that would resolve remaining identities

- U8: a sharply focused, perpendicular macro photograph and package dimensions, or a passive sensor-bus capture that reveals identification transactions. No software driver should be selected from the current marking alone.
- U6 and U10: close-ups with readable top markings; trace accessible connections to establish whether they regulate, charge, switch, or perform another function.
- X1: a readable marking or circuit/documentation evidence for its frequency.
- Transducers: manufacturer markings, if already accessible, to establish speaker impedance and motor requirements.

These are research findings, not instructions to dismantle components or apply power. The existing [pad-reference and measurement record](pad-reference.md) remains the place for TASK-3's electrical evidence.

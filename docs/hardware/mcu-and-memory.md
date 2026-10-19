# MCU and memory identification

Hardware: [SB-FB-001](force-band-01.md), the owner's Sphero Force Band.  
Date: 2026-10-19. Related task: TASK-2.

## MCU: confirmed from package markings

The new [U1 close-up](photos/notion-1302842f4cb337b6ba910e472c81b469da36f2065f739eab0ea66d3ffe53bfc6.jpg) clearly shows:

```text
N52832
QFAAB0
1616BB
```

Nordic's nRF52832 Product Specification v1.0, section 52 (pages 536–538), defines the marking fields:

- `N52832`: nRF52832 device.
- `QF`: QFN48 package, 6 × 6 mm.
- `AA`: function variant with 512 kB flash and 64 kB RAM, explicitly distinguished from the `AB` variant with 256 kB flash and 32 kB RAM.
- `B0`: hardware-version and production-configuration fields, rather than a different memory capacity.
- `1616BB`: tracking code (year/week/lot), rather than a memory specification.

The resulting part identification is **Nordic nRF52832-QFAA**. This is supported by the actual photograph and the manufacturer marking table, rather than inferred from the nRF52 family alone.

| Property | Specification | Evidence in Nordic specification v1.0 |
|---|---|---|
| CPU | 32-bit Arm Cortex-M4 with single-precision FPU | Section 7, page 18 |
| CPU clock | 64 MHz | Section 7.2.1, page 18 |
| Internal program flash | 512 KiB = 524,288 bytes | Section 52.4, table 129, page 538; memory chapter |
| Internal RAM | 64 KiB = 65,536 bytes | Section 52.4, table 129, page 538; memory chapter |
| Recommended MCU supply VDD | 1.7–3.6 V | Section 6, table 4, page 17 |
| Debug/programming interface | Two-pin SWD: SWDIO and SWDCLK | Section 16, page 70 |

These are component specifications. The actual board voltage, electrical test-pad connections, debug access, and flash protection state have not been measured. The reverse-side `3V3` label does not establish a measured rail voltage, and the MCU supply range does not specify the allowable voltage for every other component.

## External flash: capacity inferred; full variant unresolved

The [U9 close-up](photos/notion-ebf5392cf414c558350cb9208f9eda7e486806c65ca3c8dd85e455796494b271.jpg) shows the Winbond logo and a `25Q40` part prefix. The remaining suffix is insufficiently clear for a definitive full ordering-code transcription.

This identifies a **Winbond W25Q40-family serial NOR flash candidate**, with **4 Mbit = 512 KiB = 524,288 bytes** of storage. The flashrom chip database independently lists 512 KiB for its W25Q40.V, W25Q40BW, and W25Q40EW entries. This supports the capacity inference without choosing between suffixes with different supply requirements.

The complete suffix, rated supply voltage, JEDEC identity, actual bus wiring, contents, and readable access remain unverified. No SPI read or firmware dump has been performed. Do not use another W25Q40 variant's voltage specification to wire this board.

## Other new photo

The [U7/U8 close-up](photos/notion-cdc6a89ca5c02d1ae4bb1f523fd93005035ef17c29d9ef78b83f164f42328942.jpg) also shows the `TAS / 2505` marking on U7, supporting the earlier TAS2505 audio-device identification. Neither U7 nor U8 is evidence of additional RAM; U8's exact identification remains for the peripheral investigation.

See the [front-side component inventory](front-side-components.md) for the remaining visible parts, confidence levels, and evidence needed to identify U8 and the smaller support ICs.

## Implications for Lua and application storage

The firm working-memory budget is **64 KiB total internal RAM**. Firmware stacks, drivers, buffers, any Bluetooth stack, and the interpreter share that capacity; the free Lua heap must be measured after a target build. No interpreter configuration has yet been built or verified.

The 512 KiB MCU flash and inferred 512 KiB external flash are separate storage resources. External SPI flash could potentially hold scripts or assets after its interface and contents are understood. It does not expand the ordinary CPU-addressable RAM heap, and the two flash devices do not automatically form a single executable program space.

## Sources and provenance

1. **Nordic Semiconductor, nRF52832 Product Specification v1.0**, dated 2016-02-17. The manufacturer-authored PDF was retrieved from [SparkFun's archived copy](https://github.com/sparkfun/nRF52832_Breakout/blob/5ec26d8fab88fd07b2bd83e1ec6898b84da76ae5/Documentation/nRF52832_PS_v1.0.pdf) at commit `5ec26d8fab88fd07b2bd83e1ec6898b84da76ae5` and its relevant tables and sections were read. PDF SHA-256: `f58876a3e41141d1c8e55c53e90dae708eda885022bbee79740f0591e0813e65`. The current Nordic document portal was blocked by the environment proxy; this identification uses the retrieved archival specification and does not claim review of the latest revision or errata.
2. **Nordic Semiconductor nrfx v2.11.0**, [nrf52_bitfields.h](https://github.com/NordicSemiconductor/nrfx/blob/v2.11.0/mdk/nrf52_bitfields.h): `FICR_INFO_RAM_RAM_K64` and `FICR_INFO_FLASH_FLASH_K512` independently document the chip's memory-identification register values. These registers have not been read from this board.
3. **flashrom**, [Winbond chip database](https://github.com/flashrom/flashrom/blob/e7bfc93e1b0a5ad63fe953b6404451a052f74975/flashchips/winbond.c), commit `e7bfc93e1b0a5ad63fe953b6404451a052f74975`. This is a supporting software source for W25Q40-family capacity, not the manufacturer's datasheet for the unresolved exact suffix. The attempted Winbond documentation request was blocked by the proxy.
4. Images and Notion source block IDs: [Notion photo manifest](photos/notion-manifest.json). The three close-ups are 4032 × 3024 pixels and fully decode. Published copies exclude private image metadata without pixel recompression. Original-download and published-file sizes/hashes are recorded separately; decoded pixels, orientation, and colour profiles remain unchanged. See [publication checks](../publication-checks.md).

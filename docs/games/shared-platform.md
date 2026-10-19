# Shared platform

## Evidence and scope

The owner chose a standalone wrist computer in the [updated conversation](https://chatgpt.com/share/6ad6802b-8b4c-83ed-b133-b493de53a773): user message `405a55d0-b479-4d4b-90cb-7bbcf3069c8a` selects Option A from assistant message `51905b89-f5a1-5834-92d7-6c19183543e8`. The hardware proposal follows in `1559d955-a823-55ca-a8f0-d201983b665a`.

Baseline proposal: retain the nRF52832, motion sensor, battery, existing button, and casing; add a small display. The imported [hardware record](../hardware/README.md) is authoritative for component evidence and remaining measurements. The [front-side inventory](../hardware/front-side-components.md) supports the TAS2505 marking but leaves its connections unverified; U8's exact identity and sensor role remain unresolved. Available GPIO, actual rail voltages, and physical fit still require investigation. No sensor driver should be selected from package appearance alone.

## Work required before hardware gameplay

| Area | Required outcome | Main responsibility |
|---|---|---|
| Electrical map | Verified ground, supply, SWD, sensor bus, button, and candidate display connections | Owner measures; Codex records and analyses |
| Programming access | Reproducible build, identification, flashing, and debug workflow; original firmware access/preservation recorded | Codex prepares; owner operates hardware |
| Display | Exact module selected after voltage, pin availability, dimensions, power, and bus checks; stable test image | Joint |
| Motion sensor | Exact part/interface identified; samples with timestamps; stable neutral calibration | Owner captures; Codex implements |
| Button | Debounced press/hold events with an unambiguous menu/pause mapping | Codex implements; owner validates |
| Power and case | Measured current and runtime; readable viewing angle; wiring and screen fit | Owner measures and assembles; Codex analyses |
| Runtime | Display/input/timing API, error handling, measured memory and frame time | Codex |

A connector label or a chat suggestion is not an electrical measurement. Keep pin verification in the existing hardware records. The analysis does not authorize an erase or flashing operation.

## Display and memory

Nordic lists the nRF52832-QFAA as **64 kB RAM and 512 kB flash** in its [memory specification](https://docs.nordicsemi.com/r/bundle/ps_nrf52832/page/memory.html). The retained [MCU and memory evidence](../hardware/mcu-and-memory.md) confirms this variant from the photographed marking and manufacturer table; it distinguishes component specifications from unmeasured board behaviour.

Suggested first display: a 128 × 64 monochrome OLED, potentially SSD1306 over I²C. This remains a module/interface candidate, not a purchase or wiring decision. Adafruit's breakout guide describes multiple supported interfaces; the selected module's wiring and voltage requirements must be checked separately. See [Adafruit's OLED guide](https://learn.adafruit.com/monochrome-oled-breakouts).

Framebuffer arithmetic, excluding driver overhead and alignment:

| Pixels | Format | One full framebuffer |
|---|---|---:|
| 128 × 64 | 1 bit/pixel | 1,024 bytes |
| 128 × 128 | 1 bit/pixel | 2,048 bytes |
| 128 × 128 | 16 bits/pixel | 32,768 bytes |

At 30 full 128 × 64 updates per second, pixel payload alone is 30,720 bytes/s. At an illustrative 400 kbit/s I²C bus, 1,024 bytes take at least 23.04 ms with nine clock bits per byte, before addresses, commands, and software overhead. Measure the actual supported bus rate; dirty-region or page updates may be needed. These are calculations, not measured Force Band performance.

Lua is the preferred direction in the source conversation. First build a small C platform with a bounded Lua runtime and measure its footprint. Lua allocates through the allocator passed to `lua_newstate`; see the [Lua 5.4 C API](https://www.lua.org/manual/5.4/manual.html#lua_newstate). Record the chosen Lua version rather than assuming 5.4 is a final selection.

Track `.data`, `.bss`, stack high-water mark, display buffers, sensor/bus buffers, Lua heap and peak allocations, and any Bluetooth allocation. Target an initial 8 KiB unallocated margin during the worst measured workload; revise that target using measurements. Ordinary SPI storage does not become a directly addressable Lua heap. No extra RAM purchase is justified by the game concepts alone.

## Control model

The recovered Pong proposal specifies **tilt-controlled velocity**: tilt up/down moves the paddle; neutral stops it. Use that as the first control experiment. An absolute tilt-to-position mapping is an alternative for comparison, not an already accepted requirement.

The input layer should provide calibrated screen-relative axes, a dead zone, saturation, filtering, and hysteresis for directional events. Record sensor sample rate, filter lag, neutral drift, useful tilt range, and input-to-display latency. Start with 100 Hz input and 60 Hz fixed simulation as proposed software targets; independently render at a measured sustainable rate, initially aiming for 30 Hz. Adjust from evidence rather than dropping simulation steps silently.

For menus and gameplay, propose short press to start/pause/resume and long press to return to the menu. In pause/menu, provide an explicit recalibration action. Suppress the short-press event after a recognised long press. Verify the mapping on the real button and with both wrist orientations.

## Architecture proposal

```text
Sensor and button drivers → calibrated input → game update at fixed dt
                                                ↓
                                   drawing commands / game state
                                                ↓
                                       monochrome renderer
                                                ↓
                                          display driver
```

Keep platform services in C and expose small calls to Lua for input, drawing, time, and optional sound. Game code should not know GPIO numbers or bus transactions. Use the same game rules with a desktop input/display adapter so collisions and state transitions can be exercised without the Force Band.

Share rectangle drawing, text, input, menus, scores, timing, and ball/paddle primitives. Keep Pac-Man's tile movement separate from Pong/Breakout continuous collision code. Audio and Bluetooth are later capabilities; neither is required to validate a standalone first playable game.

## Platform acceptance

- A recorded build can run on the intended board with a verified hardware map.
- Display orientation, pixel boundaries, text, and update rate are demonstrated on the selected module.
- A stationary wrist remains neutral after calibration; both extremes are reachable comfortably.
- Pause freezes simulation, resume causes no large time step, and restart clears game state.
- Peak RAM, stack, runtime heap, update time, and power are recorded during representative gameplay and repeated game switches.
- A runtime/game error returns to a usable menu with a diagnostic instead of leaving the interface unresponsive.

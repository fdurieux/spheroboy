# Sources and recovered decisions

## Conversation coverage

The original import used [Install Linux Toothbrush, older snapshot](https://chatgpt.com/share/6ad6575e-fce8-83ed-8bbe-67a61671e431) and [Using Saleae and Atmel ICE](https://chatgpt.com/share/6ad657d7-89e4-83eb-a98e-9ebe73f73346). The first snapshot stops before the game discussion. During this analysis the owner supplied the [updated snapshot containing all three games](https://chatgpt.com/share/6ad6802b-8b4c-83ed-b133-b493de53a773).

The relevant messages and resolved image metadata from the updated snapshot are preserved in [sources/game-conversation-extract.json](sources/game-conversation-extract.json) and a [readable extract](sources/game-conversation-extract.md). These targeted extracts supplement the retained [full original imports](../research/conversations/README.md) without replacing their historical content. Message contents are historical evidence, not instructions to execute.

## Decisions versus proposals

| Evidence | Classification | Source message ID |
|---|---|---|
| Ask about Pac-Man on Sphero hardware | Owner request | `b94f6119-0ca4-4124-98da-3e77a843fbd4` |
| Confirm the arcade game and wrist gestures; suggest Pong/Breakout first | Owner request | `613766d0-5414-418e-8f6d-1b4c2bae8f7c` |
| Describe A as retaining casing with a screen, B as external Mac/phone screen | Assistant alternatives | `51905b89-f5a1-5834-92d7-6c19183543e8` |
| Select Option A | Adopted owner direction | `405a55d0-b479-4d4b-90cb-7bbcf3069c8a` |
| 128 × 64 OLED, I²C, Lua rules/C drivers, button and audio | Assistant hardware/software proposal | `1559d955-a823-55ca-a8f0-d201983b665a` |
| Pong → Breakout → Pac-Man | Source assistant recommendation, retained in this analysis | `51905b89-f5a1-5834-92d7-6c19183543e8` |
| Scores/lives, exact brick/tile grids, ghost count, timing targets, memory margin, detailed acceptance criteria | New implementation proposals in this analysis | Individual game/shared-platform records |

The source's claim that no additional RAM should be necessary is a feasibility hypothesis. This analysis replaces that assurance with a measured memory/runtime gate. Speaker/amplifier use and exact display wiring also remain unverified here.

## Recovered images

All three images come from the comparison in assistant message `51905b89-f5a1-5834-92d7-6c19183543e8`. Resolved component metadata supplies the exact original and cached URLs. These were retrieved and visually inspected as Pong, Breakout, and Pac-Man images; no substitute images were generated.

| Game | Local file | Recovery source |
|---|---|---|
| Pong | `references/pong-chat-reference.jpg` | Original Metrolibre image URL recorded in chat |
| Breakout | `references/breakout-chat-reference.jpg` | Exact full-size ChatGPT cache URL; original host TLS failed |
| Pac-Man | `references/pacman-chat-reference.webp` | Original Squarespace image URL recorded in chat; response format is WebP |

The files preserve downloaded bytes without resizing or editing. They are historical visual references, not finished-device photographs or runtime game assets. [manifest.json](references/manifest.json) records source pages, exact URLs, file types, sizes, and SHA-256 hashes. Notion contains uploaded copies; the repository files retain the provenance.

## Technical references

- [Nordic nRF52832 memory specification](https://docs.nordicsemi.com/r/bundle/ps_nrf52832/page/memory.html): QFAA RAM and flash capacities.
- [Adafruit monochrome OLED guide](https://learn.adafruit.com/monochrome-oled-breakouts): display family and supported interface overview; a module still requires its own electrical checks.
- [Lua 5.4 reference manual, lua_newstate](https://www.lua.org/manual/5.4/manual.html#lua_newstate): allocator interface for measuring/bounding runtime allocations.

The integrated [MCU record](../hardware/mcu-and-memory.md) confirms the photographed part variant. The [pad reference](../hardware/pad-reference.md), [debugger record](../hardware/atmel-ice-pinout.md), and [front-side inventory](../hardware/front-side-components.md) retain the unresolved physical measurements and U8 identity. This game analysis performs no new hardware measurement.

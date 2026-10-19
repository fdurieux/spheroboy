# 0003: Standalone wrist display

Status: Accepted direction
Date: 2026-10-19

## Context and evidence

The older imported conversation stops before the game's display-choice exchange. The owner supplied an [updated shared conversation](https://chatgpt.com/share/6ad6802b-8b4c-83ed-b133-b493de53a773) while the game plans were being prepared. In assistant message `51905b89-f5a1-5834-92d7-6c19183543e8`, Option A retains the Force Band casing and adds a wrist screen; Option B uses the Force Band as a motion controller for a Mac or phone. The owner selected **Option A** in user message `405a55d0-b479-4d4b-90cb-7bbcf3069c8a`.

The [source inventory](../games/source-inventory.md) and its linked six-message extract preserve that evidence. The existing decision to [modify the selected Force Band](0002-modify-existing-force-band.md) remains unchanged.

## Decision

Pursue a standalone programmable wrist computer using the selected Force Band, with a screen mounted on the retained casing and wrist gestures as game controls.

## Consequences

- Display integration, power, enclosure fit, viewing angle, and calibrated motion input are common platform work for all three games.
- A desktop harness can help develop rules and layouts, but the intended application runs on the wrist computer.
- The chat's 128 × 64 OLED/I²C candidate and Lua/C split remain proposals. Existing TASK-6 evaluates a display; TASK-7 evaluates Lua and a native baseline.
- Pong → Breakout → Pac-Man is the recommended implementation order in the game analysis, not a claim that any game or firmware currently exists.
- No exact module, pinout, driver, toolchain, runtime version, or erase/flash procedure is approved by this direction alone.

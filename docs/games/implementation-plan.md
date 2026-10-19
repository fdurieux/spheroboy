# Proposed implementation work

This is a dependency and responsibility analysis, not an active second backlog. The cloud snapshot and its [Backlog.md records](../../backlog/README.md) are now integrated; preserve that task history and use the mappings below. No game code has been created by this analysis.

| Order | Work package | Codex contribution | Owner contribution | Completion evidence |
|---|---|---|---|---|
| 0 | Reconcile project records | Retain the finalized cloud snapshot and integrate the game plans, tracked by TASK-10 | Review the reconciliation PR | Source snapshot, retained records, and one backlog documented in the reconciliation record |
| 1 | Hardware access and bus map | Analyse manuals/captures, prepare wiring and programming procedure | Measurements, captures, physical connections | Verified connection map and reproducible programming access |
| 2 | Display and motion proof | Implement drivers, test screen, calibrated input diagnostic | Select/assemble the verified module, measure power, perform wrist checks | Readable test image plus stable recorded tilt input |
| 3 | Runtime feasibility | Small C services, bounded Lua build, instrument memory/timing, desktop adapter | Run on-device trials and supply measurements | Peak RAM/stack/heap, update time, and sustained display rate recorded |
| 4 | Pong first playable | Implement rules/opponent and meaningful collision/state checks | Evaluate feel, viewing angle, comfort, and difficulty | Pong acceptance criteria and recorded hardware session |
| 5 | Breakout first playable | Reuse platform/physics, implement grid/lives/win, stress corners | Playtest speed and readability | Breakout acceptance criteria and recorded hardware session |
| 6 | Maze and control proof | Actual-size tile mockup and four-direction buffered movement | Judge readability and directional comfort | Chosen maze scale and usable movement before ghost scope expands |
| 7 | Pac-Man adaptation | Maze/pellets/one ghost, state checks, memory measurement | On-device playtest | Pac-Man acceptance criteria and recorded session |
| 8 | Polish and enclosure | Analyse power/runtime; optional audio, settings, saved scores | Assemble screen mount and measure battery/runtime | Wearable assembly with documented operating behaviour |

## Work that can proceed in parallel without new hardware

A keyboard-driven desktop harness can develop ball collisions, brick handling, tile movement, and state transitions while physical investigation continues. A pixel-accurate 128 × 64 mockup can evaluate layouts early. Neither proves motion control, display bus timing, power, or enclosure fit.

## Existing task mapping

- **TASK-3:** measured power rails and candidate debug connections; prerequisite for wiring decisions.
- **TASK-4:** motion-sensor communication capture and identification.
- **TASK-5:** non-destructive debug access and firmware backup feasibility.
- **TASK-6:** display feasibility against verified board constraints; link the shared platform and game layouts here.
- **TASK-7:** Lua evaluation and first firmware milestone, including a native baseline and measured resource budget.
- **TASK-10:** reconcile the actual cloud files with these plans and publish the review PR.

Create future implementation tasks for Pong, Breakout, or maze gameplay when their scope is picked up, with the relevant acceptance criteria and prerequisites. Do not turn these documentation work packages into competing copies of TASK-3 through TASK-7.

## Decisions and experiments

| Choice | Starting proposal | What resolves it |
|---|---|---|
| Display module/interface | Small monochrome 128 × 64 OLED, I²C candidate | Verified GPIO/voltage/bus availability, mounting and measured update rate |
| Lua integration | Lua game rules with C hardware services, as proposed in source | Measured heap/stack/flash and timing; choose version and bindings |
| Paddle mapping | Tilt controls velocity; neutral stops | Compare comfort and accuracy against position mapping |
| Button behaviour | Short press start/pause; long press menu | Real-button playtest and deliberate exit/recalibration flow |
| Pac-Man scope | Small custom maze and one ghost | Actual-size readability and four-direction input trials |
| Sound | Optional after first playable | Verified audio hardware/control and power/timing impact |

Avoid delivery-date estimates until hardware access, display, and runtime gates are measured. Relative effort is Pong < Breakout < Pac-Man for game logic; shared hardware work is the largest unknown. Current work is documentation and recovered references, not a commitment to purchase parts, flash hardware, or implement all proposed extensions.

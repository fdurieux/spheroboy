# Recovered game discussion

Source: [Install Linux Toothbrush](https://chatgpt.com/share/6ad6802b-8b4c-83ed-b133-b493de53a773)

Targeted extract: six game discussion messages plus resolved image metadata. The complete conversation is not copied.

Custom presentation markup is preserved below as source text. Resolved image metadata is retained in the JSON extract.

## user — b94f6119-0ca4-4124-98da-3e77a843fbd4

Before I continue with the light bulb: could I run pacman on the sphero hardware?

## assistant — 389d3b25-2b1e-5e2d-9229-af091a18cdf6

**Yes! If you mean the classic Pac-Man arcade game, the Sphero Force Band has enough processing power to run a Pac-Man clone.** 👻

In fact, that could be a fun first project before building your general-purpose Lua wrist computer.

The Force Band's Nordic nRF52832 has a 64 MHz ARM Cortex-M4 processor, 512 KB flash and 64 KB RAM. That's sufficient for Pac-Man's game logic, maze, ghosts and scoring. <Cite ref="turn32search0"/>

The main limitation is that the Force Band has **no screen**.

## Three ways to play Pac-Man

<box gap={3}>
  <row align="start" gap={3}>
    <AsyncImage query="tiny monochrome OLED SSD1306 display 0.96 inch electronics module" aspectRatio="1:1" maxWidth="116px"/>
    <box flex="1" gap={1}>
      **1. Add a tiny OLED display**

      <badge color="success">My favourite option</badge>

      Run the game on the Force Band and display it on a small OLED attached to the wrist unit. Use wrist gestures to steer Pac-Man.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="smartphone retro pixel art Pac Man maze game screen" aspectRatio="1:1" maxWidth="116px"/>
    <box flex="1" gap={1}>
      **2. Use a smartphone as the screen**

      Run the game logic on the nRF52832 and transmit the game state over Bluetooth. The phone renders the maze and characters.
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="retro arcade Pac Man game on small 1.8 inch TFT LCD display electronics module" aspectRatio="1:1" maxWidth="116px"/>
    <box flex="1" gap={1}>
      **3. Attach a colour TFT display**

      This would provide a more authentic arcade experience, although it requires additional wiring, display drivers and power.
    </box>
  </row>
</box>

### How I'd implement it

- **Lua:** Game rules, movement, scoring and ghost behaviour.
- **C firmware:** Display driver, Bluetooth and motion sensor.
- **Wrist gestures:** Up, down, left and right.
- **Force Band speaker:** Sound effects.
- **Physical button:** Start/pause.

A monochrome version would be particularly suitable for the available RAM.

One clarification: if you meant **`pacman`, the Arch Linux package manager**, the answer is no. That requires a Linux-like environment, which the nRF52832 doesn't provide.

But if you're thinking of the game, **yes—it's genuinely feasible, and you wouldn't need to add RAM to start.**

## user — 613766d0-5414-418e-8f6d-1b4c2bae8f7c

The game, using wrist gestures. Maybe even better to start with a different game such as breakout or pong.

## assistant — 51905b89-f5a1-5834-92d7-6c19183543e8

I agree. **Pong is the best first game, followed by Breakout, then Pac-Man.** The Sphero Force Band is particularly well suited to games controlled by wrist movements.

The interesting challenge isn't processing power—it's translating motion-sensor readings into precise, enjoyable controls.

## Which game should we start with?

<box gap={3}>
  <row align="start" gap={3}>
    <AsyncImage query="classic 1972 Atari Pong black screen white paddles ball retro video game screenshot" aspectRatio="4:3" maxWidth="132px"/>
    <box flex="1" gap={1}>
      <row align="center" wrap="wrap" gap={2}>
        **1. <Entity category="video_game" value="Pong" disambig="1972 Atari arcade game"/>**
        <badge color="success">Easiest</badge>
      </row>
      Rotate your wrist to move the paddle up and down. Play against a computer-controlled opponent.

      <text color="secondary" size="xs">One ball, two paddles and simple collision detection.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="classic Atari Breakout arcade game screenshot rows colored bricks paddle ball black background" aspectRatio="4:3" maxWidth="132px"/>
    <box flex="1" gap={1}>
      <row align="center" wrap="wrap" gap={2}>
        **2. <Entity category="video_game" value="Breakout" disambig="1976 Atari arcade game"/>**
        <badge color="success">Best wrist game</badge>
      </row>
      Tilt your wrist left and right to move the paddle and bounce a ball into bricks.

      <text color="secondary" size="xs">Natural one-handed controls; slightly more game logic.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="start" gap={3}>
    <AsyncImage query="original 1980 Pac-Man arcade game maze gameplay screenshot ghosts dots" aspectRatio="4:3" maxWidth="132px"/>
    <box flex="1" gap={1}>
      <row align="center" wrap="wrap" gap={2}>
        **3. <Entity category="video_game" value="Pac-Man" disambig="1980 Namco arcade game"/>**
        <badge>Later project</badge>
      </row>
      Tilt in four directions to navigate the maze.

      <text color="secondary" size="xs">Requires more sophisticated gesture recognition and game logic.</text>
    </box>
  </row>
</box>

## How I'd build Pong on the Force Band

The nRF52832 would run the complete game:

- **Motion sensor:** Detect wrist orientation.
- **Lua interpreter:** Calculate ball movement, paddle position and collisions.
- **Display driver:** Draw the game.
- **Speaker:** Produce collision and scoring sounds.
- **Physical button:** Start or pause.

For a standalone wrist game, I'd add a small monochrome **128 × 64 OLED display**, preferably using I²C. A complete 1-bit framebuffer requires only 1 KB RAM.

We would still need to identify the Force Band's motion sensor and available GPIO connections.

## The development sequence

<list marker="number" connector="solid" gap={2}>
  <list-item>**Get Lua running.** Boot a small embedded interpreter on the nRF52832.</list-item>
  <list-item>**Read wrist motion.** Calibrate the sensor and convert tilt into paddle movement.</list-item>
  <list-item>**Implement Pong.** Begin with a ball bouncing between walls and a movable paddle.</list-item>
  <list-item>**Connect a display.** Initially, we could render over Bluetooth on your Mac to test the logic, then use a miniature OLED.</list-item>
  <list-item>**Upgrade to Breakout.** Reuse the paddle, ball physics and display code, adding bricks, scores and levels.</list-item>
</list>

No additional RAM should be necessary for either Pong or Breakout.

### One design decision

Would you prefer:

- **A:** Keep the original Force Band casing and build a tiny screen onto it—essentially a homemade gaming smartwatch.
- **B:** Use the Force Band purely as a motion controller, with the game displayed on your Mac or iPhone.

I'd lean toward **A** for your general-purpose programmable wrist-computer project. It would give us a reusable foundation for other Lua applications.

## user — 405a55d0-b479-4d4b-90cb-7bbcf3069c8a

Option A

## assistant — 1559d955-a823-55ca-a8f0-d201983b665a

Perfect. Let's build a **standalone Pong wrist computer using the Sphero Force Band**, retaining its motion sensor, battery and speaker.

My preference is to make the modification reversible wherever possible, given that your BB-8 is a collector's edition.

## Proposed hardware

<box border radius="lg" padding={3} gap={3}>
  <row align="center" justify="between">
    **Sphero Force Band — Pong Edition**

    <badge color="success">Proposed design</badge>
  </row>
  <AsyncImage query="0.96 inch monochrome 128x64 OLED module SSD1306 bare circuit board display black" aspectRatio="5:3" maxHeight={180} fit="contain"/>
  <text color="secondary" size="xs" textAlign="center">Proposed display component, not a photograph of the finished wristband.</text>
  | Component | Design |
  |---|---|
  | Processor | Existing nRF52832 |
  | Display | 0.96-inch, 128 × 64 OLED |
  | Display interface | I²C |
  | Controls | Wrist tilting + existing button |
  | Sound | Existing TAS2505 amplifier and speaker |
  | Power | Original rechargeable battery |
  | Game engine | Lua, with low-level C drivers |
</box>

An SSD1306-based I²C OLED would be a sensible starting point. It needs only four connections: power, ground, SDA and SCL. Its monochrome framebuffer occupies just **1,024 bytes** of RAM. <Cite ref="turn33search18"/>

## How the controls would work

| Wrist action | Pong behaviour |
|---|---|
| Tilt wrist upward | Paddle moves up |
| Tilt wrist downward | Paddle moves down |
| Return wrist to neutral | Paddle stops |
| Press existing button | Start or pause |

We can use a dead zone around the neutral position to prevent the paddle from drifting when your wrist moves slightly.

## What I can identify on your existing board

Looking again at your earlier PCB photographs:

- **U1:** Nordic nRF52832 processor.
- **U7:** TAS2505 audio amplifier.
- **U9:** Winbond external flash.
- **Bottom edge:** Four small holes or test-pad positions near the `REV15` marking.

Those four positions are interesting because they could provide access to programming or testing signals. But **we haven't established their pinout**, so we shouldn't connect a programmer yet.

Also, the nRF52832 can be protected against firmware reading. Clearing that protection may require erasing the original firmware. <Cite ref="turn33search3"/>

## Development order

1. Identify the SWD programming connections and available I²C pins.
2. Verify that we can program the processor.
3. Connect the OLED and display a test image.
4. Read and calibrate the motion sensor.
5. Implement Pong using Lua.
6. Design a replacement front cover to hold the screen, ideally without permanently cutting the original housing.

### What I need from you next

Could you send me **a clear photograph of the reverse side of the Force Band PCB**?

You've already provided excellent photographs of the component side. The reverse side may reveal programming pads, available connections and the motion sensor.

Once we have both sides, we can start tracing the necessary connections and produce an actual wiring plan for your Pong wrist computer.

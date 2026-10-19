# Capture evidence

Commit a Markdown metadata record for each useful capture. Include:

- Date, operator, device, board orientation, and related task.
- Instrument model and software version.
- Measured target logic voltage, channel-to-signal mapping, and acquisition settings.
- Actions performed during recording and expected events.
- Raw filename, SHA-256 checksum, and retained storage location.
- Decoder settings, observations, and derived outputs.

Keep large raw files in `raw/` and original firmware backups in `firmware-dumps/`; both are Git-ignored. Retain important files in durable storage and record an accessible location rather than relying solely on this workspace. Small decoded exports may be committed alongside metadata when appropriate.

There are no captures or backups yet. Do not describe a backup as verified until its size, checksum, and read procedure have been recorded.

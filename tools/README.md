# Development and analysis tools

Place reproducible capture-analysis scripts and development helpers here as they are needed. Each tool should document its input format, invocation, dependencies, and expected output. No hardware programming helper is configured yet.

Backlog.md is run through the version-pinned commands in the root README; it does not require an application package manifest.

## Notion photo import

`import_notion_photos.py` reads the inbox configured in `notion-inbox.json` and saves supported photos, checksums, captions, and source references in `docs/hardware/photos/`. It requires Python 3.10+ and the securely injected `NOTION_TOKEN`; there are no third-party Python dependencies.

```bash
python -B tools/import_notion_photos.py
python -B -m unittest discover -s tools -p 'test_*.py' -v
```

Run these commands from the repository root. See [inbox instructions](../docs/notion-photo-inbox.md) for setup, supported photo types, retry behavior, and current live validation status. The importer reads Notion and never edits the inbox.

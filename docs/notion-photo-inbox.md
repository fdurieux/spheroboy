# Connect a Notion photo inbox

Use a dedicated Notion page as a phone-friendly upload inbox. Imports will be requested in chat; there is no background watcher or synchronization configured.

## Grant access

1. Create a page in Notion called **Spheroboy — Photo inbox**. Add uploaded images or image files directly to this page, with captions identifying the device, board side, and observation. Keep original resolution where possible.
2. Open [Notion integrations](https://www.notion.so/profile/integrations) and create an **internal integration** for the workspace containing the page. Suggested name: **Spheroboy Photo Import**. A workspace owner may need to create it if your role does not permit this.
3. Give the integration **Read content** capability. This import workflow does not require inserting or updating Notion content or reading user details.
4. Grant the integration access to the inbox page. Depending on the Notion interface, select the page under the integration's content access settings, or open the page's **Connections** menu and add the integration. Share only the page and descendants you want imported.
5. Copy the integration's internal secret into the cloud environment's secure secret setting for **NOTION_TOKEN**. Never paste it into chat, repository files, or a terminal command.
6. Review and save the environment changes, then publish the environment as requested by the environment UI. A draft requirement for NOTION_TOKEN with destination **api.notion.com** has been saved; saving the draft alone does not inject credentials or publish it.
7. Send the inbox page URL in chat after saving. The URL identifies the page; the integration secret stays in environment settings.

## Configured inbox and current verification

The configured [Spheroboy Photo inbox](https://app.notion.com/p/Spheroboy-Photo-inbox-3feb8589dab080be8a6cda3d72410d28) is stored in `tools/notion-inbox.json`. Live authenticated page access and photo downloads were verified on 2026-10-19: two photos imported successfully with no failures. A repeat import found both unchanged and created no duplicate files. Network access to **api.notion.com** and **prod-files-secure.s3.us-west-2.amazonaws.com** now works in this environment. The earlier file-host proxy blocker is resolved.

The integration token is sent only to `api.notion.com`. Attachment requests use the signed download URLs returned by Notion without an Authorization header. These temporary URLs are not written to the repository or printed in diagnostics.

## Import photos

From `/workspace/spheroboy`, run:

```bash
python -B tools/import_notion_photos.py
```

Or ask **Import new photos from the Notion inbox**. This runs on request, not in the background.

The importer requires Python 3.10 or later and the securely injected `NOTION_TOKEN`; it uses only the Python standard library. It traverses the page and accessible nested blocks/child pages with pagination. Supported photo blocks are Notion images and file attachments named with a JPEG, PNG, GIF, WebP, HEIC, or HEIF extension. Other file attachments and linked database contents are not imported. Keep inbox photos directly on the page or inside ordinary nested blocks.

Files are saved in `docs/hardware/photos/`. Identical contents reuse an existing photo, including photos recovered from the original conversations. Changed photo contents retain earlier versions; removing a photo from Notion does not delete the local copy. A file modified locally is preserved rather than silently overwritten.

- [notion-index.md](hardware/photos/notion-index.md) lists imported photos and captions with source block links.
- [notion-manifest.json](hardware/photos/notion-manifest.json) records source IDs, edit timestamps, byte sizes, and SHA-256 checksums.
- Output reports `found`, `imported`, `duplicates`, `unchanged`, and `failed`. A failed run exits nonzero; rerunning retries failed or missing files.

The importer checks supported file signatures and preserves downloaded bytes. It does not establish component identities or perform full image decoding. The per-image download limit is 50 MiB. Run one importer at a time.

Before public commits, follow the [publication checks](publication-checks.md). New or changed downloads can contain GPS/owner/serial metadata. The existing publication files have that metadata removed without recompression; `sha256` records their current bytes and `source_sha256` records the original download. Known sanitized files are reused across caption edits or duplicate-source blocks. This does not sanitize newly downloaded content automatically.

Unchanged blocks with intact local files are skipped. Captions and replacements trigger a fresh download when Notion updates the block timestamp. Copy captions into technical findings only after reviewing their accuracy.

## Validation

```bash
python -B -m unittest discover -s tools -p 'test_*.py' -v
```

All eleven tests pass. They cover source identification, retained bytes and captions, pagination and nested blocks, file attachments, deduplication, changed images, retry after failure, missing/modified local files, credentials across redirects, and retention of metadata-sanitized files on reimport. Live verification initially imported two photos; subsequent batches brought the inbox total to eight. The latest post-sanitation run skipped all eight as unchanged. Pagination and nesting are covered by fixtures; the current inbox did not require pagination.

Automatic detection would require a separate scheduled or event-driven service and is not enabled by this access setup. Existing recovered conversation photos are saved independently of the Notion importer.

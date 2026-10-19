# Publication checks for project evidence

The owner authorized a public cloud snapshot on `codex/cloud-project-snapshot`, based on `origin/main` commit `94a3e0fd7df129aa5359a2e78e7ef6726236f9f9`. The local reconciliation chat will combine it with `docs/games` and create a PR. This snapshot does not merge or create a PR.

## Included evidence and privacy handling

- Maintained hardware records, original conversation message content, tools/tests, photographs and provenance, and Backlog.md files are included.
- The eight Notion photographs contained location EXIF. GPS/location, owner, serial, and image-unique-ID metadata were removed where present with **ExifTool 13.59**, without pixel recompression. Every decoded frame, EXIF orientation, and ICC profile was checked against the original and remained identical.
- Notion filenames retain their original download hashes for stable links. In `docs/hardware/photos/notion-manifest.json`, `source_sha256` / `source_size_bytes` identify the raw download; `sha256` / `size_bytes` identify the sanitized file actually in Git. The per-file publication record describes the check. Original bytes are retained only in the private recovery archive, which is not published.
- Annotation provenance now points to the sanitized source-photo hash and retains `source_original_sha256` for the original download. The annotation image itself is unchanged.
- Conversation Markdown and all **179 + 21** message content records remain unchanged. Published HTML removes anonymous visitor/session bootstrap data and CSP nonces. Signed/authentication query fields were removed from search/source metadata URLs while preserving hosts, paths, fragments, and ordinary query parameters. [Archive provenance](research/conversations/archive/publication-provenance.json) distinguishes raw and published hashes.

The preservation archive, original raw imports, temporary downloads, local dependency caches, environment secrets, and unrelated execution/session data are outside the publication set. No `.env`, key, credential, or upload-token file is included. Hardware photos can still show ordinary visible background objects and equipment labels; this metadata review is not image-content redaction.

## Required check for future imports

**New or replaced photos require this review before every public commit or push.** The Notion importer downloads original bytes; it is not an automatic privacy sanitizer.

1. Review the proposed file list; exclude `.env` files, credentials, raw/private archives, caches, and temporary downloads.
2. Inspect image metadata without printing location or identity values. Check GPS, XMP location, owner, serial-number, and unique-identifier fields, including nested EXIF data.
3. Preserve raw originals outside Git. Use a metadata-aware tool to remove private tags without re-encoding image pixels. For ExifTool, the metadata-only deletion arguments used here were `-GPS:all=`, `-XMP:GPS*=`, `-*Owner*=`, `-*Serial*=`, and `-ImageUniqueID=` with `-overwrite_original`, after a private backup.
4. Verify every decoded image frame, orientation, and ICC profile before and after. Update published sizes/checksums and retain original-download checksums separately. Update annotation/source references when their source-file bytes change.
5. Recheck conversation/source archives for visitor data, signed download URLs, authentication query parameters, and credentials. Preserve actual conversation content and source attachment IDs; document any necessary metadata exclusions.
6. Run the importer tests, verify maintained document links and recorded hashes, and inspect the staged diff before publishing.

The importer recognizes a known original-download hash for an intact sanitized file and reuses that file when captions change or the same source is posted again. New or genuinely replaced image content still requires the publication review above.

## Validation performed for this snapshot

- **11 importer tests passed**, including retention of sanitized publication bytes across caption edits and duplicate sources.
- Live import reported **8 unchanged, 0 imported, 0 failed** after metadata sanitation.
- **24 photo records**, the annotation and its source reference, the manufacturer manual, and the conversation publication provenance were checked against their file hashes.
- Both published chat archives were checked independently for removal of visitor bootstrap data and signed/token-bearing URL fields, while preserving all 200 conversation message bodies.
- Maintained Markdown links were checked; source conversation links are archival references and are not a claim that every external source remains available.
- No physical board measurements, debugger connection, firmware build, or flashing has been performed.

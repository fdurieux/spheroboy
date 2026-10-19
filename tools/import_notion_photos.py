#!/usr/bin/env python3
"""Read the configured Notion inbox and retain photos without modifying Notion."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parents[1]
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".heif"}
MAX_BYTES = 50 * 1024 * 1024


class ImportFailure(Exception):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def page_id(value):
    path = urllib.parse.urlsplit(value).path if "://" in value else value
    matches = re.findall(r"[0-9a-fA-F]{32}|[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}", path)
    if not matches:
        raise ImportFailure("The inbox URL must contain a Notion page ID.")
    return str(uuid.UUID(matches[-1]))


def https_url(url):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ImportFailure("Attachment URLs must use HTTPS without user credentials.")
    return parsed.hostname


class NotionClient:
    def __init__(self, token):
        self.token = token
        self.opener = urllib.request.build_opener(NoRedirect())

    def api(self, path):
        request = urllib.request.Request(
            "https://api.notion.com/v1/" + path,
            headers={"Authorization": "Bearer " + self.token, "Notion-Version": "2022-06-28"},
        )
        for attempt in range(3):
            try:
                with self.opener.open(request, timeout=30) as response:
                    return json.load(response)
            except urllib.error.HTTPError as error:
                if error.code == 429 and attempt < 2:
                    time.sleep(min(5, max(1, int(error.headers.get("Retry-After", "1")))))
                    continue
                raise ImportFailure(f"Notion API returned HTTP {error.code}; check page access and environment settings.") from None
            except (urllib.error.URLError, TimeoutError):
                raise ImportFailure("Notion API connection failed; check network access.") from None

    def download(self, url):
        # Never forward the integration token to attachment hosts or redirects.
        for _ in range(6):
            host = https_url(url)
            request = urllib.request.Request(url, headers={"User-Agent": "Spheroboy-Photo-Import/1"})
            try:
                with self.opener.open(request, timeout=60) as response:
                    data = response.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES:
                    raise ImportFailure("Attachment exceeds the 50 MiB limit.")
                return data
            except urllib.error.HTTPError as error:
                if error.code in (301, 302, 303, 307, 308) and error.headers.get("Location"):
                    url = urllib.parse.urljoin(url, error.headers["Location"])
                    continue
                raise ImportFailure(f"Attachment host {host} returned HTTP {error.code}; check allowed domains.") from None
            except (urllib.error.URLError, TimeoutError):
                raise ImportFailure(f"Attachment download from {host} failed; check allowed domains.") from None
        raise ImportFailure("Attachment exceeded the redirect limit.")


def walk_blocks(client, root_id, visited=None):
    visited = set() if visited is None else visited
    if root_id in visited:
        return
    visited.add(root_id)
    cursor = None
    while True:
        query = {"page_size": 100}
        if cursor:
            query["start_cursor"] = cursor
        response = client.api(f"blocks/{root_id}/children?" + urllib.parse.urlencode(query))
        for block in response["results"]:
            yield block
            if block.get("has_children") or block["type"] == "child_page":
                yield from walk_blocks(client, block["id"], visited)
        if not response.get("has_more"):
            break
        next_cursor = response.get("next_cursor")
        if not next_cursor or next_cursor == cursor:
            raise ImportFailure("Notion returned invalid pagination; import is incomplete.")
        cursor = next_cursor


def image_suffix(data):
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return ".gif"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return ".webp"
    if data[4:8] == b"ftyp" and any(brand in data[8:40] for brand in (b"heic", b"heix", b"hevc", b"hevx", b"mif1", b"msf1")):
        return ".heic"
    raise ImportFailure("Attachment is not a supported JPEG, PNG, GIF, WebP, or HEIF image.")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_text(path, text):
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def render_index(state):
    lines = ["# Notion inbox photos", "", f"Source inbox: https://www.notion.so/{state['page_id'].replace('-', '')}", "",
             "Generated by `tools/import_notion_photos.py`. Originals are retained locally; imports do not delete files or modify Notion.", "",
             "| Photo | Caption | Source block |", "|---|---|---|"]
    for photo in state["photos"]:
        caption = photo["caption"].replace("|", "\\|").replace("\n", " ")
        link = f"https://www.notion.so/{state['page_id'].replace('-', '')}#{photo['block_id'].replace('-', '')}"
        lines.append(f"| [{photo['filename']}]({photo['filename']}) | {caption} | [Notion]({link}) |")
    if not state["photos"]:
        lines += ["", "No photos have been imported from this inbox yet."]
    return "\n".join(lines) + "\n"


def import_photos(client, inbox_id, output):
    client.api("pages/" + inbox_id)  # Verify access before touching local state.
    output.mkdir(parents=True, exist_ok=True)
    manifest = output / "notion-manifest.json"
    state = json.loads(manifest.read_text()) if manifest.exists() else {"version": 1, "page_id": inbox_id, "photos": []}
    if state.get("version") != 1 or state.get("page_id") != inbox_id:
        raise ImportFailure("Existing manifest belongs to another inbox or format; use a separate output directory.")
    existing = {digest(path): path.name for path in sorted(output.iterdir()) if path.is_file() and not path.is_symlink() and path.suffix.lower() in IMAGE_SUFFIXES}
    retained = {p["filename"]: p for p in state["photos"] if existing.get(p["sha256"]) == p["filename"]}
    # A privacy-reviewed publication file can differ from the original download
    # solely in metadata. Reuse it instead of restoring the original metadata.
    for photo in retained.values():
        if photo.get("source_sha256"):
            existing[photo["source_sha256"]] = photo["filename"]
    summary = {"found": 0, "imported": 0, "duplicates": 0, "unchanged": 0, "failed": 0}
    for block in walk_blocks(client, inbox_id):
        kind = block["type"]
        if kind not in ("image", "file"):
            continue
        attachment = block[kind]
        if kind == "file" and Path(attachment.get("name", "")).suffix.lower() not in IMAGE_SUFFIXES:
            continue
        summary["found"] += 1
        prior = [p for p in state["photos"] if p["block_id"] == block["id"]]
        if prior:
            latest = prior[-1]
            path = output / latest["filename"]
            if path.parent != output or path.is_symlink():
                raise ImportFailure("Invalid local photo path in manifest.")
            if block.get("last_edited_time") and latest["last_edited_time"] == block["last_edited_time"] and path.is_file() and digest(path) == latest["sha256"]:
                summary["unchanged"] += 1
                continue
        try:
            source = attachment.get(attachment.get("type"), {})
            if not source.get("url"):
                raise ImportFailure("Image block has no downloadable URL.")
            data = client.download(source["url"])
            suffix = image_suffix(data)
            sha = hashlib.sha256(data).hexdigest()
            if sha in existing:
                filename = existing[sha]
                summary["duplicates"] += 1
            else:
                filename = f"notion-{sha}{suffix}"
                with (output / filename).open("xb") as handle:
                    handle.write(data)
                existing[sha] = filename
                summary["imported"] += 1
            caption = "".join(p.get("plain_text", p.get("text", {}).get("content", "")) for p in attachment.get("caption", []))
            current_file = output / filename
            current_sha = digest(current_file)
            photo = dict(retained.get(filename, {}))
            photo.update({"block_id": block["id"], "last_edited_time": block.get("last_edited_time"), "filename": filename,
                          "caption": caption, "sha256": current_sha, "size_bytes": current_file.stat().st_size})
            if current_sha != sha:
                photo.update({"source_sha256": sha, "source_size_bytes": len(data)})
            matching = next((p for p in prior if p["sha256"] == current_sha), None)
            if matching:
                state["photos"].remove(matching)
            state["photos"].append(photo)
            retained[filename] = photo
        except ImportFailure as error:
            summary["failed"] += 1
            print(f"Block {block['id']}: {error}", file=sys.stderr)
    atomic_text(manifest, json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    atomic_text(output / "notion-index.md", render_index(state))
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page", help="Override the configured inbox URL or page ID")
    parser.add_argument("--output", type=Path, default=ROOT / "docs/hardware/photos")
    args = parser.parse_args()
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        parser.exit(1, "NOTION_TOKEN is missing; configure it in secure environment settings.\n")
    try:
        inbox = args.page or json.loads((ROOT / "tools/notion-inbox.json").read_text())["page_url"]
        summary = import_photos(NotionClient(token), page_id(inbox), args.output.resolve())
        print(json.dumps(summary, sort_keys=True))
        return 1 if summary["failed"] else 0
    except ImportFailure as error:
        print(str(error), file=sys.stderr)
    except (OSError, ValueError, KeyError, TypeError):
        # Exceptions can contain signed URLs; keep diagnostics free of credentials.
        print("Import failed while reading source data or local files; no successful run is claimed.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())

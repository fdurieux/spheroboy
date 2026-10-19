import base64
import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock
import urllib.error

from import_notion_photos import ImportFailure, NotionClient, import_photos, page_id


PAGE = "3feb8589-dab0-80be-8a6c-da3d72410d28"
PNG = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII=")


def image(identifier, url="https://attachments.example/photo?temporary-signature=private", edited="2026-10-19T12:00:00Z"):
    return {"id": identifier, "type": "image", "has_children": False, "last_edited_time": edited,
            "image": {"type": "file", "file": {"url": url}, "caption": [{"plain_text": "PCB front"}]}}


def children(blocks, more=False, cursor=None):
    return {"results": blocks, "has_more": more, "next_cursor": cursor}


class FixtureClient:
    def __init__(self, blocks):
        self.responses = {f"blocks/{PAGE}/children?page_size=100": children(blocks)}
        self.download = Mock(return_value=PNG)

    def api(self, path):
        if path == "pages/" + PAGE:
            return {"object": "page", "id": PAGE}
        return self.responses[path]


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name)

    def manifest(self):
        return json.loads((self.output / "notion-manifest.json").read_text())

    def test_shared_page_url_parses_ignoring_query(self):
        self.assertEqual(page_id("https://app.notion.com/p/Spheroboy-Photo-inbox-" + PAGE.replace("-", "") + "?source=copy_link"), PAGE)

    def test_realistic_image_import_and_repeat_preserve_bytes_and_sources(self):
        client = FixtureClient([image("photo-1")])
        first = import_photos(client, PAGE, self.output)
        record = self.manifest()["photos"][0]
        self.assertEqual((self.output / record["filename"]).read_bytes(), PNG)
        self.assertEqual(record["caption"], "PCB front")
        self.assertEqual(record["block_id"], "photo-1")
        self.assertEqual(first["imported"], 1)
        second = import_photos(client, PAGE, self.output)
        self.assertEqual(second["unchanged"], 1)
        self.assertEqual(client.download.call_count, 1)
        self.assertNotIn("temporary-signature", (self.output / "notion-manifest.json").read_text())
        self.assertNotIn("temporary-signature", (self.output / "notion-index.md").read_text())

    def test_nested_blocks_pagination_and_preexisting_photo_deduplication(self):
        (self.output / "conversation-photo.png").write_bytes(PNG)
        nested = {"id": "nested", "type": "toggle", "has_children": True}
        client = FixtureClient([])
        client.responses[f"blocks/{PAGE}/children?page_size=100"] = children([nested], True, "next")
        client.responses["blocks/nested/children?page_size=100"] = children([image("photo-1")])
        file_block = {"id": "file-photo", "type": "file", "last_edited_time": "today", "file": {"name": "board.jpg", "type": "external", "external": {"url": "https://attachments.example/file"}}}
        client.responses[f"blocks/{PAGE}/children?page_size=100&start_cursor=next"] = children([file_block])
        result = import_photos(client, PAGE, self.output)
        self.assertEqual(result["found"], 2)
        self.assertEqual(result["duplicates"], 2)
        self.assertEqual(result["imported"], 0)
        self.assertEqual({p["filename"] for p in self.manifest()["photos"]}, {"conversation-photo.png"})

    def test_failed_attachment_is_not_marked_imported_and_can_be_retried(self):
        client = FixtureClient([image("photo-1"), image("photo-2")])
        client.download.side_effect = [ImportFailure("Download failed"), PNG]
        with contextlib.redirect_stderr(io.StringIO()):
            result = import_photos(client, PAGE, self.output)
        self.assertEqual(result["failed"], 1)
        self.assertEqual(len(self.manifest()["photos"]), 1)
        client.download.side_effect = None
        client.download.return_value = PNG
        retried = import_photos(client, PAGE, self.output)
        self.assertEqual(retried["failed"], 0)
        self.assertEqual(retried["duplicates"], 1)
        self.assertEqual(len(self.manifest()["photos"]), 2)

    def test_changed_image_preserves_previous_revision(self):
        client = FixtureClient([image("photo-1")])
        import_photos(client, PAGE, self.output)
        client.responses[f"blocks/{PAGE}/children?page_size=100"] = children([image("photo-1", edited="2026-10-20T12:00:00Z")])
        client.download.return_value = b"GIF89a" + b"new-image-content"
        result = import_photos(client, PAGE, self.output)
        self.assertEqual(result["imported"], 1)
        self.assertEqual(len(self.manifest()["photos"]), 2)
        self.assertTrue(all((self.output / p["filename"]).is_file() for p in self.manifest()["photos"]))

    def test_metadata_sanitized_file_survives_caption_edit_and_duplicate_source(self):
        client = FixtureClient([image("photo-1")])
        import_photos(client, PAGE, self.output)
        state = self.manifest()
        record = state["photos"][0]
        # Model metadata removal as different source bytes with identical retained
        # published image content. No image-processing dependency is required.
        original_download = PNG + b"metadata retained only in private storage"
        record.update({"source_sha256": hashlib.sha256(original_download).hexdigest(),
                       "source_size_bytes": len(original_download),
                       "publication_sanitization": {"decoded_pixels_unchanged": True}})
        (self.output / "notion-manifest.json").write_text(json.dumps(state))
        client.responses[f"blocks/{PAGE}/children?page_size=100"] = children([
            image("photo-1", edited="2026-10-20T12:00:00Z"), image("photo-2")])
        client.download.return_value = original_download
        result = import_photos(client, PAGE, self.output)
        self.assertEqual(result["imported"], 0)
        self.assertEqual(result["duplicates"], 2)
        for photo in self.manifest()["photos"]:
            self.assertEqual((self.output / photo["filename"]).read_bytes(), PNG)
            self.assertEqual(photo["sha256"], hashlib.sha256(PNG).hexdigest())
            self.assertEqual(photo["source_sha256"], hashlib.sha256(original_download).hexdigest())
            self.assertTrue(photo["publication_sanitization"]["decoded_pixels_unchanged"])

    def test_non_image_response_is_rejected_and_non_image_file_is_ignored(self):
        client = FixtureClient([image("photo-1"), {"id": "pdf", "type": "file", "file": {"name": "manual.pdf"}}])
        client.download.return_value = b"<!DOCTYPE html><html>Access denied</html>"
        with contextlib.redirect_stderr(io.StringIO()):
            result = import_photos(client, PAGE, self.output)
        self.assertEqual(result["found"], 1)
        self.assertEqual(result["failed"], 1)
        self.assertEqual(self.manifest()["photos"], [])

    def test_missing_or_changed_local_file_is_repaired(self):
        client = FixtureClient([image("photo-1")])
        import_photos(client, PAGE, self.output)
        photo = self.output / self.manifest()["photos"][0]["filename"]
        photo.unlink()
        self.assertEqual(import_photos(client, PAGE, self.output)["imported"], 1)
        photo.write_bytes(b"corrupted")
        # Preserve the changed local file; do not overwrite it silently.
        with self.assertRaises(FileExistsError):
            import_photos(client, PAGE, self.output)

    def test_download_redirects_never_receive_integration_token(self):
        client = NotionClient("test-token")
        client.opener = Mock()
        redirect = urllib.error.HTTPError("https://attachments.example/start", 302, "redirect", {"Location": "https://storage.example/photo"}, None)
        client.opener.open.side_effect = [redirect, io.BytesIO(PNG)]
        self.assertEqual(client.download("https://attachments.example/start"), PNG)
        for call in client.opener.open.call_args_list:
            self.assertIsNone(call.args[0].get_header("Authorization"))

    def test_api_redirect_cannot_forward_token(self):
        client = NotionClient("test-token")
        client.opener = Mock()
        client.opener.open.side_effect = urllib.error.HTTPError("https://api.notion.com/v1/pages/test", 302, "redirect", {"Location": "https://elsewhere.example"}, None)
        with self.assertRaises(ImportFailure):
            client.api("pages/" + PAGE)
        self.assertEqual(client.opener.open.call_count, 1)

    def test_attachment_https_is_required_after_redirect(self):
        client = NotionClient("test-token")
        client.opener = Mock()
        client.opener.open.side_effect = urllib.error.HTTPError("https://attachments.example/start", 302, "redirect", {"Location": "http://storage.example/photo"}, None)
        with self.assertRaises(ImportFailure):
            client.download("https://attachments.example/start")
        self.assertEqual(client.opener.open.call_count, 1)


if __name__ == "__main__":
    unittest.main()

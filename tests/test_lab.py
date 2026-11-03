import json
import tempfile
import unittest
from pathlib import Path

from scripts.lab import ManifestError, load_manifest, project_path, validate_manifest


class LabManifestTests(unittest.TestCase):
    def test_workspace_manifest_is_valid(self):
        manifest = load_manifest()
        self.assertEqual(manifest["schema_version"], 1)

    def test_rejects_unknown_integration_target(self):
        manifest = {
            "schema_version": 1,
            "projects": [
                {
                    "id": "alpha",
                    "name": "Alpha",
                    "path": "alpha",
                    "provides": "example",
                    "runs_alone": True,
                    "integrates_with": ["missing"],
                }
            ],
        }
        with self.assertRaisesRegex(ManifestError, "unknown integration target"):
            validate_manifest(manifest)

    def test_rejects_paths_outside_workspace(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(ManifestError, "escapes workspace"):
                project_path(root, "../outside")

    def test_manifest_file_is_read_as_json(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest_path = Path(directory) / "lab.json"
            manifest_path.write_text(
                json.dumps({"schema_version": 1, "projects": []}),
                encoding="utf-8",
            )
            self.assertEqual(load_manifest(manifest_path)["projects"], [])


if __name__ == "__main__":
    unittest.main()

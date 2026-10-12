from __future__ import annotations

import json
import re
import shutil
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = re.search(r'^  version: "([^"]+)"$', (ROOT / "skills/ai-native-sdlc/SKILL.md").read_text(), re.M).group(1)
REFERENCES = ("completion-evidence", "knowledge-vault", "project-grounding", "test-integrity")
PREFIX = f"ai-native-sdlc-{VERSION}"
PLUGIN = "plugins/ai-native-sdlc"
SKILL = f"{PLUGIN}/skills/ai-native-sdlc"
SOURCES = {
    ".agents/plugins/marketplace.json": "packaging/codex-marketplace.json",
    ".claude-plugin/marketplace.json": "packaging/claude-marketplace.json",
    f"{PLUGIN}/.codex-plugin/plugin.json": "packaging/codex-plugin.json",
    f"{PLUGIN}/.claude-plugin/plugin.json": "packaging/claude-plugin.json",
    f"{PLUGIN}/LICENSE": "LICENSE",
    f"{SKILL}/SKILL.md": "skills/ai-native-sdlc/SKILL.md",
    **{f"{SKILL}/references/{name}.md": f"skills/ai-native-sdlc/references/{name}.md" for name in REFERENCES},
}


class DistributionTests(unittest.TestCase):
    def fixture(self, directory: Path) -> None:
        shutil.copy2(ROOT / "Makefile", directory / "Makefile")
        shutil.copy2(ROOT / "LICENSE", directory / "LICENSE")
        shutil.copytree(ROOT / "packaging", directory / "packaging")
        shutil.copytree(ROOT / "skills", directory / "skills")

    def build(self, directory: Path) -> subprocess.CompletedProcess:
        return subprocess.run(["make", "package"], cwd=directory, capture_output=True, text=True, timeout=30)

    def archive(self, directory: Path) -> Path:
        return directory / "build" / f"{PREFIX}.tar.gz"

    def test_bundle_contains_only_allowlisted_sources_with_identical_bytes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="sdlc-package-test-") as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            for private_path in (".env", "memory/private.md", "docs/audit/private.md", "dist/old.zip", "reports/private.json"):
                target = directory / private_path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("PRIVATE_TEST_SENTINEL")
            result = self.build(directory)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with tarfile.open(self.archive(directory)) as archive:
                files = {member.name for member in archive.getmembers() if member.isfile()}
                self.assertEqual(files, {f"{PREFIX}/{target}" for target in SOURCES})
                self.assertFalse(any(member.issym() or member.islnk() for member in archive.getmembers()))
                for target, source in SOURCES.items():
                    self.assertEqual(archive.extractfile(f"{PREFIX}/{target}").read(), (directory / source).read_bytes())

    def test_native_catalogs_and_manifests_agree_and_stay_inside_bundle(self) -> None:
        for host in ("codex", "claude"):
            manifest = json.loads((ROOT / "packaging" / f"{host}-plugin.json").read_text())
            catalog = json.loads((ROOT / "packaging" / f"{host}-marketplace.json").read_text())
            self.assertEqual(manifest["name"], "ai-native-sdlc")
            self.assertEqual(manifest["version"], VERSION)
            self.assertEqual(catalog["name"], "sdlc-local")
            self.assertEqual(len(catalog["plugins"]), 1)
            entry = catalog["plugins"][0]
            self.assertEqual(entry["name"], manifest["name"])
            source = entry["source"] if host == "claude" else entry["source"]["path"]
            self.assertEqual(source, "./plugins/ai-native-sdlc")
            self.assertFalse({"hooks", "mcpServers", "apps", "agents", "commands"} & manifest.keys())
            if host == "codex":
                self.assertEqual(manifest["skills"], "./skills/")
                self.assertEqual(entry["source"]["source"], "local")
            else:
                self.assertTrue(catalog["description"])

    def test_existing_archive_is_refused_and_preserved(self) -> None:
        with tempfile.TemporaryDirectory(prefix="sdlc-package-test-") as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            archive = self.archive(directory)
            archive.parent.mkdir()
            archive.write_bytes(b"existing archive with unwanted stale material")
            result = self.build(directory)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(archive.read_bytes(), b"existing archive with unwanted stale material")

    def test_missing_required_reference_blocks_packaging(self) -> None:
        with tempfile.TemporaryDirectory(prefix="sdlc-package-test-") as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            (directory / "skills/ai-native-sdlc/references/project-grounding.md").unlink()
            self.assertNotEqual(self.build(directory).returncode, 0)
            self.assertFalse(self.archive(directory).exists())

    def test_symlinked_skill_file_blocks_packaging(self) -> None:
        with tempfile.TemporaryDirectory(prefix="sdlc-package-test-") as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            target = directory / "skills/ai-native-sdlc/SKILL.md"
            target.unlink()
            target.symlink_to(directory / "LICENSE")
            self.assertNotEqual(self.build(directory).returncode, 0)
            self.assertFalse(self.archive(directory).exists())

    def test_symlinked_build_directory_cannot_redirect_output(self) -> None:
        with tempfile.TemporaryDirectory(prefix="sdlc-package-test-") as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            external = directory / "external-target"
            external.mkdir()
            (directory / "build").symlink_to(external, target_is_directory=True)
            self.assertNotEqual(self.build(directory).returncode, 0)
            self.assertEqual(list(external.iterdir()), [])

    def test_output_override_cannot_write_into_private_collection(self) -> None:
        with tempfile.TemporaryDirectory(prefix="sdlc-package-test-") as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            result = subprocess.run(
                ["make", "package", "OUT=memory/unwanted.tar.gz"],
                cwd=directory, capture_output=True, text=True, timeout=30,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((directory / "memory/unwanted.tar.gz").exists())

    def test_version_override_cannot_mislabel_bundle(self) -> None:
        with tempfile.TemporaryDirectory(prefix="sdlc-package-test-") as temporary:
            directory = Path(temporary)
            self.fixture(directory)
            result = subprocess.run(
                ["make", "package", "VERSION=9.9.9"],
                cwd=directory, capture_output=True, text=True, timeout=30,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((directory / "build/ai-native-sdlc-9.9.9.tar.gz").exists())

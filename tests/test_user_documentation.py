from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = (
    ROOT / "README.md",
    ROOT / "CHANGELOG.md",
    ROOT / "docs" / "USER-GUIDE.md",
    ROOT / "docs" / "USE-CASES.md",
)


def local_targets(document: Path):
    text = document.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        yield (document.parent / unquote(parsed.path)).resolve()


class UserDocumentationTests(unittest.TestCase):
    def test_documentation_and_local_link_targets_exist(self) -> None:
        for document in DOCUMENTS:
            with self.subTest(document=document.name):
                self.assertTrue(document.is_file(), str(document))
                for target in local_targets(document):
                    self.assertTrue(target.exists(), str(target))

    def test_local_doc_links_stay_in_repo_and_avoid_private_corpus(self) -> None:
        private_roots = ("memory", "docs/audit", "dist", "reports")
        for document in DOCUMENTS:
            with self.subTest(document=document.name):
                self.assertTrue(document.is_file(), str(document))
                for target in local_targets(document):
                    self.assertTrue(target.is_relative_to(ROOT), str(target))
                    relative = target.relative_to(ROOT).as_posix()
                    for private_root in private_roots:
                        self.assertFalse(
                            relative == private_root or relative.startswith(private_root + "/"),
                            str(target),
                        )

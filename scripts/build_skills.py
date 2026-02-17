#!/usr/bin/env python3
"""Build helper for Codex skills.

Copies shared Conductor references into each curated skill's references directory.
"""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = ROOT / "skills" / "_shared"
CURATED_DIR = ROOT / "skills" / ".curated"


def main() -> int:
    if not SHARED_DIR.is_dir():
        raise SystemExit(f"Missing shared directory: {SHARED_DIR}")
    if not CURATED_DIR.is_dir():
        raise SystemExit(f"Missing curated directory: {CURATED_DIR}")

    shared_files = sorted(SHARED_DIR.glob("*.md"))
    if not shared_files:
        raise SystemExit("No shared markdown references found.")

    copied = 0
    for skill_dir in sorted(p for p in CURATED_DIR.iterdir() if p.is_dir()):
        references_dir = skill_dir / "references"
        references_dir.mkdir(parents=True, exist_ok=True)
        for shared_file in shared_files:
            dst = references_dir / shared_file.name
            shutil.copy2(shared_file, dst)
            copied += 1
            print(f"[copy] {shared_file.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")

    print(f"[done] copied {copied} shared reference files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

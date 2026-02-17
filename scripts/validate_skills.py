#!/usr/bin/env python3
"""Validation for Codex Conductor skills repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CURATED_DIR = ROOT / "skills" / ".curated"
REQUIRED_SKILLS = {
    "conductor-setup",
    "conductor-new-track",
    "conductor-implement",
    "conductor-status",
    "conductor-revert",
    "conductor-review",
}
FORBIDDEN_STRINGS = (
    "/" + "conductor:",
    "~/" + ".gemini/",
    "gemini " + "extensions install",
)
TEXT_FILE_EXTENSIONS = {
    ".md",
    ".toml",
    ".yaml",
    ".yml",
    ".json",
    ".txt",
    ".py",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="strict")


def parse_frontmatter(content: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        raise ValueError("Missing or malformed YAML frontmatter")

    frontmatter = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"').strip("'")
    return frontmatter


def validate_skill_dir(skill_dir: Path, errors: list[str]) -> None:
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    protocol_md = skill_dir / "references" / "protocol.md"

    for required in (skill_md, openai_yaml, protocol_md):
        if not required.exists():
            errors.append(f"Missing required file: {required.relative_to(ROOT)}")

    if skill_md.exists():
        try:
            content = read_text(skill_md)
            fm = parse_frontmatter(content)
            for key in ("name", "description"):
                if not fm.get(key):
                    errors.append(f"{skill_md.relative_to(ROOT)} missing required frontmatter key '{key}'")
            if fm.get("name") and fm.get("name") != skill_name:
                errors.append(
                    f"{skill_md.relative_to(ROOT)} frontmatter name '{fm.get('name')}' does not match directory '{skill_name}'"
                )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"Invalid SKILL.md in {skill_name}: {exc}")

    if openai_yaml.exists():
        text = read_text(openai_yaml)
        required_lines = ("interface:", "display_name:", "short_description:", "default_prompt:")
        for required_line in required_lines:
            if required_line not in text:
                errors.append(f"{openai_yaml.relative_to(ROOT)} missing '{required_line}'")


def scan_forbidden_strings(errors: list[str]) -> None:
    self_path = Path(__file__).resolve()
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.resolve() == self_path:
            continue
        if path.suffix not in TEXT_FILE_EXTENSIONS and path.name not in {"README", "LICENSE"}:
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            errors.append(f"Unable to read {path.relative_to(ROOT)}: {exc}")
            continue

        for forbidden in FORBIDDEN_STRINGS:
            if forbidden in text:
                errors.append(f"Forbidden legacy string '{forbidden}' found in {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []

    if not CURATED_DIR.is_dir():
        errors.append(f"Missing curated skill directory: {CURATED_DIR}")
    else:
        actual_skills = {p.name for p in CURATED_DIR.iterdir() if p.is_dir()}
        missing = sorted(REQUIRED_SKILLS - actual_skills)
        extra = sorted(actual_skills - REQUIRED_SKILLS)

        if missing:
            errors.append(f"Missing required skill directories: {', '.join(missing)}")
        if extra:
            print(f"[warn] Extra curated skill directories found: {', '.join(extra)}")

        for skill in sorted(REQUIRED_SKILLS & actual_skills):
            validate_skill_dir(CURATED_DIR / skill, errors)

    scan_forbidden_strings(errors)

    if errors:
        print("Validation failed:")
        for issue in errors:
            print(f"- {issue}")
        return 1

    print("Validation passed: curated skills structure and legacy-string checks are clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

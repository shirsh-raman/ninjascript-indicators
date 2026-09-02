#!/usr/bin/env python3
"""Validate the public files and contents of a skill package."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit


REQUIRED_FILES = ("SKILL.md", "references/source-index.jsonl")
SOURCE_FIELDS = {
    "record_id",
    "canonical_url",
    "title",
    "focused_track",
    "reference_version",
    "classification",
}

FORBIDDEN = (
    ("ninjascipt", re.compile(r"ninjascipt", re.IGNORECASE)),
    ("/home/", re.compile(r"/home/")),
    ("/Users/", re.compile(r"/Users/")),
    (r"C:\\Users\\", re.compile(r"C:\\Users\\", re.IGNORECASE)),
    ("email address", re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.IGNORECASE)),
    ("credential-like value", re.compile(r"(?i)\b(?:password|passwd|token|secret|api[_ -]?key)\s*[:=]\s*[^\s,;]+")),
    ("private-key pattern", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("ninja-docs-focused/", re.compile(r"ninja-docs-focused/")),
    ("../../../", re.compile(r"\.\./\.\./\.\./")),
)
PRIVATE_URL = re.compile(
    r"(?i)\b(?:https?|ftp)://(?:[^/\s:@]+:[^/\s@]+@|localhost|[^/]*\.local|10\.|127\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.)"
)
MARKDOWN_LINK = re.compile(r"!?(?:\[[^]]*\])\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)")
VCS_DIRECTORIES = {".git", ".hg", ".svn", ".bzr", "CVS"}


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _check_frontmatter(path: Path, errors: list[str]) -> None:
    try:
        text = _read_text(path)
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path}: cannot read ({exc})")
        return
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{path}: frontmatter must start with ---")
        return
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        errors.append(f"{path}: frontmatter is not closed")
        return
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            errors.append(f"{path}: invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    for key in ("name", "description"):
        if not fields.get(key):
            errors.append(f"{path}: frontmatter requires {key}")


def _check_manifest(path: Path, errors: list[str]) -> None:
    try:
        lines = _read_text(path).splitlines()
    except (OSError, UnicodeError) as exc:
        errors.append(f"{path}: cannot read ({exc})")
        return
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{number}: malformed JSONL ({exc.msg})")
            continue
        if not isinstance(record, dict):
            errors.append(f"{path}:{number}: source-index record must be an object")
            continue
        missing = sorted(SOURCE_FIELDS - record.keys())
        if missing:
            errors.append(f"{path}:{number}: missing source-index fields: {', '.join(missing)}")


def _check_links(path: Path, package: Path, errors: list[str]) -> None:
    try:
        text = _read_text(path)
    except (OSError, UnicodeError):
        return
    for destination in MARKDOWN_LINK.findall(text):
        if destination.startswith(("#", "/", "\\")):
            if destination.startswith(("/", "\\")):
                errors.append(f"{path}: link escapes package: {destination}")
            continue
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / parsed.path).resolve()
        try:
            target.relative_to(package.resolve())
        except ValueError:
            errors.append(f"{path}: link escapes package: {destination}")
        else:
            if not target.exists():
                errors.append(f"{path}: broken local link: {destination}")


def validate_bundle(package_dir: str | Path = ".") -> list[str]:
    """Return validation errors; an empty list means the package is valid."""
    package = Path(package_dir).resolve()
    errors: list[str] = []
    if not package.is_dir():
        return [f"package directory does not exist: {package_dir}"]
    for required in REQUIRED_FILES:
        if not (package / required).is_file():
            errors.append(f"missing required public file: {required}")
    if (package / "SKILL.md").is_file():
        _check_frontmatter(package / "SKILL.md", errors)
    if (package / "references/source-index.jsonl").is_file():
        _check_manifest(package / "references/source-index.jsonl", errors)

    paths: list[Path] = []
    for root, directories, filenames in os.walk(package):
        directories[:] = [directory for directory in directories if directory not in VCS_DIRECTORIES]
        paths.extend(
            path for path in (Path(root) / filename for filename in filenames) if path.is_file()
        )

    for path in sorted(paths):
        relative = path.relative_to(package).as_posix()
        if path.name == ".env" or path.name.startswith(".env."):
            errors.append(f"forbidden file: {relative}")
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            errors.append(f"forbidden generated file: {relative}")
        # The validator and tests necessarily contain examples of rejected text.
        if relative in {"scripts/validate_bundle.py", "tests/test_bundle.py"}:
            continue
        try:
            text = _read_text(path)
        except (OSError, UnicodeError):
            continue
        for label, pattern in FORBIDDEN:
            if pattern.search(text) or pattern.search(relative):
                errors.append(f"forbidden {label}: {relative}")
        if PRIVATE_URL.search(text):
            errors.append(f"private URL: {relative}")
        if path.suffix.lower() in {".md", ".markdown"}:
            _check_links(path, package, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a skill package")
    parser.add_argument("package_dir", nargs="?", default=".")
    args = parser.parse_args(argv)
    errors = validate_bundle(args.package_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("bundle valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

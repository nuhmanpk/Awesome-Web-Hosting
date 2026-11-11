#!/usr/bin/env python3
"""Validate README.md service tables.

Usage:
    python3 .github/scripts/validate_readme.py [BASE_README]

Errors (exit 1):
  - a row inside a service table does not match `| [Name](https://url) | Description | Free tier |`
  - rows in a category are not in alphabetical order (case-insensitive)
  - a service name or URL appears more than once

Warnings (exit 0), only when BASE_README is given:
  - more than one service row was added
  - service rows were removed
"""

import os
import re
import sys
from pathlib import Path

CATEGORIES = {
    "🌐 Static Site Hosting",
    "🔧 Full-Stack Platforms",
    "⚡ Serverless & Edge",
    "☁️ VPS & Cloud Infrastructure",
    "🎨 No-Code & Low-Code Builders",
    "🧪 Indie & Hobby Projects",
}
HEADER = re.compile(r"^\|\s*Service\s*\|\s*Description\s*\|\s*Free Tier Highlights\s*\|$")
ROW = re.compile(r"^\| \[([^\]]+)\]\((https?://[^)\s]+)\) \| ([^|]+?) \| ([^|]+?) \|$")
IN_ACTIONS = os.environ.get("GITHUB_ACTIONS") == "true"


def report(level, msg, line=None):
    if IN_ACTIONS:
        loc = f" file=README.md,line={line}" if line else " file=README.md"
        print(f"::{level}{loc}::{msg}")
    else:
        print(f"{level.upper()}: {msg}" + (f" (line {line})" if line else ""))


def parse(text):
    """Return list of (category, name, url, line_no) and list of format errors."""
    services, errors = [], []
    category, in_table = None, False
    for no, line in enumerate(text.splitlines(), 1):
        heading = re.match(r"^## (.+)", line)
        if heading:
            category = heading.group(1).strip()
            in_table = False
            continue
        if category not in CATEGORIES:
            continue
        if HEADER.match(line):
            in_table = True
            continue
        if not in_table:
            continue
        if re.match(r"^\|[-| :]+\|$", line):
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        m = ROW.match(line)
        if not m:
            errors.append((no, f"Row in '{category}' has the wrong format. Expected: | [Name](https://url) | Description | Free tier |"))
            continue
        services.append((category, m.group(1).strip(), m.group(2).rstrip("/").lower(), no))
    return services, errors


def main():
    text = Path("README.md").read_text(encoding="utf-8")
    services, errors = parse(text)

    for no, msg in errors:
        report("error", msg, no)

    by_cat = {}
    for svc in services:
        by_cat.setdefault(svc[0], []).append(svc)
    for cat, rows in by_cat.items():
        for prev, cur in zip(rows, rows[1:]):
            if cur[1].lower() < prev[1].lower():
                errors.append((cur[3], ""))
                report("error", f"'{cur[1]}' is out of alphabetical order in '{cat}': it must come before '{prev[1]}'.", cur[3])

    seen_names, seen_urls = {}, {}
    for cat, name, url, no in services:
        key = name.lower()
        if key in seen_names:
            errors.append((no, ""))
            report("error", f"Duplicate service name '{name}' (first listed on line {seen_names[key]}).", no)
        if url in seen_urls:
            errors.append((no, ""))
            report("error", f"Duplicate URL '{url}' for '{name}' (first listed on line {seen_urls[url]}).", no)
        seen_names.setdefault(key, no)
        seen_urls.setdefault(url, no)

    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        base, _ = parse(Path(sys.argv[1]).read_text(encoding="utf-8"))
        base_keys = {(n.lower(), u) for _, n, u, _ in base}
        head_keys = {(n.lower(), u) for _, n, u, _ in services}
        added = [s for s in services if (s[1].lower(), s[2]) not in base_keys]
        removed = base_keys - head_keys
        if len(added) > 1:
            report("warning", f"This PR adds {len(added)} services: {', '.join(s[1] for s in added)}. "
                              "Please add one service per PR unless a maintainer agreed otherwise.")
        if removed:
            report("warning", f"This PR removes or renames {len(removed)} service(s): "
                              f"{', '.join(sorted(n for n, _ in removed))}. Explain why in the PR description.")
        for s in added:
            print(f"Added: {s[1]} -> {s[0]}")

    print(f"Checked {len(services)} services in {len(by_cat)} categories.")
    if errors:
        print(f"{len(errors)} problem(s) found. See CONTRIBUTING.md for the required format.")
        sys.exit(1)
    print("README.md looks good.")


if __name__ == "__main__":
    main()

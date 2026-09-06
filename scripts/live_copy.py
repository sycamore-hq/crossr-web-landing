#!/usr/bin/env python3
"""Live-copy calculations for the CrossR door.

Data and pure checks live here. I/O stays in main() and in the tests.
The door links out and owns no law; this module only flags stale copy.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Retired by PR 5. Whole-token match so "rust" the book is not a hit.
RETIRED_NAMES = (
    "rust-team-lead",
    "rust-code-writer",
    "rust-errors",
    "ocaml-code-writer",
    "rust-code-reviewer",
    "rust-code-tester",
)

# Prompt-set decision 7. Same order as docs/public-skills.json featured.
FEATURED_PILLS = (
    "code-writer",
    "rust",
    "code-review",
    "agent-harness",
    "skill-evaluator",
)

# Consumer pins on harness main until 5f. Not the 5d/5e tag names.
SKILLS_PIN = "v1-gan-layers"
LOOPS_PIN = "v1-cards"

PILL_NAME = re.compile(
    r'class="skill-pill[^"]*">\s*<div class="font-semibold">([^<]+)</div>'
)
PIN_ASSIGN = re.compile(r'(skills|loops)\s*=\s*"?([v][^\s"<]+)"?', re.I)
V0_TOKEN = re.compile(r"\bv0\b")


def token_hits(text: str, names: tuple[str, ...]) -> tuple[str, ...]:
    """Names that appear as whole tokens. Hyphens are part of the token."""
    hits = []
    for name in names:
        if re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", text):
            hits.append(name)
    return tuple(hits)


def featured_pill_names(html: str) -> tuple[str, ...]:
    """Skill names from .skill-pill .font-semibold, in document order."""
    return tuple(PILL_NAME.findall(html))


def pin_assignments(text: str) -> tuple[tuple[str, str], ...]:
    """Lockfile-style skills=/loops= assignments in the text."""
    return tuple((key.lower(), value) for key, value in PIN_ASSIGN.findall(text))


def assigned_values(assigns: tuple[tuple[str, str], ...], key: str) -> tuple[str, ...]:
    return tuple(value for name, value in assigns if name == key)


def html_failures(html: str) -> tuple[str, ...]:
    """5g defects on the Zola door. Empty means the live HTML is current."""
    failures: list[str] = []
    retired = token_hits(html, RETIRED_NAMES)
    if retired:
        failures.append("retired names: " + ", ".join(retired))
    pills = featured_pill_names(html)
    if pills != FEATURED_PILLS:
        failures.append(f"featured pills {pills} != {FEATURED_PILLS}")
    if V0_TOKEN.search(html):
        failures.append("live HTML still names v0")
    assigns = pin_assignments(html)
    if SKILLS_PIN not in assigned_values(assigns, "skills"):
        failures.append(f"skills pin {SKILLS_PIN} missing")
    if LOOPS_PIN not in assigned_values(assigns, "loops"):
        failures.append(f"loops pin {LOOPS_PIN} missing")
    return tuple(failures)


def pin_surface_failures(text: str) -> tuple[str, ...]:
    """Current-pin defects on a live surface (README, book bootstrap)."""
    failures: list[str] = []
    if V0_TOKEN.search(text):
        failures.append("live surface still names v0")
    assigns = pin_assignments(text)
    if SKILLS_PIN not in assigned_values(assigns, "skills"):
        failures.append(f"skills pin {SKILLS_PIN} missing")
    if LOOPS_PIN not in assigned_values(assigns, "loops"):
        failures.append(f"loops pin {LOOPS_PIN} missing")
    return tuple(failures)


def report_lines(html: str) -> tuple[str, ...]:
    failures = html_failures(html)
    if not failures:
        return ("live HTML copy is current",)
    return tuple(f"FAIL: {item}" for item in failures)


def main(argv: list[str] | None = None) -> int:
    root = Path(__file__).resolve().parent.parent
    path = root / "site" / "templates" / "index.html"
    html = path.read_text()
    lines = report_lines(html)
    for line in lines:
        print(line)
    return 0 if html_failures(html) == () else 1


if __name__ == "__main__":
    sys.exit(main())

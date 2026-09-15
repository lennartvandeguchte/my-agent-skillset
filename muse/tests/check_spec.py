#!/usr/bin/env python3
"""Check that a MUSE spec contains every required section, in order, with the required lines.

Usage:
    python3 tests/check_spec.py sessions/2026-09-15-some-slug.md [more files]
    python3 tests/check_spec.py            # checks every sessions/*.md and tests/fixtures/*.md

Exit code 0 when every file passes, 1 otherwise. No dependencies beyond the standard library.
"""
import glob
import os
import re
import sys

SECTIONS = [
    "The spark",
    "The problem",
    "The idea",
    "Values fit",
    "Council verdicts",
    "Weekend scope",
    "First prompt for Claude Code",
    "Kill criteria",
]

# Lines that must appear inside a given section (prefix match on a stripped line).
REQUIRED_LINES = {
    "The idea": ["What it is NOT:"],
    "Values fit": ["- Circularity:", "- Sustainability:", "- AI for good:"],
    "Council verdicts": ["- Jobs:", "- Einstein:", "- Gandhi:", "- Ostrom:", "- Builder:",
                         "Open question I chose not to answer:"],
    "Weekend scope": ["Ships:", "Stack:", "Data source:", "The one screen or command:"],
}

HEDGES = re.compile(r"\b(could|might|potentially|perhaps|maybe)\b", re.IGNORECASE)


def split_sections(text):
    """Return (title, ordered list of (heading, body))."""
    title = None
    sections = []
    current = None
    body = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("# ") and title is None:
            title = line[2:].strip()
            continue
        if not in_fence and line.startswith("## "):
            if current is not None:
                sections.append((current, "\n".join(body)))
            current = line[3:].strip()
            body = []
            continue
        body.append(line)
    if current is not None:
        sections.append((current, "\n".join(body)))
    return title, sections


def check(path):
    problems = []
    with open(path, encoding="utf-8") as f:
        text = f.read()
    title, sections = split_sections(text)
    if not title:
        problems.append("missing '# <Idea name>' title")
    headings = [h for h, _ in sections]
    if headings != SECTIONS:
        missing = [s for s in SECTIONS if s not in headings]
        extra = [h for h in headings if h not in SECTIONS]
        if missing:
            problems.append("missing sections: " + ", ".join(missing))
        if extra:
            problems.append("unexpected sections: " + ", ".join(extra))
        if not missing and not extra:
            problems.append("sections out of order: " + " > ".join(headings))
    bodies = dict(sections)
    for heading, body in sections:
        if not body.strip():
            problems.append(f"section '{heading}' is empty")
    for heading, needles in REQUIRED_LINES.items():
        body = bodies.get(heading, "")
        stripped = [l.strip() for l in body.splitlines()]
        for needle in needles:
            if not any(l.startswith(needle) for l in stripped):
                problems.append(f"section '{heading}' lacks a line starting with '{needle}'")
    spark = bodies.get("The spark", "")
    paragraphs = [p for p in re.split(r"\n\s*\n", spark.strip()) if p.strip()]
    if spark.strip() and not 2 <= len(paragraphs) <= 3:
        problems.append(f"'The spark' has {len(paragraphs)} paragraphs, expected 2-3")
    if any(l.lstrip().startswith(("- ", "* ")) for l in spark.splitlines()):
        problems.append("'The spark' contains bullet points")
    hedges = HEDGES.findall(spark)
    if hedges:
        problems.append("'The spark' hedges: " + ", ".join(sorted(set(h.lower() for h in hedges))))
    if "```" not in bodies.get("First prompt for Claude Code", ""):
        problems.append("'First prompt for Claude Code' has no fenced code block")
    return problems


def main(argv):
    paths = argv[1:]
    if not paths:
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        paths = sorted(glob.glob(os.path.join(here, "sessions", "*.md")))
        paths += sorted(glob.glob(os.path.join(here, "tests", "fixtures", "*.md")))
    if not paths:
        print("no spec files found")
        return 0
    failed = 0
    for path in paths:
        problems = check(path)
        if problems:
            failed += 1
            print(f"FAIL {path}")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"ok   {path}")
    print(f"{len(paths) - failed}/{len(paths)} specs pass")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

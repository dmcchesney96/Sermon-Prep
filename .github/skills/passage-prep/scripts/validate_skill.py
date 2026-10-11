#!/usr/bin/env python3
"""Small dependency-free structural audit for Passage Prep. Not a substitute for live research evals."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILL_DIR = ROOT / ".github/skills/passage-prep"
checks = []

def check(name: str, result: bool) -> None:
    checks.append((name, bool(result)))
    print(("PASS" if result else "FAIL") + ": " + name)

skill_path = SKILL_DIR / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8")
header = re.match(r"\A---\n(.*?)\n---\n", skill, flags=re.S)
check("YAML-like frontmatter delimiters", header is not None)
meta = header.group(1) if header else ""
name = re.search(r"^name:\s*([^\n]+)$", meta, flags=re.M)
desc = re.search(r'^description:\s*["\']?(.+?)["\']?$', meta, flags=re.M)
check("Skill name matches directory", bool(name) and name.group(1).strip() == SKILL_DIR.name)
check("Discoverable description length", bool(desc) and 40 <= len(desc.group(1)) <= 1024)
check("Skill body under 500 lines", len(skill.splitlines()) < 500)

refs = [
    "references/source-lists.md",
    "references/archive-directory.md",
    "references/archive-index.json",
    "references/source-policy.md",
    "references/output-format.md",
    "assets/reader-template.md",
    "evals/evals.json",
    "evals/README.md",
    "examples/matthew-5-4-smoke-test.md",
]
for relative in refs:
    check("Resource exists: " + relative, (SKILL_DIR / relative).is_file())

check("Commentary comes before sermon maps",
      skill.find("### Part 1 — COMMENTARY READING ROOM") >= 0 and
      skill.find("### Part 1 — COMMENTARY READING ROOM") <
      skill.find("### Part 2 — SERMON WORKSHOP"))
check("Explicit one-part override preserved",
      "If the user expressly requests only one part" in skill)
check("Do not ghostwrite default preserved",
      "Never write the user's final sermon" in skill)
check("Copyright boundary preserved",
      "copyrighted transcripts" in skill)
check("Verified illustrations required",
      "never invent what a preacher said" in skill)

archive = json.loads((SKILL_DIR / "references/archive-index.json").read_text(encoding="utf-8"))
sources = archive.get("sources", [])
check("Curated source registry includes 15 routes", len(sources) >= 15)
check("Every archive has at least one full official URL",
      all(s.get("official") and all(u.startswith("https://") for u in s["official"]) for s in sources))
check("Distinct source IDs", len({s.get("id") for s in sources}) == len(sources))
check("No automatic unverified timestamps",
      archive.get("defaultTimestamps") == "off-unless-checked-in-exact-recording")
tests = json.loads((SKILL_DIR / "evals/evals.json").read_text(encoding="utf-8"))
cases = tests.get("cases", [])
check("Seven or more evaluation cases", len(cases) >= 7)
check("Unique test ids", len({c.get("id") for c in cases}) == len(cases))
check("All cases have prompts, outcomes, and observable assertions",
      all(c.get("prompt") and c.get("expected") and len(c.get("assertions", [])) >= 4 for c in cases))
check("Contains direct passage/partial reference regression",
      "PARTIAL REFERENCE" in (SKILL_DIR / "examples/matthew-5-4-smoke-test.md").read_text(encoding="utf-8"))
failed = [name for name, ok in checks if not ok]
print(f"\n{len(checks) - len(failed)}/{len(checks)} structural checks passing")
if failed:
    print("Failures:", ", ".join(failed))
    sys.exit(1)
print("Live source retrieval, rights and document-layout evaluations must be run separately.")
